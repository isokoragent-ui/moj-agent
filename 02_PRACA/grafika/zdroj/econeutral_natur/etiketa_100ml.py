"""Etiketa EcoNeutral pre 100 ml fľašu VO VIDEU: kópia novej NO etikety 500 ml, len „500ml“ → „100ml“
(Luk 15. 11.: „etikety budú rovnaké, len rozdiel vo veľkosti“). Nie je to tlačová etiketa —
na tlač treba rozmer 100 ml etikety od výrobcu.
Použitie: python3 etiketa_100ml.py → etiketa_econeutral_100ml_video.png"""
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SRC = '../../../etikety/Isokor_EcoNeutral_500ml_etikett_NO.png'
KHAND = '../../../sikkerhetsdatablad/zdroj/Khand-Bold.ttf'
im = Image.open(SRC).convert('RGB')
a = np.asarray(im).astype(int)
BOX = (1290, 1270, 1540, 1385)                          # okolie nápisu „500ml“
reg = a[BOX[1]:BOX[3], BOX[0]:BOX[2]]
green = (reg[:, :, 1] - reg[:, :, 0] > 40)              # zelené písmo
ys, xs = np.where(green)
x0, y0, x1, y1 = xs.min() + BOX[0], ys.min() + BOX[1], xs.max() + BOX[0], ys.max() + BOX[1]
col = tuple(int(c) for c in np.median(reg[green], axis=0))
print('500ml bbox', (x0, y0, x1, y1), 'farba', col)

# veľkosť písma: „500ml“ v Khand Bold musí mať rovnakú výšku ako originál
size = 10
while True:
    f = ImageFont.truetype(KHAND, size + 1)
    bb = f.getbbox('500ml')
    if bb[3] - bb[1] > (y1 - y0):
        break
    size += 1
f = ImageFont.truetype(KHAND, size)
bb = f.getbbox('500ml')
d = ImageDraw.Draw(im)
d.rectangle((x0 - 4, y0 - 4, x1 + 4, y1 + 4), fill=(255, 255, 255))
d.text((x0 - bb[0], y0 - bb[1]), '100ml', font=f, fill=col)
im.save('etiketa_econeutral_100ml_video.png')
im.crop(BOX).save('/tmp/claude-0/-home-user-moj-agent/c4e2cb7e-8354-5ae8-933f-aa0f52d34aa4/scratchpad/lbl100.png')
print('ok, písmo', size)
