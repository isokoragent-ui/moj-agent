# Viac okien naraz — každé okno = jedna téma

**Dátum:** 2026-10-29
**Rozhodol:** Luk

## Čo sme rozhodli
Každé okno Claude Code je venované jednej téme (napr. etikety, Hytteservice). Okná bežia súčasne a všetky zapisujú do `main`.

## Prečo (a čo sme zavrhli)
Luk tak drží témy oddelené. 29. 10. pri zlučovaní PR #15 vznikol konflikt s PR #14 (etikety, Universalrens) v `AKTUALNE.md`, denníku a `PROJEKTY.md` — vyriešené zachovaním oboch strán.

## Čo to mení v praxi
Pravidlá v `AGENT.md` (Moje doplnky) a v `/odovzdaj` (krok 0): pred zápisom do zdieľaných súborov zlúčiť `main`, pri konflikte zachovať obe strany, v okne meniť len vlastnú tému.
