# Hĺbková analýza e-shopu isokor-skandinavia.no

*Verzia 2 · 2026-10-18 · dáta zo Shopify (iba čítanie, nič nezmenené)*
*Predchádzajúca verzia (2026-10-17) je v histórii gitu.*

## 1. Čísla
| | |
|---|---|
| Tržby za 12 mesiacov | 8 260 NOK čistých, 28 objednávok |
| Návštevy za 90 dní | 1 167 (66 % mobil) → do košíka 45 (3,9 %) → pokladňa 33 → **nákup 6** |
| **Pokladňa → nákup** | **18 %** (bežne 40–50 %) — najväčší únik |
| Zdroje (90 dní) | priamo 544 · sociálne siete 502 · Google 107 |
| Platby | Shopify Payments (karty, Apple/Google Pay), Vipps funguje (#1038), PayPal, Faktura |

## 2. Cenová politika — pred a po zmene (27. 8. 2026)
| Košík | Pred: 149 + doprava | Teraz: 199 vrátane dopravy + zľava |
|---|---|---|
| 1 fľaša | 149 + 99 = **248** | **199** |
| 2 fľaše | 298 + 99 = 397 | 398 − 7 % = **370** |
| 3 fľaše | 447 + 49 = **496** | 597 − 12 % = **525** |
| 5 fliaš | 745 + 49 = 794 | 995 − 20 % = **796** |
| 10 fliaš | 1 490 + 49 = 1 539 | 1 990 − 25 % = **1 493** |

**Zistenia:**
- Pre zákazníka je nový systém lacnejší pri 1–2 fľašiach, pri 3–4 je drahší.
- **Zľavy na stránke nikto nevidí.** Sekcia s tabuľkou zliav je na úvodnej stránke vypnutá a v pruhu hore je len „Gratis frakt“. Zákazník sa o zľave dozvie až v košíku, takže ho nemotivuje kúpiť viac.
- **Zľava platí na celú objednávku** — aj na službu Gravstein vask (1 699), balíky (Baderomssett 1 499) a 5 l balenia. Pri 2 položkách so službou ide 7 % zo služby.
- Opustené pokladne pokračujú aj po zavedení dopravy zdarma (od 27. 8.: 9 opustených, napr. košík 2 249 NOK s 11 fľašami, 2× Baderomssett 1 499). Doprava teda **nebola jediný dôvod**.
- Od zmeny sú len 3 objednávky — na posúdenie, či nový systém funguje, je to zatiaľ príliš málo dát.
- **Marža neznáma:** jedna fľaša dnes prinesie 199 namiesto 248 (−49 NOK) pri rovnakých nákladoch na PostNord. Bez nákupnej ceny a ceny dopravy sa nedá povedať, či na 1 fľaši nezarábaš 0.

## 3. Úniky — čo stratí predaj
| # | Zistenie | Dôkaz |
|---|---|---|
| 1 | **Mold Cleaner: 1 ks na sklade**, pritom 2. najčastejšia vstupná stránka | 132 návštev / 90 dní; sezóna plesní |
| 2 | **Feriepakken je koncept** (nedostupný), ale ľudia naň chodia | 32 vstupov / 90 dní → stránka nenájdená |
| 3 | Lotos standard: 1 ks, 57 vstupov | |
| 4 | Pokladňa → nákup len 18 % | 33 pokladní → 6 nákupov |
| 5 | Zľavy neviditeľné (sekcia vypnutá) | `templates/index.json` |
| 6 | **27 z 32 produktov má len 1 fotku** | žiadne pred/po, použitie, veľkosť |
| 7 | Stránka „Vårt Magasin“ v menu je **prázdna** | 0 znakov |
| 8 | „Om oss“ **nie je zverejnená** — nová značka potrebuje dôveru | |
| 9 | „For profesjonelle“ v menu je **prázdna kolekcia** | 0 produktov |
| 10 | Recenzie majú anglický nadpis „Customer Reviews“ | Fera app |
| 11 | Krátke popisy: Grave Cleaner (184 znakov), SW EKO, LMS, LM Descaling | |
| 12 | Úvodná stránka: 21 sekcií, z toho väčšina vypnutá — neprehľadná | |

## 4. Návrhy zmien (poradie = dopad / námaha)
### A) Hneď, zadarmo (opravy únikov)
1. **Doobjednať Mold Cleaner** (a Lotos standard) — dopyt je dokázaný.
2. **Feriepakken:** zverejniť (9 ks skladom), alebo presmerovať adresu na Baderomssett.
3. **Ukázať zľavy:** pruh hore „Fri frakt + opptil 25 % rabatt når du kjøper flere“ + zapnúť sekciu s tabuľkou + text na stránke produktu.
4. **Vylúčiť zo zľavy** službu Gravstein vask a balíky.
5. **Menu:** skryť „Vårt Magasin“ (prázdne) a „For profesjonelle“ (kým nebude naplnená); **zverejniť „Om oss“**.
6. **Recenzie:** nadpis po nórsky „Kundeanmeldelser“; po každej objednávke poprosiť o recenziu.
7. **Opustené pokladne:** overiť, že je zapnutý automatický e-mail (Shopify → Nastavenia → Oznámenia); urobiť skúšobný nákup na mobile.

### B) Tento mesiac (obsah)
8. **Fotky:** ku každému bestselleru 3–4 (pred/po, použitie, fľaša v ruke). Pred/po musí byť skutočné, ostatné vie pomôcť Artlist.
9. Dopísať krátke popisy (Grave Cleaner, SW EKO, LMS, LM Descaling) + nórske názvy produktov.
10. Zjednodušiť úvodnú stránku: hlavný banner so sľubom → 4 bestsellery → prečo Isokor (prírodné, certifikáty, alergici) → recenzie → služby a B2B.

### C) Návštevnosť (bez nej nič z toho nezaberie)
11. 1 167 návštev za 90 dní je málo. Sociálne siete fungujú (502 návštev) → 2–3 príspevky týždenne na témy, ktoré ľudia už hľadajú: pleseň, čistenie kameňa a dlažby, impregnácia.
12. Google: nórske názvy a popisy (dnes len 107 návštev z vyhľadávania).

## 5. Čo treba od Luka
- Nákupná cena fľaše a reálna cena PostNord za balík → výpočet marže pri 1, 2, 5 a 10 fľašiach.
