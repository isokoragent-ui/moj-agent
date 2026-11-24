# Prečo e-shop nepredáva — analýza konverzie

*2026-11-24 · dáta zo Shopify Analytics + nastavenia obchodu (len čítanie, nič nezmenené).
Predchádzajúce audity: `WEB_AUDIT_2026-10-18.md`, `ESHOP_ANALYZA.md` (18. 10.).*
*Zmeny z 17.–24. 11. (nový dizajn, sekcie produktu, hodnotenia) sa v číslach ešte neprejavia — merať od 1. 12.*

## ⚠️ Doplnenie po rozhovore s Lukom (24. 11.)
- **Doprava ostáva** 99 / 49 (400–700) / zadarmo od 700 kr → `08_ROZHODNUTIA/2026-11-24_doprava_ostava.md`. Body 2 a „#1 Doprava“ v tabuľke krokov **neplatia**.
- **Dodanie 6–10 dní je realita PostNord** (Agder → Oslo), odosiela sa do 1 dňa → bod 3 „Pomalé dodanie“ sa nedá vyriešiť dopravcom; ostáva len napísať „Sendes innen 1 virkedag“.
- **Opustené pokladne z Osla sú často falošné** („Storgata 1, 3, 5, 10“) → pokladňa → nákup nie je až taký zlý, ako ukazuje 10 %.
- **Príspevky už vedú na produkt.** Shopify ich napriek tomu ráta ako príchody na úvodnú stránku → treba odkazy s **UTM** (`?utm_source=facebook&utm_campaign=…`), aby bolo vidno, ktorý príspevok priviedol koho. Možné príčiny: odkaz v profile (bio) vedie na úvodnú, alebo prehliadač v aplikácii FB/IG stratí cestu.
- ✅ **„Norsko“ → „Norge“** v kontakte opravil Luk 24. 11. (overené). Konektor nemá oprávnenie upravovať podmienky obchodu (`write_legal_policies`) → Vilkår for bruk tiež len ručne.

## 1. Čísla (posledných 60 dní, 26. 9.–24. 11. 2026)

| Krok | Návštevy | Podiel | Bežný e-shop |
|---|---:|---:|---:|
| Návštevy | 890 | 100 % | — |
| Vložili do košíka | 27 | **3,0 %** | 5–8 % |
| Došli do pokladne | 20 | 2,2 % | 3–5 % |
| **Dokončili nákup** | **2** | **0,2 %** | 1–2 % |
| Pokladňa → nákup | 2 z 20 | **10 %** | 40–50 % |

- **Mesačne:** aug 507 návštev / 2 nákupy · sep 189 / 2 · **okt 458 / 0** · nov 394 / 2.
- **Objednávky za 6 mesiacov: 23**, z toho 15 v júli. Priemerná objednávka ~250 kr.
- **Vracajúci sa zákazníci: 0.** Nikto nenakúpil druhýkrát.
- Pozor: časť návštev aj opustených pokladní sú Lukove vlastné testy (adresa Vegårshei/Agder). Skutočný stav je teda ešte o niečo horší.

### Odkiaľ ľudia prichádzajú (60 dní)
| Zdroj | Návštevy | Do košíka | Odíde hneď (bounce) | Nákup |
|---|---:|---:|---:|---:|
| Priamo (aj Luk sám) | 521 | 19 | 77 % | 2 |
| Facebook | 243 | 5 | 86 % | 0 |
| Google | 68 | 3 | **56 %** (najlepší) | 0 |
| Instagram | 52 | 0 | **98 %** | 0 |

- **Prvá stránka:** 527 z 890 návštev začína na úvodnej stránke, nie na produkte.
- **Počítač:** 350 návštev, 93 % hneď odíde, 0 nákupov (asi roboty a vlastné návštevy).
- **Mobil:** 520 návštev, 69 % hneď odíde, 2 nákupy.

### Opustené pokladne (posledných 16)
Väčšinou **1 produkt za 149–199 kr, adresa Oslo/Trondheim**. Príklad z 9. 11.: GreenGuard 149 kr → v pokladni **248 kr** (frakt 99 kr). Človek odíde, keď uvidí cenu dopravy.

## 2. Prečo ľudia nekupujú — od najväčšej príčiny

### 🔴 1. Málo návštev s úmyslom kúpiť
~400 návštev mesačne. Aj pri bežnej konverzii 1,5 % je to ~6 objednávok ≈ 1 500 kr mesačne.
**E-shop sám z tohto množstva návštev cieľ 40–50 tis. kr neurobí**; najprv treba 5–10× viac cielených návštev.
Google (ľudia, ktorí hľadajú riešenie) prináša len 68 návštev za 2 mesiace.

### 🔴 2. Doprava zabíja malé objednávky
- Produkt 149 kr + **frakt 99 kr = +66 %** k cene. Ľudia to zistia až v pokladni.
- Doprava zadarmo až od 700 kr = ~5 fliaš. Priemerná objednávka je 250 kr, takže na ňu takmer nikto nedosiahne.
- Dôkaz: Badepakken so „frakt inkludert“ má najviac návštev produktu (92) aj košíkov (5).

