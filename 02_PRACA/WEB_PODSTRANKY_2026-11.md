# Podstránky e-shopu — kontrola a plán (2026-11-17)

*Okno „Nová úvodná stránka“. Dáta: Shopify (téma „Isokor – JUL 2026 (teraz)“ = živá, stránky, presmerovania, analytika 60 dní). Nič nezmenené.*

## Čísla (19. 9. – 17. 11., 60 dní)
| | |
|---|---|
| Návštevy | 728 (66 % mobil) |
| Pridali do košíka | 22 (3 %) |
| Došli do pokladne | 18 |
| **Nakúpili** | **2** → z pokladne len **11 %** (bežne 40–50 %) |
| Vstupné stránky | úvod 390 · produkty ~250 (Badepakken 75, Multi Steinrens 44, Peisglassrens 17, Muggfjerner 16…) · Hytteservice 9 |

**Najväčší únik nie je dizajn, ale pokladňa:** 16 ľudí z 18 odišlo až v pokladni. Príčinu z dát nevidno
(doprava sa ukáže až tam? platobné metódy? Vipps?) → treba **skúšobný nákup na mobile** (visí od októbra).

## Čo som našiel na podstránkach
### 1. Stránka produktu (druhá najnavštevovanejšia po úvode)
- 11 rôznych šablón produktu (`product.cleaner`, `product.lm-descaling`…) — každá trochu iná, ťažko sa udržiava.
- Hore sa ukazuje „vendor“ (názov firmy) nad názvom; tlačidlo „**Share**“ po anglicky.
- Hviezdičky recenzií sa ukazujú aj pri 0 recenziách (`hide_when_no_reviews: false`).
- „Dette kan du også like“ je v hlavnej šablóne **vypnuté**; na mobile skryté náhľady fotiek.
- **32 z 37 produktov má 1 fotku.** Pri tlačidle Kúpiť nie je nič, čo buduje dôveru: cena dopravy, kedy príde, Vipps, vrátenie.
- Chýba: ako sa používa (kroky), na čo áno / na čo nie, pred/po, otázky, odkaz na bezpečnostný list, „kúp v balíčku a ušetri“.

### 2. Hlavička, pätička, košík (sú na každej stránke)
- Pruh hore **vypnutý** (bol tam „Gratis frakt“, už neplatí) → zákazník nevie cenu dopravy.
- Pätička: menu len „Søk“, **žiadny kontakt, org. č., ikony platieb (vypnuté), sociálne siete, newsletter**.
- Menu: „Startside“ navyše, „Produkter“ má 10 dlhých názvov.
- Košík: chýba „ešte X kr do dopravy zdarma“.

### 3. Kolekcie
- Holá mriežka, fotky orezané na výšku (`portrait`) → fľaše odrezané; bez úvodu, bez rýchleho pridania do košíka.

### 4. Stránky dôvery
- **Sertifikater:** odkazuje na slovenský web isokor.sk; sľúbené PDF (V-Label, laboratórne správy) nie sú priložené; zoznam rozbitý; veta „effekt mot mikroorganismer“ = riziko biocídu (audit bod 6).
- **Om oss:** všeobecný text, žiadna fotka, žiadny človek, žiadny príbeh (prečo Luk, prečo Vegårshei).
- **Tjenester:** staré modré odkazy so sledovacími parametrami, oblasť „Agder, Telemark, Vestfold“ nesedí s Hytteservice, recenzie „Customer Reviews“ po anglicky.
- Gravstein / boligrengjøring / solceller: obyčajný text; „100 % naturlig“ bez dokladu.

### 5. Rozbité
- **Feriepakken je koncept, ale prišlo naň 5 ľudí** → stránka nenájdená. Presmerovať na Badepakken alebo zverejniť.
- ISOKOR FVP: 0 ks.

## Plán (poradie = peniaze / námaha)
| # | Čo | Kto | Dopad |
|---|---|---|---|
| 1 | Skúšobný nákup na mobile → nájsť, prečo 16 z 18 odíde v pokladni | Luk + agent | najväčší |
| 2 | **Nová stránka produktu** (1 šablóna pre všetky): dôvera pri tlačidle, „Slik bruker du“, passer til, pred/po, otázky, bezpečnostný list, balíček, súvisiace | agent | veľký |
| 3 | Hlavička + pätička + pruh dopravy + košík s „X kr til gratis frakt“ | agent | veľký, každá stránka |
| 4 | Kolekcie: úvod, štvorcové fotky, rýchle pridanie | agent | stredný |
| 5 | Om oss (s fotkou a príbehom), Sertifikater (vlastné PDF na webe), Tjenester | agent píše, Luk dá fotky a fakty | dôvera |
| 6 | Feriepakken presmerovať | agent po „áno“ | malý, hneď |

## Ako technicky
Živá téma je teraz „Isokor – JUL 2026 (teraz)“ → do nej agent nezapisuje. Spraví sa kópia
„Isokor – JUL + podstránky“, v nej sa pracuje, Luk pozrie náhľad a zverejní. To isté potom
do „po sviatkoch“ (pasca: dve témy, zmeny kódu nahrávať do oboch).
