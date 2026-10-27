# Sikkerhetsdatablad (bezpečnostné karty) pre Nórsko

| Produkt | Súbor | Stav |
|---|---|---|
| Isokor Baderomsrens (Bath Cleaner) | `Isokor_Baderomsrens_Sikkerhetsdatablad_NO.pdf` | ✅ NO verzia 1.0 · 27. 10. 2026 · čaká na nahratie na web (po Lukovom „áno“) |

## Čo sa menilo oproti SK originálu (`zdroj/original_SK_…pdf`)
- Preklad do bokmålu podľa oficiálnej nórskej terminológie REACH/CLP (Avsnitt 1–16).
- 1.3 dodávateľ: Isokor Skandinavia AS, org. č. 922 112 975, Nærestadveien 1, 4985 Vegårshei, +47 486 42 178, info@isokor-skandinavia.no. Výrobca (Rodinná firma s.r.o.) ostal ako „Produsent“.
- 1.4 núdzové čísla: 113 + Giftinformasjonen 22 59 13 00.
- Poľské predpisy (8.1, 13, 15) nahradené nórskymi (REACH-forskriften, CLP-forskriften, avfallsforskriften, forskrift om tiltaks- og grenseverdier…), pridané nariadenie o detergentoch 648/2004 a veta o Produktregisteret.
- Opravené chyby originálu: dvakrát nadpis 4.3, „OoC“ → 0 °C, pokazená veta v disclaimeri, chýbajúce číslovanie 11.1/11.2.
- Slogan v logu: „vaske og beskytte“.

## Ako spraviť ďalšiu kartu
1. Text → `zdroj/content.py` (jedna položka = jedna strana, rovnaké stránkovanie ako originál).
2. `python3 zdroj/build.py x` → `zdroj/sds.html`; potom `NODE_PATH=$(npm root -g) node zdroj/render.js <cesta>/sds.html <výstup>.pdf`.
   Skript vypíše výšku obsahu každej strany (max 220 mm), ak niečo pretečie, dá strane červený rámik.
3. Názov produktu a dátum sa menia v `build.py` (hlavička).

**Pasce:** Playwright je len v Node (`require('playwright')`), nie v Pythone. Fonty Khand z GitHubu cez `raw.githubusercontent.com` (github.com/raw je blokovaný). Slogan je súčasť obrázka hlavičky → `logo.py`.
