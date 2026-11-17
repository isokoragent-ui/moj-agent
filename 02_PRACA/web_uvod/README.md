# Nová úvodná stránka — sekcie v kópii témy (2026-11-17)

**Kópia témy:** „Isokor – nová úvodná 2026-11“ (`gid://shopify/OnlineStoreTheme/156284649651`, NEZVEREJNENÁ)
**Živá téma:** „Dawn“ (`…/146881511603`) — **nezmenená**. Po zverejnení novej ostane v knižnici tém.

- Náhľad: https://isokor-skandinavia.no/?preview_theme_id=156284649651
- Editor: https://admin.shopify.com/store/h14838-qn/themes/156284649651/editor

## Čo je v kópii
| Súbor | Čo robí |
|---|---|
| `sections/isokor-hero.liquid` | nadpis, 2 tlačidlá, 3 výhody, obrázok alebo 3 fotky produktov, štítok „fra 149 kr“ |
| `sections/isokor-problemer.liquid` | „Hva vil du bli kvitt?“ — dlaždice problém → produkt |
| `sections/isokor-bestselgere.liquid` | 4 produkty: cena a sklad živo zo Shopify, „Legg i kurven“ (formulár `/cart/add`) |
| `sections/isokor-for-etter.liquid` | pred/po s posuvníkom; **bez 2 fotiek sa zákazníkom neukáže** |
| `sections/isokor-pakker.liquid` | Kjøkkenpakken, Badepakken (cena živo + „inkl. frakt“) |
| `sections/isokor-hvorfor.liquid` | 4 dôvody |
| `sections/isokor-hytte.liquid` | pás Hytteservice |
| `assets/isokor-forside.css` | spoločný vzhľad (farby `.isk`) |
| `assets/fraunces-600.woff2` | písmo nadpisov **uložené v téme** (nie z Google → bez GDPR rizika) |
| `sections/isokor-julepakker.liquid` | **(17. 11.)** veľké karty Badepakken + Kjøkkenpakken: obsah 2 fliaš, cena, „Du sparer“ (počíta sa živo: 2 fľaše + 99 kr doprava − cena balíčka), košík; pole „Termín objednávky pred Vianocami“ (prázdne = skryté) |
| `snippets/isokor-snoflak.liquid` | snehová vločka (dekorácia) |
| `templates/index.json` | poradie: hero → **Julepakker** → problémy → bestsellery → pred/po → prečo → Hytteservice → recenzie Fera („Kundeanmeldelser“) → newsletter → blog |

Zo starej úvodnej stránky **vypadol** blok „Les mer – mindre“ (sľub „100 % naturlige“
a „fornøydgaranti“ — protirečí podmienkam, audit bod 5–6). Je v zálohe.

## Vianočný režim (17. 11., Luk: „viac vianočné, vytiahnuť kúpeľňu a kuchyňu“)
- Hero má zaškrtávatko **„Vianočný vzhľad“** (tmavozelená, zlatá, padajúci sneh, vločky). Po Vianociach ho Luk odškrtne a prepíše texty → stránka je späť v bežnom vzhľade.
- Sekcia „Isokor – Julepakker“ je hneď pod hlavným pásom; starú sekciu „Balíčky“ som z úvodnej stránky vyradil (súbor ostal).
- Po Vianociach: sekciu Julepakker skryť alebo premenovať texty (napr. „Fordelspakker“).

## Obrázky na nahratie (v `obrazky/`, nahrá Luk v editore)
Agent ich do Shopify nenahral (priame nahratie z cloudu zablokovalo bezpečnostné pravidlo prostredia).
| Súbor | Kam v editore |
|---|---|
| `isokor-forside-hero-flasker.png` | Isokor – Hero → Obrázok |
| `isokor-forside-wc-for.jpg` / `-etter.jpg` | Isokor – Pred/po → Fotka PRED / PO |
| `isokor-forside-kjokkenpakken.png` / `-badepakken.png` | Isokor – Julepakker → blok → Obrázok (inak sa ukážu 2 fľaše) |

## Návrat späť (keby niečo)
1. Shopify → Online obchod → Témy → pri „Dawn“ → **Publikovať**. Hotovo, všetko ako predtým.
2. Záloha súborov živej témy z 17. 11.: `02_PRACA/zalohy_temy/ZIVA_Dawn_2026-11-17__*`.

Zverejnenie novej témy robí **Luk** (agent tému publikovať nesmie ani nemôže).
