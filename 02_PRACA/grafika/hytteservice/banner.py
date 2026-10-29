from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import sys, os
UP='/root/.claude/uploads/84b0f863-608e-58eb-b395-0df36cf62c83/'
OUT='/home/user/moj-agent/02_PRACA/grafika/hytteservice/'
HY=Image.open(UP+'8db350cf-image.jpg').convert('RGB')
LA=Image.open(UP+'3c17270b-image.jpg').convert('RGB')
F='/usr/share/fonts/opentype/inter/'
def f(name,size): return ImageFont.truetype(F+name,size)
GREEN=(28,58,40); CREAM=(246,243,236); ACC=(214,190,120)

def photo_layer(img, W, H, zoom=1.0, ox=0.5, oy=0.5):
    s=max(W/img.width,H/img.height)*zoom
    im=img.resize((round(img.width*s),round(img.height*s)),Image.LANCZOS)
    x=round((im.width-W)*ox); y=round((im.height-H)*oy)
    im=im.crop((x,y,x+W,y+H))
    return ImageEnhance.Sharpness(im).enhance(1.15)

def text_block(d, x, y, scale=1.0, alpha=(1,1,1,1,1), W=None):
    def A(c,a): return c+(round(255*a),)
    k=f('Inter-SemiBold.otf',int(26*scale)); h=f('InterDisplay-Bold.otf',int(78*scale))
    b=f('Inter-Regular.otf',int(30*scale)); s=f('Inter-Medium.otf',int(28*scale)); c=f('Inter-SemiBold.otf',int(30*scale))
    d.text((x,y),"NYHET  ·  ISOKOR HYTTESERVICE",font=k,fill=A(ACC,alpha[0])); y+=int(62*scale)
    for line in ["Vi passer på","hytta di i vinter"]:
        d.text((x,y),line,font=h,fill=A(CREAM,alpha[1])); y+=int(90*scale)
    y+=int(30*scale)
    for line in ["Høstlukking, tilsyn hver 14. dag med bilder","og tilsynslogg til forsikringen, og våråpning","før 17. mai."]:
        d.text((x,y),line,font=b,fill=A(CREAM,alpha[2]*0.92)); y+=int(42*scale)
    y+=int(22*scale)
    d.text((x,y),"Vegårshei  ·  Tvedestrand  ·  Risør",font=s,fill=A(ACC,alpha[3])); y+=int(64*scale)
    # button
    t="Hele sesongen fra 11 990 kr  →"
    bw=d.textlength(t,font=c); pad=int(26*scale)
    d.rounded_rectangle((x,y,x+bw+2*pad,y+int(64*scale)),radius=int(32*scale),fill=A(CREAM,alpha[4]))
    d.text((x+pad,y+int(14*scale)),t,font=c,fill=A(GREEN,alpha[4]))

def desktop(t=None, zoom=1.0, photo=HY, alphas=(1,)*5, ox=0.55):
    W,H=1920,800; PW=1150
    base=Image.new('RGB',(W,H),GREEN)
    ph=photo_layer(photo,PW,H,zoom,ox,0.45)
    base.paste(ph,(W-PW,0))
    # soft blend from panel into photo
    g=Image.new('L',(260,H))
    for i in range(260): ImageDraw.Draw(g).line([(i,0),(i,H)],fill=int(255*(1-i/259)**1.6))
    base.paste(Image.new('RGB',(260,H),GREEN),(W-PW,0),g)
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
    text_block(d,110,150,1.0,alphas)
    return Image.alpha_composite(base.convert('RGBA'),ov).convert('RGB')

def mobile():
    W,H=1080,1350; PH=800
    base=Image.new('RGB',(W,H),GREEN)
    base.paste(photo_layer(HY,W,PH,1.0,0.6,0.45),(0,0))
    g=Image.new('L',(W,140))
    for i in range(140): ImageDraw.Draw(g).line([(0,i),(W,i)],fill=int(255*(i/139)**1.4))
    base.paste(Image.new('RGB',(W,140),GREEN),(0,PH-140),g)
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
    text_block(d,70,PH+10,0.86)
    return Image.alpha_composite(base.convert('RGBA'),ov).convert('RGB')

if __name__=='__main__':
    desktop().save(OUT+'hytteservice_banner_desktop_1920x800.jpg',quality=90,optimize=True,progressive=True)
    mobile().save(OUT+'hytteservice_banner_mobil_1080x1350.jpg',quality=90,optimize=True,progressive=True)
    print('ok')
