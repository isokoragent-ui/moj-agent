# ZVEREJNENIE NOVEJ TÉMY E-SHOPU (Shopify)

**Kedy sa použije:** keď je nová téma (alebo jej sezónna verzia) hotová v kópii a má ísť von.
**Naposledy prešla:** 17. 11. 2026 (vianočná úvodná stránka) — pripravené, zverejňuje Luk.

## Kto čo robí
- **Agent:** pripraví kópiu témy, overí produkty (`status ACTIVE`, `availableForSale`), zálohuje živú tému do `02_PRACA/zalohy_temy/`. Publikovať tému **nemôže** (konektor to blokuje) a ani nesmie bez „áno“.
- **Luk:** pozrie náhľad na mobile aj PC a klikne Publikovať. Agent ho vedie **po jednom kroku** (KÓD #7).

## Kroky (pre Luka — agent ich dáva po jednom, nie naraz)
1. Otvoriť zoznam tém: https://admin.shopify.com/store/h14838-qn/themes
2. V časti „Knižnica tém“ nájsť tému (napr. „Isokor – JUL 2026 (teraz)“).
3. Pri nej ťuknúť na „…“ (tri bodky) → „Publikovať“.
4. Potvrdiť „Publikovať“ v okne.
5. Otvoriť https://isokor-skandinavia.no na mobile → skontrolovať, či je tam nový vzhľad (pri starom: obnoviť stránku).
6. Agent overí: `themes { role }` → nová téma = `MAIN`.

## Návrat späť
Rovnaké kroky, len pri téme „Dawn“ → Publikovať. Nič sa nestratí — stará téma ostáva v knižnici.

## Pasce
- ⚠️ **Úpravy v editore platia len pre tú tému, v ktorej sa robia.** Máme 2 verzie (JUL / po sviatkoch) — zmena kódu sekcie alebo CSS sa nahráva do OBOCH.
- ⚠️ **Kópia témy je fotka v čase.** Ak sa po vytvorení kópie zmení niečo v živej téme (menu je spoločné, ale pätička, hlavička, nastavenia aplikácií v téme nie), kópia to nemá. Pred zverejnením porovnať `updatedAt` živej témy s dátumom kópie.
- ⚠️ **Natiahnuté obrázky:** `image_tag` dáva `height` z originálu → v CSS vždy `height:auto`, keď sa mení šírka.
- ⚠️ Sekcia Pred/po sa bez dvoch fotiek zákazníkom neukáže (zámer, nie chyba).
- ⚠️ Agent náhľad témy nevidí (`theme_screenshot` bez oprávnenia) → kontrolu očami robí Luk.
