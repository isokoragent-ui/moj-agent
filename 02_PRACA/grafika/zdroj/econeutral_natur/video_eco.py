"""Video EcoNeutral „Frisk luft – også inne“ (2026-11-15): Gemini fotky (in/1–4) rozpohybované + skutočné fľaše
500 ml a 100 ml (Lukove fotky, vystrihni_flase.py). Postup a pomocné funkcie ako ../cleaner_natur/video3.py.
Použitie: python3 video_eco.py PRIECINOK [časy]      (WIDE=1 → na šírku 1920×1080 s textovým panelom vľavo)
Výstup: snímky f0000.jpg … 30 fps, 18 s."""
import os, sys
import numpy as np
import cv2

D = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
FPS, DUR = 30, 18.0
WIDE = os.environ.get('WIDE') == '1'
FW, FH, PANEL = 1920, 1080, 800
W, H = (FW - PANEL, FH) if WIDE else (1080, 1920)


def load(name):
    return cv2.imread(os.path.join(D, 'in', name))[:, :, ::-1].astype(np.float32) / 255


def load_rgba(path):
    im = cv2.imread(path, cv2.IMREAD_UNCHANGED).astype(np.float32) / 255
    im = im[:, :, [2, 1, 0, 3]]
    im[:, :, :3] *= im[:, :, 3:4]
    return im


def bottle(path):
    """Fľaša z izbovej fotky: vyváženie bielej (biely plast → ~0,95) + jemne teplejšie ranné svetlo."""
    b = load_rgba(os.path.join(D, path))
    a = b[:, :, 3] > 0.95
    rgb = b[:, :, :3][a]
    ref = np.percentile(rgb, 97, axis=0)
    b[:, :, :3] *= (0.95 / np.maximum(ref, 1e-3)).astype(np.float32) * np.array([1.0, 0.99, 0.97], np.float32)
    b[:, :, :3] = np.minimum(b[:, :, :3], b[:, :, 3:4])
    return b


IMG = {k: load(f) for k, f in [(1, '1_fjord.jpg'), (2, '2_hytte_valp.jpg'), (3, '3_fjellsko.jpg'), (4, '4_bord.jpg')]}
SH, SW = IMG[1].shape[:2]
BASE = max(SW / W, SH / H)
# 500 ml s NOVOU nórskou etiketou (Luk 15. 11.: „nech môžeme video používať aj do budúcnosti“):
# ../kjokkenpakken_jul/nalep.py ../../../etikety/Isokor_EcoNeutral_500ml_etikett_NO.png flasa_500ml_nova_etiketa.png
# 100 ml: rovnaká etiketa, len „100ml“ (etiketa_100ml.py) nalepená na Lukovu fotku (nalep_valec.py).
B500 = bottle('flasa_500ml_nova_etiketa.png')
B100 = bottle('flasa_100ml_nova_etiketa.png')
BOT_X = {id(B500): 414.0, id(B100): 280.0}         # stred dna v obrázku fľaše
TXT = {k: load_rgba(os.path.join(D, 'texty_wide' if WIDE else 'texty', k + '.png')) for k in ['t1', 't2', 't3', 't4', 't6', 't7']}

clamp = lambda x, a=0.0, b=1.0: max(a, min(b, x))
lin = lambda t, a, b: clamp((t - a) / (b - a))
ease = lambda x: 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2
eout = lambda x: 1 - (1 - x) ** 3


def win(t, a, b, fi=.5, fo=.5):
    return min(ease(lin(t, a, a + fi)), 1 - ease(lin(t, b - fo, b)))


def camera(src, zoom, cx, cy):
    if WIDE:  # fotky na výšku → väčší zoom a výrez držaný vo fotke
        zoom *= 1.98
        hx, hy = W * BASE / zoom / 2, H * BASE / zoom / 2
        cx, cy = min(max(cx, hx + 8), SW - hx - 8), min(max(cy, hy + 8), SH - hy - 8)
    s = BASE / zoom
    M = np.array([[s, 0, cx - s * W / 2], [0, s, cy - s * H / 2]], np.float32)
    return cv2.warpAffine(np.ascontiguousarray(src, np.float32), M, (W, H), flags=cv2.INTER_CUBIC | cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REFLECT)


def over(dst, layer, op=1.0):
    a = layer[:, :, 3:4] * op
    return dst * (1 - a) + layer[:, :, :3] * op


