"""Video Cleaner v3 — jednoduchšie (Luk 15. 11.): bez kuchyne, fľaša veľká na ľane medzi surovinami (in/4b, Gemini bez podstavca).
Použitie: python3 video2.py VYSTUP_PRIECINOK [časy oddelené čiarkou = len kontrolné snímky]
Výstup: snímky f0000.jpg … (30 fps, 12 s, 1080×1920). Potom ffmpeg (pozri README grafiky)."""
import os, sys
import numpy as np
import cv2

D = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
FPS, DUR = 30, 18.0          # 15. 11.: zábery predĺžené (Luk: viac času na čítanie textov)
W, H = 1080, 1920


def load(name):
    return cv2.imread(os.path.join(D, 'in', name))[:, :, ::-1].astype(np.float32) / 255


def load_rgba(path):
    im = cv2.imread(path, cv2.IMREAD_UNCHANGED).astype(np.float32) / 255
    im = im[:, :, [2, 1, 0, 3]]
    im[:, :, :3] *= im[:, :, 3:4]          # premultiplied
    return im


IMG = {k: load(f) for k, f in [(1, '1_sad.jpg'), (2, '2_suroviny.jpg'), (3, '3_kvapka.jpg'),
                                  (4, '4b_bez_podstavca.jpg')]}
SH, SW = IMG[1].shape[:2]                  # 2752 × 1536
BASE = max(SW / W, SH / H)                 # zdrojové px na výstupný px
BOT = load_rgba(os.path.join(D, '..', 'kjokkenpakken_jul', 'flaska_fett.png'))   # nórska etiketa FETT- OG FLEKKFJERNER (Luk 15. 11.)
BOT[:, :, :3] *= np.array([1.0, 0.985, 0.95], np.float32)   # teplejšie, nech sedí k rannému svetlu
BH, BW = BOT.shape[:2]
NOZ = np.array([1145.0, 200.0])           # ústie hubice v obrázku fľaše (strieka doprava)
BODY_X, BODY_Y = 414.0, 2992.0             # stred dna fľaše
TXT = {k: load_rgba(os.path.join(D, 'texty', k + '.png')) for k in ['t1', 't2', 't3', 't4', 't6', 't7']}

clamp = lambda x, a=0.0, b=1.0: max(a, min(b, x))
lin = lambda t, a, b: clamp((t - a) / (b - a))


def ease(x):
    return 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2


def eout(x):
    return 1 - (1 - x) ** 3


def win(t, a, b, fi=.5, fo=.5):
    return min(ease(lin(t, a, a + fi)), 1 - ease(lin(t, b - fo, b)))


# ---------- pomocné: kamera a skladanie ----------
def camera(src, zoom, cx, cy, rot=0.0):
    """Výrez zo zdroja: stred (cx,cy) v zdrojových px, zoom 1 = celý obraz na výšku."""
    s = BASE / zoom
    a = np.deg2rad(rot)
    M = np.array([[s * np.cos(a), -s * np.sin(a), 0], [s * np.sin(a), s * np.cos(a), 0]], np.float32)
    M[:, 2] = np.array([cx, cy]) - M[:, :2] @ np.array([W / 2, H / 2])
    return cv2.warpAffine(np.ascontiguousarray(src, np.float32), M, (W, H), flags=cv2.INTER_CUBIC | cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REFLECT)


def over(dst, layer, op=1.0):
    """layer = premultiplied RGBA rovnakej veľkosti."""
    a = layer[:, :, 3:4] * op
    return dst * (1 - a) + layer[:, :, :3] * op


def place(sprite, M, size):
    """sprite (premult RGBA) → plátno size=(w,h) cez maticu sprite→plátno."""
    return cv2.warpAffine(sprite, M.astype(np.float32), size, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))


def bottle_standing(h, bx, by):
    s = h / BH
    return np.array([[s, 0, bx - s * BODY_X], [0, s, by - s * BODY_Y]])


def bottle_spray(h, nx, ny, deg):
    """Fľaša zrkadlovo otočená (strieka doľava) a natočená o deg proti smeru hodín; ústie v (nx,ny)."""
    s = h / BH
    d = np.deg2rad(deg)
    R = np.array([[np.cos(d), np.sin(d)], [-np.sin(d), np.cos(d)]])
    F = np.array([[-1, 0], [0, 1]])
    A = s * R @ F
    noz_f = NOZ
    b = np.array([nx, ny]) - A @ noz_f
    return np.hstack([A, b[:, None]]), np.array([-np.cos(d), np.sin(d)])


def soft_ellipse(size, cx, cy, rx, ry, ang=0, blur=25):
    m = np.zeros((size[1], size[0]), np.float32)
    cv2.ellipse(m, (int(cx), int(cy)), (int(rx), int(ry)), ang, 0, 360, 1.0, -1)
    k = int(blur) * 2 + 1
    return cv2.GaussianBlur(m, (k, k), 0)


