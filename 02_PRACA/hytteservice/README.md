# Isokor Hytteservice — balík na spustenie (2026-10-29)

**Stav:** ✅ **SPUSTENÉ 29. 10. 2026 ~20:40** (Lukovo „áno"). Stránky, kolekcia a 5 produktov sú živé v Online Store, „Hytteservice" je v hlavnom menu za „Tjenester" (záloha menu: `02_PRACA/zalohy/2026-10-29_menu_hovedmeny_pred_hytteservice.json`). Fotky od Luka (chata v snehu, krajina) na produktoch a na stránke. Overené čítaním cez API (živý web je z cloudu blokovaný → Luk pozrie na mobile).

**Príspevky naplánované (Metricool, autoPublish):** pi 30. 10. 10:30 FB + IG + Threads ([plánovač](https://app.metricool.com/planner/calendar?blogId=7484747&openWithPostUuid=-1272555852719438972)), 10:35 Google profil ([plánovač](https://app.metricool.com/planner/calendar?blogId=7484747&openWithPostUuid=5383102661922670992)). Text bez emoji podľa `03_STYL/HLAS.md`.

**Robí Luk ručne:** príspevok do miestnych FB skupín, Finn inzerát, list pre hyttevel, leták — texty v `REKLAMA_NO.md`.

## V e-shope (Shopify) — vytvorené ako koncept, overené čítaním
| Čo | Handle | Stav |
|---|---|---|
| Stránka „Hytteservice" | `/pages/hytteservice` | ✅ živá |
| Stránka „Vilkår for Hytteservice" | `/pages/vilkar-hytteservice` | ✅ živá |
| Kolekcia „Hytteservice" (automaticky podľa štítku `hytteservice`) | `/collections/hytteservice` | ✅ živá, 5 produktov |
| Hytteservice – Høstlukking | 3 490 / 4 490 kr | ✅ ACTIVE |
| Hytteservice – Vintertilsyn hver 14. dag | 5 490 / 6 490 kr | ✅ ACTIVE |
| Hytteservice – Våråpning | 4 490 / 6 490 kr | ✅ ACTIVE |
| Hytteservice – Hele vintersesongen | 11 990 / 15 990 kr | ✅ ACTIVE |
| Hytteservice – Ekstra tilsynsbesøk | 590 kr | ✅ ACTIVE |

Produkty: bez dopravy (`requiresShipping: false`), bez skladu, typ „Tjeneste".
Varianty „Opptil 100 m²" / „Over 100 m²". Ceny = konečné pre súkromníkov
(obchod má `taxesIncluded: true` → po registrácii MVA sa cena nemení).
Zdroj textov: `stranka_hytteservice.html`, `stranka_vilkar_hytteservice.html`, `produkty.json`.

## Podklady pre prácu
- `SJEKKLISTER.md` — zatvorenie / kontrola / otvorenie
- `EMAIL_PO_OBJEDNAVKE_NO.md` — otázky po objednávke + súhlas so štartom pred koncom lehoty na odstúpenie
- `_nastroje/tilsynslogg.py` + `logg/` — PDF záznam pre poisťovňu (vzor `logg/_PRIKLAD.pdf`)
- `REKLAMA_NO.md` — FB/IG, Google, FB skupiny, Finn, hyttevel, leták, newsletter

## Spustenie — ako sa to spravilo (29. 10.)
1. Zverejniť obe stránky, produkty → ACTIVE + Online Store, kolekciu → Online Store
2. Pridať „Hytteservice" do menu
3. Overiť čítaním + Luk pozrie na mobile
4. Príspevky do Metricoolu ako draft (s Lukovou fotkou)

## Pasce
- `collectionCreate(input:)` je v API 2026-10 zastarané → `collection:` + `sources` (podmienka `productTag`).
- `pages(query:"title:…")` nenašlo nové stránky → overovať cez `page(id:)`.

## Úpravy 29. 10. večer (Luk)
- Úvod bez konkrétnych miest („bor et stykke unna – kanskje i en annen by eller landsdel"); oblasť len **Vegårshei, Tvedestrand og Risør** (Gjerstad a Åmli preč) — stránka, produkty, príspevky, reklamné texty.
- Sneh: žiadna cena za m², „snømåking kun etter avtale og når vi har kapasitet"; snømåking **nie je súčasť kontroly**, pri veľkom snehu bez záruky (stránka, podmienky bod 2, Vintertilsyn, Hele sesongen).
- Galéria náhrobných kameňov dole: pochádzala zo šablóny `page.json` (XO Gallery „gravsttter-vedlikehold"). Tému nemeníme → stránka Hytteservice prepnutá na šablónu **`tjenester`** (text + recenzie), Vilkår na **`sertifikater`** (len text).
