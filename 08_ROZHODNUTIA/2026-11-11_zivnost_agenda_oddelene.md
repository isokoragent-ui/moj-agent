# 2026-11-11 — Živnosť: vlastné faktúry, agenda, raporty a rozpočet, oddelene od AS

**Rozhodol:** Luk (okno „Živnosť — faktúry a agenda“)

**Čo:** Pre živnosť (Lukas Hric Liten Husservice, ORG.NR. 912689441 MVA) rovnaký
systém ako pre Isokor - Skandinavia AS — faktúry podľa Lukovej šablóny (Faktura 530),
agenda príjmov/výdavkov/aktivít, raporty, rozpočet. **Nesmie sa to miešať.**

**Ako:** jeden spoločný kód (`faktura.py`, `agenda.py`) s prepínačom `--firma zivnost`;
cesty každej firmy sú na jedinom mieste (`_nastroje/firmy.py`). Dáta živnosti len
v `02_PRACA/zivnost/`. Bez prepínača všetko funguje pre AS ako doteraz.

**Prečo nie kópia skriptov:** dve kópie by sa časom rozišli (oprava v jednej, chyba
v druhej) — KÓD #1. Oddelenie je v dátach a nastavení, nie v kóde.

**Rozpočet:** agent navrhne z reálnych dát (najskôr po celom decembri 2026), zapíše
až po Lukovom „áno“. Platí pre obe firmy.
