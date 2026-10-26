# Grafika — zásobník návrhov

*Hotové grafiky pre web a siete. Zdroj je HTML, PNG sa prerenderuje: `node zdroj/render.js` (Playwright).*

## Doprava podľa výšky objednávky (2026-10-26)
Text: „Frakt i hele Norge · Jo mer du handler, jo billigere frakt“ — under 400 kr 99 kr · fra 400 kr 49 kr (halv frakt) · fra 700 kr 0 kr (gratis frakt) · „Sendes med PostNord · Alle priser inkl. mva“ · isokor-skandinavia.no.
Farby: šalviová #eef3ec, tmavozelená #1f4d36; písmo Assistant (ako téma webu).

| Súbor | Rozmer | Na čo | Stav |
|---|---|---|---|
| `frakt_banner.png` | 2000 × 640 | úvodná stránka (počítač) | |
| `frakt_square.png` | 1080 × 1080 | vyskakovacie okno, Facebook | |
| `frakt_mobile.png` | 1080 × 1350 | mobil, Instagram | |

- 2026-10-26: Luk jeden z nich použil sám (ktorý a kde — doplniť, keď povie). Zvyšné nechať v zálohe, vrátime sa k nim.
- Pri zmene cien dopravy (hranice 400/700, sadzby 99/49) treba grafiky prerenderovať — upraviť `zdroj/frakt.html`.

## Badepakken — vianočná ponuka (2026-10-26)
„Julepakke · Julen starter med et rent bad“ — LM Descaling + Bath Cleaner, **begge for 349 kr inkl. frakt**, „hver for seg 397 kr med frakt – du sparer 48 kr“ (2 × 149 + 99). Pred/po: dvere sprchy s vodným kameňom → čisté (Lukove fotky). Fľaše = Lukove fotky, pozadie odstránené (rembg isnet, zvyšok činelu ručne vymazaný).
Farby: ihličnatá zelená #0f3326, zlatá #d9b56b; písmo Fraunces + Assistant. Starý návrh („Gjør kupp på Badepakken!“, AI fľaše) nahradený.

| Súbor | Rozmer | Na čo |
|---|---|---|
| `badepakken_jul_portrait.png` | 1080 × 1350 | Instagram/Facebook feed |
| `badepakken_jul_square.png` | 1080 × 1080 | feed, vyskakovacie okno, produktová fotka |
| `badepakken_jul_story.png` | 1080 × 1920 | Story / Reels |

Zdroj: `zdroj/badepakken_jul/` → `node render.js` (výstup do `02_PRACA/grafika/`).
⚠️ Produkt „Isokor Badepakken“ (349 kr) je v Shopify **DRAFT** a pri cene 349 by sa pripočítala doprava 99 kr → treba vyriešiť „inkl. frakt“, kým sa grafika zverejní.
