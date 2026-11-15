"""Prispôsobí Lukovu skladbu dĺžke videa: začiatok skladby + strih na úder taktu do jej záveru.
„Sunlight on the Floor“ (in/hudba_Sunlight_on_the_Floor.mp3): 120 BPM, takt = 2,0 s, hudba nastupuje v 2,01 s,
posledný akord v 54,01 s, doznie ~57,7 s (analýza 15. 11.).
Video v3 18 s (predvolené): skladba 1,70–12,01 s → video 0–10,31 s (prechod na fľašu); strih na takt → skladba 50,01–57,70 s
→ video 10,31–18,00 s. Posledný akord udrie v 14,31 s, keď príde záverečný text, a doznie do konca.
Použitie: python3 hudba_strih.py vystup.wav [A0 CUT_A CUT_B B1 DĹŽKA [SKLADBA.mp3 [PAUZA_s]]]
EcoNeutral (Salt Air and Cedar, mriežka 0,05 + 0,4k s): python3 hudba_strih.py out.wav 0 10.85 146.05 153.2 18 ../econeutral_natur/in/hudba_Salt_Air_and_Cedar.mp3 0.5"""
import subprocess, sys
import numpy as np

SRC = sys.argv[7] if len(sys.argv) > 7 else 'in/hudba_Sunlight_on_the_Floor.mp3'
PAUZA = float(sys.argv[8]) if len(sys.argv) > 8 else 0.0   # s: úvod pred strihom stíšiť (ako pauza v skladbe)
SR = 48000
raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', SRC, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'],
                     capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)

# skladba: úvod A0–CUT_A, záver CUT_B–B1 (strihy na úder taktu = 2,01 + 2k s); predvolené = video 18 s
# 12 s verzia: python3 hudba_strih.py out.wav 1.70 8.01 52.01 57.70 12
A0, CUT_A, CUT_B, B1, DUR = [float(v) for v in sys.argv[2:7]] if len(sys.argv) > 6 else (1.70, 12.01, 50.01, 57.70, 18.0)
XF = 0.08                                            # krátke prelínanie na údere (bez cvaknutia)

a = x[int(A0 * SR):int((CUT_A + XF / 2) * SR)]
if PAUZA > 0:
    m = int(PAUZA * SR)
    a = a.copy(); a[-m:] *= np.linspace(1, 0.25, m)[:, None] ** 1.5
b = x[int((CUT_B - XF / 2) * SR):int(B1 * SR)]
n = int(XF * SR)
t = np.linspace(0, np.pi / 2, n)[:, None]
mid = a[-n:] * np.cos(t) + b[:n] * np.sin(t)         # prelínanie s rovnakou energiou
y = np.concatenate([a[:-n], mid, b[n:]])
N = int(DUR * SR)
y = np.pad(y, ((0, max(0, N - len(y))), (0, 0)))[:N]
fi = int(0.15 * SR); y[:fi] *= np.linspace(0, 1, fi)[:, None]          # mäkký nástup
fo = int(0.6 * SR); y[-fo:] *= np.linspace(1, 0, fo)[:, None] ** 2     # dozvuk do ticha
print('strih vo videu: %.2f s' % (CUT_A - A0))
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-i', '-', sys.argv[1]],
               input=y.astype(np.float32).tobytes(), check=True)
