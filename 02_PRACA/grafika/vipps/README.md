# Vipps QR — plagát na pult (ISOKOR-SKANDINAVIA AS, Vippsnummer 62769)

| Súbor | Na čo |
|---|---|
| `vipps_qr_a5.pdf` | tlač A5 (148 × 210 mm), vektor — QR ostrý |
| `vipps_qr_a4.pdf` | tlač A4 (210 × 297 mm), ten istý plagát zväčšený, vektor |
| `vipps_qr_a5.png` | 1748 × 2480 px (300 dpi) — záloha / na mobil |

- **Odkaz v QR:** `https://qr.vipps.no/vp/naP8rFUcM` — prečítaný z Vipps appky (fotka obrazovky 17. 11. 2026).
  QR je nakreslený nanovo (oprava chýb H, tichá zóna 4 moduly), vzor štvorčekov sa líši od Vippsu, **odkaz je rovnaký**.
- Overené: všetky tri súbory sa dekódujú na tento odkaz, aj zmenšené na ¼. **Pred tlačou ho Luk naskenuje mobilom.**
- Zdroj: `zdroj/vipps.html` → `node zdroj/render.js`; QR: `python3 zdroj/qr.py` (keby Vipps vydal nový kód, zmeň `URL`).
- Pasca: Vipps appka sťahuje QR ako „txt“ a na tablete sa neotvorí → stačí screenshot obrazovky, kód sa z neho prečíta.
- Logo Vipps zámerne nie je (ochranná známka) — len text „Betal med Vipps“.
