# PRÍSPEVOK NA SOCIÁLNE SIETE (Facebook, Instagram cez Metricool)

**Kedy sa použije:** keď treba pripraviť a naplánovať príspevok o produkte
alebo službe Isokor na Facebook, Instagram (prípadne TikTok, YouTube, Google).
**Naposledy prešla:** 18. 10. 2026 (Peisglassrens, jesenný príspevok)

## Kroky
1. **Over pripojenia volaním** — Metricool `getBrandSettings`, značka
   `isokorskandinavia` (blogId 7484747). V `networksData` musí byť sieť, na
   ktorú ideš (`facebookData`, `instagramData`…). Nie z pamäte (KÓD #4).
2. **Fakty o produkte vždy čerstvo zo Shopify** — `search_products` +
   `get-product`: cena, sklad, adresa (`handle`), popis, fotka. Tvrdenia
   ber len z popisu produktu, nič nové nevymýšľaj.
3. **Text po nórsky podľa `03_STYL/HLAS.md`** — krátke odseky, vecne, bez
   tlaku a superlatívov, bez emoji. Štruktúra: situácia zákazníka → čo
   produkt robí + ako sa používa → cena / doprava → kde kúpiť → 3–4 hashtagy.
   Odkaz: `isokor-skandinavia.no/products/<handle>`.
4. **Obrázok: skutočná fotka produktu zo Shopify** (URL z `featuredImageUrl`),
   Artlist len na náladové pozadie bez fľaše.
5. **Čas:** `getBestTimeToPostByNetwork` pre Facebook na najbližší týždeň,
   timezone `Europe/Oslo`. Overený vrchol: stred týždňa 10:00–12:00.
6. **Vytvor príspevok ako DRAFT** (`createScheduledPost`, `"draft": true`),
   providers facebook + instagram, `facebookData.type` a `instagramData.type`
   = `POST`. Draft sa sám nezverejní.
7. **Ukáž Lukovi** text (+ krátky preklad), fotku, čas a odkaz `plannerUrl`.
8. **Až po jeho výslovnom „áno“** prepni draft na naplánovaný
   (`updateScheduledPost`, `draft: false`).
9. **Po čase zverejnenia over** `getScheduledPosts`: na každej sieti `status: PUBLISHED` + `publicUrl`. Draft môže Luk pustiť aj sám v Metricoole (tak prebehol prvý test).
10. Zapíš do `09_ODOVZDANIE/AKTUALNE.md`, čo vyšlo, kedy a odkazy.

## Pasce — čo nás už vypálilo
- ⚠️ **Pripojenie Facebooku cez web Metricoolu na tablete nefungovalo** —
  tlačidlo „Připojit stránku Facebook“ len znova otvorilo tú istú stránku,
  aj v anonymnom okne. **Funguje appka Metricool** (Google Play). Pri novej
  sieti rovno odporúčaj appku.
- ⚠️ **AI obrázok produktu = vymyslená etiketa.** Zákazník by videl inú
  fľašu, než dostane. Na produkt vždy reálna fotka.
- ⚠️ **Instagram nemá klikateľné odkazy v texte** — adresu písať ako text
  (`isokor-skandinavia.no/...`), nie spoliehať sa na klik.
- ⚠️ **Instagram nemá „najlepší čas“, kým nemá históriu** (pripojený
  18. 10. 2026 → samé nuly). Zatiaľ sa riadiť Facebookom.
- ⚠️ **„Na schválenie“ (review) v Metricoole sme neskúšali** — podľa popisu
  nástroja vyžaduje plán s tímovou správou. Zatiaľ draft + schválenie v chate.
- ⚠️ **Konektor Metricool nevie príspevok zmazať** (overené 18. 10. 2026 — nástroj na mazanie neexistuje). Zbytočné drafty maže Luk ručne v Plánovači.
- ⚠️ Instagram musí byť **profesionálny účet prepojený s FB stránkou**, inak
  ho Metricool nepripojí na publikovanie.

## Čo agent spraví sám / kde čaká na moje „áno"
- sám: overenie pripojení, fakty zo Shopify, text, výber fotky a času,
  vytvorenie DRAFTU v Metricoole
- čaká: prepnutie draftu na naplánovaný / zverejnenie, platená propagácia
  (boost), čokoľvek s cenou alebo zľavou, ktorá ešte nie je na webe
