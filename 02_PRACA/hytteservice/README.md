# Isokor Hytteservice — balík na spustenie (2026-10-29)

**Stav:** všetko pripravené, **nič nie je zverejnené**. Spustenie až po Lukovom „áno".

## V e-shope (Shopify) — vytvorené ako koncept, overené čítaním
| Čo | Handle | Stav |
|---|---|---|
| Stránka „Hytteservice" | `/pages/hytteservice` | nezverejnená |
| Stránka „Vilkår for Hytteservice" | `/pages/vilkar-hytteservice` | nezverejnená |
| Kolekcia „Hytteservice" (automaticky podľa štítku `hytteservice`) | `/collections/hytteservice` | nezverejnená, 5 produktov |
| Hytteservice – Høstlukking | 3 490 / 4 490 kr | DRAFT |
| Hytteservice – Vintertilsyn hver 14. dag | 5 490 / 6 490 kr | DRAFT |
| Hytteservice – Våråpning | 4 490 / 6 490 kr | DRAFT |
| Hytteservice – Hele vintersesongen | 11 990 / 15 990 kr | DRAFT |
| Hytteservice – Ekstra tilsynsbesøk | 590 kr | DRAFT |

Produkty: bez dopravy (`requiresShipping: false`), bez skladu, typ „Tjeneste".
Varianty „Opptil 100 m²" / „Over 100 m²". Ceny = konečné pre súkromníkov
(obchod má `taxesIncluded: true` → po registrácii MVA sa cena nemení).
Zdroj textov: `stranka_hytteservice.html`, `stranka_vilkar_hytteservice.html`, `produkty.json`.

## Podklady pre prácu
- `SJEKKLISTER.md` — zatvorenie / kontrola / otvorenie
- `EMAIL_PO_OBJEDNAVKE_NO.md` — otázky po objednávke + súhlas so štartom pred koncom lehoty na odstúpenie
- `_nastroje/tilsynslogg.py` + `logg/` — PDF záznam pre poisťovňu (vzor `logg/_PRIKLAD.pdf`)
- `REKLAMA_NO.md` — FB/IG, Google, FB skupiny, Finn, hyttevel, leták, newsletter

## Spustenie (po „áno") — agent vie spraviť sám cez API
1. Zverejniť obe stránky, produkty → ACTIVE + Online Store, kolekciu → Online Store
2. Pridať „Hytteservice" do menu
3. Overiť čítaním + Luk pozrie na mobile
4. Príspevky do Metricoolu ako draft (s Lukovou fotkou)

## Pasce
- `collectionCreate(input:)` je v API 2026-10 zastarané → `collection:` + `sources` (podmienka `productTag`).
- `pages(query:"title:…")` nenašlo nové stránky → overovať cez `page(id:)`.
