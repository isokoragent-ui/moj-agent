"""Reklamy Isokor LMS — dlažba (Lukove skutočné fotky, 29. 10. 2026).
1) pred/po:   lms_dlazba_pred_po_1080x1350.jpg + _1080x1920.jpg
2) 3 kroky:   lms_dlazba_kroky_1080x1350.jpg + _1080x1920.jpg  (Før · Spray på · Etter)
Použitie: python3 reklama_lms_dlazba.py <pred.jpg> <nastrek.jpg> <po.jpg> <flasa.jpg> <výstupný_priečinok>"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance

PRED, NASTREK, PO, FLASA, OUT = sys.argv[1:6]
F = '/usr/share/fonts/opentype/inter/'
GREEN = (28, 58, 40); CREAM = (246, 243, 236); RUST = (190, 92, 38); ACC = (214, 190, 120)


def f(name, size):
    return ImageFont.truetype(F + name, size)


def fit(img, w, h, cx=0.5, cy=0.5):
    img = ImageOps.exif_transpose(img).convert('RGB')
    s = max(w / img.width, h / img.height)
    im = img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)
    x = round((im.width - w) * cx); y = round((im.height - h) * cy)
    return im.crop((x, y, x + w, y + h))


def label(d, x, y, text, fill, size=40):
    ft = f('Inter-Bold.otf', size)
    w = d.textlength(text, font=ft)
    d.rounded_rectangle((x, y, x + w + size * 1.1, y + size * 1.6), radius=size * 0.8, fill=fill)
    d.text((x + size * 0.55, y + size * 0.22), text, font=ft, fill=CREAM)


def bottom(can, d, W, PH, headline, lines):
    fs = ImageOps.exif_transpose(Image.open(FLASA))
    W0, H0 = fs.size
    fs = fs.crop((int(W0 * 0.18), int(H0 * 0.10), int(W0 * 0.78), int(H0 * 0.97)))
    fl = ImageEnhance.Brightness(fit(fs, 300, 470)).enhance(1.05)
    mask = Image.new('L', fl.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, *fl.size), radius=24, fill=255)
    can.paste(fl, (W - 350, PH + 40), mask)
    x, y = 60, PH + 50
    d.text((x, y), headline, font=f('InterDisplay-Bold.otf', 70), fill=CREAM); y += 108
    for line in lines:
        d.text((x, y), line, font=f('Inter-Regular.otf', 36), fill=CREAM); y += 50
    y += 26
    t = "149 kr  ·  Kjøp på nett"
    c = f('Inter-SemiBold.otf', 38); bw = d.textlength(t, font=c)
    d.rounded_rectangle((x, y, x + bw + 60, y + 78), radius=39, fill=CREAM)
    d.text((x + 30, y + 16), t, font=c, fill=GREEN); y += 104
    d.text((x, y), "isokor-skandinavia.no", font=f('Inter-Medium.otf', 32), fill=ACC)


TEXT = ["Isokor LMS fjerner rustflekker", "fra belegningsstein og fliser –", "også i fugene."]


def pred_po(W, H, PH, path):
    can = Image.new('RGB', (W, H), GREEN); half = W // 2
    can.paste(fit(Image.open(PRED), half - 3, PH, 0.45, 0.55), (0, 0))
    can.paste(fit(Image.open(PO), half - 3, PH, 0.35, 0.45), (half + 3, 0))
    d = ImageDraw.Draw(can)
    label(d, 28, 28, "FØR", RUST); label(d, half + 31, 28, "ETTER", GREEN)
    bottom(can, d, W, PH, "Rust på steinen?", TEXT)
    can.save(path, quality=90, optimize=True, progressive=True)


def kroky(W, H, PH, path):
    can = Image.new('RGB', (W, H), GREEN); cw = (W - 12) // 3
    for i, (src, cx, cy, txt, col) in enumerate([
            (PRED, 0.45, 0.55, "1  FØR", RUST),
            (NASTREK, 0.45, 0.6, "2  SPRAY", GREEN),
            (PO, 0.35, 0.45, "3  ETTER", GREEN)]):
        x0 = i * (cw + 6)
        can.paste(fit(Image.open(src), cw, PH, cx, cy), (x0, 0))
        label(ImageDraw.Draw(can), x0 + 18, 22, txt, col, 30)
    d = ImageDraw.Draw(can)
    bottom(can, d, W, PH, "Rust på steinen?", TEXT)
    can.save(path, quality=90, optimize=True, progressive=True)


os.makedirs(OUT, exist_ok=True)
pred_po(1080, 1350, 700, os.path.join(OUT, 'lms_dlazba_pred_po_1080x1350.jpg'))
pred_po(1080, 1920, 1000, os.path.join(OUT, 'lms_dlazba_pred_po_1080x1920.jpg'))
kroky(1080, 1350, 700, os.path.join(OUT, 'lms_dlazba_kroky_1080x1350.jpg'))
kroky(1080, 1920, 1000, os.path.join(OUT, 'lms_dlazba_kroky_1080x1920.jpg'))
print('ok')
