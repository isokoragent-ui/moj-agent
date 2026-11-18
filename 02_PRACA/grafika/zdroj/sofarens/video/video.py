"""Video Isokor Sofarens na siete — 20 s, 1080×1920 (Reels, TikTok, Stories, Shorts), 30 fps.
Obrázky: Lukove z Gemini (`obr/`, zmenšené na 1300 px) + fľaša s novou etiketou (`../flaska_sofarens_nova.png`, Lukov obrázok 18. 11.).
Hudba: `hudba_Sun_on_the_Floorboards.mp3` (od Luka) od 46,05 s — drop skladby (48,85 s) padne na prvý strih škvŕn (2,8 s).
Použitie:  python3 video.py <priečinok_snímok> [koniec]   (koniec = len jedna kontrolná snímka záverečného záberu)
Potom:     python3 ../../../hytteservice/hudba.py hudba.wav 20 && ffmpeg … (pozri README)."""
import os, sys, math
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, T = 1080, 1920, 30, 20.0
FD = '/usr/share/fonts/opentype/inter/'
def font(n, s): return ImageFont.truetype(FD + n, s)
GOLD = (200, 176, 128); DARK = (30, 28, 26); WHITE = (255, 255, 255)

def load(n): return np.array(Image.open(os.path.join(HERE, 'obr', n + '.jpg')).convert('RGB'))

def ease(x): return 0.0 if x < 0 else 1.0 if x > 1 else x * x * (3 - 2 * x)

def cam(img, z, ox=0.5, oy=0.5, dx=0.0, dy=0.0):
    """Výrez 1080×1920 so zoomom z okolo bodu (ox, oy) — Ken Burns."""
    h, w = img.shape[:2]
    s = max(W / w, H / h) * z
    cx = ox * w + dx; cy = oy * h + dy
    # nedovoľ výrez mimo obrázka
    hw, hh = W / 2 / s, H / 2 / s
    cx = min(max(cx, hw), w - hw); cy = min(max(cy, hh), h - hh)
    M = np.float32([[s, 0, W / 2 - s * cx], [0, s, H / 2 - s * cy]])
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)

# ---------- záverečný záber: skutočná fľaša na stolíku ----------
def end_scene():
    bg = Image.fromarray(load('10_stolik'))
    b = Image.open(os.path.join(HERE, '..', 'flaska_sofarens_nova.png')).convert('RGBA')
    bh = 800                                      # výška fľaše v px obrázka 1300 × 2329
    b = b.resize((round(b.width * bh / b.height), bh), Image.LANCZOS)
    a = np.array(b).astype(np.float32)
    a[..., :3] *= np.array([1.03, 0.97, 0.88]) * 0.93   # teplé večerné svetlo scény (lampa, sviečky)
    # jemný prechod svetla zľava (lampa) doprava
    a[..., :3] *= np.linspace(1.03, 0.90, a.shape[1])[None, :, None]
    b = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    body_cx = 442 * bh / 2198                     # stred tela fľaše vo výreze (spúšť trčí doľava)
    foot = (470, 1735)                            # kde stojí fľaša na doske stolíka (px obrázka)
    x = round(foot[0] - body_cx); y = foot[1] - bh
    # tieň: kontaktný pod fľašou + mäkký vrhnutý doprava (lampa vľavo)
    sh = Image.new('L', bg.size, 0); d = ImageDraw.Draw(sh)
    bw = (734 - 150) * bh / 2198
    d.ellipse((foot[0] - bw / 2 - 6, foot[1] - 22, foot[0] + bw / 2 + 10, foot[1] + 14), fill=170)
    d.polygon([(foot[0] - bw * 0.3, foot[1] - 8), (foot[0] + bw * 0.5, foot[1] - 14),
               (foot[0] + bw * 1.9, foot[1] - 60), (foot[0] + bw * 1.2, foot[1] + 4)], fill=70)
    sh = sh.filter(ImageFilter.GaussianBlur(16))
    bg = Image.composite(Image.new('RGB', bg.size, (60, 45, 30)), bg, sh.point(lambda v: int(v * 0.75)))
    bg.paste(b, (x, y), b)
    return np.array(bg)

