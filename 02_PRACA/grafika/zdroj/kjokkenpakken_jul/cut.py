from rembg import remove, new_session
from PIL import Image, ImageOps
s = new_session("isnet-general-use")
im = ImageOps.exif_transpose(Image.open("in/cleaner_foto.jpg")).convert("RGB")
print(im.size)
out = remove(im, session=s, post_process_mask=True)
out = out.crop(out.getbbox())
out.save("cleaner_cut.png"); print(out.size)
