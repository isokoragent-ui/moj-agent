# Automatické e-maily — plán (návrh 2026-11-26)

*Stav: 📝 návrh agenta, čaká na Lukovo schválenie. Texty (nórsky) píše agent až po schválení plánu.*
*Kde sa nastavuje: Shopify **Messaging → Automatizácie** (marketingové) a **Nastavenia → Oznámenia** (transakčné). Messaging nemá API → nastavuje Luk podľa krokov, agent pripraví texty na kopírovanie (ako Black Friday).*

## Prečo
- 0 vracajúcich sa zákazníkov, pokladňa → nákup ~10 % (`ESHOP_KONVERZIA_2026-11-24.md`).
- Len 4 hodnotenia vo Fere (priemer 4,8). Hodnotenia predávajú.
- Automatika beží sama — raz nastaviť, potom len vyhodnocovať čísla.

## Dve skupiny — dôležité pravidlo
- **Transakčné** (potvrdenie objednávky, odoslanie): idú **každému** kupujúcemu. Nesmú obsahovať reklamu.
- **Marketingové** (Messaging): idú len tým, čo **súhlasili s odberom**. Tu môže byť ponuka, zľava, ďalšie produkty.
- ⚠️ Overiť: ktoré automatizácie v Messaging idú aj ľuďom bez súhlasu (opustená pokladňa môže mať výnimku). Agent overí v dokumentácii Shopify pri nastavovaní — nehádať.

## Plán — 9 e-mailov v poradí dôležitosti

| # | E-mail | Kedy | Komu | Obsah | Tlačidlo | Teraz |
|---|---|---|---|---|---|---|
| 1 | **Forlatt kasse** (opustená pokladňa) | 1 h po opustení + 2. pripomienka po 24 h | kto začal pokladňu a nedokončil | „Glemte du noe?“ — obsah košíka, doprava PostNord, kontakt („svar på e-posten hvis noe var uklart“). 2. e-mail: krátke + istota (naturlige produkter, V-Label, rýchla odpoveď). **Bez zľavy** (inak sa ľudia naučia čakať). | Fullfør bestillingen | „Fullfør bestillingen din“ = **návrh, nie zapnuté** |
| 2 | **Takk for kjøpet** (poďakovanie) | hneď po 1. nákupe | kupujúci so súhlasom | Osobné poďakovanie od Lukasa, kedy príde balík (6–10 pracovných dní, PostNord), krátky návod „ako dosiahnuť najlepší výsledok“, kontakt. | Se bruksanvisning / produkt | „Takk skal du ha!“ = aktívne → **prepísať** |
| 3 | **Hvordan gikk det? + hodnotenie** | **15 dní** po objednávke (balík je doma ~5 dní) | kupujúci | Ako sa darilo, tip na použitie, prosba o hodnotenie (Fera: 5 % zľava za recenziu s fotkou). | Gi en anmeldelse | ❓ overiť, či Fera neposiela vlastnú žiadosť (aby nešli dve) |
| 4 | **Velkommen** (nový odberateľ) | hneď po prihlásení na odber | nový odberateľ bez nákupu | Kto sme (malá nórska firma, naturlige produkter), 3 najobľúbenejšie produkty/balíky, ako funguje doprava. Rozhodnúť: s uvítacou zľavou alebo bez. | Se produktene | „Vi er glade for å se deg igjen“ = aktívne → **skontrolovať text** |
| 5 | **Forlatt handlekurv** (košík) | 4 h po vložení do košíka bez pokladne | identifikovaný zákazník so súhlasom | Krátke: „Handlekurven din venter“. | Gå til handlekurven | „Vi har lagret handlekurven din“ = návrh |
| 6 | **Passer godt sammen med** (ďalší produkt) | 30 dní po nákupe | kupujúci so súhlasom | Jeden doplnkový produkt k tomu, čo kúpil (Kalkfjerner → Baderomsrens, Sofarens → Møbelrens/EcoNeutral, Kjøleskapsrens → Fett- og flekkfjerner…). | Se produktet | nové |
| 7 | **Snart tom?** (doplnenie) | ~75 dní po nákupe (**Luk potvrdí**, ako dlho vydrží 500 ml) | kupujúci so súhlasom | Pripomienka, že fľaša sa asi míňa, odkaz rovno na ten istý produkt. | Bestill igjen | nové |
| 8 | **Vi savner deg** (návrat) | 120 dní bez nákupu | kupujúci so súhlasom | Čo je nové (Junior, sezónne produkty), jedna ponuka; jediný e-mail so zľavou 10 % (jednorazový kód). | Se hva som er nytt | nové |
| 9 | **Fortsett der du slapp** (prezeranie) | 1 deň po prezeraní produktu bez košíka | identifikovaný zákazník so súhlasom | Produkt, ktorý si pozeral + 1 veta o ňom. Nízka priorita (málo návštev). | Se produktet | existuje návrh (50 % otvorení) |

**Transakčné (Nastavenia → Oznámenia)** — len skontrolovať, nie nové:
- Potvrdenie objednávky: nórsky, doručenie „6–10 virkedager med PostNord“, kontakt.
- Odoslanie: číslo zásielky PostNord funguje.
- Zrušenie / vrátenie peňazí: nórsky text.

## Pravidlá textov
- Nórsky, `03_STYL/HLAS.md`: krátke odseky, bez emoji, bez tlaku a falošnej urgentnosti, podpis Lukas.
- Žiadne biocídne tvrdenia (antimikrobielt, dreper bakterier) — `07_SCHEMY/NEDELNY_EMAIL.md`.
- Jedno hlavné tlačidlo na e-mail, rovno na produkt/košík, nie na úvodnú stránku.
- Max. 1 automatický e-mail so zľavou (č. 8, prípadne uvítací) — inak zľava stratí hodnotu.
- Nekolidovať s nedeľným newsletterom: ak niekto dostal automatický e-mail, newsletter v ten deň nevadí, ale nepridávať ďalšie.

## Postup zavádzania
1. **Fáza 1 (tento týždeň):** č. 1, 2, 3 — najväčší dopad (dokončené nákupy + hodnotenia). Pred č. 3 overiť nastavenie žiadostí vo Fere (Luk fotí obrazovku Fera → Requests).
2. **Fáza 2 (december):** č. 4, 5 + kontrola transakčných.
3. **Fáza 3 (január):** č. 6, 7, 8, 9.
4. Každý e-mail: agent napíše text na kopírovanie → Luk zadá v Messaging (krok po kroku so snímkami) → test na mobil → zapnúť.

## Ako meráme (agent raz mesačne)
- Opustené pokladne → koľko sa dokončilo po e-maile.
- Počet nových hodnotení vo Fere (dnes 4) — agent číta cez API.
- Vracajúci sa zákazníci (dnes 0) a tržba z automatizácií (Messaging → štatistiky, Luk pošle snímku).
