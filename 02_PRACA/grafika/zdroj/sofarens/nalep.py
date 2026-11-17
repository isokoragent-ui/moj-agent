# Nalepí nórsku etiketu Sofarens na Lukovu fotku fľaše Sofa Cleaner (vzor ../kjokkenpakken_jul/nalep.py).
# python3 nalep.py ../../../etikety/Isokor_Sofarens_500ml_etikett_NO.png flaska_sofarens.png
import sys, numpy as np, cv2
from PIL import Image
from scipy.ndimage import median_filter, gaussian_filter1d

bottle = np.array(Image.open("sofa_cut.png").convert("RGBA")).astype(np.float32)
lab = np.array(Image.open(sys.argv[1]).convert("RGB")).astype(np.float32)
LH, LW = lab.shape[:2]
H, W = bottle.shape[:2]

# geometria (merané na mriežke sofa_cut.png, 17. 11. 2026)
Y0, Y1 = 1062.0, 2636.0          # horná / spodná hrana etikety na bokoch
E0, E1 = 3.0, 15.0               # prehnutie hrany hore / dole (fotené zhora → dole viac)
L0, L1 = 303.0, 338.0            # ľavý okraj fľaše hore / dole
R0, R1 = 981.0, 979.0            # pravý okraj
PX_RAD = 354.0                   # px etikety na radián (polomer 339 px × 1654/1586)
CENTER_LX = 649.0                # stred čelného panelu v etikete (px pri 300 dpi)
THETA_C = -0.28                  # kde je stred panelu na fľaši (posunuté doľava, aby logo a podnadpis neboli na hrane)

ys, xs = np.mgrid[0:H, 0:W].astype(np.float32)
v = (ys - Y0) / (Y1 - Y0)
for _ in range(4):
    vc = np.clip(v, 0, 1)
    xl = L0 + (L1 - L0) * vc; xr = R0 + (R1 - R0) * vc
    cx = (xl + xr) / 2; r = (xr - xl) / 2
    s = np.clip((xs - cx) / r, -1, 1)
    th = np.arcsin(s)
    e = E0 + (E1 - E0) * vc
    v = (ys - Y0 - e * np.cos(th)) / (Y1 - Y0)
inside = (v >= 0) & (v <= 1) & (np.abs((xs - cx) / r) < 1) & (bottle[..., 3] > 128)

lx = ((CENTER_LX + (th - THETA_C) * PX_RAD) % LW).astype(np.float32)
ly = (np.clip(v, 0, 1) * (LH - 1)).astype(np.float32)
warped = cv2.remap(lab, lx, ly, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

# svetlo: stará etiketa je celá potlačená → farba bieleho plastu nad a pod etiketou, po stĺpcoch, prelínaná podľa výšky
def band(y0, y1):
    row = bottle[y0:y1, :, :3].mean(axis=0)
    row = median_filter(row, size=(41, 1))
    return gaussian_filter1d(row, 12, axis=0)
top, bot = band(1015, 1045), band(2655, 2670)
vc = np.clip(v, 0, 1)[..., None]
white = (top[None] * (1 - vc) + bot[None] * vc) / 255.0
out = bottle.copy()
col = warped * white * 1.04
out[..., :3] = np.where(inside[..., None], np.clip(col, 0, 255), bottle[..., :3])
# len najväčší súvislý kus
a = (out[..., 3] > 20).astype(np.uint8)
n, cc, st, _ = cv2.connectedComponentsWithStats(a)
big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
out[..., 3] = np.where(cc == big, out[..., 3], 0)
# vyrovnanie expozície (fotka z miestnosti je teplá a šedá)
m = out[..., 3] > 128
p = np.percentile(out[..., :3][m], 99.5, axis=0)
out[..., :3] = np.clip((out[..., :3] / p) ** 0.8 * 255, 0, 255)
Image.fromarray(out.astype(np.uint8)).save(sys.argv[2])
print("ok", sys.argv[2])
