"""Prispôsobí Lukovu skladbu dĺžke videa: začiatok skladby + strih na úder taktu do jej záveru.
„Sunlight on the Floor“ (in/hudba_Sunlight_on_the_Floor.mp3): 120 BPM, takt = 2,0 s, hudba nastupuje v 2,01 s,
posledný akord v 54,01 s, doznie ~57,7 s (analýza 15. 11.).
Video v3 (12 s): skladba 1,70–8,01 s → video 0,00–6,31 s; strih na takt → skladba 52,01–57,70 s → video 6,31–12,00 s.
Posledný akord tak udrie vo videu v 8,31 s — keď fľaša dosadne a príde „Samlet i én flaske“.
Použitie: python3 hudba_strih.py vystup.wav"""
import subprocess, sys
import numpy as np

SRC = 'in/hudba_Sunlight_on_the_Floor.mp3'
SR = 48000
raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', SRC, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'],
                     capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)

A0, CUT_A, CUT_B, B1 = 1.70, 8.01, 52.01, 57.70     # skladba: úvod do CUT_A, záver od CUT_B
DUR = 12.0
XF = 0.08                                            # krátke prelínanie na údere (bez cvaknutia)

a = x[int(A0 * SR):int((CUT_A + XF / 2) * SR)]
b = x[int((CUT_B - XF / 2) * SR):int(B1 * SR)]
n = int(XF * SR)
t = np.linspace(0, np.pi / 2, n)[:, None]
mid = a[-n:] * np.cos(t) + b[:n] * np.sin(t)         # prelínanie s rovnakou energiou
y = np.concatenate([a[:-n], mid, b[n:]])
N = int(DUR * SR)
y = np.pad(y, ((0, max(0, N - len(y))), (0, 0)))[:N]
fi = int(0.15 * SR); y[:fi] *= np.linspace(0, 1, fi)[:, None]          # mäkký nástup
fo = int(0.6 * SR); y[-fo:] *= np.linspace(1, 0, fo)[:, None] ** 2     # dozvuk do ticha
print('strih vo videu: %.2f s, posledný akord vo videu: %.2f s' % (CUT_A - A0, CUT_A - A0 + (54.01 - CUT_B)))
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-i', '-', sys.argv[1]],
               input=y.astype(np.float32).tobytes(), check=True)
