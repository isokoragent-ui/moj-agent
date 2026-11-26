# Dodacie listy (følgesedler) — Isokor - Skandinavia AS

*Založené 24. 11. 2026 podľa Lukovho papierového tlačiva „Følgeseddel“
(`sablona/folgeseddel_povodne_tlacivo.jpg`). Platí pre **AS** (KÓD #25).*

## Načo
Pri **dodaní tovaru** dostane zákazník dodací list. Zákazník podpíše
**„Varene mottatt“** (dátum, podpis, meno paličkovým písmom) → **až potom ide faktúra.**

## Ako to funguje
1. Luk povie: komu, čo, koľko kusov, cena (bez MVA), dátum dodania.
2. Agent: `python3 _nastroje/folgeseddel.py nova` → vyplní `data/<číslo>.json`.
3. `python3 _nastroje/folgeseddel.py <číslo> --kontrola` → ukáže Lukovi riadky a súčty.
4. Po Lukovom „áno“: `python3 _nastroje/folgeseddel.py <číslo>` → `pdf/Folgeseddel_<číslo>.pdf` (A4, na tlač, **2 kópie**: jedna zákazníkovi, podpísaná zostáva nám).
5. Keď je podpísaný: Luk povie „podpísal“ → agent zmení `stav` na `podpísaný`.
6. Faktúra: `python3 _nastroje/folgeseddel.py <číslo> --faktura` → kostra faktúry v `02_PRACA/faktury/data/` s odkazom „Følgeseddel nr. X“ → ďalej podľa `02_PRACA/faktury/README.md` (PDF faktúry až po „áno“).

**Prázdne tlačivo** na ručné vypĺňanie v teréne: `pdf/Folgeseddel_prazdny.pdf`
(`python3 _nastroje/folgeseddel.py prazdny`). Ručne vyplnený list → odfotiť → agent ho prepíše do `data/`, aby sa z neho dala spraviť faktúra.

## Čo kde je
| Súbor | Čo |
|---|---|
| `data/<číslo>.json` | zadanie listu (zdroj pravdy) |
| `pdf/` | hotové PDF + prázdne tlačivo |
| `ZOZNAM.md` | prehľad: číslo, dátum, kupujúci, suma, stav, faktúra |
| `sablona/` | fotka pôvodného papierového tlačiva |

## Pole v `data/<číslo>.json`
`dato`, `ekspedert_av`, `kjoper {navn, adresse[]}`, `linjer [{spesifikasjon, antall, pris (bez MVA, za kus), mva}]`,
nepovinné: `uten_priser: true` (list bez cien), `levert_til` (iné miesto dodania), `betalt_dato`, `poznamka` (len pre nás).

## Pasce
- **Dodávateľ sa berie z `02_PRACA/faktury/nastavenie.json`** — keď sa zmení adresa/telefón, zmení sa aj tu.
- **Ceny bez MVA**, MVA 25 % sa dopočíta (firma v MVA od 6. 11. 2026). Súčty dole: KRONER (bez MVA) / MVA / TOTAL SUM.
- Na jeden list sa zmestí **16 riadkov** — viac → rozdeliť na dva listy.
- Číslovanie listov je **samostatné** (1, 2, 3 …), nemieša sa s číslami faktúr.
- `--faktura` sa dá spustiť len raz — list si zapamätá číslo faktúry a stav `fakturovaný`.
- Agent list **nikdy neposiela** zákazníkovi — len PDF. Odoslanie/odovzdanie ide cez Luka.
- Oproti papierovému tlačivu pridané: **NR.** (číslo listu), riadok **Underskrift** a **Navn** pod „Varene mottatt“ (potvrdenie od zákazníka), logo a údaje firmy predvyplnené.
