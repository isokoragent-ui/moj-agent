# Návrh: späť k modelu „nižšia cena + doprava v košíku“

*2026-10-26 · Luk chce vrátiť pôvodný koncept. Stav: NÁVRH, nič nezmenené — čaká na „áno“.*

## Čo hovoria objednávky (Shopify, overené 2026-10-26)
| Obdobie | Model | Objednávky |
|---|---|---|
| 1. 7. – 26. 8. 2026 (8 týždňov) | 149 + doprava 99 / 49 / 0 | **17** |
| 27. 8. – 26. 10. 2026 (8,5 týždňa) | 199, doprava 0, zľava za kusy | **3** (posledná 23. 9.) |

Pozor: júl = sezóna GreenGuard (10 zo 17 objednávok). Pokles nie je len cenou — ale smer
sedí s Lukovým pocitom. Starý model navyše priniesol viac za 1 fľašu (248 vs. 199).

## Pôvodný model (z objednávok)
- Fľaša 149, doprava 99; 3 fľaše (447) → doprava 49; 699+ → doprava 0.

## Návrh
1. **Ceny:** 12 variantov za 199 → **149** (Gravsteinrens 500 ml, Kalkfjerner, Baderomsrens,
   Fett- og flekkfjerner, Sofarens, Peisglassrens, LMS, Kjøleskapsrens, Bilrens, Møbelrens,
   Muggfjerner, EcoNeutral 500 ml). Ostatné ceny bez zmeny, kým Luk nepovie inak.
   GreenGuard (dnes 239, predtým 149) — rozhodne Luk.
2. **Doprava (Standardlevering, Norge):** do 399 kr → **99** · od 400 kr → **49** · od 700 kr → **0**.
3. **Zľavy za kusy (7–25 %):** vypnúť (nie zmazať). S lacnejšou fľašou + zľavou + lacnou dopravou
   by sa marža stratila a model by bol neprehľadný.
4. **Texty, ktoré by inak klamali:** pruh hore „Gratis frakt på alle ordre“ (živá téma → Luk),
   podmienka Frakt (Luk vloží), popisy kolekcií „Gratis frakt på alle bestillinger“ (agent).
   Nový pruh: „Halv frakt over 400 kr · Gratis frakt over 700 kr“.

## Úniková cesta
Pred zmenou uložiť súčasné ceny, zľavy a sadzby do `02_PRACA/zalohy/`. Zľavy sa len vypnú.

## Stále chýba
Nákupná cena fľaše a reálna cena PostNord → bez toho nevieme maržu pri 1 fľaši.
