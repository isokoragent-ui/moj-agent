#!/usr/bin/env python3
"""Reel 9:16 zo statických fotiek: pomalý zoom/posun + text + prelínanie.

Použitie:  python3 video_reel.py <scenar.json> <vystup.mp4>
Scenár (JSON): {"scenes":[{"img":"cesta.jpg","text":"…","sub":"…","dur":2.6,
                 "zoom":[1.0,1.12],"focus":[0.5,0.5]}, …],
               "end":{"lines":["…"],"dur":3.5}}
Originály sa len čítajú (EXIF otočenie sa rieši tu).
"""
import json, subprocess, sys
from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageFilter

W, H, FPS, FADE = 1080, 1920, 30, 0.4
BOLD = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
MED = "/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf"
CREAM = (250, 245, 236)
INK = (40, 34, 30)
ACCENT = (176, 62, 52)   # teplá červená (nite na testovacích stehoch)


def load(path):
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    # pokrytie 9:16 s rezervou na zoom
    s = max(W / im.width, H / im.height) * 1.25
    return im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)


def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines


def caption_layer(text, sub):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if not text:
        return layer
    d = ImageDraw.Draw(layer)
    f, fs = ImageFont.truetype(BOLD, 74), ImageFont.truetype(MED, 46)
    lines = wrap(d, text, f, W - 220)
    slines = wrap(d, sub, fs, W - 220) if sub else []
    lh, slh = 92, 60
    boxh = len(lines) * lh + len(slines) * slh + 80
    y0 = 300  # horná tretina — spodok a pravý okraj zakrýva IG/FB rozhranie
    d.rounded_rectangle((70, y0, W - 70, y0 + boxh), 36, fill=(*CREAM, 238))
    d.rectangle((70, y0 + 30, 82, y0 + boxh - 30), fill=ACCENT)
    y = y0 + 40
    for ln in lines:
        d.text((110, y), ln, font=f, fill=INK); y += lh
    for ln in slines:
        d.text((110, y), ln, font=fs, fill=(95, 85, 78)); y += slh
    return layer


def frame(im, t, sc):
    z0, z1 = sc.get("zoom", [1.0, 1.1])
    fx, fy = sc.get("focus", [0.5, 0.5])
    z = z0 + (z1 - z0) * t
    cw, ch = im.width / 1.25 / z, im.height / 1.25 / z
    cw, ch = min(cw, im.width), min(ch, im.height)
    cw = ch * W / H if cw / ch > W / H else cw
    ch = cw * H / W
    cx = min(max(fx * im.width, cw / 2), im.width - cw / 2)
    cy = min(max(fy * im.height, ch / 2), im.height - ch / 2)
    box = (cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2)
    return im.resize((W, H), Image.BICUBIC, box=box)


def end_card(lines):
    im = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(im)
    y = 620
    for i, (txt, size, col, font) in enumerate(lines):
        f = ImageFont.truetype(BOLD if font == "b" else MED, size)
        for ln in wrap(d, txt, f, W - 160):
            d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=tuple(col))
            y += int(size * 1.3)
        y += 30
    return im


def main(spec_path, out):
    spec = json.load(open(spec_path))
    clips = []  # (počet snímok, funkcia index -> snímka) — šetrí pamäť
    for sc in spec["scenes"]:
        im = load(sc["img"]); cap = caption_layer(sc.get("text"), sc.get("sub"))
        n = int(sc.get("dur", 2.6) * FPS)
        clips.append((n, lambda i, im=im, cap=cap, sc=sc, n=n: Image.alpha_composite(
            frame(im, i / max(n - 1, 1), sc).convert("RGBA"), cap).convert("RGB")))
    e = spec["end"]; card = end_card(e["lines"])
    clips.append((int(e.get("dur", 3.5) * FPS), lambda i: card))

    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                           "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-f", "lavfi", "-i",
                           "anullsrc=r=44100:cl=stereo", "-shortest", "-c:v", "libx264", "-preset", "medium",
                           "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-movflags", "+faststart", out],
                          stdin=subprocess.PIPE)
    nf = int(FADE * FPS)
    for ci, (n, get) in enumerate(clips):
        last = ci == len(clips) - 1
        for i in range(nf if ci > 0 else 0, n if last else n - nf):
            ff.stdin.write(get(i).tobytes())
        if not last:
            n2, get2 = clips[ci + 1]
            for k in range(nf):
                ff.stdin.write(Image.blend(get(n - nf + k), get2(k), (k + 1) / (nf + 1)).tobytes())
    ff.stdin.close(); ff.wait()

if __name__ == "__main__":
    main(*sys.argv[1:3])
