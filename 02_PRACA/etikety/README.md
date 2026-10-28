# Etikety — nórske verzie zo SK originálov

*Zdroj: SK tlačové PDF od výrobcu (Illustrator, texty prevedené na krivky). Výrobca povolil nahradiť jeho údaje údajmi Isokor Skandinavia AS.*

| Produkt | Súbory | Stav |
|---|---|---|
| Isokor Fett- og flekkfjerner 500 ml (SK: Cleaner) | `Isokor_Fett_og_flekkfjerner_500ml_etikett_NO.pdf` (tlač, spadávka 3 mm + orezové značky ako originál) · `…_NO.png` (300 dpi, čistý formát 210 × 140 mm, do Wordu) · `…_NO_A4_2ks.pdf` (2 ks na A4, 95 %, domáca tlač) | 🟡 návrh 28. 10. 2026 — čaká na Lukovu kontrolu |

## Ako vzniká (`zdroj/etikett.py <modul>`)
1. Z originálu sa **vektorovo vystrihnú** SK texty a staré logo (cesty ležiace celé v oblastiach `REGIONS`) — nič sa neprekrýva bielym, pozadie (šesťuholníky, fotky, ikony, čiarový kód) ostáva originál v CMYK.
2. Nórske texty (`zdroj/<produkt>.py`) sa položia písmom **Khand** (to isté ako na SK etikete), farby z originálu: zelená C48 M5 Y99 K0, text K100.
3. Nové logo (`zdroj/isokor_logo_new_riadkove.pdf`) ide **vektorovo**: celé hore, samotná ikona pri dovozcovi. Prefarbené na **čistú čiernu K100** (v zdrojovom súbore je 95/95/45/95 = 380 % farby — na malom logu riziko rozmazania a posunu farieb).
4. Výstup: tlačové PDF + PNG + A4 s dvoma kusmi.

Ďalšia etiketa: nový modul podľa `fettfjerner_500ml.py`; ak má originál iné rozloženie, upraviť `REGIONS` a pozície (merané v px na náhľade 100 dpi).

## Čo sa menilo oproti SK originálu a Lukovej skúšobnej verzii
- Názov v zelenom páse: **FETT- OG FLEKKFJERNER** (= názov na webe).
- Pod BIO: **Miljøvennlig** namiesto „Økologisk“ — „økologisk“ v nórčine znamená certifikovaný bio pôvod (Debio), SK „ekologický“ znamená šetrný k prírode.
- Odznak „PRÍRODNÝ PRODUKT“ → **NATURLIG PRODUKT**.
- Zloženie preložené zo SK originálu aj s CAS číslami. Lukova verzia mala chyby: „geraniol“ (správne geraniumolje), „olivenolje“, „flerumettede fettsyrer“, „mineralstoffer og vitaminer“ (v origináli nie sú); chýbal cesnakový extrakt, voda a veta o karcinogénoch.
- Doplnené riadky z originálu: **Holdbarhet: Se emballasjen**, **Forbruk: ca. 100 ml/m²**.
- Výrobca → **Importør og distributør: Isokor Skandinavia AS**, org. nr., adresa, telefón, web, „PRODUSERT I EU“.
- **Vynechaná veta** o „inhibičnom vplyve na baktérie, vírusy a hmyz“ — v EÚ/EHP je to biocídne tvrdenie (nariadenie 528/2012), bez povolenia nesmie byť na etikete.

## Otvorené (Luk rozhodne / overí)
- Prečítať texty, skontrolovať názov v páse (alternatíva: ponechať „CLEANER“).
- „Produsert i EU“ vs. „Produsert i Slovakia“.
- **V-label** (European Vegetarian Union) — licencia patrí výrobcovi; overiť, že platí aj pre predaj v Nórsku pod Isokor Skandinavia.
- **Čiarový kód** 8588006889239 ostáva výrobcov (prefix 858 = GS1 Slovensko — to je v poriadku, krajinu pôvodu neurčuje).
- Nariadenie o detergentoch 648/2004 (platí v Nórsku cez EHP) chce na etikete aj zoznam zložiek vo forme „<5 % …“ (tenzidy, parfum, alergény) a web so zoznamom zložiek — overiť s výrobcom, či sa na tento výrobok vzťahuje.
- Niektoré CAS čísla v SK origináli nesedia s názvom (napr. 8007-02-1 je olej citrónovej trávy, 8016-20-4 grapefruitový) — preložené presne podľa originálu; overiť u výrobcu.
- Pred veľkotlačou: poslať tlačiarni PDF a spýtať sa na ich požiadavky (profil farieb, spadávka) — zatiaľ sme sa držali výrobcovho originálu (3 mm spadávka).
