# Sikkerhetsdatablad (bezpečnostné karty) pre Nórsko

| Produkt | Súbor | Stav |
|---|---|---|
| Isokor SW EKO → web „Isokor SW EKO impregnering for fasade og tak“ | `Isokor_SW_EKO_Sikkerhetsdatablad_NO.pdf` | ✅ NO 1.0 · 27. 10. 2026 · na webe od 27. 10. · H319 (Advarsel), nie je nebezpečný tovar pri preprave |
| Isokor SW → web „Isokor SW treimpregnering“ | `Isokor_SW_Sikkerhetsdatablad_NO.pdf` | ✅ NO 1.0 · 27. 10. 2026 · na webe od 27. 10. · **nebezpečný** (H225, H319, H336) |
| Isokor Baderomsrens (Bath Cleaner) | `Isokor_Baderomsrens_Sikkerhetsdatablad_NO.pdf` | ✅ NO verzia 1.0 · 27. 10. 2026 · na webe od 27. 10. (odkaz na konci popisu produktu) |

## Čo sa menilo oproti SK originálu (`zdroj/original_SK_…pdf`)
- Preklad do bokmålu podľa oficiálnej nórskej terminológie REACH/CLP (Avsnitt 1–16).
- 1.3 dodávateľ: Isokor Skandinavia AS, org. č. 922 112 975, Nærestadveien 1, 4985 Vegårshei, +47 486 42 178, info@isokor-skandinavia.no. Výrobca (Rodinná firma s.r.o.) ostal ako „Produsent“.
- 1.4 núdzové čísla: 113 + Giftinformasjonen 22 59 13 00.
- Poľské predpisy (8.1, 13, 15) nahradené nórskymi (REACH-forskriften, CLP-forskriften, avfallsforskriften, forskrift om tiltaks- og grenseverdier…), pridané nariadenie o detergentoch 648/2004 a veta o Produktregisteret.
- Opravené chyby originálu: dvakrát nadpis 4.3, „OoC“ → 0 °C, pokazená veta v disclaimeri, chýbajúce číslovanie 11.1/11.2.
- Slogan v logu: „vaske og beskytte“.

## Ako spraviť ďalšiu kartu
1. Text → nový modul `zdroj/<produkt>.py` (PRODUCT, DATE, PAGES; jedna položka = jedna strana, stránkovanie ako originál; voliteľne EXTRA_CSS). Vzor: `baderomsrens.py` (nie nebezpečný), `sw_impregnering.py` (nebezpečný: piktogramy, zloženie, limity, ADR tabuľka), `sw_eko.py` (len H319, preberá CSS zo SW).
2. `cd zdroj && python3 build.py <produkt>` → `<produkt>.html`; potom `NODE_PATH=$(npm root -g) node render.js $PWD/<produkt>.html <výstup>.pdf` (HTML potom zmazať).
   Skript vypíše výšku obsahu každej strany (max 220 mm), ak niečo pretečie, dá strane červený rámik.
3. Názov produktu a dátum sú v module (hlavička sa berie odtiaľ).

**Pasce:** Playwright je len v Node (`require('playwright')`), nie v Pythone. Fonty Khand z GitHubu cez `raw.githubusercontent.com` (github.com/raw je blokovaný). Slogan je súčasť obrázka hlavičky → `logo.py`.

## Ako nahrať na web
stagedUploadsCreate (resource FILE, application/pdf) → curl POST súboru → fileCreate (contentType FILE) → počkať na READY a vziať `url` → záloha popisu do `02_PRACA/zalohy/` → productUpdate: na koniec descriptionHtml `<hr><h3>Sikkerhetsdatablad</h3><p>… <a href=URL target=_blank>Last ned sikkerhetsdatablad (PDF)</a></p>`.

**Text na webe (Luk, 27. 10.):** bez „på norsk“ — web je nórsky, jazyk sa nepíše: „Sikkerhetsdatabladet (SDS) for <produkt> kan lastes ned her: Last ned sikkerhetsdatablad (PDF)“.

**Pasce pri nebezpečných produktoch:** tabuľky v SK origináli sú obrázky (pdftotext ich nevidí) → čítať stránky ako obrázok. Poľské limity (NDS) nahradiť nórskymi grenseverdi (izopropanol: 100 ppm / 245 mg/m³, 8 h — overené z viacerých nórskych SDS; lovdata.no je z cloudu blokovaný). V SW origináli mali prepravné nálepky chybne „2“ → vlastná `adr3.svg`. GHS piktogramy `ghs02.png`, `ghs07.png`.
