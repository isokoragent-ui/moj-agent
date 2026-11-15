"""Vystrihne fľaše EcoNeutral z Lukových fotiek (rembg isnet) + očistenie (najväčší kus, bez odrezkov).
Použitie: python3 vystrihni_flase.py → flasa_500ml.png, flasa_100ml.png (+ výpis rozmerov pre video)"""
import numpy as np, cv2
from rembg import remove, new_session
from PIL import Image, ImageOps
s = new_session("isnet-general-use")
for src, dst in [("in/flasa_500ml_foto.jpg", "flasa_500ml.png"), ("in/flasa_100ml_foto.jpg", "flasa_100ml.png")]:
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    out = np.asarray(remove(im, session=s, post_process_mask=True)).copy()
    a = out[:, :, 3]
    n, lab, st, _ = cv2.connectedComponentsWithStats((a > 128).astype(np.uint8), 8)
    big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
    out[:, :, 3] = a * cv2.dilate((lab == big).astype(np.uint8), np.ones((5, 5), np.uint8))
    ys, xs = np.where(out[:, :, 3] > 10)
    out = out[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    Image.fromarray(out).save(dst)
    a = out[:, :, 3]; h = a.shape[0]
    for y in (int(h * .6), int(h * .9), h - 12):
        r = np.where(a[y] > 128)[0]; print(dst, out.shape[:2], 'y', y, 'x', r.min(), r.max(), 'stred', (r.min() + r.max()) / 2)
