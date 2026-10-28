# Etikety — nórske verzie zo SK originálov

*Zdroj: SK tlačové PDF od výrobcu (Illustrator, texty prevedené na krivky). Výrobca povolil nahradiť jeho údaje údajmi Isokor Skandinavia AS.*

| Produkt | Súbory | Stav |
|---|---|---|
| Isokor Fett- og flekkfjerner 500 ml (SK: Cleaner) | `Isokor_Fett_og_flekkfjerner_500ml_etikett_NO.pdf` (tlač, spadávka 3 mm + orezové značky ako originál) · `…_NO.png` (300 dpi, čistý formát 210 × 140 mm, do Wordu) · `…_NO_A4_2ks.pdf` (2 ks na A4, 95 %, domáca tlač) | 🟡 návrh 28. 10. 2026 — čaká na Lukovu kontrolu |
| Isokor EcoNeutral 500 ml (SK: Anti Urine Cleaner) | `Isokor_EcoNeutral_500ml_etikett_NO.pdf` · `…_NO.png` · `…_NO_A4_2ks.pdf` | 🟡 návrh 28. 10. 2026 — čaká na Lukovu kontrolu |
| Isokor Antidugg 250/500 ml (SK: Antifog) | `Isokor_Antidugg_250_500ml_etikett_NO.pdf` · `…_NO.png` · `…_NO_A4_2ks.pdf` (2 ks na A4 v 100 %) | 🟡 návrh 28. 10. 2026 — čaká na Lukovu kontrolu |
| Isokor Antidugg 100 ml (SK: Antifog 100 ml) | `Isokor_Antidugg_100ml_etikett_NO.pdf` · `…_NO.png` · `…_NO_A4_2ks.pdf` | 🟡 návrh 28. 10. 2026 — texty = 250/500 ml, písmo 5 pt (malá etiketa + CLP blok) |

### EcoNeutral — iný typ SK súboru (pozor pri ďalších)
- SK PDF nie je vektorový originál ako Cleaner: **pozadie je obrázok 150 dpi v RGB**, texty sú písmo, názov v páse a odznaky „Prírodný produkt“ sú zapečené v obrázku, logo a čiarový kód sú znaky písma.
- Riešenie v `econeutral_500ml.py`: texty sa mažú podľa polohy, pás sa pretrie farbou z obrázku a názov sa napíše znova, SK texty v odznakoch a zvyšky starého loga prekryté bielou, oblúkový nápis „NØYTRALISERER LUKT“ položený na kruh zmeraný z pôvodných písmen.
- **Na veľkotlač si od výrobcu vypýtať vektorový originál (Illustrator/PDF ako pri Cleaneri)** — 150 dpi pozadie je na hrane, na domácu tlač stačí.
- **28. 10. neskôr: obsah podľa Lukovej NO verzie** (`zdroj/Luk_NO_EcoNeutral_500ml.jpg`) — produkt má širšie použitie (pot, posilňovne, šatne, obuv, auto). Podnadpis „Universell lukt- og flekkfjerner“, Lukove fotky (sofa, posilňovňa, tenisky, šteňa) vystrihnuté z jeho JPG a vložené presne do šesťuholníkov originálu. Forma (písmo, logo, dovozca, odznaky) ostala ako pri ostatných etiketách. Fotky nie sú od výrobcu → ich licencia je Lukova vec.
- Zmeny proti SK: CAS 144-55-8 presunuté k natron (v origináli omylom pri pelargóniovom oleji); vynechaná nezmyselná zátvorka „(anti-kyanidíny)“. Tvrdenia „dermatologicky testovaný“ a „bezpečný pre človeka aj zvieratá“ ponechané (od výrobcu).

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

### Antidugg — nebezpečný výrobok (H319)
- SK originál je vektorový ako Cleaner, formát 150 × 130 mm **bez spadávky** (orez = okraj súboru); A4 nesie 2 ks v 100 %.
- SK etiketa má piktogram GHS07, ale **chýbajú signálne slovo a H/P vety** → doplnené po nórsky presne podľa oddielu 2.2 našej bezpečnostnej karty: ADVARSEL, H319, P102, P305+P351+P338, P501 + UFI 6W20-J050-9000-JN6H, blok stojí nad piktogramom.
- **Rozpor na overenie u výrobcu:** etiketa uvádza „voda, etanol, aditíva“, bezpečnostná karta (rovnaká ako SW EKO) uvádza izopropylalkohol 5–10 %.
- Odporúčanie „Isokor Cleaner“ → „Isokor Fett- og flekkfjerner“ (nórsky názov). Ikony „eco friendly“ a „fog stop“ ostali po anglicky (grafika výrobcu).
- **Piktogram GHS07 je menší, než chce CLP** (min. 10 × 10 mm): 250/500 ml má stranu kosoštvorca ~8,4 mm, 100 ml ~5,9 mm — tak je to už v SK origináli. **Luk 28. 10.: necháva podľa výrobcu** (nezväčšovať, neotvárať znova).
- Dovozca bez org. č. a „Produsert i EU“ — na malej etikete by adresa narazila do čiarového kódu; povinné je meno, adresa a telefón.

## Otvorené (Luk rozhodne / overí)
*Logá, názvy, V-label, čiarový kód a ostatné licencie výrobcu sú vybavené dohodou → `08_ROZHODNUTIA/2026-10-28_vyrobca_prava_znacky.md`.*
- Prečítať texty, skontrolovať názov v páse (alternatíva: ponechať „CLEANER“).
- „Produsert i EU“ vs. „Produsert i Slovakia“.
- Nariadenie o detergentoch 648/2004 (platí v Nórsku cez EHP) chce na etikete aj zoznam zložiek vo forme „<5 % …“ (tenzidy, parfum, alergény) a web so zoznamom zložiek — overiť s výrobcom, či sa na tento výrobok vzťahuje.
- Niektoré CAS čísla v SK origináli nesedia s názvom (napr. 8007-02-1 je olej citrónovej trávy, 8016-20-4 grapefruitový) — preložené presne podľa originálu; overiť u výrobcu.
- Pred veľkotlačou: poslať tlačiarni PDF a spýtať sa na ich požiadavky (profil farieb, spadávka) — zatiaľ sme sa držali výrobcovho originálu (3 mm spadávka).
