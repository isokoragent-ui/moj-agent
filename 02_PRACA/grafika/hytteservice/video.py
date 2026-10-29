import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from banner import desktop, HY, LA
from PIL import Image

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'frames')
os.makedirs(D, exist_ok=True)
FPS = 25; T = 10.0; N = int(FPS * T)


def ease(x):
    return 0 if x < 0 else 1 if x > 1 else x * x * (3 - 2 * x)


for i in range(N):
    t = i / FPS
    out = ease((t - 9.2) / 0.8)
    a = [ease((t - 0.3 - 0.35 * k) / 0.8) * (1 - out) for k in range(5)]
    f = desktop(zoom=1.0 + 0.07 * (t / 6.5), photo=HY, alphas=a)
    m = ease((t - 5.5) / 1.0)
    if m > 0:
        f2 = desktop(zoom=1.0 + 0.06 * max(0, (t - 5.5) / 4.5), photo=LA, alphas=a, ox=0.5)
        f = Image.blend(f, f2, m)
    if t > 9.2:
        f = Image.blend(f, desktop(zoom=1.0, photo=HY, alphas=(0,) * 5), out)
    f.save(os.path.join(D, f'{i:04d}.jpg'), quality=92)
print(N)
