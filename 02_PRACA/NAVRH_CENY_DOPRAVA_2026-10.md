# Návrh: späť k modelu „nižšia cena + doprava v košíku“

*2026-10-26 · Luk „áno“. ✅ ZMENENÉ a overené čítaním zo Shopify (body 1–3 + texty kolekcií). Záloha: `02_PRACA/zalohy/ceny_zlavy_doprava_PRED_2026-10-26.json`.*

## Čo je teraz naozaj nastavené (2026-10-26)
- 12 variantov 199 → **149** (overené).
- Doprava Norge: „Standardlevering“ 99 kr (0–399,99) · „Standardlevering – halv frakt“ 49 kr (400–699,99) · „Gratis frakt“ 0 kr (700+).
- 5 zliav za kusy vypnutých (stav EXPIRED, nezmazané — dajú sa znova aktivovať).
- Kolekcie Solcelle a For profesjonelle: „Gratis frakt … over 700 kr“.
- Pruh hore je v téme vypnutý → nič netreba. Feriepakken (799) „inkludert gratis frakt“ platí.
- Podmienka Frakt („Fraktkostnad vises ved kassen“) teraz sedí; konkrétne hranice v nej nie sú.
- GreenGuard 239 → **149** (Luk, 2026-10-26, overené). EcoNeutral 500 ml ostáva 149.
- EcoNeutral 100 ml 129 → **49** (Luk potvrdil, 2026-10-26, overené).


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
