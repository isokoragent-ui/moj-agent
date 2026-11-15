"""Vystrihne fľašu z Lukovej fotky (rembg isnet, ako ../kjokkenpakken_jul/cut.py).
Použitie: python3 vystrihni_flasu.py  → flasa_cleaner_nova.png"""
from rembg import remove, new_session
from PIL import Image, ImageOps
s = new_session("isnet-general-use")
im = ImageOps.exif_transpose(Image.open("in/flasa_cleaner_nova_foto.jpg")).convert("RGB")
out = remove(im, session=s, post_process_mask=True)
out = out.crop(out.getbbox())
out.save("flasa_cleaner_nova.png"); print(im.size, out.size)

# očistenie: len najväčší súvislý kus (preč odrezky kartónu) + hlava rozprašovača bez hnedého nádychu kartónu
import numpy as np, cv2
a = np.asarray(out).astype(np.float32)
alpha = a[:, :, 3]
n, lab, st, _ = cv2.connectedComponentsWithStats((alpha > 128).astype(np.uint8), 8)
big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
keep = cv2.dilate((lab == big).astype(np.uint8), np.ones((5, 5), np.uint8)).astype(np.float32)
a[:, :, 3] = alpha * keep
a[:48, 560:900, 3] = 0                          # odrezok kartónu nad hlavou
HEAD = 1000                                      # hlava + spúšť (nad etiketou)
rgb = a[:HEAD, :, :3]
lum = rgb @ np.array([0.299, 0.587, 0.114], np.float32)
neutral = np.stack([lum * 1.0, lum * 0.99, lum * 0.97], -1) * 1.04
w = np.clip((HEAD - np.arange(HEAD, dtype=np.float32)) / 120, 0, 1)[:, None, None]   # plynulý prechod k telu
a[:HEAD, :, :3] = rgb * (1 - 0.85 * w) + neutral * 0.85 * w
Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save("flasa_cleaner_nova.png")
ys, xs = np.where(a[:, :, 3] > 128)
for y in (2500, 2900, ys.max() - 10):
    r = np.where(a[y, :, 3] > 128)[0]; print('y', y, 'x', r.min(), r.max(), 'stred', (r.min() + r.max()) / 2)
print('spodok', ys.max())
