# Stránka produktu rozdelená na samostatné sekcie (24. 11. 2026)

**Prečo:** Luk chce v editore témy posúvať časti pod produktom a dať hodnotenia (Fera) úplne dole.
Predtým bolo všetko v jednej sekcii `isokor-produkt-info` → nedalo sa posúvať.

**Téma:** kópia živej „Isokor – JUL 2026 sekcie produktu (24.11.)“ `gid://shopify/OnlineStoreTheme/156454813875` (nezverejnená).

| Sekcia (súbor) | V editore | Obsah |
|---|---|---|
| `isokor-p-postup` | Isokor – postup | „Slik gjør du“ (metapole `steg`) |
| `isokor-p-pred-po` | Isokor – pred/po | fotky pred/po s posuvníkom |
| `isokor-p-info` | Isokor – passer til | Passer til / Ikke bruk på / SDS |
| `isokor-p-otazky` | Isokor – otázky | FAQ |
| `isokor-p-suvisiace` | Isokor – súvisiace | „Passer godt sammen med“ (+ nastaviteľný počet 2–8) |
| `apps` (id `anmeldelser`) | Aplikácie | prázdna — sem Luk pridá blok Fera „recenzie“ |
| `isokor-p-kupit-mobil` | Isokor – kúpiť (mobil) | prilepený pruh „Legg i kurven“ |

`product.json` + 9 šablón `product.<suffix>.json` sú rovnaké (checksum `48942488…`). Pôvodná sekcia `isokor-produkt-info` v téme ostala (nepoužitá).

## Pasce
- **Názov sekcie v `{% schema %}` max. 25 znakov** — inak Shopify súbor odmietne („name er for lang“).
- Hodnotenia Fera vkladá app embed sám; či prestane, keď je blok Fera pridaný ručne do sekcie, **neoverené**.
- Agent náhľad nevidí → kontrolu robí Luk.
