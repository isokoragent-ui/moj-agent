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

### Video Story Badepakken (2026-10-26)
`badepakken_jul_story.mp4` — 13 s, 1080 × 1920, 30 fps, **bez zvuku** (hudbu pridá Luk v Instagrame/TikToku).
Scény: „Før – Kalk på dusjdøra?“ (0–3 s) → stierka na „Etter – Blank igjen, uten harde kjemikalier“ (3–6 s) → fľaše + „Julen starter med et rent bad“ + „Begge for 349 kr inkl. frakt“ + „spar 48 kr“ + isokor-skandinavia.no (6–13 s). Sneží celý čas.
Zdroj: `zdroj/badepakken_jul/video.html` + `frames.js` (snímky) → `ffmpeg -framerate 30 -i frames/f%04d.jpg -c:v libx264 -pix_fmt yuv420p -crf 18`.

### Video na šírku Badepakken (2026-10-27)
`badepakken_jul_wide.mp4` — 13 s, 1920 × 1080, bez zvuku, na web (úvodná stránka / produkt). Rovnaký príbeh ako Story: fotka vľavo v rámčeku, text vpravo → fľaše vpravo, nadpis + cena + adresa vľavo.
Zdroj: `zdroj/badepakken_jul/video_wide.html` + `frames_wide.js`.

## Kjøkkenpakken — vianočná ponuka (2026-10-30)
„Julepakke · Julen starter med et rent kjøkken" — Kjøleskapsrens + Fett- og flekkfjerner, **begge for 349 kr inkl. frakt**, „hver for seg 397 kr med frakt – du sparer 48 kr". Rovnaký dizajn ako Badepakken (séria). Dole namiesto pred/po tri ikony: Kjøleskap · Fryser · Komfyr og benk.
Fľaše = Lukova fotka Cleaner, vystrihnutá, **nalepené nové nórske etikety** (schéma `07_SCHEMY/ETIKETA_NA_FLASU.md`).

| Súbor | Rozmer | Na čo |
|---|---|---|
| `kjokkenpakken_jul_portrait.png` | 1080 × 1350 | Instagram/Facebook feed |
| `kjokkenpakken_jul_square.png` / `.jpg` | 1080 × 1080 | feed, hlavná fotka produktu (JPEG pre TikTok) |
| `kjokkenpakken_jul_story.png` | 1080 × 1920 | Story / Reels |
| `kjokkenpakken_produkt.jpg` | 2048 × 2048 | produktová fotka (obe fľaše, svetlé pozadie) |

Zdroj: `zdroj/kjokkenpakken_jul/` → `node render.js` (grafika), `python3 packshot.py` (fotka), `python3 nalep.py` (fľaše).

