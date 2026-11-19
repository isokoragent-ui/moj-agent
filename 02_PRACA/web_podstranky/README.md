# Podstránky e-shopu — nový dizajn (od 2026-11-17)

**Pracovná téma:** „Isokor – JUL 2026 + nové podstránky“ (premenovaná 17. 11.; predtým „PRACOVNÁ (podstránky)“) `gid://shopify/OnlineStoreTheme/156287008947` (kópia živej JUL, NEZVEREJNENÁ).
Náhľad LMS: https://isokor-skandinavia.no/products/lms?preview_theme_id=156287008947
⚠️ Po pozretí náhľadu: https://isokor-skandinavia.no/?preview_theme_id= (inak prehliadač ukazuje náhľad ďalej).

## Čo je hotové v pracovnej téme
- **Vzhľad celého webu** (`assets/isokor-global.css`, načíta ho sekcia `isokor-stil` v hlavičke): zelené oblé tlačidlá, nadpisy Fraunces, zaoblené fotky, tmavá pätička.
- **Pruh hore** (2 správy): doprava 99/49/zdarma · Vipps + 14 dní angrerett. Hlavička sa pri posune nahor ukáže.
- **Pätička:** firma, adresa, org. č. 922 112 975 MVA, telefón, e-mail · menu „Butikk“ (`isokor-butikk`) a „Kundeservice“ (`isokor-kundeservice`) · ikony platieb. (Menu sú nové, živú pätičku neovplyvnili.) „Vilkår“ zámerne nie — podmienky sú nevyplnená šablóna (audit).
- **Košík:** lišta „X kr til billigere / gratis frakt“ + doba doručenia.
- **Stránka produktu – 1 šablóna pre všetky** (`product.json`, skopírovaná aj do 9 starých `product.*.json`):
  kategória · názov · hviezdičky (len ak sú recenzie) · krátky popis + štítky · cena · „På lager · levering 6–10 virkedager“ · výber · množstvo · Kúpiť + Vipps · **box dôvery** (`snippets/isokor-tillit.liquid`: koľko do lacnejšej/bezplatnej dopravy, platby, doručenie, angrerett, telefón) · popis ·
  sekcia `isokor-produkt-info`: Slik gjør du · pred/po s posuvníkom · Passer til / Ikke bruk på / bezpečnostný list · otázky · Passer godt sammen med · na mobile lišta „Legg i kurven“ dole.
- **Kolekcie:** fotky sa už neorezávajú (CSS).

## Obsah produktu = metapolia „Isokor – …“ (Shopify → Produkt → dole Metapolia)
`isokor.kategori` · `kort` · `fordeler` (štítky) · `steg` (kroky) · `passer_til` · `ikke_bruk` · `faq` (JSON `[{"q":"…","a":"…"}]`) · `sds` (odkaz na PDF) · `for_bilde` / `etter_bilde` (fotky pred/po) · `passer_med` (súvisiace produkty).
Prázdne pole = tá časť sa neukáže. Bez `passer_med` sa ukážu produkty z prvej kolekcie.

