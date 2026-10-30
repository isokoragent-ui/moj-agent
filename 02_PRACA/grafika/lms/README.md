# Grafika Isokor LMS (kampaň Rust, okt./nov. 2026)
- `fotky/` — Lukove skutočné fotky (fľaša, WC pred/po, dlažba 1–4). `dlazba_pred_po.jpg` = spojené v Gemini, nepoužíva sa.
- Obrázky: `lms_wc_pred_po_*`, `lms_dlazba_pred_po_*`, `lms_dlazba_kroky_*` (1080×1350 feed, 1080×1920 Stories).
- Videá 15 s s hudbou: `lms_video_vertikal_1080x1920.mp4`, `lms_video_16x9_1920x1080.mp4` (WC pred/po → dlažba pred / sprej / po → záver s fľašou a cenou).
- Postup: `python3 video_lms.py vertikal|sirka <priečinok>` → hudba `python3 ../hytteservice/hudba.py hudba.wav 15` → ffmpeg (libx264 crf 22, aac 160k, -shortest, +faststart).
- `fotky/lms_flasa_cela.jpg` (Luk 30. 10., celá fľaša) → `fotky/lms_flasa_vystrihnuta.png` (pozadie odstránené rembg isnet-general-use + len najväčší súvislý kus). `fotky/lms_flasa_hrdza_eshop.jpg` = hlavná fotka v e-shope (nápis na etikete iný než na skutočnej fľaši → pravdepodobne AI, do reklám nie).
- **Karusel (30. 10.)** — prezentácia produktu, 8 slajdov 1080×1350: `karusel/lms_karusel_1…8.jpg` (obálka pred/po · kde všade · WC · dlažba 3 kroky · slik gjør du · aj vodný kameň · služba „Store flater? Vi tar jobben.“ · cena 149 kr). Skript `python3 karusel_lms.py fotky karusel`, text príspevku `karusel/TEXT_PRISPEVKU_NO.md`. Kov / pozinkované vozíky / profily v karuseli nie sú (karta 10.5: nezlučiteľné s kovmi) — čaká na výrobcu.