def place(sprite, M, size):
    return cv2.warpAffine(sprite, M.astype(np.float32), size, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))


def soft_ellipse(size, cx, cy, rx, ry, ang=0, blur=25):
    m = np.zeros((size[1], size[0]), np.float32)
    cv2.ellipse(m, (int(cx), int(cy)), (int(rx), int(ry)), ang, 0, 360, 1.0, -1)
    k = int(blur) * 2 + 1
    return cv2.GaussianBlur(m, (k, k), 0)


def dust(img, t, x0, x1, y0, y1, n=60, seed=3):
    r = np.random.default_rng(seed)
    for i in range(n):
        x = x0 + r.random() * (x1 - x0) + 22 * t + 9 * np.sin(t * .7 + i)
        y = y0 + r.random() * (y1 - y0) - 14 * t
        if 0.5 + 0.5 * np.sin(t * 1.4 + i * 1.7) > .55:
            cv2.circle(img, (int(x), int(y)), 1 + (i % 3), (1.0, .98, .93), -1, lineType=cv2.LINE_AA)
    return img


# ---------- 1: fjord — hmla sa pomaly valí po vode ----------
_r = np.random.default_rng(5)
FOG = cv2.GaussianBlur(_r.random((SH // 8, SW // 4)).astype(np.float32), (0, 0), 9)
FOG = (FOG - FOG.min()) / (FOG.max() - FOG.min())
FOG = np.tile(FOG, (1, 2))
_yy = np.arange(SH, dtype=np.float32)[:, None]
FOG_BAND = np.exp(-((_yy - 1760) / 120) ** 2)          # pás hmly nad hladinou


def scene1(t):
    u = lin(t, 0, 4.2)
    shift = int(t * 9) % (SW // 4)
    fog = cv2.resize(FOG[:, shift:shift + SW // 4], (SW, SH), interpolation=cv2.INTER_CUBIC)
    a = (0.25 + 0.45 * fog) * FOG_BAND
    src = IMG[1] * (1 - a[:, :, None] * .55) + a[:, :, None] * .55 * np.array([.95, .96, .97], np.float32)
    img = camera(src, 1.0 + 0.08 * ease(u), 768, 1430 - 30 * u)
    g = soft_ellipse((W, H), 0, int(H * .55), int(W * .5), int(H * .3), blur=150)
    return img + g[:, :, None] * np.array([1.0, .93, .80], np.float32) * (0.06 + 0.03 * np.sin(t * 1.8))


# ---------- 2: šteňa — jemne dýcha ----------
_yy2, _xx2 = np.mgrid[0:SH, 0:SW].astype(np.float32)
BREATH = soft_ellipse((SW, SH), 1110, 1945, 260, 120, blur=60)   # hrudník a bok
Y0 = 2065.0                                                       # kde šteňa leží na deke


def scene2(t):
    u = lin(t, 3.8, 7.8)
    eps = 0.022 * (0.5 + 0.5 * np.sin(2 * np.pi * (t - 3.8) / 2.3))
    mapy = Y0 + (_yy2 - Y0) / (1 + eps * BREATH)
    src = cv2.remap(IMG[2], _xx2, mapy.astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return camera(src, 1.04 + 0.08 * ease(u), 900 + 40 * u, 1500 + 60 * u)


# ---------- 3: topánky po túre — prach v svetle z okna ----------
def scene3(t):
    u = lin(t, 7.4, 11.2)
    img = camera(IMG[3], 1.03 + 0.07 * ease(u), 720 + 70 * u, 1480 + 40 * u)
    return dust(img, t - 7.4, 0, W * .45, H * .2, H * .8, n=70)


# ---------- 4: stôl — obe fľaše dosadnú, prejde svetlo, záver ----------
P500 = np.array([800.0, 2200.0 if not WIDE else 2185.0])
H500 = 920 if WIDE else 1250
P100 = np.array([1050.0, 1968.0])
H100 = 480 if WIDE else 650


def put(src, spr, h, base, k, sweep):
    near = eout(k)
    op = ease(clamp(k * 2.2))
    if op <= 0:
        return src
    bh, bw = spr.shape[:2]
    s = h / bh
    by = base[1] - 220 * (1 - near)
    w = bw * s * 0.62
    sh = soft_ellipse((SW, SH), base[0] + 6, base[1] - 4, w * .55, w * .10, blur=12) * 0.55
    sh2 = soft_ellipse((SW, SH), base[0] + w * .9, base[1] - h * .03, w * .95, w * .16, ang=-8, blur=45) * 0.26
    shade = np.clip(sh + sh2, 0, 1)[:, :, None] * op * near
    src = src * (1 - shade * np.array([0.5, 0.55, 0.62], np.float32))
    M = np.array([[s, 0, base[0] - s * BOT_X[id(spr)]], [0, s, by - s * (bh - 6)]])
    lay = place(spr, M, (SW, SH))
    gx = np.clip((np.arange(SW, dtype=np.float32) - (base[0] - w)) / (2 * w), 0, 1)[None, :, None]
    lay[:, :, :3] *= (1.06 - 0.14 * gx)                       # svetlo zľava (ako lúč na stene)
    if 0 < sweep < 1:
        xx = np.arange(SW, dtype=np.float32)[None, :]
        yy = np.arange(SH, dtype=np.float32)[:, None]
        band = np.exp(-(((xx - (base[0] - 420 + 840 * sweep)) + (yy - base[1] + h / 2) * 0.35) / 55) ** 2) * np.sin(np.pi * sweep)
        lay[:, :, :3] += band[:, :, None] * 0.25 * lay[:, :, 3:4]
    return over(src, lay, op)


def scene4(t):
    u = lin(t, 10.8, 18.0)
    src = IMG[4]
    src = put(src, B100, H100, P100, lin(t, 11.6, 12.6), lin(t, 13.0, 14.0))
    src = put(src, B500, H500, P500, lin(t, 11.0, 12.1), lin(t, 12.8, 13.8))
    return camera(src, 1.05 + 0.04 * ease(u), 800, 1740 if WIDE else 1440)


SCENES = [(scene1, 0, 4.2), (scene2, 3.8, 7.8), (scene3, 7.4, 11.2), (scene4, 10.8, 18.01)]
TEXTS = [('t1', .6, 3.9, .6, .5), ('t2', 4.3, 7.4, .6, .5), ('t3', 7.9, 10.9, .6, .5), ('t4', 12.2, 14.3, .6, .5),
         ('t6', 14.6, 99, .7, .1), ('t7', 15.2, 99, .6, .1)]

GRAIN = np.random.default_rng(1).normal(0, 1, (FH // 2, FW // 2) if WIDE else (H // 2, W // 2)).astype(np.float32)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
VIG = 1 - 0.2 * np.clip(((xx - W / 2) / (W * .62)) ** 2 + ((yy - H / 2) / (H * .62)) ** 2, 0, 1.5)[:, :, None]
_py = np.linspace(0, 1, FH, dtype=np.float32)[:, None, None]
_px = np.linspace(0, 1, PANEL, dtype=np.float32)[None, :, None]
PANEL_BG = np.array([.94, .94, .925], np.float32) * (1.0 - 0.05 * _py - 0.03 * _px)   # chladnejšia biela než Cleaner


def frame(t):
    img = None
    for fn, a, b in SCENES:
        if a <= t < b:
            op = min(ease(lin(t, a, a + 0.4)) if a > 0 else 1, 1 - ease(lin(t, b - 0.4, b)) if b < DUR else 1)
            f = fn(t)
            img = f if img is None else img * (1 - op) + f * op
    img = img * VIG
    if WIDE:
        canvas = np.empty((FH, FW, 3), np.float32)
        canvas[:, :PANEL] = PANEL_BG
        canvas[:, PANEL:] = img
        img = canvas
    for k, a, b, fi, fo in TEXTS:
        op = win(t, a, b, fi, fo)
        if op > 0:
            tx = TXT[k]
            dy = int((1 - op) * 24)
            if dy:
                tx = np.roll(tx, dy, axis=0)
            img = over(img, tx, op)
    g = cv2.resize(np.roll(GRAIN, int(t * 997) % 400, axis=1), (img.shape[1], img.shape[0]))
    return np.clip(img + g[:, :, None] * 0.012, 0, 1)


if __name__ == '__main__':
    times = [float(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [i / FPS for i in range(int(FPS * DUR))]
    for i, t in enumerate(times):
        cv2.imwrite(os.path.join(OUT, f'f{i:04d}.jpg'), (frame(t)[:, :, ::-1] * 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 93])