| Produkt | Stav |
|---|---|
| LMS rustfjerner | ✅ 17. 11. (karusel + SDS), kov opravený podľa `08_ROZHODNUTIA/2026-11-17_lms_kalkfjerner_kov.md`; fotky pred/po čakajú na Luka |
| Fett- og flekkfjerner | ✅ 17. 11. (etiketa + SDS = Baderomsrens; pred/po = fotky rúry z produktu, rôzna orientácia → Luk skontroluje posuvník) |
| Baderomsrens | ✅ 17. 11. (etiketa + SDS; tvrdenia výrobcu antimikrobielt / 99,99 % podľa Luka → `08_ROZHODNUTIA/2026-11-17_baderomsrens_tvrdenia_vyrobcu.md`) |
| Kalkfjerner for bad | ✅ 17. 11. (etiketa NO = preklad výrobcu + SDS LMD; H314 → otázka o rukaviciach) |
| Kjøleskapsrens | ✅ 18. 11. (etiketa + SDS; bez pred/po, bez „Ikke bruk“ – etiketa nič neuvádza; súvisiace: Fett-, Kjøkkenpakken, Polish) |
| Kjøkkenpakken | ✅ 18. 11. (balíček; 2 SDS ako odkazy v otázke, pole `sds` prázdne; doprava „med PostNord“ – Luk 18. 11.) |
| Badepakken | ✅ 18. 11. (balíček; 2 SDS v otázke; rukavice pri Kalkfjerner podľa etikety H314; starý popis „trygg for hele familien / hudvennlig“ ostáva – Luk zvažuje cez výrobcu) |
| Muggfjerner | ✅ 18. 11. (text výrobcu z popisu – NO etiketa nie je; tvrdenia mugg/sopp/sporer + 99,99 % podľa Luka; „bakterier“ nedané – nie je v zdroji) |
| Peisglassrens | ✅ 18. 11. (len zo starého popisu – etiketa NO ani SDS nie sú; SDS doplniť, keď príde od výrobcu; `passer_med` prázdne) |
| Multi Steinrens 5 l | ✅ 18. 11. (= Gravsteinrens, iný názov; „100 % naturlig“ podľa Luka; SDS zatiaľ nie – vlastný list s názvom Multi Steinrens vyrobiť; súvisiace LMS + SW EKO) |
| Sofarens | ✅ 18. 11. (nová NO etiketa + SDS; súvisiace podľa Luka: EcoNeutral, Lotos Standard, Møbelrens) |
| EcoNeutral | ✅ 18. 11. (NO etiketa + SDS; = Anti Urine Cleaner pod NO názvom; „dermatologisk testet og trygt for mennesker og dyr“ podľa Luka; súvisiace Sofarens, Lotos Standard, Møbelrens) |
| Antidugg | ✅ 18. 11. (NO etiketa + SDS, H319 v „Ikke bruk“; zloženie nedané – rozpor etanol/izopropanol čaká na výrobcu) |
| Bilrens | ✅ 18. 11. (NO etiketa + SDS; súvisiace Antidugg, Sofarens, EcoNeutral) |
| Universalrens | ✅ 18. 11. (NO etiketa + SDS v1.1; koncentrát 1:5–1:100; „antimikrobiell“ z etikety; zdravotné tvrdenia zo starého popisu nedané) |
| Clinic | ✅ 18. 11. (NO etiketa + SDS; „antimikrobielle egenskaper bekreftet ved testing“ + SUJCHBO 56/2015/LTL z etikety; vírusy/baktérie/99,99 % nedané) |
| EcoDescal | ✅ 18. 11. (NO etiketa + SDS = LMS, H314 → rukavice/okuliare; „uten farlige stoffer“ nedané) |
| Møbelrens | ✅ 18. 11. (= Furniture Cleaner; NO etiketa vyrobená v ten istý deň → „99,99 % proteinforurensning“ + „trygt for mennesker og husdyr“ z etikety; súvisiace Polish, Sofarens, EcoNeutral) |
| Polish | ✅ 18. 11. (nano-impregnácia, nie čistič; SDS = SW: H225/H319/H336 v „Ikke bruk“; postup nanášania chýba – doplniť zo SK etikety Polisher) |
| Lotos Standard | ✅ 18. 11. (impregnácia textílií; SDS = SW: H225/H319/H336 v „Ikke bruk“; „helsemessig trygg“ nedané; súvisiace Lotos Profi, Sofarens, EcoNeutral) |
| Lotos Profi | ✅ 18. 11. (trvalá impregnácia; SDS neklasifikovaný; „livslang“ → „varig“; súvisiace Lotos Standard, Sofarens, EcoNeutral) |
| EKO Profi | ✅ 18. 11. (impregnácia matnej dlažby; SDS neklasifikovaný; matná = EKO Profi, lesklá = Polish; súvisiace Kalkfjerner, Fett-, Polish) |
| Baderomssett | ✅ 19. 11. (Baderomsrens + Kalkfjerner + Polish 100 ml + EKO Profi; **cena 1 499 → 1 199 kr** – Luk; 4 SDS v otázke; varovania H314 + H225) |
| SW EKO | 🟡 19. 11. minimálna (popis má 2 vety; bez krokov – chýba postup, spotreba, schnutie → SK etiketa SW EKO od Luka; H319 v „Ikke bruk“; súvisiace Multi Steinrens, LMS) |
| Glass Profi | ✅ 19. 11. („flytende vindusviskere“; SDS = Polisher: H225/H319/H336; vonku vs. Antidugg vnútri; súvisiace Antidugg, Bilrens, Fett-) |
| Fasaderens | ✅ 19. 11. (SDS = Baderomsrens, nie je nebezpečný; postup + spotreba 1 l/8 m²; súvisiace SW EKO, Multi Steinrens, Fasaderens Plus) |
| GreenGuard 100 ml | ⏸ neskôr (Luk 19. 11.: teraz nie je sezóna; „prírodné, nie je biocíd“; 284 ks na sklade; SDS chýba) |
| ostatné | ⏳ produkt po produkte |

