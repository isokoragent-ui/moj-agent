# Grafika Isokor LMS (kampaň Rust, okt./nov. 2026)
- `fotky/` — Lukove skutočné fotky (fľaša, WC pred/po, dlažba 1–4). `dlazba_pred_po.jpg` = spojené v Gemini, nepoužíva sa.
- Obrázky: `lms_wc_pred_po_*`, `lms_dlazba_pred_po_*`, `lms_dlazba_kroky_*` (1080×1350 feed, 1080×1920 Stories).
- Videá 15 s s hudbou: `lms_video_vertikal_1080x1920.mp4`, `lms_video_16x9_1920x1080.mp4` (WC pred/po → dlažba pred / sprej / po → záver s fľašou a cenou).
- Postup: `python3 video_lms.py vertikal|sirka <priečinok>` → hudba `python3 ../hytteservice/hudba.py hudba.wav 15` → ffmpeg (libx264 crf 22, aac 160k, -shortest, +faststart).
