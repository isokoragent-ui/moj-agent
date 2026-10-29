# NOVÁ SLUŽBA NA WEB (stránka + produkty + menu cez Shopify API)

**Kedy sa použije:** keď Isokor spúšťa novú službu, ktorú si zákazník objedná a zaplatí cez e-shop.
**Naposledy prešla:** 29. 10. 2026 (Isokor Hytteservice)

## Kroky
1. Texty (NO) najprv do súborov v `02_PRACA/<sluzba>/` — stránka, podmienky, `produkty.json`.
2. Produkty: `productSet` (synchronous) so `status: DRAFT`, `productType: "Tjeneste"`, štítok služby,
   varianty s `inventoryItem {requiresShipping:false, tracked:false}`, `inventoryPolicy: CONTINUE`.
3. Stránky: `pageCreate` s `isPublished: false`.
4. Kolekcia: `collectionCreate(collection: {... sources:[{source:{title, targetType: PRODUCTS, inclusion:{matchType: ALL, conditions:[{productTag:{matchType: ALL, relation: TAGGED_WITH, values:[štítok]}}]}}}]})`.
5. Overiť čítaním (`products(query:"tag:…")`, `page(id:)`) → ukázať Lukovi.
6. Po „áno": fotky (stagedUploadsCreate → curl POST → `productUpdate(media:)`), `productUpdate status: ACTIVE`,
   `publishablePublish` produkty + kolekcia **len do Online Store**, `pageUpdate isPublished: true`.
7. Menu: najprv záloha do `02_PRACA/zalohy/`, potom `menuUpdate` s CELÝM zoznamom položiek (aj s id), novú bez id.
8. Overiť: `onlineStoreUrl` produktov, `resourcePublicationsV2` kolekcie, `isPublished` stránok, položky menu.

## Pasce
- ⚠️ **Predvolená šablóna stránky `page.json` má dole galériu náhrobných kameňov** (XO Gallery). Novej stránke hneď daj `templateSuffix: "tjenester"` (text + recenzie) alebo `"sertifikater"` (len text). Tému nemeníme.
- ⚠️ `collectionCreate(input:)` je v API 2026-10 zastarané → `collection:` + `sources`. `collectionAddProducts` neexistuje.
- ⚠️ `Publication.name` zastarané → `catalog { title }`. `Collection.onlineStoreUrl` neexistuje.
- ⚠️ `pages(query:"title:…")` nové stránky nenašlo → overovať cez `page(id:)`.
- ⚠️ `menuUpdate` nahrádza celé menu — chýbajúca položka zmizne. Preto záloha a celý zoznam.
- ⚠️ Pri curl uploade kopírovať `policy`/`signature` presne — preklep = 403.
- Pred registráciou MVA na webe nepísať „inkl. mva", ale „endelige priser" (obchod má `taxesIncluded: true`).
- Služba predávaná online súkromníkovi = 14 dní angrerett → v podmienkach a v e-maile po objednávke pýtať súhlas so štartom skôr.
