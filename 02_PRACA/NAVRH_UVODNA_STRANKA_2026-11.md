# Návrh novej úvodnej stránky e-shopu (2026-11-17)

*Okno „Nová úvodná stránka“. Stav: **návrh na posúdenie** — v e-shope nič nezmenené.*

**Návrh (plátno, interaktívny):** https://claude.ai/artifact/9Y65CZEaSEpZthRfhFet3Y
— úvodná stránka + grafický systém (farby, písmo, tlačidlá).

## Sekcie (poradie = cesta zákazníka)
1. Pruh dopravy: 99 / 49 nad 400 / zdarma nad 700 kr (podľa `08_ROZHODNUTIA/2026-10-26_*`).
2. Hero „Rent hjem. Ren samvittighet.“ + skutočné fľaše (výrezy z `grafika/zdroj/`), „fra 149 kr“.
3. **„Hva vil du bli kvitt?“** — 6 dlaždíc podľa problému (kalk, fett, rust, mugg, lukt, grønske) → priamo na produkt.
4. Bestsellery (4) s tlačidlom do košíka.
5. **Pred/po s posuvníkom** — skutočné WC fotky LMS.
6. Balíčky Kjøkkenpakken / Badepakken 349 kr inkl. frakt.
7. Prečo Isokor (4 body, bez čísel, ktoré nevieme doložiť).
8. Hytteservice pás.
9. Recenzie — **prázdne miesta, doplniť skutočné z Fera**.
10. Newsletter (nedeľný e-mail) + pätička s kontaktom, org. č., platbami.

## Farby a písmo
Les #1f4d36 · Ihličie #142a1f · Šalvia #e2ebdf · Ľan #f6f5f0 · Zlato #e7c987 · Fjord #0f2a3a (Hytteservice).
Nadpisy Fraunces, text Assistant (písmo témy Dawn) — nadväzuje na plagáty balíčkov.

## Ako to dostať do Shopify (odporúčanie agenta)
- **Nie** jeden veľký HTML blok cez „Custom Liquid“ — ceny, sklad, košík a obrázky by boli
  natvrdo, nedali by sa upravovať v editore a pri zmene ceny by web klamal.
- **Áno:** vlastné sekcie témy (Liquid) — vyzerajú presne ako návrh, ale produkty, ceny
  a tlačidlo „Legg i kurven“ berú zo Shopify živo; texty a obrázky sa menia v editore témy.
- Postup: kópia témy Dawn → agent tam pridá sekcie → Luk pozrie náhľad (mobil aj PC) →
  Luk publikuje sám. Živú tému agent nemení (`AKTUALNE.md` → Pozor).
- **Blokované:** Shopify konektor teraz nemá oprávnenie na témy (`theme_bash`,
  `theme_screenshot` → „requires additional permissions“, 2026-11-17). Treba ho znova
  pripojiť v nastaveniach konektorov claude.ai s prístupom k témam.

## Doplniť pred spustením
- Skutočné recenzie (Fera), org. číslo a adresa do pätičky, odkazy na sociálne siete.
- Lepšie fotky: fľaša v ruke / pri použití pre každý bestseller.
