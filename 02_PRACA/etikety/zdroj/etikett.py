"""Nórska etiketa zo SK originálu: vektorovo vystrihne SK texty a staré logo, položí NO texty a nové logo.

Použitie:  python3 etikett.py fettfjerner_500ml
Výstup do 02_PRACA/etikety/:  <OUT>.pdf (tlač: spadávka + orezové značky ako originál),
<OUT>.png (300 dpi, orezané na čistý formát — do Wordu), <OUT>_A4_2ks.pdf (2 etikety na A4 na domácu tlač).
"""
import importlib, io, os, subprocess, sys
from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.generic import (ContentStream, DecodedStreamObject, NameObject, ArrayObject,
                           FloatObject, DictionaryObject, NumberObject)
from reportlab.pdfgen import canvas
from reportlab.lib.colors import CMYKColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import Paragraph, Frame
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pdfpaths import walk

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.dirname(HERE)
KHAND = os.path.join(OUTDIR, '..', 'sikkerhetsdatablad', 'zdroj', 'Khand-{}.ttf')
for w in ('Regular', 'Medium', 'SemiBold', 'Bold'):
    pdfmetrics.registerFont(TTFont('Khand-' + w, KHAND.format(w)))
pdfmetrics.registerFont(TTFont('Arial-Bold', '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'))

GREEN = CMYKColor(0.48, 0.05, 0.99, 0)     # zelená pásu a nápisov z originálu
BLACK = CMYKColor(0, 0, 0, 1)
WHITE = CMYKColor(0, 0, 0, 0)

W, H = 660.947, 462.487                    # MediaBox originálu (TrimBox 33..627.9 × 33..429.5)
def X(px): return px * 0.72                # súradnice merané na náhľade 100 dpi
def Y(px): return H - px * 0.72

# Čo sa z originálu vystrihne (px pri 100 dpi, y zhora). Maže sa len to, čo leží CELÉ vnútri.
REGIONS = {
    'text':    (460, 60, 848, 400),
    'text2':   (460, 390, 700, 452),
    'logo':    (296, 96, 446, 140),
    'nazov':   (130, 183, 400, 258),
    'eko':     (320, 344, 453, 432),
    'vyrobca': (478, 503, 650, 592),
    'odznak':  (725, 470, 761, 502),
}

def strip(page, writer):
    cs = ContentStream(page.get_contents(), writer)
    ops = cs.operations
    drop, hits = set(), {}
    inside = lambda b, r: b[0] >= r[0] and b[1] >= r[1] and b[2] <= r[2] and b[3] <= r[3]
    for s, i, o, col, bb, a in walk(ops):
        if o == b'n':
            continue
        for name, reg in REGIONS.items():
            if inside(bb, reg):
                drop.update(range(s, i + 1)); hits[name] = hits.get(name, 0) + 1; break
    cs.operations = [op for k, op in enumerate(ops) if k not in drop]
    page.replace_contents(cs)
    return hits

def logo_form(writer, bbox):
    """Nové logo ako vektorový Form XObject, prefarbené na čistú čiernu K100 (originál má 95/95/45/95 = 380 % farby)."""
    r = PdfReader(os.path.join(HERE, 'isokor_logo_new_riadkove.pdf'))
    p = r.pages[0]
    cs = ContentStream(p.get_contents(), r)
    for k, (a, o) in enumerate(cs.operations):
        if o == b'k':
            cs.operations[k] = ([FloatObject(0), FloatObject(0), FloatObject(0), FloatObject(1)], o)
    form = DecodedStreamObject()
    form.set_data(cs.get_data())
    form.update({NameObject('/Type'): NameObject('/XObject'), NameObject('/Subtype'): NameObject('/Form'),
                 NameObject('/BBox'): ArrayObject([FloatObject(v) for v in bbox]),
                 NameObject('/Resources'): p['/Resources'].clone(writer)})
    return writer._add_object(form)

def para(text_pairs, size):
    st = ParagraphStyle('b', fontName='Khand-Regular', fontSize=size, leading=size * 1.18,
                        alignment=TA_JUSTIFY, textColor=BLACK)
    html = ' '.join('<font name="Khand-Bold">{}</font> {}'.format(h, t) for h, t in text_pairs)
    return Paragraph(html, st)

