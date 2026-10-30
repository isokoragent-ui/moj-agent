"""Karusel Isokor LMS — prezentácia produktu (FB/IG, 8 slajdov 1080×1350), 30. 10. 2026.
Lukove skutočné fotky z fotky/. Povrchy len podľa popisu výrobcu + betón (Luk);
kov/pozinkované NIE (karta 10.5: nezlučiteľné s kovmi) — kým nepotvrdí výrobca.
Použitie: python3 karusel_lms.py <priečinok_fotiek> <výstupný_priečinok>"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance

SRC, OUT = sys.argv[1:3]
F = '/usr/share/fonts/opentype/inter/'
GREEN = (28, 58, 40); CREAM = (246, 243, 236); RUST = (190, 92, 38); ACC = (214, 190, 120)
W, H = 1080, 1350


def f(name, size):
    return ImageFont.truetype(F + name, size)


def img(name):
    return Image.open(os.path.join(SRC, name))


def fit(im, w, h, cx=0.5, cy=0.5):
    im = ImageOps.exif_transpose(im).convert('RGB')
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = round((im.width - w) * cx); y = round((im.height - h) * cy)
    return im.crop((x, y, x + w, y + h))


def label(d, x, y, text, fill, size=40):
    ft = f('Inter-Bold.otf', size)
    w = d.textlength(text, font=ft)
    d.rounded_rectangle((x, y, x + w + size * 1.1, y + size * 1.6), radius=size * 0.8, fill=fill)
    d.text((x + size * 0.55, y + size * 0.22), text, font=ft, fill=CREAM)


def flasa(h):
    """Celá fľaša (Lukova fotka, pozadie odstránené rembg) — výška h, vracia RGBA."""
    fl = Image.open(os.path.join(SRC, 'lms_flasa_vystrihnuta.png')).convert('RGBA')
    return fl.resize((round(fl.width * h / fl.height), h), Image.LANCZOS)


def vloz_flasu(can, x, y, h):
    fl = flasa(h)
    tien = Image.new('RGBA', can.size, (0, 0, 0, 0))
    ImageDraw.Draw(tien).ellipse((x + fl.width * 0.1, y + h - 22, x + fl.width * 0.9, y + h + 14), fill=(0, 0, 0, 90))
    from PIL import ImageFilter
    can.paste(tien.filter(ImageFilter.GaussianBlur(12)), (0, 0), tien.filter(ImageFilter.GaussianBlur(12)))
    can.paste(fl, (x, y), fl)
    return fl.width


def lines(d, x, y, rows, font, fill=CREAM, step=None):
    step = step or round(font.size * 1.3)
    for r in rows:
        d.text((x, y), r, font=font, fill=fill); y += step
    return y


def strana(d, n):
    d.text((W - 60, H - 50), f"{n}/8", font=f('Inter-Medium.otf', 28), fill=ACC, anchor='rs')
    d.text((60, H - 50), "ISOKOR LMS", font=f('Inter-Bold.otf', 26), fill=ACC, anchor='ls')


def tlacidlo(d, x, y, t, fill=CREAM, col=GREEN):
    c = f('Inter-SemiBold.otf', 38); bw = d.textlength(t, font=c)
    d.rounded_rectangle((x, y, x + bw + 60, y + 78), radius=39, fill=fill)
    d.text((x + 30, y + 16), t, font=c, fill=col)


def s1(path):  # obálka
    can = Image.new('RGB', (W, H), GREEN); PH = 760; half = W // 2
    can.paste(fit(img('dlazba_1_pred.jpg'), half - 3, PH, 0.45, 0.55), (0, 0))
    can.paste(fit(img('dlazba_4_po.jpg'), half - 3, PH, 0.35, 0.45), (half + 3, 0))
    d = ImageDraw.Draw(can)
    label(d, 28, 28, "FØR", RUST); label(d, half + 31, 28, "ETTER", GREEN)
    y = lines(d, 60, PH + 60, ["Rust?", "Borte."], f('InterDisplay-Bold.otf', 120), step=130)
    lines(d, 60, y + 30, ["Isokor LMS rustfjerner –", "sveip og se hvordan"], f('Inter-Regular.otf', 40))
    vloz_flasu(can, W - 290, PH + 50, 450)
    strana(d, 1); can.save(path, quality=90, optimize=True, progressive=True)


def s2(path):  # kde všade
    can = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(can)
    y = lines(d, 70, 110, ["Rust setter seg", "der du minst vil ha den"], f('InterDisplay-Bold.otf', 68), GREEN, 82)
    y += 50
    for t, s in [("Fliser og fuger", "bad, gang, terrasse"),
                 ("Belegningsstein og betong", "gårdsplass, trapp, innkjørsel"),
                 ("Toalett, badekar og servant", "brune flekker fra jern i vannet"),
                 ("Dusj og badstue", "rust og kalk"),
                 ("Kjøkkenbenk", "flekker som ikke går bort"),
                 ("Fasade", "rustspor under rekkverk og beslag")]:
        d.ellipse((70, y + 14, 98, y + 42), fill=RUST)
        d.text((125, y), t, font=f('Inter-Bold.otf', 46), fill=GREEN)
        d.text((125, y + 58), s, font=f('Inter-Regular.otf', 32), fill=(90, 100, 92))
        y += 162
    d.text((W - 60, H - 50), "2/8", font=f('Inter-Medium.otf', 28), fill=RUST, anchor='rs')
    d.text((60, H - 50), "ISOKOR LMS", font=f('Inter-Bold.otf', 26), fill=RUST, anchor='ls')
    can.save(path, quality=90, optimize=True, progressive=True)


def s3(path):  # WC
    can = Image.new('RGB', (W, H), GREEN); PH = 860; half = W // 2
    can.paste(fit(img('wc_pred.jpg'), half - 3, PH, 0.5, 0.62), (0, 0))
    can.paste(fit(img('wc_po.jpg'), half - 3, PH, 0.5, 0.72), (half + 3, 0))
    d = ImageDraw.Draw(can)
    label(d, 28, 28, "FØR", RUST); label(d, half + 31, 28, "ETTER", GREEN)
    y = lines(d, 60, PH + 55, ["Brune flekker i toalettet?"], f('InterDisplay-Bold.otf', 64))
    lines(d, 60, y + 20, ["Jern i brønnvannet gir rustflekker på", "toalett, badekar og servant. LMS tar dem."],
          f('Inter-Regular.otf', 36))
    strana(d, 3); can.save(path, quality=90, optimize=True, progressive=True)


def s4(path):  # dlažba 3 kroky
    can = Image.new('RGB', (W, H), GREEN); PH = 900; cw = (W - 12) // 3
    for i, (src, cx, cy, txt, col) in enumerate([
            ('dlazba_1_pred.jpg', 0.45, 0.55, "1  FØR", RUST),
            ('dlazba_2_nastrek.jpg', 0.45, 0.6, "2  SPRAY", GREEN),
            ('dlazba_4_po.jpg', 0.35, 0.45, "3  ETTER", GREEN)]):
        x0 = i * (cw + 6)
        can.paste(fit(img(src), cw, PH, cx, cy), (x0, 0))
        label(ImageDraw.Draw(can), x0 + 18, 22, txt, col, 30)
    d = ImageDraw.Draw(can)
    y = lines(d, 60, PH + 55, ["Rust på steinen?"], f('InterDisplay-Bold.otf', 64))
    lines(d, 60, y + 20, ["Spray på, la virke, skrubb og skyll.", "Også rust nede i fugene."], f('Inter-Regular.otf', 36))
    strana(d, 4); can.save(path, quality=90, optimize=True, progressive=True)


def s5(path):  # ako na to
    can = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(can)
    lines(d, 70, 110, ["Slik gjør du"], f('InterDisplay-Bold.otf', 80), GREEN)
    ph = fit(img('dlazba_3_posobi.jpg'), W - 140, 430, 0.4, 0.55)
    mask = Image.new('L', ph.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, *ph.size), radius=28, fill=255)
    can.paste(ph, (70, 250), mask)
    y = 740
    for n, t, s in [("1", "Spray på flekken", "direkte fra flasken"),
                    ("2", "La virke en liten stund", "syrene løser opp rusten"),
                    ("3", "Skrubb og skyll med vann", "ferdig")]:
        d.ellipse((70, y, 160, y + 90), fill=RUST)
        d.text((115, y + 45), n, font=f('InterDisplay-Bold.otf', 54), fill=CREAM, anchor='mm')
        d.text((195, y + 2), t, font=f('Inter-Bold.otf', 46), fill=GREEN)
        d.text((195, y + 58), s, font=f('Inter-Regular.otf', 32), fill=(90, 100, 92))
        y += 150
    d.text((W - 60, H - 50), "5/8", font=f('Inter-Medium.otf', 28), fill=RUST, anchor='rs')
    d.text((60, H - 50), "ISOKOR LMS", font=f('Inter-Bold.otf', 26), fill=RUST, anchor='ls')
    can.save(path, quality=90, optimize=True, progressive=True)


def s6(path):  # aj vodný kameň
    can = Image.new('RGB', (W, H), GREEN); d = ImageDraw.Draw(can)
    y = lines(d, 70, 130, ["Ikke bare rust."], f('InterDisplay-Bold.otf', 92), CREAM, 110)
    y = lines(d, 70, y + 10, ["Kalk også."], f('InterDisplay-Bold.otf', 92), ACC, 110)
    lines(d, 70, y + 50, ["Samme flaske fjerner kalkbelegg i dusjen,",
                          "på badekaret, servanten og i badstua.",
                          "",
                          "Én flaske – to problemer mindre."], f('Inter-Regular.otf', 40))
    vloz_flasu(can, (W - flasa(540).width) // 2, 720, 540)
    strana(d, 6); can.save(path, quality=90, optimize=True, progressive=True)


def s7(path):  # služba
    can = Image.new('RGB', (W, H), GREEN)
    bg = ImageEnhance.Brightness(fit(img('dlazba_1_pred.jpg'), W, H, 0.5, 0.5)).enhance(0.35)
    can.paste(bg, (0, 0)); d = ImageDraw.Draw(can)
    y = lines(d, 70, 300, ["Store flater?", "Vi tar jobben."], f('InterDisplay-Bold.otf', 96), CREAM, 112)
    y = lines(d, 70, y + 50, ["Rust på gårdsplassen, terrassen eller",
                              "fasaden? Vi rengjør for deg.",
                              "",
                              "Send oss en melding – du får et",
                              "uforpliktende tilbud."], f('Inter-Regular.otf', 42))
    tlacidlo(d, 70, y + 50, "Send melding")
    strana(d, 7); can.save(path, quality=90, optimize=True, progressive=True)


def s8(path):  # CTA
    can = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(can)
    vloz_flasu(can, (W - flasa(740).width) // 2, 80, 740)
    d.text((W // 2, 870), "Isokor LMS rustfjerner", font=f('InterDisplay-Bold.otf', 66), fill=GREEN, anchor='mt')
    d.text((W // 2, 960), "149 kr", font=f('InterDisplay-Bold.otf', 110), fill=RUST, anchor='mt')
    t = "Kjøp på nett"; c = f('Inter-SemiBold.otf', 42); bw = d.textlength(t, font=c)
    x = (W - bw - 70) // 2
    d.rounded_rectangle((x, 1110, x + bw + 70, 1196), radius=43, fill=GREEN)
    d.text((W // 2, 1153), t, font=c, fill=CREAM, anchor='mm')
    d.text((W // 2, 1235), "isokor-skandinavia.no", font=f('Inter-Medium.otf', 34), fill=RUST, anchor='mt')
    d.text((W - 60, H - 40), "8/8", font=f('Inter-Medium.otf', 28), fill=RUST, anchor='rs')
    can.save(path, quality=90, optimize=True, progressive=True)


os.makedirs(OUT, exist_ok=True)
for i, fn in enumerate([s1, s2, s3, s4, s5, s6, s7, s8], 1):
    fn(os.path.join(OUT, f'lms_karusel_{i}.jpg'))
print('ok')
