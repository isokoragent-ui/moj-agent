# Vystrihne fľašu Sofarens s novou etiketou (Lukov obrázok 18. 11.) — vzor cut.py
from rembg import remove, new_session
from PIL import Image, ImageOps
import numpy as np, cv2
s = new_session("isnet-general-use")
im = ImageOps.exif_transpose(Image.open("foto_sofarens_nova_etiketa.jpg")).convert("RGB")
out = remove(im, session=s, post_process_mask=True)
a = np.array(out); m = (a[..., 3] > 20).astype(np.uint8)
n, cc, st, _ = cv2.connectedComponentsWithStats(m)
big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA]); a[..., 3] = np.where(cc == big, a[..., 3], 0)
out = Image.fromarray(a); out = out.crop(out.getbbox())
out.save("flaska_sofarens_nova.png"); print(out.size)