# ---------- scény: (začiatok, koniec, obrázok, zoom od, zoom do, ox, oy) ----------
S = [
    (0.0, 2.8, '01_vino', 1.20, 1.04, 0.45, 0.62),
    (2.8, 3.55, '02_cucoriedky', 1.04, 1.16, 0.45, 0.55),
    (3.55, 4.3, '03_polievka', 1.04, 1.16, 0.45, 0.5),
    (4.3, 5.05, '04_krv', 1.04, 1.18, 0.45, 0.55),
    (5.05, 5.8, '05_saft', 1.04, 1.16, 0.5, 0.55),
    (5.8, 7.7, '06_olej', 1.0, 1.12, 0.5, 0.42),
    (7.7, 9.5, '07_extrakty', 1.12, 1.0, 0.5, 0.55),
    (9.5, 12.2, '08_sprej', 1.0, 1.05, 0.6, 0.5),
    (12.2, 14.8, '09_cista_sofa', 1.14, 1.0, 0.42, 0.62),
    (14.8, 20.0, 'KONIEC', 1.0, 1.06, 0.47, 0.6),
]
VARIANT = os.environ.get('VARIANT', 'jul')    # jul | neutral (VARIANT=neutral python3 video.py …)
XF = 0.3                                          # prelínačka (s) — okrem rýchlej série škvŕn

IMG = {}
def img(n):
    if n not in IMG:
        IMG[n] = end_scene() if n == 'KONIEC' else load(n)
    return IMG[n]

def shot(k, t):
    t0, t1, n, z0, z1, ox, oy = S[k]
    p = (t - t0) / (t1 - t0)
    z = z0 + (z1 - z0) * ease(p) if k else z0 + (z1 - z0) * (1 - (1 - min(max(p, 0), 1)) ** 2)
    dx = dy = 0.0
    if k == 0 and t < 0.45:                       # krátke trhnutie pri rozliatí
        a = 14 * (1 - t / 0.45); dx = a * math.sin(t * 70); dy = a * math.cos(t * 55)
    return cam(img(n), z, ox, oy, dx, dy)

def scene(t):
    k = max(i for i, s in enumerate(S) if s[0] <= t)
    fr = shot(k, t)
    t0 = S[k][0]
    fast = 1 <= k <= 4 or k == 5 and False
    if k and not (2 <= k <= 4) and t - t0 < XF:   # prelínačka z predošlého záberu
        m = ease((t - t0) / XF)
        fr = (shot(k - 1, t).astype(np.float32) * (1 - m) + fr.astype(np.float32) * m).astype(np.uint8)
    if 2 <= k <= 4 and t - t0 < 2 / FPS:          # rýchly strih s bielym zábleskom
        fr = (fr.astype(np.float32) * 0.45 + 255 * 0.55).astype(np.uint8)
    return Image.fromarray(fr)

# ---------- texty ----------
def box_text(d, lines, y, a, size=84, fnt='InterDisplay-Bold.otf', x=72, pad=26, col=WHITE, boxa=0.62, slide=0):
    """Riadky textu v tmavom zaoblenom boxe (biely text na svetlej fotke inak nie je čitateľný)."""
    f = font(fnt, size); lh = round(size * 1.18)
    wmax = max(d.textlength(s, font=f) for s in lines)
    yy = y + round(40 * (1 - a)) if slide else y
    d.rounded_rectangle((x - pad, yy - pad * 0.7, x + wmax + pad, yy + lh * len(lines) + pad * 0.3),
                        radius=22, fill=DARK + (round(255 * boxa * a),))
    for i, s in enumerate(lines):
        d.text((x, yy + i * lh), s, font=f, fill=col + (round(255 * a),))
    return yy + lh * len(lines) + pad

def fade(t, t0, t1, i=0.35, o=0.3):
    return min(ease((t - t0) / i), ease((t1 - t) / o))

