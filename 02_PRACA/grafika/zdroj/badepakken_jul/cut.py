import sys
from rembg import remove, new_session
from PIL import Image
s = new_session("isnet-general-use")
for src, dst in [("in/ce483590-image.jpg","lm.png"),("in/71a8187e-image.jpg","bath.png")]:
    im = Image.open(src).convert("RGB")
    out = remove(im, session=s, post_process_mask=True)
    out = out.crop(out.getbbox())
    out.save(dst)
    print(dst, out.size)