### 🔴 3. Pomalé dodanie
- Na produkte: „levering 6–10 virkedager“. V podmienkach: odoslanie do 2 dní + 4–10 dní = **až 12 pracovných dní**, len do pakkeboksu.
- V Nórsku je bežné 1–3 dni; pri 149 kr čistiacom prostriedku ľudia nechcú čakať 2 týždne.
- **Otázka na Luka:** je 6–10 dní reálne? Zásielky PostNord z Vegårshei zvyčajne idú rýchlejšie — ak áno, napísať pravdu („Sendes innen 1 virkedag · 2–5 dager“).

### 🟠 4. Málo dôvery k neznámej značke
- **Len 4 hodnotenia** v celom obchode (2 overené).
- **Vilkår for bruk je stále šablóna s „[SETT INN HANDELSNAVN]“, „[SETT INN BEDRIFTENS ADRESSE]“, „[KOBLING]“** (otvorené od auditu 18. 10.). Kto si podmienky otvorí, vidí nedokončený obchod.
- Kontakt: „Vegårshei, **Norsko**“ (slovensky). Angrerett v podmienkach hovorí „ved levering til **EU**“ — v Nórsku platí 14 dní podľa angrerettloven.
- **30 zo 40 produktov má len 1 fotku**, niektoré vyzerajú ako AI (LMS: etiketa na fotke ≠ skutočná fľaša).
- Neznámy výrobok za 149 kr vedľa Jif/Zalo za 30–60 kr v obchode: človek potrebuje **dôkaz, že to funguje** (pred/po, video, recenzia) — inak si kúpi známe.

### 🟠 5. Sociálne siete prinášajú „pozerajúcich“, nie kupujúcich
- 295 návštev z FB/IG, **0 nákupov**, IG 98 % odchod.
- Príspevky vedú na úvodnú stránku, nie na konkrétny produkt s ponukou.
- Človek zo sociálnej siete nehľadá čistič — potrebuje jednu jasnú ponuku a jedno tlačidlo.

### 🟡 6. Priveľa produktov, žiadny jasný „hrdina“
40 položiek (čistiace prostriedky, impregnácie, solárne panely, náhrobky, Hytteservice). Nový návštevník nevie, čím je Isokor známy. Predávajú sa hlavne balíky (Badepakken, Kjøkkenpakken) — to je správny smer.

### 🟡 7. Žiadny druhý nákup
0 vracajúcich sa zákazníkov. Chýba e-mail po nákupe („Hvordan gikk det? Gi oss en anmeldelse“) a pripomienka opustenej pokladne — **neoverené, či je zapnutá** (agent toto nastavenie Shopify neprečíta; Luk: Innstillinger → Varsler → Forlatt kasse).

## 3. Čo spraviť — poradie podľa dopadu / námahy

| # | Krok | Dopad | Námaha | Kto |
|---|---|---|---|---|
| 1 | **Doprava:** frakt 49 kr na všetko, zadarmo od 399 kr; na produkte vidieť „Frakt 49 kr · gratis over 399 kr“ (alebo ceny „frakt inkludert“ ako pri balíkoch) | veľký | malá | Luk rozhodne, agent nastaví |
| 2 | **Dodanie:** reálna lehota + „Sendes innen 1 virkedag“; overiť s PostNord lacnejšiu a rýchlejšiu službu pre malé fľaše (pakke i postkassen) | veľký | malá | Luk + agent |
| 3 | **Vilkår for bruk vyplniť**, „Norsko“ → „Norge“, angrerett pre Nórsko | stredný (dôvera) | malá | agent pripraví, Luk „áno“ |
| 4 | **Recenzie:** požiadať všetkých 23 doterajších zákazníkov + B2B (Esso, Halvor) o hodnotenie (Fera má už 5 % zľavu za recenziu s fotkou) | stredný | malá | agent pripraví e-mail, Luk odošle |
| 5 | **Reklama a príspevky na konkrétny produkt/balík**, nie na úvodnú stránku; jedno video pred/po + cena + „frakt inkludert“ | veľký | stredná | agent + Luk |
| 6 | Pripomienka opustenej pokladne — overiť, že je zapnutá | stredný | malá | Luk (1 klik) |
| 7 | Skutočné fotky: 2–4 na produkt (fľaša, použitie, pred/po) — začať najpredávanejšími 6 | stredný | stredná | Luk fotí, agent upraví |
| 8 | Google: Search Console + Google Business Profile (miestne vyhľadávanie Agder) | stredný (dlhodobo) | stredná | Luk + agent |

## 4. Ako meráme
- Porovnávať **týždenne od 1. 12.**: návštevy → košík → pokladňa → nákup, podľa zdroja.
- Pri ~100 návštevách týždenne treba **aspoň 4 týždne** dát, kým sa dá povedať, či zmena zabrala.
- Cieľ na december: **pokladňa → nákup z 10 % na 35 %+**, košík z 3 % na 5 %.