## Pasce
- **Doprava v texte (Luk 18. 11.): „med PostNord“** — zjednotené pri všetkých 6 hotových produktoch → `08_ROZHODNUTIA/2026-11-18_doprava_postnord.md`.
- Otázky (`faq.a`) sa vypisujú ako HTML → dá sa vložiť odkaz `<a href>` (použité pri balíčkoch na 2 bezpečnostné listy).
- **Fotky pri produktoch sú skutočné** (Luk 17. 11.), niektoré upravené (Gemini/agent) len na veľkosť → smú sa použiť aj do pred/po (metapole file_reference berie MediaImage ID z médií produktu).
- Hlavička: `padding_top/bottom` musí byť násobok 4 (14 neprešlo).
- Živú tému (JUL) agent nemení → všetko v pracovnej; po dokončení Luk zverejní pracovnú. Potom to isté do „po sviatkoch“ (homepage index.json sa líši, ostatné súbory rovnaké).
- Fotky z cloudu do Shopify nenahrám (blokované) → fotky pred/po nahrá Luk priamo do metapoľa produktu.

## Platby — overené 17. 11. 2026
- Shopify `paymentSettings.supportedDigitalWallets` = **Shop Pay, Apple Pay, Google Pay** → zákazník platí telefónom; Luk ich mať nemusí.
- Karta / Apple Pay / Google Pay / Shop Pay = Shopify Payments → **automatická výplata na bankový účet** (napr. #1040 248 kr zo 4. 11. → výplata 9. 11. 236,58 kr, „settes inn på bankkontoen din i løpet av 1–2 virkedager“; poplatok ~11 kr).
- Vipps (#1038) ide cez Vipps/MobilePay. **PayPal je na e-shope deaktivovaný** (Luk 17. 11.; účet PayPal má len na platobný terminál) — posledná PayPal objednávka #1027 bola v júli, keď ešte bol zapnutý. Na webe PayPal neuvádzať.
- Účet na výplaty Luk zmenil 10. 11. → výplata zadržaná do 14. 11. (bezpečnostné pravidlo Shopify).
- Agent nevidí číslo účtu ani rozvrh výplat (konektor bez oprávnenia `read_shopify_payments`).

## Zverejnenie (17. 11.)
Luk chce LMS online hneď → zverejniť „Isokor – JUL 2026 + nové podstránky“ (vianočná úvodná + nové podstránky). Overené: JUL naposledy zmenená 20:59, kópia vznikla 21:33 → nič sa nestratí. Návrat: „Isokor – JUL 2026 (teraz)“ → Publikovať. **Potom** nahrať tie isté súbory podstránok do „po sviatkoch 2027“.

## ✅ ZVEREJNENÉ 17. 11. 2026 ~21:58 (Luk) — overené `themes(roles:MAIN)`
- **Živá:** „Isokor – JUL 2026 + nové podstránky“ `…/156287008947`.
- **Po sviatkoch:** „Isokor – PO SVIATKOCH 2027 (s podstránkami)“ `…/156287566003` = kópia živej + bežná úvodná (index.json bez `jul`). Po Novom roku Luk zverejní túto.
- „ZASTARANÉ – nepoužívať“ `…/156285272243` (stará po-sviatkoch bez podstránok) — Luk môže zmazať.
- Návrat: „Isokor – JUL 2026 (teraz)“ alebo „Dawn“.

## Ďalšie produkty = len metapolia (nie téma!)
Obsah produktu je v metapoliach → po zápise je **hneď na živom webe**. Preto: agent pripraví texty → Luk schváli → agent zapíše.
Zmena kódu šablóny = nová pracovná kópia živej + to isté do „po sviatkoch“.
