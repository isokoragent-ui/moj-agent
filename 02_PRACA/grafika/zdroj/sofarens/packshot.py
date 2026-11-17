# Produktová fotka Sofarens: fľaša s novou etiketou na svetlom pozadí (2048 × 2048) — vzor ../kjokkenpakken_jul/packshot.py
from PIL import Image, ImageFilter, ImageDraw
S = 2048
bg = Image.new("RGBA", (S, S), (244, 243, 239, 255))
b = Image.open("flaska_sofarens.png")
h = 1780
k = h / b.height
b = b.resize((round(b.width * k), h), Image.LANCZOS)
body_cx = 642 * k                      # stred tela fľaše vo výreze (spúšť trčí doľava)
x = round(S / 2 - body_cx); y = S - h - 140
sh = Image.new("RGBA", (S, S), (0, 0, 0, 0))
bw = (980 - 305) * k
ImageDraw.Draw(sh).ellipse((x + 305 * k - 20, y + h - 55, x + 305 * k + bw + 60, y + h + 35), fill=(0, 0, 0, 110))
bg = Image.alpha_composite(bg, sh.filter(ImageFilter.GaussianBlur(28)))
bg.alpha_composite(b, (x, y))
bg.convert("RGB").save("../../sofarens_produkt.jpg", quality=92)
b.save("../../sofarens_flaska_bez_pozadia.png")
print("ok")
