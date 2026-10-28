"""Nórska etiketa zo SK originálu: vystrihne SK texty a staré logo, položí NO texty a nové logo.

Použitie:  python3 etikett.py fettfjerner_500ml
Výstup do 02_PRACA/etikety/:  <OUT>.pdf (tlač: spadávka + orezové značky ako originál),
<OUT>.png (300 dpi, orezané na čistý formát — do Wordu), <OUT>_A4_2ks.pdf (2 etikety na A4 na domácu tlač).

Rozloženie (súradnice v px na náhľade 100 dpi, y zhora) je v LAYOUT; modul produktu prepíše, čo má inak (m.LAYOUT).
"""
import importlib, io, math, os, subprocess, sys
from PIL import Image
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.generic import (ContentStream, DecodedStreamObject, NameObject, ArrayObject,
                           FloatObject, DictionaryObject)
from reportlab.pdfgen import canvas
from reportlab.lib.colors import CMYKColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import Paragraph, Frame
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pdfpaths import walk, text_ops

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.dirname(HERE)
KHAND = os.path.join(OUTDIR, '..', 'sikkerhetsdatablad', 'zdroj', 'Khand-{}.ttf')
for w in ('Regular', 'Medium', 'SemiBold', 'Bold'):
    pdfmetrics.registerFont(TTFont('Khand-' + w, KHAND.format(w)))
pdfmetrics.registerFont(TTFont('Arial-Bold', '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'))

GREEN = CMYKColor(0.48, 0.05, 0.99, 0)     # zelená pásu a nápisov z originálu Cleaner
BLACK = CMYKColor(0, 0, 0, 1)
WHITE = CMYKColor(0, 0, 0, 0)

W, H = 660.947, 462.487                    # MediaBox originálu; build() prepíše podľa zdroja
def X(px): return px * 0.72                # súradnice merané na náhľade 100 dpi
def Y(px): return H - px * 0.72

# Predvolené rozloženie = Cleaner 500 ml (vektorový originál, texty v krivkách)
LAYOUT = {
    # čo sa z originálu vystrihne; maže sa len to, čo leží CELÉ vnútri (texty: počiatok riadku)
    'regions': {
        'text':    (460, 60, 848, 400),
        'text2':   (460, 390, 700, 452),
        'logo':    (296, 96, 446, 140),
        'nazov':   (130, 183, 400, 258),
        'eko':     (320, 344, 453, 432),
        'vyrobca': (478, 503, 650, 592),
        'odznak':  (725, 470, 761, 502),
    },
    'masks': [],                           # biele obdĺžniky (px) — na texty zapečené v obrázku
    'green': GREEN,
    'band': (75, 181, 448, 255),           # zelený pás s názvom
    'band_fill': None,                     # farba na pretretie pásu, keď je názov zapečený v obrázku
    'claims': (451, (358, 379, 400), 'Khand-Regular', 11.5),   # pravý okraj, účiaria, písmo, veľkosť
    'badges': [(728, 759, (479.5, 488), 5.2)],  # odznak NATURLIG PRODUKT: ľavý/pravý okraj textu, účiaria, max. písmo
    'body': (465, 842, 63, 398),           # x0, x1, horný okraj, spodná hranica
    'producer': (527, 515),                # ľavý okraj, prvé účiarie
    'logo': (372, 140, 118),               # stred x, spodok, šírka v pt
    'icon': (487, 555, 32),                # ľavý okraj, spodok, výška v pt
    'arc': None,                           # nápis po oblúku (odznak „neutralizuje zápach“)
    'photos': [],                          # náhrada fotiek: (súbor 300 dpi, výrez px, šesťuholník originálu px)
}

def strip(page, writer, regions):
    cs = ContentStream(page.get_contents(), writer)
    ops = cs.operations
    drop, hits = set(), {}
    inside = lambda b, r: b[0] >= r[0] and b[1] >= r[1] and b[2] <= r[2] and b[3] <= r[3]
    for s, i, o, col, bb, a in walk(ops, H):
        if o == b'n':
            continue
        for name, reg in regions.items():
            if inside(bb, reg):
                drop.update(range(s, i + 1)); hits[name] = hits.get(name, 0) + 1; break
    for i, (x, y) in text_ops(ops, H):
        for name, reg in regions.items():
            if inside((x, y, x, y), reg):
                drop.add(i); hits[name] = hits.get(name, 0) + 1; break
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

