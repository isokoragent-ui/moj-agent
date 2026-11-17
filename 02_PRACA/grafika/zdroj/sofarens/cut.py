# Vystrihne fľašu Sofa Cleaner z Lukovej fotky (rembg isnet) — vzor kjokkenpakken_jul/cut.py
from rembg import remove, new_session
from PIL import Image, ImageOps
s = new_session("isnet-general-use")
im = ImageOps.exif_transpose(Image.open("foto_sofa_cleaner.jpg")).convert("RGB")
print(im.size)
out = remove(im, session=s, post_process_mask=True)
out = out.crop(out.getbbox())
out.save("sofa_cut.png"); print(out.size)
