"""Vertikálne video 1080×1920 (Stories, Reels, TikTok, Shorts) pre Isokor Hytteservice.
Použitie: python3 video_vertikal.py <priečinok_na_snímky>  → potom ffmpeg (pozri README)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from banner import photo_layer, f, HY, LA, GREEN, CREAM, ACC
from PIL import Image, ImageDraw

W, H = 1080, 1920
PH = 960          # výška fotky
FPS = 25; T = 10.0; N = int(FPS * T)
D = sys.argv[1]
os.makedirs(D, exist_ok=True)


def ease(x):
    return 0 if x < 0 else 1 if x > 1 else x * x * (3 - 2 * x)


def frame(t):
    z1 = 1.0 + 0.08 * (t / 6.5)
    ph = photo_layer(HY, W, PH, z1, 0.62, 0.45)
    m = ease((t - 5.5) / 1.0)
    if m > 0:
        ph = Image.blend(ph, photo_layer(LA, W, PH, 1.0 + 0.06 * max(0, (t - 5.5) / 4.5), 0.5, 0.5), m)
    base = Image.new('RGB', (W, H), GREEN)
    base.paste(ph, (0, 0))
    g = Image.new('L', (W, 220))
    for i in range(220):
        ImageDraw.Draw(g).line([(0, i), (W, i)], fill=int(255 * (i / 219) ** 1.4))
    base.paste(Image.new('RGB', (W, 220), GREEN), (0, PH - 220), g)

    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    a = [ease((t - 0.4 - 0.4 * k) / 0.8) for k in range(6)]
    A = lambda c, x: c + (round(255 * x),)
    x, y = 80, PH - 40
    d.text((x, y), "NYHET  ·  ISOKOR HYTTESERVICE", font=f('Inter-SemiBold.otf', 34), fill=A(ACC, a[0])); y += 70
    for line in ["Vi passer på", "hytta di i vinter"]:
        d.text((x, y), line, font=f('InterDisplay-Bold.otf', 96), fill=A(CREAM, a[1])); y += 110
    y += 24
    for line in ["Høstlukking  ·  Tilsyn hver 14. dag", "Bilder og tilsynslogg  ·  Våråpning"]:
        d.text((x, y), line, font=f('Inter-Regular.otf', 40), fill=A(CREAM, a[2] * 0.92)); y += 56
    y += 22
    d.text((x, y), "Vegårshei  ·  Tvedestrand  ·  Risør", font=f('Inter-Medium.otf', 38), fill=A(ACC, a[3])); y += 84
    c = f('Inter-SemiBold.otf', 40); t1 = "Hele sesongen fra 11 990 kr"
    bw = d.textlength(t1, font=c)
    d.rounded_rectangle((x, y, x + bw + 64, y + 84), radius=42, fill=A(CREAM, a[4]))
    d.text((x + 32, y + 18), t1, font=c, fill=A(GREEN, a[4]))
    # URL pod tlačidlom — nad spodným okrajom, ktorý zakrýva rozhranie Stories
    d.text((x, y + 120), "isokor-skandinavia.no/pages/hytteservice", font=f('Inter-Medium.otf', 36), fill=A(CREAM, a[5]))
    return Image.alpha_composite(base.convert('RGBA'), ov).convert('RGB')


for i in range(N):
    frame(i / FPS).save(os.path.join(D, f'{i:04d}.jpg'), quality=92)
print(N)
