# Kjøkkenpakken – Julen starter med et rent kjøkken

*2026-10-30 · okno „Kjøkkenpakken" · Luk „áno" (30. 10.): nórska červená verzia, zverejnenie pi 6. 11., e-mail ne 8. 11.*

## Produkt (Shopify)
- **Isokor Kjøkkenpakken** · `/products/kjokkenpakken` · id gid://shopify/Product/8767215173811
- Obsah: Isokor Kjøleskapsrens (Fridge Cleaner) 500 ml + Isokor Fett- og flekkfjerner (Cleaner) 500 ml
- **349 kr vrátane dopravy** (Luk 30. 10.) — variant v doručovacom profile „Badepakken – frakt inkludert" (0 kr Nórsko), presne ako Badepakken
- Hver for seg: 2 × 149 + 99 = 397 kr → spar 48 kr
- Vlastný sklad **9 ks** (= sklad Fett- og flekkfjerner 9; Kjøleskapsrens má 20). Predaj balíka neodráta jednotlivé fľaše → stráži Luk ručne (ako Badepakken).
- Váha 1,2 kg · kolekcie Produktkatalog + Kjøkken · štítky bundle, kitchen, fridge, cleaner, eco, jul
- Fotky: vianočná grafika 1080×1080 (hlavná) + produktová fotka 2048×2048 (obe fľaše na svetlom pozadí)
- Popis NO + SEO + odkazy na oba bezpečnostné listy
- Marža: chýbajú nákupné ceny Kjøleskapsrens a Fett- og flekkfjerner — doplniť, keď ich Luk pošle (pri Badepakken 2 × 59,40 kr).

## Plán (Luk 30. 10.)
- **Piatok 6. 11. 2026** — zverejniť produkt + príspevok (streda 4. 11. je obsadená iným príspevkom). Návrh čas 10:30.
- **Nedeľa 8. 11. 2026, 9:30** — e-mail (nyhetsbrev č. 2) s Kjøkkenpakken všetkým zákazníkom e-shopu (Shopify Messaging).
  ⚠️ Pred odoslaním overiť, komu smieme písať: so súhlasom s marketingom áno; zákazníkom bez súhlasu len podľa výnimky v markedsføringsloven § 15 (podobné vlastné produkty, jednoduché odhlásenie) — agent overí pri príprave.
- Grafika: **nórska červená verzia** (selburose, „Ribbe eller pinnekjøtt?") alebo zelená (séria s Badepakken) — vyberá Luk.

## Po „áno" (agent spraví)
1. Hlavnú fotku produktu vymeniť za vybranú verziu. `productUpdate status: ACTIVE` + `publishablePublish` s `publishDate` pi 6. 11. (produkt sa sám ukáže v ten deň) (Badepakken je aj v POS, Facebook, Shop, Google — rovnako?).
2. Overiť `onlineStoreUrl` a košík: Kjøkkenpakken samotný → doprava 0 kr.
3. Príspevok naplánovať v Metricoole (FB + IG + Threads + Google; TikTok len JPEG → `kjokkenpakken_jul_square.jpg`).

## Text príspevku (NO, návrh — sedí aj na Threads)
*Pri nórskej verzii prvý riadok: „Ribbe eller pinnekjøtt? 🎄 Rent kjøleskap uansett."*

Julen starter med et rent kjøkken 🎄

Før julematen skal inn, fortjener kjøleskapet en skikkelig vask. Kjøkkenpakken fra Isokor:

🧊 Kjøleskapsrens – kjøleskap og fryser, trygt der maten står, uten skylling
🍳 Fett- og flekkfjerner – fett på komfyr, benk, ventilator og fliser

Naturlig · Biologisk nedbrytbar · V-Label

Begge for 349 kr – frakt i hele Norge inkludert (hver for seg 397 kr med frakt).

👉 isokor-skandinavia.no/products/kjokkenpakken

## Grafika → `02_PRACA/grafika/` (README, sekcia Kjøkkenpakken)

## ✅ NAPLÁNOVANÉ (30. 10., Luk „áno")
- **Shopify — ŽIVÝ od 30. 10. 2026 23:44 Oslo** (Luk: „nemusíme čakať") vo všetkých 5 kanáloch (Online Store, POS, Facebook, Shop, Google), `onlineStoreUrl` = https://isokor-skandinavia.no/products/kjokkenpakken, `availableForSale: true`, doprava 0 kr (overené). Pôvodný plán nižšie už neplatí.
- ~~**Shopify:** produkt ACTIVE, hlavná fotka = nórska červená verzia. Zverejnenie **pi 6. 11. 2026 8:00 Oslo** naplánované v **Online Store + Google** (publishDate). Overené: teraz `onlineStoreUrl: null`, `isPublished: false`.
  ~~⚠️ POS, Facebook a Shop naplánovanie (publishDate) **neprijali** → v piatok po 8:00 zverejniť aj tam (ako Badepakken).
- **Metricool pi 6. 11. 10:30** FB + IG + Threads + TikTok (foto JPEG) + Google — text nižšie (490 znakov), obrázok `kjokkenpakken_norsk_portrait.jpg` → [plánovač](https://app.metricool.com/planner/calendar?blogId=7484747&openWithPostUuid=2058566352876947904)
- **Metricool pi 6. 11. 12:00** Story FB + IG (`kjokkenpakken_norsk_story.jpg`) → [plánovač](https://app.metricool.com/planner/calendar?blogId=7484747&openWithPostUuid=-5477645151936428240)
- **E-mail ne 8. 11. 9:30** → `02_PRACA/emaily/2026-11-08_nyhetsbrev_Kjokkenpakken.md` (text čaká na Lukovo OK, zadáva Luk v Messaging).
- Obrázky v Shopify Súboroch: kjokkenpakken-norsk-feed.jpg, kjokkenpakken-norsk-story.jpg.

### Text príspevku (naplánovaný)
Ribbe eller pinnekjøtt? Der blir vi aldri enige – men et rent kjøleskap trenger alle før julematen skal inn.

Kjøkkenpakken fra Isokor: Kjøleskapsrens til kjøleskap og fryser, trygt der maten står, og Fett- og flekkfjerner til komfyr, benk og kjøkkenvifte. Naturlig og biologisk nedbrytbar.

Begge for 349 kr, frakt i hele Norge inkludert. Begrenset antall.
isokor-skandinavia.no/products/kjokkenpakken

Hva blir det hos dere – ribbe eller pinnekjøtt?

#julevask #kjøleskap #julemat #isokor

### Ako „hecnúť" Nórov (návrhy agenta)
- Otázka na konci = komentáre → Meta ukáže príspevok viac ľuďom zadarmo. **Na každý komentár odpovedať** v prvých hodinách (Luk / agent pripraví odpovede).
- Sponzorovanie (Luk zváži): ak, tak tento obrázok, cieľ „návštevy webu" na /products/kjokkenpakken, celé Nórsko, 30–65, ~50 kr/deň — poučenie z Badepakken (5 miest bolo príliš úzko).
- Ďalší krok, ak nepôjde: súťaž „Ribbe eller pinnekjøtt? Kommenter og vinn en Kjøkkenpakke" (stojí 1 balík, pravidlá súťaže treba napísať).
