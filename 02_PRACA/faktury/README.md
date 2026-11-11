# Faktúry — Isokor - Skandinavia AS

*Založené 11. 11. 2026 z Lukovej Word šablóny (Faktura 19). Platí pre **AS**,
nie pre živnosť (KÓD #25).*

## Ako to funguje
1. Luk povie: číslo (alebo „ďalšia“), klient + adresa, dátum, riadky (popis, cena, počet).
2. Agent zapíše `data/<číslo>.json` (kostra: `python3 _nastroje/faktura.py nova`).
3. `python3 _nastroje/faktura.py <číslo> --kontrola` → agent ukáže Lukovi súčty.
4. Po Lukovom „áno“: `python3 _nastroje/faktura.py <číslo>` → `pdf/Faktura_<číslo>.pdf` (A4, na tlač) + `ZOZNAM.md`.
5. Commit + push → faktúra je viditeľná v každom okne.

## Čo kde je
| Súbor | Čo |
|---|---|
| `nastavenie.json` | firma, adresa, ORG.NR., telefón, web, účet, banka, splatnosť (4 dni ako v šablóne), MVA 0 % |
| `data/<číslo>.json` | zadanie faktúry (zdroj pravdy) |
| `pdf/Faktura_<číslo>.pdf` | hotové PDF |
| `ZOZNAM.md` | prehľad všetkých faktúr + stav (vystavená / odoslaná / zaplatená) |
| `sablona/` | pôvodné PDF Faktura 19 + logo vytiahnuté z neho |

## Pasce
- **Číslovanie:** ďalšie číslo = najvyššie v `data/` + 1. Faktúry vystavené mimo agenta (vo Worde) sem treba dopísať, inak sa číslo zopakuje.
- **MVA:** šablóna má 0 %. Keby AS prešla na MVA, zmeň `mva_predvolene` (alebo `mva` na riadku) — súčty sa dopočítajú.
- Oproti šablóne opravené preklepy: „Meverdiavgift“ → **Merverdiavgift**, „Sprarebank“ → **Sparebank**. Formát A4 (šablóna bola Letter).
- Sumy po nórsky: `10 320`, desatinné `4 106,50`.
- Faktúru agent **nikdy neodosiela** — len PDF. Odoslanie klientovi ide cez Lukovo „áno“.
