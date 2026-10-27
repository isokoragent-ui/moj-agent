# Sikkerhetsdatablad (bezpečnostné karty) pre Nórsko

| Produkt | Súbor | Stav |
|---|---|---|
| Isokor SWB | `Isokor_SWB_Sikkerhetsdatablad_NO.pdf` | ✅ NO 1.0 · 27. 10. 2026 · **len do zásoby, produkt nie je v e-shope** · obsahovo = SW EKO (H319), iný len názov a UFI |
| Isokor WhiteWood | `Isokor_WhiteWood_Sikkerhetsdatablad_NO.pdf` | ✅ NO 1.0 · 27. 10. 2026 · **len do zásoby, nie je na webe** (Luk ho zatiaľ v Nórsku nepredáva) · obsahovo = LMS (žieravý H314, UN 1760), iný len názov a UFI |
| Isokor Gravsteinrens (SK: Na hroby / Grave Cleaner) | `Isokor_Gravsteinrens_Sikkerhetsdatablad_NO.pdf` | ✅ NO 1.0 · 27. 10. 2026 · na webe od 27. 10. · obsahovo = Baderomsrens (nie je nebezpečný), iný len názov |
| Isokor Lotos Profi → web „Isokor Lotos Profi nanoimpregnering“ | `Isokor_Lotos_Profi_Sikkerhetsdatablad_NO.pdf` | ✅ NO 1.0 · 27. 10. 2026 · na webe od 27. 10. · **nie je klasifikovaný** (izopropanol 5–<10 %, EUH210), bez UFI; základ = SW EKO |
| Isokor Lotos Standard → web „Isokor Lotos Standard nanoimpregnering“ | `Isokor_Lotos_Standard_Sikkerhetsdatablad_NO.pdf` | ✅ NO 1.0 · 27. 10. 2026 · na webe od 27. 10. · obsahovo = SW (horľavý, UN 1219), iný len názov a UFI |
| Isokor Polisher → web „Isokor Polish for blanke overflater“ | `Isokor_Polisher_Sikkerhetsdatablad_NO.pdf` | ✅ NO 1.0 · 27. 10. 2026 · na webe od 27. 10. · obsahovo = SW (H225/H319/H336, UN 1219), iné len použitie a UFI |
| Isokor Sofarens (SK: Na tepovanie / Sofa Cleaner) | `Isokor_Sofarens_Sikkerhetsdatablad_NO.pdf` | ✅ NO 1.0 · 27. 10. 2026 · na webe od 27. 10. · obsahovo = Baderomsrens (nie je nebezpečný), iný len názov |
| Isokor LMD (LM Descaling) → web „Isokor Kalkfjerner for bad“ | `Isokor_LMD_Sikkerhetsdatablad_NO.pdf` | ✅ NO 1.0 · 27. 10. 2026 · na webe od 27. 10. · obsahovo = LMS (žieravý H314, UN 1760), iný len názov a UFI |
| Isokor LMS → web „Isokor LMS rustfjerner“ | `Isokor_LMS_Sikkerhetsdatablad_NO.pdf` | ✅ NO 1.0 · 27. 10. 2026 · na webe od 27. 10. · **žieravý** (H314, Fare), ADR UN 1760 trieda 8 |
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
1. Text → nový modul `zdroj/<produkt>.py` (PRODUCT, DATE, PAGES; jedna položka = jedna strana, stránkovanie ako originál; voliteľne EXTRA_CSS). Vzor: `baderomsrens.py` (nie nebezpečný), `sw_impregnering.py` (nebezpečný: piktogramy, zloženie, limity, ADR tabuľka), `sw_eko.py` (len H319, preberá CSS zo SW), `lms.py` (žieravý, 7 zložiek, DNEL/PNEC v dvoch stĺpcoch), `lmd.py` (= LMS, mení len názov a UFI), `sofarens.py` (= Baderomsrens, mení len názov), `polisher.py` (= SW, mení názov, použitie a UFI), `lotos_standard.py` (= SW, mení názov a UFI), `gravsteinrens.py` (= Baderomsrens, mení len názov), `whitewood.py` (= LMS, mení názov a UFI), `swb.py` (= SW EKO, mení názov a UFI), `lotos_profi.py` (= SW EKO, ale neklasifikovaný – prepísané strany 1–4, 7, 9, 14).
2. `cd zdroj && python3 build.py <produkt>` → `<produkt>.html`; potom `NODE_PATH=$(npm root -g) node render.js $PWD/<produkt>.html <výstup>.pdf` (HTML potom zmazať).
   Skript vypíše výšku obsahu každej strany (max 220 mm), ak niečo pretečie, dá strane červený rámik.
3. Názov produktu a dátum sú v module (hlavička sa berie odtiaľ).

**Pasce:** Playwright je len v Node (`require('playwright')`), nie v Pythone. Fonty Khand z GitHubu cez `raw.githubusercontent.com` (github.com/raw je blokovaný). Slogan je súčasť obrázka hlavičky → `logo.py`.

## Ako nahrať na web
stagedUploadsCreate (resource FILE, application/pdf) → curl POST súboru → fileCreate (contentType FILE) → počkať na READY a vziať `url` → záloha popisu do `02_PRACA/zalohy/` → productUpdate: na koniec descriptionHtml `<hr><h3>Sikkerhetsdatablad</h3><p>… <a href=URL target=_blank>Last ned sikkerhetsdatablad (PDF)</a></p>`.

**Text na webe (Luk, 27. 10.):** bez „på norsk“ — web je nórsky, jazyk sa nepíše: „Sikkerhetsdatabladet (SDS) for <produkt> kan lastes ned her: Last ned sikkerhetsdatablad (PDF)“.

**Pasce pri nebezpečných produktoch:** tabuľky v SK origináli sú obrázky (pdftotext ich nevidí) → čítať stránky ako obrázok. Poľské limity (NDS) nahradiť nórskymi grenseverdi (izopropanol: 100 ppm / 245 mg/m³, 8 h — overené z viacerých nórskych SDS; lovdata.no je z cloudu blokovaný). V SW origináli mali prepravné nálepky chybne „2“ → vlastná `adr3.svg`. GHS piktogramy `ghs02.png`, `ghs07.png`.

**LMS (27. 10.):** symboly žieraviny `ghs05.svg` a ADR `adr8.svg` sú vlastné kresby. Prvá pomoc (4.1) a ochranné pomôcky (8.2) boli v SK origináli príliš mierne na H314 → zosúladené s P-vetami z 2.2 (uvedené v revízii). Limity: oksalsyre a fosforsyre 1 mg/m³ (8 h), izopropanol 100 ppm/245 mg/m³.

**Pasca:** pred prekladom porovnaj nový SK originál s už preloženými (`diff` textu + `md5sum` obrázkov z `pdfimages -j`) — LMD bol zhodný s LMS.
