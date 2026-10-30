# Produktová fotka Kjøkkenpakken: obe fľaše na svetlom pozadí (2048 × 2048)
from PIL import Image, ImageFilter
S = 2048
bg = Image.new("RGBA", (S, S), (244, 243, 239, 255))
a = Image.open("flaska_kjol.png"); b = Image.open("flaska_fett.png")
h = 1650
a = a.resize((round(a.width * h / a.height), h), Image.LANCZOS)
b = b.resize((round(b.width * h / b.height), h), Image.LANCZOS)
gap = -150
x0 = (S - (a.width + b.width + gap)) // 2 + 60
y0 = S - h - 170
for im, x in ((a, x0), (b, x0 + a.width + gap)):
    sh = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    ell = Image.new("RGBA", (im.width, 120), (0, 0, 0, 0))
    from PIL import ImageDraw
    ImageDraw.Draw(ell).ellipse((40, 20, im.width * 0.68, 100), fill=(0, 0, 0, 120))
    sh.alpha_composite(ell, (x, y0 + h - 70))
    bg = Image.alpha_composite(bg, sh.filter(ImageFilter.GaussianBlur(30)))
    bg.alpha_composite(im, (x, y0))
bg.convert("RGB").save("../../kjokkenpakken_produkt.jpg", quality=92)
print("ok")