def arc_text(c, L, text, color):
    """Text po spodnom oblúku (vrchy písmen do stredu), pod ním biely pás, ktorý zakryje starý nápis."""
    cx, cy, r, span, mask_w = L                # stred a polomer stredu písmen v px, rozpätie nápisu v °, šírka masky px
    cxp, cyp, rp = X(cx), Y(cy), r * 0.72
    c.saveState()
    c.setStrokeColor(WHITE); c.setLineWidth(mask_w * 0.72); c.setLineCap(1)
    p = c.beginPath(); p.arc(cxp - rp, cyp - rp, cxp + rp, cyp + rp, startAng=-178, extent=176)
    c.drawPath(p, stroke=1, fill=0)
    font = 'Khand-Bold'
    size = 3.0
    while pdfmetrics.stringWidth(text, font, size + 0.1) / (rp + (size + 0.1) * 0.35) < math.radians(span):
        size += 0.1
    cap = size * 0.70
    rb = rp + cap / 2                          # účiarie je na vonkajšej strane
    total = pdfmetrics.stringWidth(text, font, size) / rb
    ang = -math.pi / 2 - total / 2
    c.setFillColor(color); c.setFont(font, size)
    for ch in text:
        cw = pdfmetrics.stringWidth(ch, font, size) / rb
        a = ang + cw / 2
        c.saveState()
        c.translate(cxp + rb * math.cos(a), cyp + rb * math.sin(a)); c.rotate(math.degrees(a) + 90)
        c.drawCentredString(0, 0, ch)
        c.restoreState()
        ang += cw
    c.restoreState()

def overlay(m, L):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(W, H))
    green = L['green']

    # Fotky do šesťuholníkov: výrez z cudzieho obrázka, orezaný presne na tvar originálu (o 1 % väčší — prekryje okraj)
    for src, (ux0, uy0, ux1, uy1), poly in L['photos']:
        im = Image.open(os.path.join(HERE, src)).convert('RGB').crop((ux0 * 3, uy0 * 3, ux1 * 3, uy1 * 3))
        cx = sum(x for x, _ in poly) / len(poly); cy = sum(y for _, y in poly) / len(poly)
        pts = [(cx + (x - cx) * 1.01, cy + (y - cy) * 1.01) for x, y in poly]
        xs = [x for x, _ in pts]; ys = [y for _, y in pts]
        c.saveState()
        path = c.beginPath(); path.moveTo(X(pts[0][0]), Y(pts[0][1]))
        for x, y in pts[1:]:
            path.lineTo(X(x), Y(y))
        path.close(); c.clipPath(path, stroke=0, fill=0)
        c.drawImage(ImageReader(im), X(min(xs)), Y(max(ys)), X(max(xs) - min(xs)), X(max(ys) - min(ys)))
        c.restoreState()

    for x0, y0, x1, y1 in L['masks']:
        c.setFillColor(WHITE); c.rect(X(x0), Y(y1), X(x1 - x0), X(y1 - y0), stroke=0, fill=1)

    # 1) Názov v zelenom páse, biele písmo, na stred
    bx0, by0, bx1, by1 = L['band']
    if L['band_fill'] is not None:
        c.setFillColor(L['band_fill']); c.rect(X(bx0), Y(by1), X(bx1 - bx0), X(by1 - by0), stroke=0, fill=1)
    cx, top, bot = X((bx0 + bx1) / 2), Y(by0), Y(by1)
    n = len(m.TITLE)
    size = 34 if n == 1 else 25
    while max(pdfmetrics.stringWidth(t, 'Khand-Bold', size) for t in m.TITLE) > X(bx1 - bx0) - 30:
        size -= 0.5
    cap = size * 0.70; gap = size * 0.22
    block = n * cap + (n - 1) * gap
    y = bot + (top - bot + block) / 2 - cap
    c.setFillColor(WHITE)
    for t in m.TITLE:
        c.setFont('Khand-Bold', size); c.drawCentredString(cx, y, t); y -= cap + gap

    # 2) Tvrdenia / podnadpis pod pásom, zarovnané doprava ako originál
    rx, ys, font, fs = L['claims']
    c.setFillColor(green)
    for t, py in zip(m.CLAIMS, ys):
        c.setFont(font, fs); c.drawRightString(X(rx), Y(py), t)

    # 3) Odznaky „naturlig produkt“
    for x0, x1, ys, fs in L['badges']:
        while pdfmetrics.stringWidth(m.BADGE[0], 'Arial-Bold', fs) > X(x1 - x0):
            fs -= 0.1
        for t, py in zip(m.BADGE, ys):
            c.setFont('Arial-Bold', fs); c.drawString(X(x0), Y(py), t)

    if L['arc']:
        arc_text(c, L['arc'], m.ARC, green)

    # 4) Hlavný text — veľkosť písma sa prispôsobí, aby blok sedel nad ikonami
    x0, x1, t0, b0 = L['body']
    fx, fw, ftop, fbot = X(x0), X(x1) - X(x0), Y(t0), Y(b0)
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
    px, py = L['producer']
    tx, y = X(px), Y(py)
    c.setFillColor(BLACK)
    c.setFont('Khand-Bold', 7.2); c.drawString(tx, y, m.PRODUCER['head']); y -= 8.4
    for i, t in enumerate(m.PRODUCER['lines']):
        c.setFont('Khand-SemiBold' if i == 0 else 'Khand-Regular', 7.2); c.drawString(tx, y, t); y -= 7.6
    c.setFont('Khand-Bold', 7.2); c.drawString(tx, y - 1, m.PRODUCER['tail'])
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0], body_size