# ---------- príprava scény 3: kvapka oddelená od pozadia ----------
def drop_halfwidth(y):
    if y < 885 or y > 1342:
        return 0.0
    if y < 1150:
        u = clamp((y - 885) / (1150 - 885))
        return 50 + (179 - 50) * (u ** 0.85)
    return 179 * np.sqrt(max(0.0, 1 - ((y - 1150) / 192) ** 2))


I3 = IMG[3]
dmask = np.zeros(I3.shape[:2], np.float32)
for y in range(870, 1350):
    hw = drop_halfwidth(y)
    if hw > 0:
        cx = 757 + (767 - 757) * clamp((y - 885) / 200)
        dmask[y, int(cx - hw):int(cx + hw) + 1] = 1
dmask_soft = cv2.GaussianBlur(dmask, (7, 7), 0)
# pozadie bez kvapky: inpaint v 1/4 rozlíšení + rozmazanie (pozadie je aj tak rozostrené)
small = cv2.resize((I3 * 255).astype(np.uint8), (SW // 4, SH // 4), interpolation=cv2.INTER_AREA)
msmall = cv2.dilate((cv2.resize(dmask, (SW // 4, SH // 4)) > 0.05).astype(np.uint8), np.ones((5, 5), np.uint8))
fill = cv2.inpaint(small, msmall, 9, cv2.INPAINT_TELEA)
fill = cv2.GaussianBlur(fill, (0, 0), 6)
fill = cv2.resize(fill, (SW, SH), interpolation=cv2.INTER_CUBIC).astype(np.float32) / 255
mbig = cv2.GaussianBlur(cv2.dilate(dmask, np.ones((25, 25), np.uint8)), (0, 0), 6)[:, :, None]
PLATE3 = I3 * (1 - mbig) + fill * mbig
DROP = np.dstack([I3 * dmask_soft[:, :, None], dmask_soft])  # premult
DX0, DY0 = 757, 885                         # bod úchytu kvapky

# ---------- scény ----------
def scene1(t):  # sad, 0–2.9
    u = lin(t, 0, 2.9)
    img = camera(IMG[1], 1.0 + 0.08 * ease(u), 780 + 40 * u, 1400 + 10 * u)
    # ranný opar za textom
    fog = soft_ellipse((W, H), 540, 420, 560, 260, blur=120)
    img = img * (1 - fog[:, :, None] * .42) + fog[:, :, None] * .42 * np.array([.97, .93, .85], np.float32)
    # dýchajúce ranné svetlo zľava
    g = soft_ellipse((W, H), 80, 760, 520, 820, blur=160)
    img = img + g[:, :, None] * np.array([1.0, .82, .55]) * (0.10 + 0.05 * np.sin(t * 2.2))
    # prach v svetle
    r2 = np.random.default_rng(3)
    for i in range(70):
        x0, y0 = r2.random() * 600, 200 + r2.random() * 1400
        x = x0 + 25 * t + 10 * np.sin(t * .8 + i)
        y = y0 - 18 * t
        a = 0.35 * (0.5 + 0.5 * np.sin(t * 1.5 + i * 1.7))
        cv2.circle(img, (int(x), int(y)), 2 + (i % 3), (1.0, .95, .85), -1, lineType=cv2.LINE_AA) if a > .45 else None
    return img


def scene2(t):  # suroviny, 2.5–5.3
    u = lin(t, 2.5, 5.3)
    src = IMG[2]
    # záblesky na kvapkách oleja
    for i, (x, y) in enumerate([(1000, 1470), (1101, 1541), (1005, 1693), (1060, 1620)]):
        a = np.exp(-((t - 3.0 - i * .45) / .18) ** 2)
        if a > .02:
            fl = np.zeros((SH, SW), np.float32)
            cv2.line(fl, (x - 46, y), (x + 46, y), 0.7, 2, cv2.LINE_AA)
            cv2.line(fl, (x, y - 46), (x, y + 46), 0.7, 2, cv2.LINE_AA)
            fl = cv2.GaussianBlur(fl, (0, 0), 1.2) + soft_ellipse((SW, SH), x, y, 16, 16, blur=9) * 0.8
            src = src + fl[:, :, None] * a * np.array([1, .97, .85], np.float32)
    return camera(src, 1.12 + 0.08 * ease(u), 768 + 30 * u, 1430 + 50 * u, rot=-1.5 * u)   # zoom ≥1,12 → kamera nevyjde z obrázka


def scene3(t):  # kvapka, 4.9–7.4
    u = lin(t, 4.9, 7.4)
    src = PLATE3.copy()
    swell = 1 + 0.05 * ease(lin(t, 5.0, 5.95))
    tf = max(0.0, t - 5.95)
    fall = 0.5 * 8000 * tf ** 2
    vel = 8000 * tf
    sx = 1 + 0.04 * min(1, tf * 4)
    sy = swell * (1 - 0.06 * min(1, tf * 4))
    wob = 3 * np.sin(t * 9) * (1 - lin(t, 5.0, 5.95)) * lin(t, 4.9, 5.2)
    M = np.array([[sx, 0, DX0 - sx * DX0 + wob], [0, sy, DY0 - sy * DY0 + fall]])
    spr = DROP
    if vel > 50:
        k = int(min(120, vel / FPS * 0.6)) | 1
        ker = np.zeros((k, 1), np.float32); ker[:] = 1.0 / k
        spr = cv2.filter2D(DROP, -1, ker)
    lay = place(spr, M, (SW, SH))
    src = over(src, lay)
    return camera(src, 1.0 + 0.07 * ease(u), 768, 1300 + 120 * u)


BASE_PT = np.array([767.0, 2350.0])        # kde fľaša stojí na ľane (stred dna)


def scene_bottle(t):  # fľaša medzi surovinami, 6.7–12
    u = lin(t, 6.7, 12.0)
    src = IMG[4].copy()
    h = 1350
    k = lin(t, 6.95, 8.0)
    near = eout(k)
    op = ease(clamp(k * 2.2))
    by = BASE_PT[1] - 240 * (1 - near)
    # tieň: kontaktný pod dnom + mäkký vrhnutý doprava dozadu (svetlo zľava hore)
    sh = soft_ellipse((SW, SH), BASE_PT[0] + 8, BASE_PT[1] - 6, 185, 32, blur=14) * 0.6 * near
    sh2 = soft_ellipse((SW, SH), BASE_PT[0] + 300, BASE_PT[1] - 60, 330, 55, ang=-8, blur=55) * 0.30 * near
    shade = np.clip(sh + sh2, 0, 1)[:, :, None] * op
    src = src * (1 - shade * np.array([0.55, 0.6, 0.68], np.float32))
    lay = place(BOT, bottle_standing(h, BASE_PT[0], by), (SW, SH))
    # svetlo zľava (ako lúč na stene): ľavá strana fľaše teplejšia a svetlejšia, pravá v tieni
    gx = np.clip((np.arange(SW, dtype=np.float32) - (BASE_PT[0] - 200)) / 400, 0, 1)[None, :, None]
    lay = lay.copy()
    lay[:, :, :3] *= (1.14 - 0.16 * gx) * np.array([1.0, 0.985, 0.955], np.float32)   # fotka fľaše bola v šere → +8 %
    sweep = lin(t, 8.3, 9.3)
    if 0 < sweep < 1:  # svetelný prechod cez fľašu
        xx = np.arange(SW, dtype=np.float32)[None, :]
        yy = np.arange(SH, dtype=np.float32)[:, None]
        band = np.exp(-(((xx - (BASE_PT[0] - 400 + 800 * sweep)) + (yy - 1700) * 0.35) / 60) ** 2) * np.sin(np.pi * sweep)
        lay = lay.copy()
        lay[:, :, :3] += band[:, :, None] * 0.25 * lay[:, :, 3:4]
    src = over(src, lay, op)
    return camera(src, 1.05 + 0.04 * ease(u), 767, 1440)


# (scéna, začiatok, koniec v novom videu, pôvodný začiatok, pôvodný koniec) — pohyb scény sa spomalí úmerne
SCENES = [(scene1, 0, 4.2, 0, 2.9), (scene2, 3.8, 7.6, 2.5, 5.3), (scene3, 7.2, 10.8, 4.9, 7.1), (scene_bottle, 10.4, 18.01, 6.7, 12.01)]
TEXTS = [('t1', .6, 3.9, .6, .5), ('t2', 4.3, 7.3, .6, .5), ('t3', 7.8, 10.4, .6, .5), ('t4', 12.0, 14.2, .6, .5),
         ('t6', 14.6, 99, .7, .1), ('t7', 15.2, 99, .6, .1)]

GRAIN = np.random.default_rng(1).normal(0, 1, (H // 2, W // 2)).astype(np.float32)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
VIG = 1 - 0.22 * np.clip(((xx - W / 2) / (W * .62)) ** 2 + ((yy - H / 2) / (H * .62)) ** 2, 0, 1.5)[:, :, None]


def frame(t):
    img = None
    for fn, a, b, oa, ob in SCENES:
        if a <= t < b:
            op = min(ease(lin(t, a, a + 0.4)) if a > 0 else 1, 1 - ease(lin(t, b - 0.4, b)) if b < DUR else 1)
            f = fn(oa + (t - a) * (ob - oa) / (b - a))
            img = f if img is None else img * (1 - op) + f * op
    for k, a, b, fi, fo in TEXTS:
        op = win(t, a, b, fi, fo)
        if op > 0:
            tx = TXT[k]
            dy = int((1 - op) * 24)
            if dy:
                tx = np.roll(tx, dy, axis=0)
            img = over(img, tx, op)
    img = img * VIG
    g = cv2.resize(np.roll(GRAIN, int(t * 997) % 400, axis=1), (W, H))
    img = img + g[:, :, None] * 0.012
    return np.clip(img, 0, 1)


if __name__ == '__main__':
    times = [float(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [i / FPS for i in range(int(FPS * DUR))]
    for i, t in enumerate(times):
        f = frame(t)
        cv2.imwrite(os.path.join(OUT, f'f{i:04d}.jpg'), (f[:, :, ::-1] * 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 93])
