"""Nalepí etiketu na vystrihnutú fotku fľaše (ohnutie po valci, svetlo a tiene z fotky) — všeobecná verzia
../kjokkenpakken_jul/nalep.py (tá má geometriu natvrdo pre 500 ml fľašu). Geometria sa meria na mriežke.
Použitie: python3 nalep_valec.py FLASA.png ETIKETA.png VYSTUP.png Y0 Y1 E XL0 XL1 XR0 XR1 [THETA_C]
  Y0/Y1 = horná/spodná hrana etikety na boku, E = prehnutie hrany (elipsa, px),
  XL0/XL1, XR0/XR1 = ľavý/pravý okraj fľaše pri Y0 / Y1, THETA_C = kde je stred čelného panelu (rad).
100 ml EcoNeutral: python3 nalep_valec.py flasa_100ml.png etiketa_econeutral_100ml_video.png flasa_100ml_nova_etiketa.png 815 2075 22 4 8 560 540 -0.25"""
import sys
import numpy as np, cv2
from PIL import Image
from scipy.ndimage import gaussian_filter1d

bottle = np.array(Image.open(sys.argv[1]).convert('RGBA')).astype(np.float32)
lab = np.array(Image.open(sys.argv[2]).convert('RGB')).astype(np.float32)
Y0, Y1, E, L0, L1, R0, R1 = [float(v) for v in sys.argv[4:11]]
THETA_C = float(sys.argv[11]) if len(sys.argv) > 11 else -0.05
LH, LW = lab.shape[:2]
H, W = bottle.shape[:2]
PX_RAD = LW / (2 * np.pi)              # etiketa obopína celý obvod
CENTER_LX = 663 / 2479 * LW            # stred čelného panelu (logo + názov) v etikete

ys, xs = np.mgrid[0:H, 0:W].astype(np.float32)
v = (ys - Y0) / (Y1 - Y0)
for _ in range(4):
    vc = np.clip(v, 0, 1)
    xl = L0 + (L1 - L0) * vc; xr = R0 + (R1 - R0) * vc
    cx = (xl + xr) / 2; r = (xr - xl) / 2
    th = np.arcsin(np.clip((xs - cx) / r, -1, 1))
    v = (ys - Y0 - E * np.cos(th)) / (Y1 - Y0)
inside = (v >= 0) & (v <= 1) & (np.abs((xs - cx) / r) < 0.995) & (bottle[..., 3] > 128)

lx = ((CENTER_LX + (th - THETA_C) * PX_RAD) % LW).astype(np.float32)
ly = (v * (LH - 1)).astype(np.float32)
warped = cv2.remap(lab, lx, ly, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

# svetlo po stĺpcoch: najsvetlejšie (biele) miesta starej etikety v každom stĺpci, vyhladené
band = bottle[int(Y0) + 20:int(Y1) - 20, :, :3]
lum = band.mean(2)
white = np.zeros((W, 3), np.float32)
for x in range(W):
    col = band[:, x][lum[:, x] >= np.percentile(lum[:, x], 85)] if lum[:, x].max() > 0 else None
    white[x] = col.mean(0) if col is not None and len(col) else 0
white = gaussian_filter1d(white, 12, axis=0)
out = bottle.copy()
colr = warped / 255.0 * white[None, :, :] * 1.03
out[..., :3] = np.where(inside[..., None], np.clip(colr, 0, 255), bottle[..., :3])
Image.fromarray(out.astype(np.uint8)).save(sys.argv[3])
print('ok', sys.argv[3])
