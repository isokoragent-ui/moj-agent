# Analýza: Isokor EcoDescal – bezpečnostná karta vs. popis na webe

*Agent Iso, 27. 10. 2026. Zdroj: SK karta výrobcu „Isokor Odvápňovač (Isokor Eco Descal)“, v1.0 z 15. 1. 2026
(`02_PRACA/sikkerhetsdatablad/zdroj/original_SK_Isokor-Odvapnovac_Eco-Descal.pdf`), a popis produktu v e-shope
(záloha `02_PRACA/zalohy/popis_EcoDescal_PRED_2026-10-27.html`). Na webe sa zatiaľ nič nemenilo, pribudol len odkaz na kartu.*

## 1. Čo hovorí karta výrobcu (overené priamo z obrázkov v PDF)

| Bod | Karta EcoDescal |
|---|---|
| Klasifikácia (2.1) | **Skin Corr. 1C; H314** + **Eye Dam. 1; H318** → piktogram GHS05, **„Nebezpečenstvo / Fare“** |
| Základ klasifikácie (16) | „na základe obsahu zložiek (metóda výpočtu)“ |
| pH (9.1) | **približne 1** |
| Zloženie (3.2), každá zložka v rozsahu | kys. citrónová 1–5 % · kys. vínna (D-) 1–5 % · **kys. mliečna 1–5 % (Skin Corr. 1C)** · **kys. šťaveľová 1–5 % (Acute Tox. 4 H302/H312, Eye Dam. 1)** · **kys. fosforečná 1–5 % (Skin Corr. 1B)** · **kys. amidosulfónová 1–5 %** · **izopropanol 1–10 %** |
| Preprava (14) | UN 1760, trieda 8, obalová skupina III |
| UFI | W120-G081-7002-X7CT (iné ako LMS → výrobca podal samostatné hlásenie do ECHA) |

**Dôležité zistenie:** text aj všetky tabuľky karty EcoDescal sú **pixel po pixeli zhodné s kartou Isokor LMS
(odstraňovač hrdze)**, líši sa iba názov a UFI. Rovnako zhodná je aj karta WhiteWood a LM Descaling.
Buď majú tieto výrobky naozaj rovnaké zloženie, alebo spracovateľ (SPIN-DORADZTWO) kartu skopíroval.
Z webu sa to rozhodnúť nedá – vie to len výrobca.

## 2. Sedí klasifikácia H314? (prepočet podľa CLP, príloha I, 3.2.3 a 3.3.3)

Zložky sú uvedené len v rozsahoch, preto som prepočítal hraničné prípady:

- **Žieravosť kože (H314):** Σ(C/SCL) ≥ 1. Pri 1 % kys. mliečnej a 1 % kys. fosforečnej vychádza index 0,24
  (nie je žieravý); pri hornej hranici 5 % + 5 % vychádza 1,20 (je žieravý). **Z rozsahov sa to jednoznačne určiť nedá.**
- **Ale pH ≈ 1:** podľa CLP (3.2.3.1.2) je extrémne pH ≤ 2 samo osebe dôvod klasifikovať zmes ako žieravú,
  kým výrobca testom (kyslá rezerva) nedokáže opak. **H314 je preto opodstatnená.**
- **Dráždivosť kože:** minimálne Skin Irrit. 2 v každom prípade (index 1,2–6,0).
- **Vážne poškodenie očí (H318):** kys. mliečna + šťaveľová spolu ≥ 3 % → Eye Dam. 1 (pri spodnej hranici 2 % by
  išlo „len“ o Eye Irrit. 2). Opäť: pH 1 podporuje H318.
- **Akútna toxicita pri požití:** zmes sa ako celok neklasifikuje (ATEmix ≈ 10 000 mg/kg), ale obsahuje
  kys. šťaveľovú (H302 – škodlivá po požití).

**Záver:** klasifikáciu výrobcu nemáme ako vyvrátiť, je logická. Isokor Skandinavia AS je v rámci EHP
**distribútor** a musí použiť klasifikáciu, ktorú mu dal dodávateľ. Kým výrobca nevydá opravenú kartu,
platí: **EcoDescal je žieravý výrobok (Fare, H314).**

## 3. Čo je na webe v rozpore s kartou

| Veta na webe | Problém | Návrh |
|---|---|---|
| „…og er **helt uten farlige stoffer**“ | Nepravda – 5 zložiek je klasifikovaných, zmes je H314 | **odstrániť** |
| „**Ikke farlig ved utilsiktet inntak** av små mengder.“ | Karta: pri požití nevyvolávať zvracanie, ihneď volať lekára/Giftinformasjonen; obsahuje kys. šťaveľovú (H302) | **odstrániť** (najvážnejšie – výrobok do kanvice/kávovaru) |
| „raskt, effektivt, **trygt** og skånsomt“ | „trygt“ pri žieravine zavádza | vypustiť „trygt“ |
| „**Uten petrokjemiske ingredienser**“ | Obsahuje izopropanol (bežne petrochemický) | odstrániť, kým výrobca nepotvrdí bio-pôvod |
| „**svært lett biologisk nedbrytbart**“ | Karta 12.2: „pre výrobok nie sú údaje“ | odstrániť alebo zmierniť (organické kyseliny sú ľahko odbúrateľné) |
| Ingredienser: „druesyre, oksalsyre, sitronsyre, fruktekstrakter“ | Karta uvádza navyše kys. mliečnu, **fosforečnú, amidosulfónovú, izopropanol** | uviesť podľa karty |
| „…ved å **varme opp** blandingen forsiktig“ | Karta 10.4: vyhnúť sa vysokým teplotám | „lunkent vann, ikke kok opp“ |
| chýba výstraha | CLP čl. 48 ods. 2: pri predaji na diaľku musí ponuka uviesť druh nebezpečnosti z etikety | pridať blok „Faremerking“ |