def build(name):
    global W, H
    m = importlib.import_module(name)
    L = dict(LAYOUT, **getattr(m, 'LAYOUT', {}))
    w = PdfWriter()
    w.append(PdfReader(os.path.join(HERE, m.SOURCE)))
    page = w.pages[0]
    W, H = float(page.mediabox.width), float(page.mediabox.height)
    trim = [float(v) for v in page.trimbox]
    hits = strip(page, w, L['regions'])
    ov, body_size = overlay(m, L)
    page.merge_page(ov)

    # Logá: celé logo hore (namiesto starého), ikona pri dovozcovi
    full = logo_form(w, [-1, -1, 584.38, 238.57])
    icon = logo_form(w, [-1, -1, 212, 238.57])
    xo = page['/Resources'].setdefault(NameObject('/XObject'), DictionaryObject())
    xo[NameObject('/IsoLogo')] = full; xo[NameObject('/IsoIcon')] = icon
    lcx, lbot, lw = L['logo']
    s_top = lw / 585.38
    lx = X(lcx) - 585.38 * s_top / 2; ly = Y(lbot)
    ix0, ibot, ih = L['icon']
    s_ic = ih / 238.57
    ix, iy = X(ix0), Y(ibot)
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

    # PNG 300 dpi orezané na TrimBox — na Word
    png = os.path.join(OUTDIR, m.OUT)
    d = lambda v: str(round(v / 72 * 300))
    subprocess.run(['pdftoppm', '-r', '300', '-png', '-singlefile', '-x', d(trim[0]), '-y', d(H - trim[3]),
                    '-W', d(trim[2] - trim[0]), '-H', d(trim[3] - trim[1]), pdf, png], check=True)
    a4(pdf, os.path.join(OUTDIR, m.OUT + '_A4_2ks.pdf'), trim)
    print('vystrihnuté:', hits, '| písmo textu', body_size, 'pt')
    print(pdf); print(png + '.png')

def _stream(data):
    s = DecodedStreamObject(); s.set_data(data); return s

def a4(src, dst, trim):
    """Dve etikety pod sebou na A4, zmenšené na 95 % (domáca tlačiareň netlačí do kraja), s orezovými značkami."""
    A4W, A4H = 595.276, 841.89
    sc = 0.95
    tw, th = (trim[2] - trim[0]) * sc, (trim[3] - trim[1]) * sc   # čistý formát po zmenšení
    w = PdfWriter(); out = w.add_blank_page(A4W, A4H)
    x0 = (A4W - tw) / 2
    gap = (A4H - 2 * th) / 3
    for k in range(2):
        y0 = A4H - gap - th - k * (th + gap)
        lab = PdfReader(src).pages[0]
        lab.mediabox.lower_left = (trim[0], trim[1]); lab.mediabox.upper_right = (trim[2], trim[3])
        out.merge_transformed_page(lab, Transformation().translate(-trim[0], -trim[1]).scale(sc).translate(x0, y0))
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
