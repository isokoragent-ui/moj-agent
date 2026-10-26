# Analýza cenníka „Skladove zasoby a ceny“ (hárok Ceny na ponuky)

*2026-10-26 · zo screenshotu od Luka · nič nezmenené*

## Ako je tabuľka postavená (overené prepočtom)
- **C = B × 15** (nákup v EUR × kurz 15 NOK) ✅ sedí vo všetkých riadkoch.
- **D = C × 1,468** (veľkoobchod bez DPH = prirážka 46,8 %) ✅ sedí všade.
- **E = D × 1,25** (+ 25 % MVA) ✅ sedí všade.
- **F** = maloobchod s MVA, zadaný ručne.

## Zisk na kus v e-shope (F bez MVA − C)
- Štandard 500 ml (149 kr): 119,20 − 59,40 = **59,80 kr**, marža 50 %.
- 1 fľaša s dopravou: zákazník 248 kr → bez MVA 198,40 − 59,40 = 139 kr − PostNord − poplatok za platbu.
- Najnižšie marže: Glass Profi 31 %, Polisher 500 ml 31 %, SW EKO 38 %.

## Chyby
1. **Glass Profi 100 ml** a **Polisher 500 ml**: maloobchod (749 / 1 099) je **nižší** než veľkoobchod s DPH (755,56 / 1 106,51). Veľkoodberateľ by platil viac než zákazník na webe.
2. **SW EKO, Polisher 100, Lotos, Wash-in, GreenGuard, Antifog:** maloobchod len 11–21 % nad veľkoobchodom → obchodník nemá priestor zarobiť pri ďalšom predaji.
3. Kurz 15 je výrazne nad reálnym kurzom EUR/NOK — ak má pokryť dopravu a clo, je to OK, ale treba to vedieť; inak je skutočná marža vyššia.

## Shopify vs. tabuľka (stĺpec F) — 2026-10-26
| Produkt | Tabuľka | Shopify |
|---|---|---|
| Antidugg 500 ml | 249 | 349 |
| Allrens (Cleaner home) | 349 | 399 |
| Clinic | 199 | 219 |
| EcoDescal | 119 | 169 |
| Fasaderens Plus 1 l | 199 | 259 |
| Fasaderens Plus 5 l | 699 | 899 |
| Fasaderens (5 l?) | 699 | 799 |
| FVE 1 l / 5 l | 199 / 699 | 249 / 829 |
| Glass Profi | 749 | 899 |
| Gravsteinrens 5 l | 699 | 799 |
| Lotos Profi / Standard | 799 / 249 | 899 / 349 |
| Polish 100 ml | 349 | 399 |
| SW EKO | 349 | 449 |
| Wash-In | 799 | 899 |
| EKO Profi | 699 | 799 |
Zhoda: všetky 149 kr produkty, SW 1 l (699), Polish 500 ml (1 099), GreenGuard (149).
Pravdepodobne pozostatok z prechodu na „dopravu zdarma“ (27. 8.), keď sa ceny zvýšili.

## Chýba v tabuľke
- EcoNeutral 100 ml (predáva sa za 49 kr) — nákupná cena?
- Baderomssett, Badepakken, Feriepakken, Multi Steinrens 5 l, FVP.
- Reálna cena PostNord za balík.

## ✅ Zosúladené so Shopify 2026-10-26 (Luk „áno“)
15 variantov zmenených na ceny zo stĺpca F, overené čítaním. Záloha: `02_PRACA/zalohy/ceny_PRED_tabulka_2026-10-26.json`.
Nezmenené (nejasné priradenie): Fasaderens Plus 5000 ml (899, vypredané) a Fasaderens (799) — ktorý je „Facade 5 L“ (699)?
Glass Profi 749 nastavené podľa tabuľky, hoci je pod veľkoobchodom s DPH (755,56) — Luk vie.