def texts(t):
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    if t < 2.8:
        box_text(d, ['Rødvin på sofaen?'], 300, fade(t, 0.35, 2.8, 0.3, 0.2), size=92, slide=1)
    elif t < 5.8:                                   # pri každom strihu jedno slovo (zoznam zakrýval fľašu sirupu)
        words = ['Blåbær.', 'Tomatsuppe.', 'Blod.', 'Saft.']
        n = sum(1 for s in S[1:5] if s[0] <= t)
        a = fade(t, 2.8, 5.8, 0.15, 0.25)
        box_text(d, [words[n - 1]], 300, a, size=104)
    elif t < 9.5:
        a = fade(t, 6.0, 9.5)
        y = box_text(d, ['Laget av'], 300, a, size=46, fnt='Inter-SemiBold.otf', col=GOLD, slide=1)
        box_text(d, ['plantebaserte', 'ekstrakter og oljer'], y + 6, fade(t, 6.3, 9.5), size=80, slide=1)  # Luk 18. 11.: bez „kaldpressede“
    elif t < 12.2:
        steps = [('Spray.', 9.75), ('Vent litt.', 10.45), ('Tørk av.', 11.15)]
        vis = [s for s, t0 in steps if t >= t0]
        if vis:
            box_text(d, vis, 300, fade(t, 9.75, 12.2, 0.25, 0.25), size=92)
    elif t < 14.8:
        line2 = 'klar for julebesøket' if VARIANT == 'jul' else 'som ny igjen'   # neutrálna = celoročná verzia
        box_text(d, ['Ren sofa –', line2], 300, fade(t, 12.45, 14.8), size=84, slide=1)
    else:
        a = fade(t, 15.1, 99)
        y = box_text(d, ['ISOKOR SOFARENS'], 230, a, size=86, slide=1)
        y = box_text(d, ['Fjerner flekker og lukt', 'Sofa · tepper · bilseter'], y + 8, fade(t, 15.5, 99),
                     size=50, fnt='Inter-SemiBold.otf', slide=1)
        box_text(d, ['V-Label-sertifisert'], y + 8, fade(t, 15.9, 99), size=38, fnt='Inter-Medium.otf',
                 col=GOLD, slide=1)
        # cenovka 149,- vyskočí
        p = (t - 16.3) / 0.45
        if p > 0:
            sc = 1 + 0.25 * math.sin(min(p, 1) * math.pi) if p < 1 else 1
            r = round(118 * min(1, ease(p * 1.4)) * sc)
            cx, cy = 820, 1000
            d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GOLD + (245,))
            if r > 40:
                f = font('InterDisplay-Bold.otf', round(r * 0.62))
                d.text((cx, cy + 4), '149,-', font=f, fill=DARK + (255,), anchor='mm')
        a2 = fade(t, 16.9, 99)
        f = font('Inter-SemiBold.otf', 46)
        s = 'isokor-skandinavia.no'; tw = d.textlength(s, font=f)
        d.rounded_rectangle((W / 2 - tw / 2 - 34, 1528, W / 2 + tw / 2 + 34, 1612), radius=42,
                            fill=WHITE + (round(235 * a2),))
        d.text((W / 2, 1570), s, font=f, fill=DARK + (round(255 * a2),), anchor='mm')
    # trvalá poznámka — obrázky sú ilustračné (AI), fľaša je skutočná
    f = font('Inter-Medium.otf', 24)
    d.text((40, 1660), 'Illustrasjonsbilder', font=f, fill=(255, 255, 255, 170),
           stroke_width=2, stroke_fill=(0, 0, 0, 90))
    return ov

def frame(t):
    return Image.alpha_composite(scene(t).convert('RGBA'), texts(t)).convert('RGB')

if __name__ == '__main__':
    D = sys.argv[1]; os.makedirs(D, exist_ok=True)
    if len(sys.argv) > 2:
        for t in [float(x) for x in sys.argv[2].split(',')]:
            frame(t).save(os.path.join(D, f'k_{t:05.2f}.jpg'), quality=90)
        sys.exit()
    N = int(FPS * T)
    for i in range(N):
        frame(i / FPS).save(os.path.join(D, f'{i:04d}.jpg'), quality=92)
    print(N)
