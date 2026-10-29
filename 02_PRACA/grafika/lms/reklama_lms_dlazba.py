"""Reklama Isokor LMS — dlažba pred/po + fľaša. 1080×1350 (feed) a 1080×1920 (Stories).
Zdroj: Lukove 2 skutočné fotky spojené v Gemini do jedného obrázka (1024×718);
rozdelí sa na polovice a spodok sa oreže, aby zmizol znak ✦ v rohu.
Použitie: python3 reklama_lms_dlazba.py <dlazba_pred_po.jpg> <flasa.jpg> <výstupný_priečinok>"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance

SRC, FLASA, OUT = sys.argv[1:4]
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


def label(d, x, y, text, fill):
    ft = f('Inter-Bold.otf', 40)
    w = d.textlength(text, font=ft)
    d.rounded_rectangle((x, y, x + w + 44, y + 64), radius=32, fill=fill)
    d.text((x + 22, y + 9), text, font=ft, fill=CREAM)


src = Image.open(SRC).convert('RGB')
PRED = src.crop((0, 0, 505, 660))      # ľavá polovica
PO = src.crop((519, 0, 1024, 660))     # pravá polovica, bez spodku so znakom ✦


def make(W, H, PH, path):
    can = Image.new('RGB', (W, H), GREEN)
    half = W // 2
    can.paste(fit(PRED, half - 3, PH, 0.6, 0.5), (0, 0))
    can.paste(fit(PO, half - 3, PH, 0.4, 0.5), (half + 3, 0))
    d = ImageDraw.Draw(can)
    label(d, 28, 28, "FØR", RUST)
    label(d, half + 31, 28, "ETTER", GREEN)
    fs = ImageOps.exif_transpose(Image.open(FLASA))
    W0, H0 = fs.size
    fs = fs.crop((int(W0 * 0.18), int(H0 * 0.10), int(W0 * 0.78), int(H0 * 0.97)))
    fl = ImageEnhance.Brightness(fit(fs, 300, 470)).enhance(1.05)
    mask = Image.new('L', fl.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, *fl.size), radius=24, fill=255)
    can.paste(fl, (W - 350, PH + 40), mask)
    x, y = 60, PH + 50
    d.text((x, y), "Rust på steinen?", font=f('InterDisplay-Bold.otf', 70), fill=CREAM); y += 108
    for line in ["Isokor LMS fjerner rustflekker", "fra belegningsstein og fliser –", "også i fugene."]:
        d.text((x, y), line, font=f('Inter-Regular.otf', 36), fill=CREAM); y += 50
    y += 26
    t = "149 kr  ·  Kjøp på nett"
    c = f('Inter-SemiBold.otf', 38); bw = d.textlength(t, font=c)
    d.rounded_rectangle((x, y, x + bw + 60, y + 78), radius=39, fill=CREAM)
    d.text((x + 30, y + 16), t, font=c, fill=GREEN); y += 104
    d.text((x, y), "isokor-skandinavia.no", font=f('Inter-Medium.otf', 32), fill=ACC)
    can.save(path, quality=90, optimize=True, progressive=True)


os.makedirs(OUT, exist_ok=True)
make(1080, 1350, 700, os.path.join(OUT, 'lms_dlazba_pred_po_1080x1350.jpg'))
make(1080, 1920, 1000, os.path.join(OUT, 'lms_dlazba_pred_po_1080x1920.jpg'))
print('ok')