Okrem toho: veta „Inneholder ingen kjente kreftfremkallende stoffer“ s kartou **nie je v rozpore** (oddiel 11:
kritériá karcinogenity nesplnené), môže zostať.

## 4. Rovnaký problém na iných stránkach (všimol som si pri kontrole)

- **Isokor Badepakken** obsahuje Kalkfjerner (LM Descaling = žieravý H314), ale píše
  „✅ Naturlige ingredienser – **trygg for hele familien**“ a „✅ **Allergifri og hudvennlig formel**“ → rovnaký rozpor.
- **Kalkfjerner for bad** a **LMS rustfjerner** majú na stránke len odkaz na kartu, **žiadnu výstrahu** (Fare, H314).
- Týka sa to všetkých klasifikovaných výrobkov v e-shope (SW, Polish, Lotos Standard, Glass Profi, FVP – horľavé;
  LMS, Kalkfjerner, EcoDescal – žieravé; SW EKO, Antidugg, FVE – oči). Navrhujem jednotný blok „Faremerking“
  nad odkazom na kartu – urobím to pre všetky naraz, keď povieš áno.
- Pozn.: revidované nariadenie CLP (EÚ 2024/2865) požiadavky na predaj na diaľku ešte sprísňuje; kedy a ako
  platí v Nórsku (EHP), som z cloudu neoveril (Lovdata je blokovaná) – treba overiť.

## 5. Návrh opraveného popisu EcoDescal (nórsky, sedí s kartou)

> **Avkalkingsmiddel for vannkokere og kaffemaskiner**
>
> Alltid en ren vannkoker eller kaffemaskin, hver dag. EcoDescal avkalkingsmiddel gir deg en effektiv fjerning
> av kalkavleiringer i både vannkokere og kaffemaskiner.
>
> **Egenskaper**
> Dette er et produkt utviklet for avkalking av vannkokere samt automatiske og halvautomatiske kaffemaskiner.
> Det er basert på organiske syrer og fruktekstrakter. Produktet fjerner kalkavleiringer raskt og effektivt og er
> skånsomt mot utstyret. Takket være fruktekstraktene gir det også en ny glans til overflater av krom og rustfritt stål.
> - Beskytter mot overdreven kalkdannelse.
> - Enkel i bruk med umiddelbar effekt.
> - Inneholder ingen kjente kreftfremkallende stoffer.
>
> **Bruksanvisning**
> For vannkokere: Hell produktet i vannkokeren og la det virke til kalkavleiringene er løst opp. Bruk eventuelt lunkent
> vann og en myk børste – ikke kok opp middelet. Skyll deretter vannkokeren grundig med rent vann, og kok opp og hell ut
> minst én full kjele med rent vann før bruk.
> For kaffemaskiner: følg produsentens instruksjoner for avkalking. Dersom produsenten ikke har oppgitt instruksjoner:
> hell produktet i vanntanken og fyll opp med vann til 1 liter, la hele væskemengden gå gjennom systemet, skyll den tomme
> tanken og kjør deretter minst to fulle tanker med rent vann gjennom maskinen.
>
> **Inneholder** (i henhold til sikkerhetsdatabladet): sitronsyre, vinsyre, melkesyre, oksalsyre, fosforsyre,
> amidosulfonsyre, isopropanol.
>
> **Faremerking**
> ⚠️ **FARE** – H314: Gir alvorlige etseskader på hud og øyne.
> Oppbevares utilgjengelig for barn. Benytt vernehansker og vernebriller. VED SVELGING: Skyll munnen. IKKE framkall
> brekninger. VED KONTAKT MED ØYNENE: Skyll forsiktig med vann i flere minutter; fjern eventuelle kontaktlinser
> og fortsett skyllingen. Kontakt umiddelbart lege eller Giftinformasjonen (22 59 13 00).
>
> **Oppbevaring** – bez zmeny.
>
> **Sikkerhetsdatablad** – odkaz bez zmeny.

## 6. Otázky pre výrobcu (Rodinná firma) – návrh, nič som neposlal

1. Je zloženie v oddiele 3 karty „Odvápňovač (Eco Descal)“ naozaj zloženie EcoDescal? Karta je zhodná s LMS
   (odstraňovač hrdze) – obsahuje EcoDescal kys. fosforečnú, amidosulfónovú a izopropanol?
2. Ak nie: pošlite opravenú kartu, ktorá zodpovedá hláseniu UFI W120-G081-7002-X7CT.
3. Je H314 odvodená len výpočtom, alebo aj z pH ≈ 1? Máte test kyslej rezervy (mohol by znížiť klasifikáciu)?
4. Je izopropanol bio-pôvodu (kvôli tvrdeniu „uten petrokjemiske ingredienser“)?
5. Je výrobok vhodný na styk s pitnou vodou (zvyšky v kanvici/kávovare) – máte k tomu vyhlásenie?

## 7. Odporúčanie

1. **Hneď** opraviť popis EcoDescal podľa bodu 5 – teraz web tvrdí opak toho, čo je v karte, ktorú sám ponúka
   na stiahnutie. To je najhoršia kombinácia, ak by sa niečo stalo.
2. Súbežne poslať výrobcovi otázky z bodu 6. Ak príde opravená karta s miernejšou klasifikáciou, popis znova upravíme.
3. Rovnako opraviť Badepakken a doplniť blok „Faremerking“ ku všetkým klasifikovaným výrobkom.
