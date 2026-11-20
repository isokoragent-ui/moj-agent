# Minimálna hodinová sadzba — výpočet

*Iso, 2026-11-20. Výpočet: `python3 10_STUDIUM_MAJETOK/kalkulacka_hodinovka.py`
(čísla na úpravu sú hore v skripte). Počítané ako **ENK (živnosť)**, dane podľa
sadzieb 2025 ⚠️ pre 2026 sa mierne líšia. Náklady firmy sú **môj odhad** —
treba ich nahradiť skutočnými.*

## Predpoklady
| Položka | Hodnota |
|---|---|
| Čisté na účet | 50 000 kr/mes. (variant 40 000) |
| Dôchodok (ENK nemá OTP) | +5 % z čistého |
| Daň + trygdeavgift (10,8 %) + trinnskatt | ~36 % zo zisku (pri 40 000: ~33 %) |
| Náklady firmy ⚠️ odhad | ~172 000 kr/rok + 10 % rezerva = **189 200 kr** (auto 80 000, náradie 25 000, poistky 10 000, telefón/softvér 12 000, účtovníčka 15 000, marketing 15 000, oblečenie 5 000, sykepengeforsikring 10 000) |
| Pracovný rok | 52 − 5 dovolenka − 2 sviatky − 1 choroba = **44 týždňov × 40 h = 1 760 h** |
| Materiál | **nie je v sadzbe** — fakturuje sa zvlášť s prirážkou |

## Výsledok — cieľ 50 000 kr čisté/mes.
Potrebný zisk 992 000 kr/rok → daň ~361 000 → **obrat bez MVA 1 181 000 kr/rok (~98 500 kr/mes.)**

| Koľko z pracovného času je fakturované | Fakturované h/rok | **Min. bez MVA** | **Min. s MVA** |
|---|---|---|---|
| 50 % (polovica je kancelária, cesty, predaj) | 880 | 1 343 kr/h | 1 678 kr/h |
| **60 %** (realistické pre remeselníka s vlastnou firmou) | 1 056 | **1 119 kr/h** | **1 398 kr/h** |
| 70 % | 1 232 | 959 kr/h | 1 199 kr/h |
| 80 % | 1 408 | 839 kr/h | 1 049 kr/h |

## Variant — 40 000 kr čisté/mes.
Obrat bez MVA ~942 500 kr/rok (~78 500 kr/mes.)

| Fakturované | Min. bez MVA | Min. s MVA |
|---|---|---|
| 50 % | 1 071 kr/h | 1 339 kr/h |
| **60 %** | **893 kr/h** | **1 116 kr/h** |
| 70 % | 765 kr/h | 956 kr/h |
| 80 % | 669 kr/h | 837 kr/h |

**Oprava:** v `07_MOTOR_PRIJMOV.md` som odhadol ~750 kr/h. To bolo **príliš
nízko** — nezapočítal som náklady firmy, dôchodok ani nefakturovaný čas.
Správne číslo pre 50 000 čistých je **~1 100 kr/h bez MVA** pri 60 % fakturovaných hodín.

## Náhrobné kamene — prepočet (tvoje čísla)
Ceny pre súkromných zákazníkov musia byť uvedené **s MVA** → 1 700 kr = 1 360 kr bez MVA.
Tu sa neplatí za hodinu, ale za kus → meradlo = **tržba bez MVA na hodinu dňa v teréne
(vrátane ciest)**. Kancelária zvlášť → porovnaj s riadkom 80 % (839 kr/h pri 50 000, 669 kr/h pri 40 000).

| Deň (8 h v teréne) | Tržba bez MVA / deň | **Na hodinu** | Pri cieli 50 000 (≥ 839) |
|---|---|---|---|
| 5 × umytie (1 700) | 6 800 | **850 kr/h** | ✅ tesne na hrane |
| 4 × umytie | 5 440 | 680 kr/h | ❌ pod |
| 3 × umytie | 4 080 | 510 kr/h | ❌ strata |
| 5 × umytie + vyrovnanie (3 000) | 12 000 | **1 500 kr/h** (pri 9 h: 1 333) | ✅ výborné |
| 3 × umytie + vyrovnanie | 7 200 | 900 kr/h | ✅ |

**Čo z toho plynie (výpočet, nie názor):**
1. **Samotné umytie sa oplatí len pri 5 kameňoch za deň na jednom mieste.** Pri 3 je to práca pod cenu.
2. **Balík (umytie + vyrovnanie / písmo / impregnácia) je to, čo z kameňov robí zlatú baňu** — skoro 2× viac na hodinu.
3. Preto:
   - **„Turné“ po cintorínoch:** vopred ohlásiť dátum pre cintorín (napr. „Vegårshei kirkegård 24. 4.“) a zbierať objednávky, kým je ich ≥ 5. Z náhody sa stane plán.
   - **Pri 1–2 kameňoch mimo turné:** príplatok za výjazd, alebo presunúť do najbližšieho turné.
   - **Vždy ponúknuť balík** (vyrovnanie, písmo, impregnácia) — pri objednávke, nie na mieste.
4. Ak by sa materiál (vlastný Gravsteinrens) účtoval zvlášť alebo si išiel z AS so ziskom, číslo ešte stúpne.

## Čo upresniť (z toho sa výpočet spresní)
- Skutočné ročné náklady živnosti (auto, poistky, účtovníčka…) — po decembri ich budeme mať z agendy.
- ✅ Luk 20. 11.: kamene idú cez **AS**, mzdu nevypláca, kombinuje so živnosťou a odpismi → táto sadzba platí pre živnosť fakturujúcu AS; AS musí predávať drahšie (pozri `09_PREDAJNY_SYSTEM.md` bod 6).
