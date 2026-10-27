import sys
from PIL import Image, ImageDraw, ImageFont
src, font, out = sys.argv[1:4]
im = Image.open(src).convert('RGB'); px = im.load()
# find slogan bbox: white pixels in region x 440-800, y 200-270
xs=[];ys=[]
for y in range(206,275):
    for x in range(440,800):
        if sum(px[x,y])>600: xs.append(x); ys.append(y)
print('slogan bbox', min(xs),min(ys),max(xs),max(ys))
x0,y0,x1,y1=min(xs),min(ys),max(xs),max(ys)
d=ImageDraw.Draw(im)
d.rectangle([x0-4,y0-4,x1+6,y1+6], fill=(0,0,0))
# size: x-height match; SK slogan has ascenders (ť,h) and descender (ý) -> full height ~ size*1.0
f=ImageFont.truetype(font, 34)
text='vaske og beskytte'
# fit width similar to original
for s in range(26,44):
    f=ImageFont.truetype(font,s); b=d.textbbox((0,0),text,font=f)
    if b[3]-b[1] > (y1-y0): break
f=ImageFont.truetype(font,s-1); b=d.textbbox((0,0),text,font=f)
print('size',s-1,b)
d.text((x0-b[0], y0-b[1]), text, font=f, fill=(255,255,255))
im.save(out)
