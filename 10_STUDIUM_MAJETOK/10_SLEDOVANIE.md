# Priebežné sledovanie — čísla, trhy, zákony

*Iso, 2026-11-20. Luk: „Priebežne sleduj dokumenty, príjmy a pohyby, prispôsobuj
marketing, smerovanie a logistiku. Buď reálny, profesionálny aj kreatívny.
Sleduj trhy, možnosti, zmeny zákonov.“*

---

## 1. Cena za zákazku, nie za hodinu (Luk má pravdu)
- Zákazník nevidí hodinovku 1 400 kr — vidí **cenu za výsledok**. Hodinovka
  z `08_HODINOVKA.md` je len **spodná hranica efektívneho zárobku**, pod ktorú
  nesmie zákazka spadnúť. Nie je to cenník.
- **Efektívna hodinovka zákazky** = (tržba bez MVA − materiál − cesta − pomocník)
  ÷ všetky hodiny (práca + cesta + príprava + faktúra).
- **Príklad Sandnes:** 38 000 kr za 2 dni. Pri 2 × 10 h tvojej práce = **1 900 kr/h**
  ešte pred odpočtom cesty a kolegyne → **~1,7× nad spodnou hranicou.**
  Presne zrátam, keď budem mať: MVA áno/nie, km, hodiny kolegyne, materiál.
- **Čo robí zákazky vysoko ziskové** (opakuje sa v tvojich číslach):
  1. špecializácia, ktorú iní nevedia (kameň, sklo, hrdza, impregnácia)
  2. vlastný produkt v cene (marža na práci aj na materiáli)
  3. väčší objem na jednom mieste (Sandnes, 5 kameňov na jednom cintoríne)
  4. pevná cena za výsledok → rýchla práca = tvoj zisk, nie zákazníkova úspora
- **Kolegyňa (fotky, video, pomoc):** z každej veľkej zákazky vzniká materiál
  na marketing → tá istá zákazka predáva ďalšie. Jej náklad treba rátať do
  zákazky, ale prínos je aj v marketingu (meria sa: dopyty z videa).

## 2. Šijacie stroje — 890 kr (Skredderstuen, firma manželky — len princíp)
- Pri 45 min práce ≈ 950 kr/h (ak 890 bez MVA), pri 90 min ≈ 475 kr/h. **Čas
  rozhoduje, nie cena.** ⚠️ je Systua registrovaná v MVA?
- Mechanizmy (rozhodne manželka a ty):
  - **2 stupne:** základný servis 890 kr (≤ 1 h) + „utvidet service“ pre staré /
    overlocky / zaseknuté (vyššia pevná cena), diely zvlášť.
  - **Séria:** zbierať stroje a robiť ich v jeden večer za sebou (jedna príprava, rutina).
  - **Prepojenie:** servis → ponuka kurzu / prenájmu šijacieho miesta / predaj
    príslušenstva. Zákazník so servisovaným strojom je najlepší kandidát na kurz.

## 3. Čo sledujem a odkiaľ (len to, čo vidím v repozitári a pripojených nástrojoch)
| Zdroj | Čo z neho čítam |
|---|---|
| `_nastroje/agenda.py` (AS aj `--firma zivnost`) | príjmy podľa kanála, výdavky, aktivity, mesiac vs. minulý mesiac |
| `02_PRACA/faktury/`, `02_PRACA/zivnost/faktury/` | zákazky, klienti, sumy, kto neplatí |
| `02_PRACA/kjorebok/` | km → náklad cesty na zákazku a región |
| Shopify | objednávky, produkty, konverzia |
| Gmail / Kalendár (ak pripojené) | dopyty, odpovede, termíny |
| Metricool | ktoré príspevky prinášajú reakcie |

**Čo z toho budem hlásiť** (stručne, s číslom):
- ktorá oblasť zarobila najviac **na hodinu**, nie len celkovo
- neplatiace faktúry po splatnosti (pôvodná príčina dlhov) — hneď
- kde je veľa km a malá tržba → logistika (zoskupiť, turné, príplatok)
- čo z marketingu prinieslo dopyt → viac toho, zvyšok vypnúť
- sezónne okno, ktoré sa blíži (napr. „o 6 týždňov 17. mai — turné ešte nie je ohlásené“)

