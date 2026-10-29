"""Pokojná zimná hudba na 10 s (vlastná, bez licencie): pad + hracia skrinka.
Použitie: python3 hudba.py vystup.wav"""
import sys, wave
import numpy as np

SR = 44100
DUR = 10.0
t_all = np.arange(int(SR * DUR)) / SR
out = np.zeros_like(t_all)


def hz(n):  # MIDI → Hz
    return 440.0 * 2 ** ((n - 69) / 12)


def env(n, a, r):
    e = np.ones(n)
    ai, ri = int(a * SR), int(r * SR)
    e[:ai] = np.linspace(0, 1, ai)
    e[-ri:] *= np.linspace(1, 0, ri)
    return e


# akordy: C – Am – F – G (každý 2,5 s), pad s mäkkými harmonickými
chords = [[48, 60, 64, 67], [45, 57, 60, 64], [41, 57, 60, 65], [43, 55, 59, 62]]
for i, ch in enumerate(chords):
    s, n = int(i * 2.5 * SR), int(2.9 * SR)
    n = min(n, len(out) - s)
    t = np.arange(n) / SR
    pad = np.zeros(n)
    for note in ch:
        f = hz(note)
        for k, amp in [(1, 1.0), (2, 0.25), (3, 0.08)]:
            pad += amp * (np.sin(2 * np.pi * f * k * t) + np.sin(2 * np.pi * f * k * 1.003 * t)) / 2
    out[s:s + n] += 0.06 * pad * env(n, 0.8, 1.0)

# hracia skrinka — arpeggio, 8 tónov na akord
mel = [72, 76, 79, 76, 72, 76, 79, 84,
       69, 72, 76, 72, 69, 72, 76, 81,
       65, 69, 72, 69, 65, 69, 72, 77,
       67, 71, 74, 71, 67, 74, 79, 83]
for j, note in enumerate(mel):
    s = int(j * 2.5 / 8 * SR)
    n = int(1.6 * SR)
    if s >= len(out):
        break
    n = min(n, len(out) - s)
    t = np.arange(n) / SR
    f = hz(note)
    tone = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * f * 2 * t) + 0.1 * np.sin(2 * np.pi * f * 4.2 * t)
    out[s:s + n] += 0.05 * tone * np.exp(-t * 3.2)

# jednoduchý dozvuk (niekoľko oneskorení)
rev = out.copy()
for d, g in [(0.083, 0.35), (0.127, 0.28), (0.191, 0.22), (0.263, 0.16), (0.347, 0.11)]:
    k = int(d * SR)
    rev[k:] += g * out[:-k]
out = rev
# fade in/out pre slučku
fi, fo = int(0.6 * SR), int(1.2 * SR)
out[:fi] *= np.linspace(0, 1, fi)
out[-fo:] *= np.linspace(1, 0, fo)
out = out / np.max(np.abs(out)) * 0.8

st = np.stack([out, np.roll(out, int(0.012 * SR))], axis=1)
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype(np.int16).tobytes())
print('ok')
