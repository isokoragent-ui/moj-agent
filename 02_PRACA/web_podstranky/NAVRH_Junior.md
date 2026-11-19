# Isokor Junior – nový produkt v e-shope (2026-11-19)
Luk 19. 11.: 149 kr, ~20 ks, dať do e-shopu + medzi najpredávanejšie na úvodnej stránke (vymeniť za iný). Poslal 4 fotky: skutočná fľaša s NO nálepkou „BABY CLEANER – Rensemiddel for vask av leker og barnemøbler“, 2× SK render 500 ml, SK kanister 5 l.
Zdroj textov: NO etiketa `02_PRACA/etikety/zdroj/junior_500ml.py` + SDS NO 1.0 (= Baderomsrens, nie je nebezpečný).

## Stav
- Produkt `gid://shopify/Product/8802227257523`, handle `isokor-junior`, názov „Isokor Junior – rens for leker og barnemøbler“, **DRAFT** (kým nie sú fotky), 149 kr, 20 ks (sklad Nærestadveien 1), 0,6 kg, kolekcie Produktkatalog, Rengjøring og vasking i husholdningen, Helsebeskyttelse og hygiene, Stue og oppholdsrom. Metapolia isokor.* vyplnené (bez `sds` – PDF nie je v Shopify Súboroch).
- Na fľaši je „BABY CLEANER“ → v popise aj FAQ „Hvorfor står det Baby Cleaner på flasken?“.
- **Úvodná stránka:** kópia živej témy „Isokor – JUL 2026 + Junior (19. 11.)“ `…/156333179059` (NEZVEREJNENÁ): v „Populært før jul“ Baderomsrens → **Junior** (tag „Barn“, „Leker, matstoler og barnevogn – ingen skylling.“). Baderomsrens ostáva v Julepakker (Badepakken). Lokálna kópia `02_PRACA/web_uvod/tema/templates/index_junior_2026-11-19.json`.

## Ďalej
1. Luk nahrá fotky (okno upload_file) → pripojiť k produktu (fileUpdate referencesToAdd).
2. Produkt ACTIVE + Online Store (+ ostatné kanály ako Baderomsrens).
3. Luk zverejní tému „…+ Junior“. Bez toho sa na úvodnej stránke nič nemení.
4. SDS Junior nahrať do Súborov (Luk) → metapole `sds`.

## Fotky (19. 11.)
- `02_PRACA/grafika/junior/junior_detska_izba_NO.jpg` — Luk: obrázok s NO etiketou JUNIOR (detská izba, macko). Luk ho pridá k produktu ručne; agent ho smie ďalej používať (siete, grafika).
  ⚠️ Generovaný obrázok: odznak má skomolený text („ANTIMIKRUBIELLE CEERIMLEKER“), vpravo dole staré logo Isokor. Fľaša, ktorú zákazník dostane, má nálepku „BABY CLEANER“.
- `02_PRACA/grafika/junior/baby_cleaner_skutocna_flasa.jpg` — skutočná fľaša s NO nálepkou BABY CLEANER (Lukova fotka).

## ✅ Overené 19. 11. (po Lukových úpravách)
- Produkt **ACTIVE**, 149 kr, 20 ks, `availableForSale` true, 2 fotky (Luk: Baby Cleaner so starým logom + Junior s novým logom; staré nechá, kým nedopredá fľaše so starou etiketou), publikovaný na 7 kanáloch (Online Store, POS, Facebook, Shop, Google, TikTok, Lovable), kolekcie + AVADA Best Sellers.
- **Živá téma = „Isokor – JUL 2026 + Junior (19. 11.)“** `…/156333179059` (Luk zverejnil), v „Populært før jul“ b_2 = Junior. Návrat: „Isokor – JUL 2026 + nové podstránky“ `…/156287008947`.
- Otvorené: alt texty fotiek prázdne; SDS Junior nie je v Súboroch (metapole `sds` prázdne); „PO SVIATKOCH 2027“ Junior nemá (rozhodnúť po Novom roku).
