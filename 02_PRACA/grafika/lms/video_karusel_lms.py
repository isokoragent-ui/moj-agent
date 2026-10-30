"""Video Isokor LMS zo slajdov karuselu (karusel_video/ = `karusel_lms.py fotky karusel_video video`), 30. 10. 2026.
Každý slajd ~2,6 s s jemným priblížením, prelínanie 0,4 s; pozadie = rozmazaný slajd.
Použitie: python3 video_karusel_lms.py vertikal|sirka <priečinok_snímok>
Potom hudba + ffmpeg (pozri README)."""
import os, sys
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw

MODE, D = sys.argv[1:3]
W, H = (1080, 1920) if MODE == 'vertikal' else (1920, 1080)
FPS, SLIDE, FADE = 25, 2.6, 0.4
SRC = [Image.open(os.path.join(os.path.dirname(__file__) or '.', 'karusel_video', f'lms_karusel_{i}.jpg')).convert('RGB')
       for i in range(1, 9)]
T = SLIDE * len(SRC) + 1.0  # posledný slajd (cena) stojí o sekundu dlhšie

# veľkosť slajdu v zábere
SH = 1290 if MODE == 'vertikal' else 980
SW = round(SH * 1080 / 1350)


def pozadie(im):
    bg = im.resize((W // 8, round(W // 8 * im.height / im.width)))
    s = max(W / bg.width, H / bg.height)
    bg = bg.resize((round(bg.width * s) + 2, round(bg.height * s) + 2), Image.BILINEAR)
    bg = bg.crop(((bg.width - W) // 2, (bg.height - H) // 2, (bg.width - W) // 2 + W, (bg.height - H) // 2 + H))
    return ImageEnhance.Brightness(bg.filter(ImageFilter.GaussianBlur(30))).enhance(0.55)


BG = [pozadie(im) for im in SRC]
MASK = Image.new('L', (SW, SH), 0)
ImageDraw.Draw(MASK).rounded_rectangle((0, 0, SW, SH), radius=28, fill=255)


def scena(i, t):
    """Záber slajdu i v čase t (sekundy od začiatku slajdu)."""
    can = BG[i].copy()
    z = 1.0 + 0.035 * min(t / (SLIDE + FADE), 1.0)
    w, h = round(SW * z), round(SH * z)
    sl = SRC[i].resize((w, h), Image.LANCZOS)
    m = MASK.resize((w, h))
    x, y = (W - w) // 2, (H - h) // 2
    tien = Image.new('L', (W, H), 0)
    ImageDraw.Draw(tien).rounded_rectangle((x + 10, y + 18, x + w + 10, y + h + 18), radius=30, fill=110)
    can.paste((0, 0, 0), (0, 0), tien.filter(ImageFilter.GaussianBlur(22)))
    can.paste(sl, (x, y), m)
    return can


def frame(t):
    i = min(int(t // SLIDE), len(SRC) - 1)
    a = scena(i, t - i * SLIDE)
    t_kon = (i + 1) * SLIDE
    if i < len(SRC) - 1 and t > t_kon - FADE:
        b = scena(i + 1, 0)
        return Image.blend(a, b, (t - (t_kon - FADE)) / FADE)
    return a


os.makedirs(D, exist_ok=True)
N = int(FPS * T)
for n in range(N):
    frame(n / FPS).save(os.path.join(D, f'{n:04d}.jpg'), quality=92)
print(N, 'snímok,', T, 's')
