"""Reklama Isokor LMS — pred/po (WC) + fľaša. Výstup 1080×1350 (feed) a 1080×1920 (Stories).
Použitie: python3 reklama_lms.py <pred.jpg> <po.jpg> <flasa.jpg> <výstupný_priečinok>"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance

PRED, PO, FLASA, OUT = sys.argv[1:5]
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


def make(W, H, PH, path):
    can = Image.new('RGB', (W, H), GREEN)
    half = W // 2
    pred = fit(Image.open(PRED), half - 3, PH, 0.5, 0.62)
    po = fit(Image.open(PO), half - 3, PH, 0.5, 0.72)
    can.paste(pred, (0, 0)); can.paste(po, (half + 3, 0))
    d = ImageDraw.Draw(can)
    label(d, 28, 28, "FØR", RUST)
    label(d, half + 31, 28, "ETTER", GREEN)
    # fľaša vpravo dole
    src = ImageOps.exif_transpose(Image.open(FLASA))
    W0, H0 = src.size
    src = src.crop((int(W0 * 0.18), int(H0 * 0.10), int(W0 * 0.78), int(H0 * 0.97)))  # len fľaša
    fl = fit(src, 300, 470, 0.5, 0.5)
    fl = ImageEnhance.Brightness(fl).enhance(1.05)
    mask = Image.new('L', fl.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, *fl.size), radius=24, fill=255)
    fy = PH + 40
    can.paste(fl, (W - 300 - 50, fy), mask)
    x, y = 60, PH + 50
    d.text((x, y), "Brune rustflekker", font=f('InterDisplay-Bold.otf', 70), fill=CREAM); y += 82
    d.text((x, y), "i toalettet?", font=f('InterDisplay-Bold.otf', 70), fill=CREAM); y += 108
    for line in ["Isokor LMS fjerner rust og kalk", "fra toalett, badekar, servant", "og belegningsstein."]:
        d.text((x, y), line, font=f('Inter-Regular.otf', 36), fill=CREAM); y += 50
    y += 26
    t = "149 kr  ·  Kjøp på nett"
    c = f('Inter-SemiBold.otf', 38); bw = d.textlength(t, font=c)
    d.rounded_rectangle((x, y, x + bw + 60, y + 78), radius=39, fill=CREAM)
    d.text((x + 30, y + 16), t, font=c, fill=GREEN); y += 104
    d.text((x, y), "isokor-skandinavia.no", font=f('Inter-Medium.otf', 32), fill=ACC)
    d.text((x, y + 50), "Etsende – bruk hansker. Test først på et skjult sted.",
           font=f('Inter-Regular.otf', 24), fill=(200, 205, 198))
    can.save(path, quality=90, optimize=True, progressive=True)


os.makedirs(OUT, exist_ok=True)
make(1080, 1350, 700, os.path.join(OUT, 'lms_wc_pred_po_1080x1350.jpg'))
make(1080, 1920, 1000, os.path.join(OUT, 'lms_wc_pred_po_1080x1920.jpg'))
print('ok')
