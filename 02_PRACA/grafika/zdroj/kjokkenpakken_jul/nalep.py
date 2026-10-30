# Nalepí nórsku etiketu na fotku fľaše (cylindrické ohnutie + tieň z fotky).
# python3 nalep.py <etiketa.png> <vystup.png>
import sys, numpy as np, cv2
from PIL import Image
from scipy.ndimage import median_filter, gaussian_filter1d

bottle = np.array(Image.open("cleaner_cut.png").convert("RGBA")).astype(np.float32)
lab = np.array(Image.open(sys.argv[1]).convert("RGB")).astype(np.float32)
LH, LW = lab.shape[:2]
H, W = bottle.shape[:2]

# geometria fľaše vo fotke (merané na mriežke)
Y0, Y1 = 1335.0, 2790.0          # horná / spodná hrana etikety na bokoch
E0, E1 = 35.0, 45.0              # prehnutie hrany (elipsa) hore / dole
L0, L1 = 48.0, 95.0              # ľavý okraj fľaše hore / dole
R0, R1 = 780.0, 738.0            # pravý okraj
PX_RAD = 400.0                   # px etikety na radián
CENTER_LX = 663 * 1.0            # stred čelného panelu v etikete (px)
THETA_C = -0.10                  # kde je stred panelu na fľaši

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
ly = (v * (LH - 1)).astype(np.float32)
warped = cv2.remap(lab, lx, ly, cv2.INTER_AREA if False else cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

# farba "bielej" etikety vo fotke po stĺpcoch (riadok nad logom, prázdna etiketa)
row = bottle[1440:1470, :, :3].mean(axis=0)
top = bottle[1240:1260, :, :3].mean(axis=0)
k = row[690] / np.maximum(top[690], 1)
row[690:] = top[690:] * k          # vpravo na starej etikete je text → berieme plast nad etiketou
row = median_filter(row, size=(61, 1))
row = gaussian_filter1d(row, 15, axis=0)
# jemný zvislý priebeh svetla (stred fľaše, prázdne miesta)
white = row[None, :, :] / 255.0
out = bottle.copy()
col = warped / 255.0 * white * 255.0 * 1.04
out[..., :3] = np.where(inside[..., None], np.clip(col, 0, 255), bottle[..., :3])
# len najväčší súvislý kus (zvyšky pozadia pri spúšti preč)
a = (out[..., 3] > 20).astype(np.uint8)
n, cc, st, _ = cv2.connectedComponentsWithStats(a)
big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
out[..., 3] = np.where(cc == big, out[..., 3], 0)
out[:40, :, 3] = 0                 # zúbky nad spúšťou
# vyrovnanie expozície (fotka z miestnosti je šedá)
m = out[..., 3] > 128
p = np.percentile(out[..., :3][m], 99.5)
out[..., :3] = np.clip((out[..., :3] / p) ** 0.8 * 255, 0, 255)
Image.fromarray(out.astype(np.uint8)).save(sys.argv[2])
print("ok", sys.argv[2])
