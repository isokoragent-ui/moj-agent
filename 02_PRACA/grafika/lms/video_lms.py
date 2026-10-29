"""Video Isokor LMS (15 s): WC pred/po → dlažba pred / sprej / po → záver s fľašou.
Použitie: python3 video_lms.py <vertikal|sirka> <priečinok_na_snímky>
Fotky berie z ./fotky (Lukove skutočné fotky). Potom ffmpeg + hudba (pozri README)."""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance

HERE = os.path.dirname(os.path.abspath(__file__))
FOT = os.path.join(HERE, 'fotky')
MODE, D = sys.argv[1], sys.argv[2]
os.makedirs(D, exist_ok=True)
F = '/usr/share/fonts/opentype/inter/'
GREEN = (28, 58, 40); CREAM = (246, 243, 236); RUST = (190, 92, 38); ACC = (214, 190, 120)
FPS, T = 25, 15.0


def f(name, size):
    return ImageFont.truetype(F + name, size)


def load(n):
    return ImageOps.exif_transpose(Image.open(os.path.join(FOT, n))).convert('RGB')


def fit(img, w, h, z=1.0, cx=0.5, cy=0.5):
    s = max(w / img.width, h / img.height) * z
    im = img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)
    x = round((im.width - w) * cx); y = round((im.height - h) * cy)
    return im.crop((x, y, x + w, y + h))


def ease(x):
    return 0 if x < 0 else 1 if x > 1 else x * x * (3 - 2 * x)


fl = load('lms_flasa.jpg'); w0, h0 = fl.size
FLASA = fl.crop((int(w0 * 0.18), int(h0 * 0.10), int(w0 * 0.78), int(h0 * 0.97)))

# (fotka, štítok, farba štítku, nadpis, text, cx, cy)
SCENES = [
    (load('wc_pred.jpg'), "FØR", RUST, "Brune rustflekker", "i toalettet?", 0.5, 0.62),
    (load('wc_po.jpg'), "ETTER", GREEN, "Isokor LMS fjerner", "rust og kalk.", 0.5, 0.72),
    (load('dlazba_1_pred.jpg'), "FØR", RUST, "Rust på steinen?", "", 0.45, 0.55),
    (load('dlazba_2_nastrek.jpg'), "SPRAY", GREEN, "Spray på flekken …", "", 0.45, 0.6),
    (load('dlazba_4_po.jpg'), "ETTER", GREEN, "… og rusten er borte.", "Også i fugene.", 0.35, 0.45),
]
SL = 2.5  # dĺžka scény, posledných 2,5 s záver


def label(d, x, y, text, fill, a, size=40):
    ft = f('Inter-Bold.otf', size); w = d.textlength(text, font=ft)
    d.rounded_rectangle((x, y, x + w + size * 1.1, y + size * 1.6), radius=size * 0.8, fill=fill + (round(255 * a),))
    d.text((x + size * 0.55, y + size * 0.22), text, font=ft, fill=CREAM + (round(255 * a),))


def scene_img(i, t_in, PW, PH):
    img, lab, col, h1, h2, cx, cy = SCENES[i]
    return fit(img, PW, PH, 1.0 + 0.06 * (t_in / SL), cx, cy)


def frame(t, W, H, vert):
    can = Image.new('RGB', (W, H), GREEN)
    if vert:
        PW, PH, px, py = W, 1240, 0, 0
    else:
        PW, PH, px, py = 1100, H, W - 1100, 0
    end = t >= SL * len(SCENES)
    if not end:
        i = int(t // SL); t_in = t - i * SL
        ph = scene_img(i, t_in, PW, PH)
        if t_in > SL - 0.4 and i + 1 < len(SCENES):   # prelínanie do ďalšej scény
            ph = Image.blend(ph, scene_img(i + 1, 0, PW, PH), ease((t_in - (SL - 0.4)) / 0.4))
        can.paste(ph, (px, py))
        if not vert:
            g = Image.new('L', (200, H))
            for k in range(200):
                ImageDraw.Draw(g).line([(k, 0), (k, H)], fill=int(255 * (1 - k / 199) ** 1.6))
            can.paste(Image.new('RGB', (200, H), GREEN), (px, 0), g)
        ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
        _, lab, col, h1, h2, _, _ = SCENES[i]
        a = ease(t_in / 0.35) * (1 - ease((t_in - (SL - 0.3)) / 0.3))
        label(d, px + 36, py + 36, lab, col, a)
        if vert:
            x, y = 70, PH + 90
        else:
            x, y = 110, 380
        d.text((x, y), h1, font=f('InterDisplay-Bold.otf', 78), fill=CREAM + (round(255 * a),))
        if h2:
            d.text((x, y + 96), h2, font=f('InterDisplay-Bold.otf', 78), fill=CREAM + (round(255 * a),))
        d.text((x, y + (230 if vert else 230)), "Isokor LMS", font=f('Inter-SemiBold.otf', 36), fill=ACC + (round(255 * a),))
        return Image.alpha_composite(can.convert('RGBA'), ov).convert('RGB')
    # záver
    te = t - SL * len(SCENES); a = ease(te / 0.5)
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    if vert:
        bw, bh, bx, by = 560, 880, (W - 560) // 2, 170
        x, y = 90, by + bh + 70
    else:
        bw, bh, bx, by = 520, 820, W - 520 - 160, (H - 820) // 2
        x, y = 140, 330
    b = ImageEnhance.Brightness(fit(FLASA, bw, bh)).enhance(1.05)
    m = Image.new('L', (bw, bh), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, bw, bh), radius=30, fill=round(255 * a))
    can.paste(b, (bx, by), m)
    A = lambda c: c + (round(255 * a),)
    d.text((x, y), "Isokor LMS", font=f('InterDisplay-Bold.otf', 92), fill=A(CREAM)); y += 116
    d.text((x, y), "Fjerner rust og kalk", font=f('Inter-Regular.otf', 44), fill=A(CREAM)); y += 90
    c = f('Inter-SemiBold.otf', 44); t1 = "149 kr  ·  Kjøp på nett"; tw = d.textlength(t1, font=c)
    d.rounded_rectangle((x, y, x + tw + 70, y + 92), radius=46, fill=A(CREAM))
    d.text((x + 35, y + 18), t1, font=c, fill=A(GREEN)); y += 130
    d.text((x, y), "isokor-skandinavia.no", font=f('Inter-Medium.otf', 40), fill=A(ACC))
    return Image.alpha_composite(can.convert('RGBA'), ov).convert('RGB')


vert = MODE == 'vertikal'
W, H = (1080, 1920) if vert else (1920, 1080)
N = int(FPS * T)
for n in range(N):
    frame(n / FPS, W, H, vert).save(os.path.join(D, f'{n:04d}.jpg'), quality=92)
print(N)
