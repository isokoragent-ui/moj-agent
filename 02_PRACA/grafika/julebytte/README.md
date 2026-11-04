# Grafika — Isokor Julebytte (4. 11. 2026, návrh)

Štýl: zelená ako Hytteservice (#1b3a28) + červený pletený pás so selburose ako Kjøkkenpakken, sneh.
Oblasť: Vegårshei a Gautefall. Slajd 4 má miesto na `interior.jpg` — AI interiér Luk 4. 11. zrušil (šetríme kredity); keby sa niekedy pridal, karusel ho použije sám.
Fotky: Lukova chata v snehu (výrez z bannera Hytteservice — originál nie je v repozitári), fľaše Kjøleskapsrens, Cleaner (Universalrens, stará etiketa), Fett- og flekkfjerner.

| Súbor | Formát | Na čo |
|---|---|---|
| `julebytte_karusel_1…6.jpg` | 1080×1350 | karusel FB + IG |
| `julebytte_foto_1…6.jpg` | 1080×1350 | **fotokarusel** — viac fotiek, menej textu (ako LMS): chata, WC pred/po, sprcha pred/po (Lukove zákazky), Cleaner, fľaše, CTA. Zdroj `fotokarusel.html` + `node render_foto.js [priečinok] [video]` |
| `julebytte_post_1080x1350.jpg` | 1080×1350 | samostatný príspevok, Google profil |
| `julebytte_story_1.jpg`, `_2.jpg` | 1080×1920 | Stories |
| `julebytte_video_story_1080x1920.mp4` | 16 s, hudba | Reels, TikTok, Shorts, Stories |
| `julebytte_video_wide_1920x1080.mp4` | 16 s, hudba | Facebook, YouTube, web |
| `julebytte_karusel_video_vertikal_1080x1920.mp4`, `julebytte_karusel_video_16x9_1920x1080.mp4` | 21,4 s, hudba | video zo slajdov karuselu (Reels/TikTok/Stories; FB/YouTube) — `VIDEO=1 node render.js karusel_video` → `python3 video_karusel.py vertikal\|sirka <priečinok>` → `hudba.py … 22` → ffmpeg (ako LMS) |
| `Isokor_Julebytte_presentasjon.pdf` + `julebytte_presentasjon_1…7.jpg` | 1920×1080, 7 strán | prezentácia pre majiteľov/správcov chát (zdroj `presentasjon.html` + `node render_pres.js`) |

Zdroj: `../zdroj/julebytte/` — `karusel.html` + `node render.js <priečinok>`; video `video.html` + `OUT=… [WIDE=1] node frames.js` → ffmpeg + `../hytteservice/hudba.py výstup.wav 16`.
Texty: `02_PRACA/julebytte/TEKSTY_NO.md`.

Pasce: fotka chaty má len 1080×720 → na Stories je mierne zväčšená; lepšia by bola originálna fotka (Luk nahrá). Na scénach s textom pod fotkou používať `mask-image` (prelínanie), nie farebný prechod — inak vidno obdĺžnik.
