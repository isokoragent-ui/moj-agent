"""Pokojná „luxusná“ hudba pre video Cleaner (vlastná, bez licencie):
mäkký pad Dmaj9 – Bm9 – Gmaj9 – A6, riedke klavírne tóny, kvapka (7,6 s) a sprej (10,45 s).
Použitie: python3 hudba.py vystup.wav [dĺžka — predvolene 15]"""
import sys, wave
import numpy as np

SR = 44100
DUR = float(sys.argv[2]) if len(sys.argv) > 2 else 15.0
N = int(SR * DUR)
out = np.zeros(N)
rng = np.random.default_rng(4)


def hz(n):
    return 440.0 * 2 ** ((n - 69) / 12)


def add(sig, start):
    s = int(start * SR)
    n = min(len(sig), N - s)
    if n > 0:
        out[s:s + n] += sig[:n]


# pad — 4 akordy po 3,75 s, pomalý nábeh
chords = [[50, 57, 61, 64, 66], [47, 54, 57, 61, 62], [43, 50, 54, 57, 59], [45, 52, 57, 61, 66]]
for i, ch in enumerate(chords):
    n = int(4.6 * SR)
    t = np.arange(n) / SR
    pad = np.zeros(n)
    for note in ch:
        f = hz(note)
        pad += (np.sin(2 * np.pi * f * t) + np.sin(2 * np.pi * f * 1.004 * t) + .2 * np.sin(2 * np.pi * 2 * f * t)) / 2
    e = np.minimum(1, t / 1.4) * np.minimum(1, (t[-1] - t) / 1.2)
    add(0.035 * pad * e, i * 3.75)

# klavír — riedka melódia
mel = [(0.6, 74), (1.5, 78), (2.4, 81), (4.2, 78), (5.0, 74), (6.0, 73),
       (7.65, 86), (8.4, 79), (9.3, 83), (11.4, 81), (12.3, 78), (13.1, 76), (13.4, 81), (13.7, 85)]
for st, note in mel:
    n = int(2.8 * SR)
    t = np.arange(n) / SR
    f = hz(note)
    tone = np.sin(2 * np.pi * f * t) + .35 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t * 3) + .12 * np.sin(2 * np.pi * 3 * f * t) * np.exp(-t * 5)
    add(0.06 * tone * np.exp(-t * 1.6) * np.minimum(1, t / .005), st)

# kvapka — klesajúci „plink“
n = int(.35 * SR); t = np.arange(n) / SR
f = 1400 * np.exp(-t * 6) + 500
add(0.12 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 14), 7.6)

# sprej — dva krátke šumy (high-pass)
for st in (10.45, 10.75):
    n = int(.32 * SR)
    w = rng.standard_normal(n)
    w = np.diff(np.concatenate([[0], w]))  # jednoduchý high-pass
    t = np.arange(n) / SR
    add(0.05 * w * np.minimum(1, t / .02) * np.exp(-t * 7), st)

# dozvuk
rev = out.copy()
for d, g in [(0.071, .32), (0.113, .27), (0.173, .22), (0.241, .17), (0.331, .12), (0.452, .08)]:
    k = int(d * SR)
    rev[k:] += g * out[:-k]
out = rev
fade = int(1.5 * SR)
out[-fade:] *= np.linspace(1, 0, fade)
out = out / np.max(np.abs(out)) * 0.8

with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((out * 32767).astype(np.int16).tobytes())