def overlay(m):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(W, H))

    # 1) Názov v zelenom páse (pás: px 75–448 × 181–255), biele písmo, na stred
    cx, top, bot = X(261.5), Y(181), Y(255)
    n = len(m.TITLE)
    size = 34 if n == 1 else 25
    while max(pdfmetrics.stringWidth(t, 'Khand-Bold', size) for t in m.TITLE) > X(448 - 75) - 30:
        size -= 0.5
    cap = size * 0.70; gap = size * 0.22
    block = n * cap + (n - 1) * gap
    y = bot + (top - bot + block) / 2 - cap
    c.setFillColor(WHITE)
    for t in m.TITLE:
        c.setFont('Khand-Bold', size); c.drawCentredString(cx, y, t); y -= cap + gap

    # 2) Tvrdenia pod BIO, zarovnané doprava ako originál
    c.setFillColor(GREEN)
    for t, py in zip(m.CLAIMS, (358, 379, 400)):
        c.setFont('Khand-Regular', 11.5); c.drawRightString(X(451), Y(py), t)

    # 3) Odznak „naturlig produkt“
    for t, py in zip(m.BADGE, (479.5, 488)):
        fs = 5.2
        while pdfmetrics.stringWidth(m.BADGE[0], 'Arial-Bold', fs) > X(759 - 728):
            fs -= 0.1
        c.setFont('Arial-Bold', fs); c.drawString(X(728), Y(py), t)

    # 4) Hlavný text — veľkosť písma sa prispôsobí, aby blok sedel nad ikonami
    fx, fw, ftop, fbot = X(465), X(842) - X(465), Y(63), Y(398)
    for size in [x / 10 for x in range(80, 55, -1)]:
        p = para(m.BODY, size)
        _, h = p.wrap(fw, 10000)
        if h <= ftop - fbot:
            break
    Frame(fx, ftop - h - 4, fw, h + 8, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
          showBoundary=0).addFromList([p], c)
    y = ftop - h - 4 - size * 1.35
    for hd, t in m.FOOT:
        c.setFillColor(BLACK); c.setFont('Khand-Bold', size); c.drawString(fx, y, hd)
        c.setFont('Khand-Regular', size); c.drawString(fx + pdfmetrics.stringWidth(hd + ' ', 'Khand-Bold', size), y, t)
        y -= size * 1.2
    body_size = size

    # 5) Dovozca (namiesto slovenského výrobcu); vľavo ikona nového loga
    tx, y = X(527), Y(515)
    c.setFillColor(BLACK)
    c.setFont('Khand-Bold', 7.2); c.drawString(tx, y, m.PRODUCER['head']); y -= 8.4
    for i, t in enumerate(m.PRODUCER['lines']):
        c.setFont('Khand-SemiBold' if i == 0 else 'Khand-Regular', 7.2); c.drawString(tx, y, t); y -= 7.6
    c.setFont('Khand-Bold', 7.2); c.drawString(tx, y - 1, m.PRODUCER['tail'])
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0], body_size

def build(name):
    m = importlib.import_module(name)
    w = PdfWriter()
    w.append(PdfReader(os.path.join(HERE, m.SOURCE)))
    page = w.pages[0]
    hits = strip(page, w)
    ov, body_size = overlay(m)
    page.merge_page(ov)

    # Logá: celé logo hore (namiesto starého), ikona pri dovozcovi
    full = logo_form(w, [-1, -1, 584.38, 238.57])
    icon = logo_form(w, [-1, -1, 212, 238.57])
    xo = page['/Resources'].setdefault(NameObject('/XObject'), DictionaryObject())
    xo[NameObject('/IsoLogo')] = full; xo[NameObject('/IsoIcon')] = icon
    s_top = 118 / 585.38                     # šírka loga hore 118 pt
    lx = X(372) - 585.38 * s_top / 2; ly = Y(140)
    s_ic = 32 / 238.57                       # ikona vysoká 32 pt
    ix, iy = X(487), Y(555)
    cs = ContentStream(page.get_contents(), w)
    extra = ('q {s} 0 0 {s} {x} {y} cm /IsoLogo Do Q q {t} 0 0 {t} {ix} {iy} cm /IsoIcon Do Q'
             .format(s=s_top, x=lx, y=ly, t=s_ic, ix=ix, iy=iy))
    data = cs.get_data() + b'\n' + extra.encode()
    page.replace_contents(DecodedStreamObject())
    page[NameObject('/Contents')] = w._add_object(_stream(data))
    w.compress_identical_objects()
    pdf = os.path.join(OUTDIR, m.OUT + '.pdf')
    with open(pdf, 'wb') as f:
        w.write(f)

    # PNG 300 dpi orezané na TrimBox (33 pt z každej strany) — na Word
    png = os.path.join(OUTDIR, m.OUT)
    subprocess.run(['pdftoppm', '-r', '300', '-png', '-singlefile', '-x', str(round(33 / 72 * 300)),
                    '-y', str(round(33 / 72 * 300)), '-W', str(round(594.947 / 72 * 300)),
                    '-H', str(round(396.487 / 72 * 300)), pdf, png], check=True)
    a4(pdf, os.path.join(OUTDIR, m.OUT + '_A4_2ks.pdf'))
    print('vystrihnuté:', hits, '| písmo textu', body_size, 'pt')
    print(pdf); print(png + '.png')

def _stream(data):
    s = DecodedStreamObject(); s.set_data(data); return s

def a4(src, dst):
    """Dve etikety pod sebou na A4, zmenšené na 95 % (domáca tlačiareň netlačí do kraja), s orezovými značkami."""
    A4W, A4H = 595.276, 841.89
    sc = 0.95
    tw, th = 594.947 * sc, 396.487 * sc       # čistý formát po zmenšení
    w = PdfWriter(); out = w.add_blank_page(A4W, A4H)
    x0 = (A4W - tw) / 2
    gap = (A4H - 2 * th) / 3
    for k in range(2):
        y0 = A4H - gap - th - k * (th + gap)
        lab = PdfReader(src).pages[0]
        lab.mediabox.lower_left = (33, 33); lab.mediabox.upper_right = (627.947, 429.487)
        out.merge_transformed_page(lab, Transformation().translate(-33, -33).scale(sc).translate(x0, y0))
    buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=(A4W, A4H)); c.setLineWidth(0.3)
    for k in range(2):
        y0 = A4H - gap - th - k * (th + gap)
        for (x, y) in [(x0, y0), (x0 + tw, y0), (x0, y0 + th), (x0 + tw, y0 + th)]:
            dx = -1 if x == x0 else 1; dy = -1 if y == y0 else 1
            c.line(x + dx * 3, y, x + dx * 12, y); c.line(x, y + dy * 3, x, y + dy * 12)
    c.save(); buf.seek(0)
    out.merge_page(PdfReader(buf).pages[0])
    w.compress_identical_objects()
    with open(dst, 'wb') as f:
        w.write(f)

if __name__ == '__main__':
    sys.path.insert(0, HERE)
    build(sys.argv[1] if len(sys.argv) > 1 else 'fettfjerner_500ml')
