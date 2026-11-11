# Živnosť — Lukas Hric Liten Husservice

*Založené 11. 11. 2026. Faktúry, agenda (príjmy, výdavky, aktivity), raporty
a rozpočet živnosti. **Úplne oddelené od Isokor - Skandinavia AS** (KÓD #25) —
iné ORG.NR., iný bankový účet, iné číslovanie faktúr, iné priečinky.*

| | Živnosť | AS (pre porovnanie — NEPLIESŤ) |
|---|---|---|
| Názov na faktúre | Lukas Hric Liten Husservice | Isokor - Skandinavia AS |
| ORG.NR. | **912689441** MVA | 922112975 MVA |
| Bankkonto | **2938 13 10130** | 2907 31 44580 |
| Splatnosť | 5 dní | 4 dni |
| Faktúry | `zivnost/faktury/` (posledná 530) | `faktury/` (posledná 19) |
| Agenda | `zivnost/agenda/` | `agenda_as/` |
| Kniha jázd | — (zatiaľ nie) | `kjorebok/` |

## Faktúry
1. Luk povie: **číslo, dátum**, klient + adresa, miesto/projekt (riadok „Et hus i Songe“), riadky (popis, cena **bez MVA**, počet).
2. Agent zapíše `faktury/data/<číslo>.json` (kostra: `python3 _nastroje/faktura.py nova --firma zivnost`).
3. `python3 _nastroje/faktura.py <číslo> --firma zivnost --kontrola` → agent ukáže súčty.
4. Po Lukovom „áno“: `python3 _nastroje/faktura.py <číslo> --firma zivnost` → `faktury/pdf/Faktura_<číslo>.pdf` + `faktury/ZOZNAM.md`.
5. Commit + push. Faktúru agent **nikdy neodosiela** sám.

Vzhľad podľa šablóny **Faktura 530** (`faktury/sablona/`): logo s robotníkmi, stĺpec MVA ukazuje **sumu** MVA (nie %), tučný riadok s miestom práce pod dátumami, bez webu v pätičke.

## Agenda a raporty
Rovnako ako pri AS (`02_PRACA/agenda_as/README.md`), len s `--firma zivnost`:
- Luk diktuje výdavky / príjmy / zákazky → agent zapíše do `agenda/zaznamy/RRRR-MM.json`.
- `python3 _nastroje/agenda.py den|tyzden|mesiac|termin|prehlad|kontrola --firma zivnost` → `agenda/reporty/`.
- Výdavky v raporte majú **podiel v %** → hneď vidno, kam idú peniaze.
- **Rozpočet:** po prvom celom mesiaci (december 2026) `agenda.py rozpocet 2027-01 --firma zivnost` → agent navrhne rozpočet + názor, po „áno“ ho zapíše do `agenda/nastavenie.json` → `rozpocet_mesacne`. Mesačný raport potom ukazuje plán vs. skutočnosť.
- Agenda beží od **1. 11. 2026** (začiatok MVA termínu nov–dec).

## Pasce
- **Najväčšia pasca: zámena firiem.** Pred každou faktúrou a každým výdavkom musí byť jasné, ktorej firmy sa týka. Keď to Luk nepovie → jedna otázka „živnosť, alebo AS?“. Nikdy netipovať.
- **Živnosť fakturuje AS** (Luk robí prevažne pre a.s.): faktúra živnosti pre Isokor - Skandinavia AS = príjem tu **a zároveň výdavok v AS** (`agenda_as`, kategória `ucty_sluzby` alebo `ine`, s odkazom na číslo faktúry). Zapísať na oboch stranách, inak AS ukazuje vyšší zisk, než má.
- **Číslovanie:** Luk zadá číslo sám. Faktúry vystavené mimo agenta (vo Worde) treba dopísať do `faktury/data/`, inak `nova` navrhne zlé číslo.
- **MVA termín:** raporty rátajú 2-mesačné termíny ako pri AS. Malé živnosti (obrat pod 1 mil. NOK) môžu mať aj **ročný termín** — overiť u účtovníčky, ak áno, prepnúť.
- **Ceny na faktúre bez MVA**, skript pripočíta 25 %. Iná sadzba na riadku: `"mva": 0`.
- Výsledok živnosti = základ dane; mzda v živnosti neexistuje → odkladať rezervu na daň a trygdeavgift.
- Oproti šablóne opravený preklep „Sprarebank“ → **Sparebank**, formát A4.
