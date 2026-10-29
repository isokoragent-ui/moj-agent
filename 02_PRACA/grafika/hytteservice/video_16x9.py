"""Video na šírku 1920×1080 (16:9 — YouTube, Facebook, web) pre Isokor Hytteservice.
Použitie: python3 video_16x9.py <priečinok_na_snímky>  → potom ffmpeg + hudba.wav (pozri README)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from banner import photo_layer, text_block, HY, LA, GREEN
from PIL import Image, ImageDraw

W, H, PW = 1920, 1080, 1150
FPS = 25; T = 10.0; N = int(FPS * T)
D = sys.argv[1]
os.makedirs(D, exist_ok=True)


def ease(x):
    return 0 if x < 0 else 1 if x > 1 else x * x * (3 - 2 * x)


def frame(t):
    out = ease((t - 9.2) / 0.8)
    a = [ease((t - 0.3 - 0.35 * k) / 0.8) * (1 - out) for k in range(5)]
    ph = photo_layer(HY, PW, H, 1.0 + 0.07 * (t / 6.5), 0.55, 0.45)
    m = ease((t - 5.5) / 1.0)
    if m > 0:
        ph = Image.blend(ph, photo_layer(LA, PW, H, 1.0 + 0.06 * max(0, (t - 5.5) / 4.5), 0.5, 0.5), m)
    if out > 0:
        ph = Image.blend(ph, photo_layer(HY, PW, H, 1.0, 0.55, 0.45), out)
    base = Image.new('RGB', (W, H), GREEN)
    base.paste(ph, (W - PW, 0))
    g = Image.new('L', (260, H))
    for i in range(260):
        ImageDraw.Draw(g).line([(i, 0), (i, H)], fill=int(255 * (1 - i / 259) ** 1.6))
    base.paste(Image.new('RGB', (260, H), GREEN), (W - PW, 0), g)
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    text_block(ImageDraw.Draw(ov), 110, 290, 1.0, a)
    return Image.alpha_composite(base.convert('RGBA'), ov).convert('RGB')


for i in range(N):
    frame(i / FPS).save(os.path.join(D, f'{i:04d}.jpg'), quality=92)
print(N)
