import sys
from pypdf import PdfReader
from pypdf.generic import ContentStream
H=462.487
def mul(a,b):
    return [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3],a[4]*b[0]+a[5]*b[2]+b[4],a[4]*b[1]+a[5]*b[3]+b[5]]
def walk(ops):
    """yield (index, op, fillcolor, bbox_px) for each painting op"""
    ctm=[1,0,0,1,0,0];col=None;stack=[];pts=[];start=None
    for i,(a,o) in enumerate(ops):
        if o==b'q': stack.append((ctm,col))
        elif o==b'Q': ctm,col=stack.pop()
        elif o==b'cm': ctm=mul([float(x) for x in a],ctm)
        elif o in (b'k',b'g',b'rg',b'sc',b'scn'): col=(o.decode(),tuple(round(float(x),3) for x in a if not hasattr(x,'startswith')) )
        elif o in (b'm',b'l',b'c',b'v',b'y',b're'):
            if start is None: start=i
            v=[float(x) for x in a]
            if o==b're':
                x,y,w,h=v; v=[x,y,x+w,y+h,x,y+h,x+w,y]
            for j in range(0,len(v),2):
                x,y=v[j],v[j+1]
                pts.append((x*ctm[0]+y*ctm[2]+ctm[4], x*ctm[1]+y*ctm[3]+ctm[5]))
        elif o in (b'f',b'f*',b'F',b'S',b's',b'B',b'B*',b'b',b'b*',b'n',b'Do'):
            if o==b'Do':
                p0=[(ctm[4],ctm[5]),(ctm[0]+ctm[4],ctm[1]+ctm[5]),(ctm[2]+ctm[4],ctm[3]+ctm[5]),(ctm[0]+ctm[2]+ctm[4],ctm[1]+ctm[3]+ctm[5])]
                s=i
            else: p0=pts; s=start
            if p0:
                xs=[p[0] for p in p0];ys=[p[1] for p in p0]
                bb=(min(xs)/0.72,(H-max(ys))/0.72,max(xs)/0.72,(H-min(ys))/0.72)
                yield (s,i,o,col,bb,a)
            pts=[];start=None
if __name__=='__main__':
    r=PdfReader(sys.argv[1]);p=r.pages[0]
    ops=ContentStream(p.get_contents(),r).operations
    for s,i,o,col,bb,a in walk(ops):
        if o==b'Do' or o!=b'f' : print(s,i,o,col,[round(x) for x in bb],a if o==b'Do' else '')