### Kjøkkenpakken — nórska verzia (2026-10-30, Luk chcel „viac nórske, chytľavé, iná farba")
„Ribbe eller pinnekjøtt? *Rent kjøleskap uansett.*" — vtip na večný nórsky spor o vianočné jedlo. Julerød #b3202d + krémová #fbf3e4, pletený pás so **selburose** (nórsky vzor z vianočných svetrov) hore a dole, cenovka ako vianočná visačka „Begge for 349,- · Frakt inkludert" (nórsky zápis ceny „349,-"), fľaše na krémovom tanieri. Písmo DM Serif Display + Assistant.

| Súbor | Rozmer |
|---|---|
| `kjokkenpakken_norsk_portrait.png` | 1080 × 1350 |
| `kjokkenpakken_norsk_square.png` / `.jpg` | 1080 × 1080 |
| `kjokkenpakken_norsk_story.png` | 1080 × 1920 |

Zdroj: `zdroj/kjokkenpakken_jul/norsk.html` → `node render_norsk.js`. Pletenina sa kreslí v canvase z bitmapy `ROSE` (13 × 13 očiek).
✅ Luk 30. 10. vybral **červenú nórsku verziu** — hlavná fotka produktu Kjøkkenpakken, príspevok pi 6. 11., e-mail ne 8. 11. Zelená ostáva v zálohe.

### Video Kjøkkenpakken — nórska verzia (2026-10-30)
`kjokkenpakken_norsk_story.mp4` (1080×1920) a `kjokkenpakken_norsk_wide.mp4` (1920×1080) — 14 s, s hudbou (`hytteservice/hudba.py`, hracia skrinka). Scény: „Ribbe – eller pinnekjøtt?" → „Uansett: kjøleskapet trenger en vask før julematen" → fľaše na tanieri, visačka 349,- spadne a zahojdá sa, „du sparer 48,-", isokor-skandinavia.no. Pletený pás sa posúva, sneží.
Zdroj: `zdroj/kjokkenpakken_jul/video_norsk.html` (`?f=wide` pre šírku) + `frames_norsk.js` (`OUT=…`, `WIDE=1`).

## Video Cleaner — „Fra naturen til kjøkkenbenken“ (2026-11-15)
`cleaner_natur_story.mp4` — 15 s, 1080 × 1920, 30 fps, s hudbou (vlastná, `zdroj/cleaner_natur/hudba.py`). Produkt: **Isokor Fett- og flekkfjerner** (SK: Cleaner). Štýl: decentný, prírodný, skoro luxusný — krémový papier, tmavozelená, zlatá; písmo Cormorant Garamond + Jost.
Scény: rastliny zo zloženia sa samy nakreslia — Appelsin, Sitron, Mandel, Seder („Det begynner i naturen“) → zlaté kvapky oleja z nich stečú do jednej („Ekte planteoljer · Dråpe for dråpe“) → kvapka padne do fľaše („Samlet i én flaske“) → zelená kamenná linka s mastnotou, sprej, utretie, lesk („Fettet løsner. Benken skinner.“) → fľaša + rastlinky, „Naturlig · Miljøvennlig · Biologisk nedbrytbar“, isokor-skandinavia.no.
Tvrdenia len z etikety (oleje: appelsin, sitron, mandel, seder sú v zložení). Stav: 🟡 návrh v1 — čaká na Lukovu kontrolu.
Zdroj: `zdroj/cleaner_natur/video.html` + `frames.js` (`OUT=…`, `KONTROLA=1.0,5.5` = len vybrané časy) → `ffmpeg -framerate 30 -i f%04d.jpg -i hudba.wav -c:v libx264 -pix_fmt yuv420p -crf 18 -af loudnorm=I=-16 -c:a aac`.

### Video Cleaner v2 — realistické (2026-11-15)
`cleaner_natur_v2_story.mp4` — 15 s, 1080 × 1920, 30 fps, s hudbou. Luk: „koncept veľmi dobrý, ale realistickejšie“. Fotky vygeneroval Luk v Gemini podľa `zdroj/cleaner_natur/PROMPTY_GEMINI.md` (`zdroj/cleaner_natur/in/1–6`), agent ich rozpohyboval a vložil **skutočnú fľašu** (`kjokkenpakken_jul/flaska_fett.png`).
Scény: sad s pomarančmi, ranný opar („Det begynner i naturen“) → suroviny na kameni, záblesky na kvapkách oleja („Ekte planteoljer · Appelsin, sitron, mandel og seder“) → zlatá kvapka sa odtrhne od cédra a padá („Dråpe for dråpe“) → fľaša zostúpi na travertínový podstavec, prebehne svetlo („Samlet i én flaske“) → kuchyňa: fľaša prilieta, **2× strikne z hubice** šikmo na mastnotu, kvapôčky na linke, stieranie odkryje čistú linku (obrázok 6), lesk („Fettet løsner. Benken skinner.“) → záver na podstavci: „Fett- og flekkfjerner · Naturlig · Miljøvennlig · Biologisk nedbrytbar“ + isokor-skandinavia.no.
Stav: 🟡 návrh v2 — čaká na Lukovu kontrolu.
Zdroj: `node texty.js` (texty → PNG) → `python3 video2.py PRIECINOK [časy]` (snímky; s časmi len kontrolné) → `python3 hudba.py hudba.wav 15 5.95 10.35,10.85` → `ffmpeg -framerate 30 -i f%04d.jpg -i hudba.wav -c:v libx264 -pix_fmt yuv420p -crf 20 -preset slow -af loudnorm=I=-16 -c:a aac`. Potrebuje `pip install opencv-python-headless`. Render celého videa ~3 min.

### Video Cleaner v3 — jednoduchšie, BEZ ZVUKU (2026-11-15) ✅ aktuálna verzia
`cleaner_natur_v3_story.mp4` — 12 s, 1080 × 1920, 30 fps, **bez zvukovej stopy** (Luk: hudbu si pridá sám ručne). Luk: kuchyňa so striekaním zbytočná → preč; fľaša väčšia, bez podstavca, medzi surovinami.
Scény: sad („Det begynner i naturen“) → suroviny („Ekte planteoljer · Appelsin, sitron, mandel og seder“) → kvapka padá („Dråpe for dråpe“) → veľká fľaša jemne dosadne na ľan pred pomaranč, list, céder a mandle, svetlo zľava, prebehne odlesk („Samlet i én flaske“) → „Fett- og flekkfjerner · Naturlig · Miljøvennlig · Biologisk nedbrytbar“ + isokor-skandinavia.no.
Obrázok bez podstavca: Luk v Gemini (`in/4b_bez_podstavca.jpg`, prompt 4b). Zdroj: `zdroj/cleaner_natur/video3.py` → `ffmpeg -framerate 30 -i f%04d.jpg -c:v libx264 -pix_fmt yuv420p -crf 20 -preset slow -an`.
- 2026-11-15 (neskôr): **fľaša vymenená za Lukovu novú fotku s etiketou CLEANER** (nové logo Isokor) — `zdroj/cleaner_natur/in/flasa_cleaner_nova_foto.jpg` → `python3 vystrihni_flasu.py` (rembg isnet + očistenie odrezkov kartónu, spúšť bez hnedého nádychu) → `flasa_cleaner_nova.png`; v scéne +8 % jas (fotka bola v šere). Záver: „Isokor · **Cleaner** · *Fett- og flekkfjerner*“ (na fľaši je CLEANER, v e-shope „Isokor Fett- og flekkfjerner“, v popise „Isokor Cleaner“).
