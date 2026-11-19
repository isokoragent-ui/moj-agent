# Opravy šijacích strojov — marketing (fotky, videá)

*Samostatný projekt. Firma manželky (Systua på Vegårshei / Skredderstuen), Luk spolupracuje — stroje opravuje
popri Isokore, po večeroch. **Nie je to Isokor** — iná firma, iné účty,
iný tón (KÓD #25). Nemiešať s `02_PRACA/` Isokor kampaňami.*

## Čo sem patrí
| Priečinok | Čo tam je | Pravidlo |
|---|---|---|
| `01_originaly/fotky/` | pôvodné fotky od Luka | **nikdy neupravovať ani nemazať** — len čítať |
| `01_originaly/videa/` | pôvodné videá od Luka | to isté; súbor nad ~90 MB → Google Drive (GitHub berie max 100 MB) a sem len odkaz v `ZOZNAM.md` |
| `02_vyber/` | vybrané zábery, výrezy, pracovné verzie | smie sa prepisovať |
| `03_hotove/` | hotové videá/obrázky na zverejnenie | názov `RRRR-MM-DD_tema_format.mp4` (napr. `_9x16`, `_1x1`) |
| `04_texty/` | popisky, hashtagy, scenáre, nápady | jeden súbor = jeden príspevok |

## Zdroje
- `ZOZNAM.md` — čo prišlo, kedy, aký stroj, čo sa na ňom robilo
  (agent dopĺňa pri každom novom súbore).

## Ako to beží
1. Luk nahrá fotky/videá do chatu (agent do tabletu nevidí) → agent ich uloží
   do `01_originaly/` a zapíše do `ZOZNAM.md`.
2. Agent navrhne video/príspevok (scenár + strih + text) → `02_vyber/`.
3. Luk schváli → hotové do `03_hotove/`.
4. Manželka si hotové video + text stiahne a zverejní ručne.

## Tón
Ľudský, odľahčený, „dielňa po večeroch“ — pred/po, detaily mechaniky,
zvuk stroja, ktorý znovu šije. Nič korporátne.

## Firma
- **Firma:** Systua på Vegårshei
- **Prevádzka:** Skredderstuen — web `www.skredderstuen.no`
- **Jazyk:** všetko po nórsky (videá, titulky, popisky, hashtagy)
- **Siete:** Facebook + Instagram → hlavný formát video na výšku 9:16
  (Reels, ide na FB aj IG), k tomu prípadne štvorec 1:1 do feedu
- **Zverejňovanie (rozhodnuté 19. 11. 2026):** manželka nahrá hotové videá
  **ručne** na FB, IG aj web. Agent nič nezverejňuje, Metricool sa pre
  Skredderstuen nepoužíva (je tam len Isokor — nikdy cez Isokor účty).
- **Agent odovzdáva:** hotové video v `03_hotove/` + nórsky popis s hashtagmi
  v `04_texty/` (pripravené na skopírovanie).

## Otvorené
- Logo/farby, názvy FB a IG profilov — doplniť.

## Nástroj
- `video_reel.py <scenar.json> <vystup.mp4>` — z fotiek spraví Reel 9:16
  (pomalý zoom, nórsky text v hornej tretine, prelínanie, záverečná karta).
  Scenáre v `02_vyber/*_scenar.json`. Video je bez hudby — tú pridá manželka
  v Instagrame. Text je hore, lebo spodok a pravý okraj zakrýva rozhranie IG/FB.

## Hotové
| Dátum | Video | Text | Stav |
|---|---|---|---|
| 2026-11-19 | `03_hotove/2026-11-19_service_symaskin_9x16.mp4` | `04_texty/2026-11-19_service_symaskin.md` | 🟡 čaká na „áno“ |

## Hudba
- `01_originaly/hudba/En_drape_olje.mp3` — **vlastná pieseň Skredderstuen
  (vygenerovaná, smieme ju voľne použiť — Luk 19. 11. 2026)**. 3:01, 120 BPM;
  refrén 42,1–73,1 s a 104–154 s; outro od 155 s.
