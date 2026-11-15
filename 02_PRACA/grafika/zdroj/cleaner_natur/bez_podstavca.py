"""⚠️ NEPOUŽITÉ (15. 11.): výsledok mal šmuhy a hrany — podstavec odstránil Luk v Gemini (prompt v PROMPTY_GEMINI.md).
Z obrázka 4 odstráni travertínový podstavec (stena = inpaint, ľan = klon zo spodku s vyrovnaním jasu).
Suroviny (pomaranč, list, céder, mandle) ostanú. Výstup: in/4b_bez_podstavca.jpg
Použitie: python3 bez_podstavca.py"""
import os
import numpy as np
import cv2

D = os.path.dirname(os.path.abspath(__file__))
im = cv2.imread(os.path.join(D, 'in', '4_podstavec.jpg')).astype(np.float32)
H, W = im.shape[:2]
HOR = 1712                                   # kde ľan stretá stenu

# oblasť podstavca + jeho vrhnutý tieň doprava
ped = np.zeros((H, W), np.uint8)
cv2.ellipse(ped, (767, 1690), (480, 70), 0, 0, 360, 255, -1)
cv2.rectangle(ped, (287, 1690), (1247, 2170), 255, -1)
cv2.ellipse(ped, (767, 2170), (480, 45), 0, 0, 180, 255, -1)
# suroviny pred podstavcom: ručné oblasti ∩ sýte/tmavé pixely
hsv = cv2.cvtColor(im.astype(np.uint8), cv2.COLOR_BGR2HSV)
hand = np.zeros((H, W), np.uint8)
cv2.ellipse(hand, (250, 2055), (190, 185), 0, 0, 360, 255, -1)       # pomaranč
cv2.fillPoly(hand, [np.array([(390, 2190), (520, 2080), (640, 2090), (760, 2280), (560, 2290), (400, 2230)])], 255)  # list
cv2.fillPoly(hand, [np.array([(900, 2290), (1000, 2070), (1200, 2060), (1420, 2120), (1400, 2260), (1050, 2300)])], 255)  # céder
obj = (hsv[:, :, 1] > 70).astype(np.uint8) * 255
obj = cv2.bitwise_and(obj, hand)
obj = cv2.morphologyEx(obj, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
obj = cv2.dilate(obj, np.ones((7, 7), np.uint8))
mask = cv2.bitwise_and(ped, cv2.bitwise_not(obj))

out = im.copy()
# 1) stena: inpaint v 1/4 + rozmazanie
wall = mask.copy(); wall[HOR + 20:] = 0
sm = cv2.resize(im.astype(np.uint8), (W // 4, H // 4), interpolation=cv2.INTER_AREA)
ms = cv2.dilate((cv2.resize(wall, (W // 4, H // 4)) > 0).astype(np.uint8), np.ones((3, 3), np.uint8))
fill = cv2.GaussianBlur(cv2.inpaint(sm, ms, 8, cv2.INPAINT_TELEA), (0, 0), 4)
fill = cv2.resize(fill, (W, H), interpolation=cv2.INTER_CUBIC).astype(np.float32)
# 2) ľan: jemná štruktúra (vysoké frekvencie) zo spodku pod mandľami, jas a tiene z okolia (inpaint)
TOP = 2340
lowsrc = cv2.resize(cv2.inpaint(sm, cv2.dilate((cv2.resize(mask, (W // 4, H // 4)) > 0).astype(np.uint8), np.ones((3, 3), np.uint8)), 10, cv2.INPAINT_TELEA), (W, H), interpolation=cv2.INTER_CUBIC).astype(np.float32)
lowsrc = cv2.GaussianBlur(lowsrc, (0, 0), 10)
hf = im - cv2.GaussianBlur(im, (0, 0), 14)
lin = np.zeros_like(im)
period = H - TOP
for y in range(HOR - 10, H):
    k = (y - (HOR - 10)) % (2 * period)
    sy = TOP + (k if k < period else 2 * period - 1 - k)      # zrkadlové opakovanie
    sy = min(H - 1, sy)
    scale = 0.55 + 0.45 * (y - HOR) / (2200 - HOR)              # vzadu jemnejšia štruktúra
    lin[y] = lowsrc[y] + hf[sy] * np.clip(scale, 0.5, 1.0)
# prechod stena → ľan cez horizont
t = np.clip((np.arange(H, dtype=np.float32) - (HOR - 8)) / 16, 0, 1)[:, None, None]
patch = fill * (1 - t) + lin * t
m = cv2.GaussianBlur(mask.astype(np.float32) / 255, (0, 0), 3)[:, :, None]
out = im * (1 - m) + patch * m
cv2.imwrite(os.path.join(D, 'in', '4b_bez_podstavca.jpg'), np.clip(out, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 95])
print('ok')