**Úprimne, ako to funguje:** nebežím nepretržite. Každé okno sa zobudí prázdne,
prečíta tento priečinok a dáta. Sledovanie preto beží v rytme nižšie — pri
`/rano`, `/tyzden` a mesačnej uzávierke. Automatické spúšťanie (rebrík stupeň 4)
sa zapne, až keď si ho zaslúži.

## 4. Rytmus
| Kedy | Čo | Výstup |
|---|---|---|
| Piatok (`/tyzden`) | dopyty · ponuky · uzavreté · obrat · neplatiči · 1 odporúčanie | 5 riadkov |
| 1. deň v mesiaci | `agenda.py mesiac` (AS + živnosť) + **efektívna hodinovka podľa oblastí** + úprava marketingu na ďalší mesiac | 1 strana |
| Štvrťročne | trhy a zákony (zoznam nižšie), čistý majetok rodiny, stupeň slobody | 1 strana |
| Okt–nov | štátny rozpočet na ďalší rok → dopad na dane, odvody, ceny | zápis do bodu 6 |

## 5. Čo chýba v dátach (aby sa dala merať hodinovka)
V agende sa pri príjme dnes zapisuje suma a kanál, ale **nie oblasť a hodiny**.
Návrh: pri každom príjme zo služby 2 nepovinné polia — `oblast` (kamene / hytte /
sklo / B2B / drevo / údržba / produkty) a `hodiny` (vrátane cesty, koľko ľudí).
Zmena nástroja patrí do okna Účtovníctvo — až po Lukovom „áno“.

## 6. Trhy a zákony — sledovací zoznam
| Oblasť | Kde | Stav k 2026-11-20 |
|---|---|---|
| Štátny rozpočet 2027 (predložený 7. 10. 2026) | regjeringen.no, Prop. 1 LS (2026–2027) | návrh: **trygdeavgift pre ENK 10,8 → 10,6 %**, vyšší personfradrag; dividenda u akcionára **37,84 % bez zmeny**; pravidlá „innbetalt kapital“ odložené; **ASK sa rozširuje**; začiatkom 2027 príde správa o veľkej daňovej reforme ⚠️ návrh, čaká na Storting |
| MVA a fakturácia | skatteetaten.no | sledovať: termíny MVA, e-faktúry (EHF) pre obce |
| Verejné zákazky | Doffin, anskaffelsesforskriften | limit priamych nákupov obcí ⚠️ over |
| Pracovné právo / pomocník | arbeidstilsynet.no, NAV | AGA zóna podľa obce, minimálne mzdy v odvetví ⚠️ |
| Cintoríny | gravferdsloven, kirkelig fellesråd | pravidlá práce na cintoríne, feste |
| Chemikálie / ADR | dsb.no, PostNord | preprava 5 l Fasaderens Plus (ADR 8) — otvorené v okne e-shop |
| Trh služieb Agder | Finn, SSB, sol.no | ceny konkurencie, dopyt po údržbe (44 % odkladá — Norstat) |
| Úroky | Norges Bank | sadzba → splátka 2. domu, výnos rezervy |

*Zdroje k bodu 6: [regjeringen.no – Statsbudsjettet 2027](https://www.regjeringen.no/no/aktuelt/foreslar-milliardkutt-i-inntektsskatten-storste-pa-over-20-ar/id3174677/),
[Revisorforeningen – skatteendringer 2027](https://www.revisorforeningen.no/fag/nyheter/skatteendringer-i-statsbudsjettet-for-2027/),
[EY – statsbudsjett 2027](https://www.ey.com/no_no/insights/tax/statsbudsjett-2027),
[Smarte Penger – statsbudsjettet 2027](https://www.smartepenger.no/skatt/3834-statsbudsjettet-for-2027).*
