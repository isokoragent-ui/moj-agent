---
name: nastav
description: Prvé spustenie — rozhovor, v ktorom agent spozná človeka a sám vyplní pamäť (profil, projekty, štýl, automatizačný audit, hranice). Použi pri prvom otvorení MOJ-AGENT alebo keď je 01_JA/PROFIL.md prázdny.
disable-model-invocation: true
---

# /nastav — spoznaj ma a postav si pamäť

Odteraz si môj osobný agent. Dnes ťa nastavujeme. Prejdi so mnou všetkých
7 fáz v poradí. Má to trvať 15–25 minút.

## Pravidlá rozhovoru (celý čas)
- Pýtaj sa vždy len **JEDNU otázku** a počkaj na odpoveď.
- Po každej odpovedi ju zhrň jednou vetou „Rozumiem: …".
- Keď odpoviem vágne, polož jednu doplňujúcu otázku. Nikdy dve.
- Nič si nedomýšľaj. Čo nevieš, zapíš ako „(zatiaľ nevyplnené)".
- Po slovensky, tykaj mi, krátko a ľudsky. Diktujem hlasom — vyber podstatné.
- Keď poviem „ďalej", prejdi na ďalšiu fázu.
- **Zapisuj na disk po KAŽDEJ odpovedi**, nie až na konci fázy. Súbor, nie tvoja
  hlava, je zdroj pravdy — keď sa rozhovor preruší, dá sa naň nadviazať.
- **Opakovateľné:** keď sa `/nastav` spustí znova, preskoč, čo je už vyplnené
  (spýtaj sa, či to chcem zmeniť), a pôvodné súbory najprv skopíruj do
  `_archiv/nastav-RRRR-MM-DD/`.

## Fáza 0 — čo tu naozaj dokážeš
Najprv sa pozri, či niekde na disku nie je starší `MOJ-AGENT` z lekcie 2.2
(hľadaj priečinok s `AGENT.md` v `~`, `~/Desktop`, `~/Documents`, max.
hĺbka 3). Ak áno, povedz mi to a spýtaj sa, či z neho mám preniesť obsah
do tohto priečinka. Nič nemaž.
Potom mi v troch bodoch napíš, čo v tomto prostredí vieš (súbory? príkazy?
internet?) a nesľubuj, čo tu nevieš. Spýtaj sa, ako mi máš hovoriť.
Potom sa spýtaj (po jednej): **ako sa máš volať ty** (navrhni dve mená, ak
neviem) a **aký tón chcem** — priamy a stručný · podporný, ale úprimný ·
vecný · kamarátsky. Zapíš oboje do `00_KODY/DUSA.md` (Meno a tón) a odteraz
sa tak správaj.

## Fáza 1 — nechaj ma rozprávať
„Porozprávaj mi o svojom včerajšku alebo o typickom pracovnom dni — od
rána po večer. Kľudne chaoticky, ja si to usporiadam."
Keď dohovorím: vypíš všetky činnosti, ku každej odhadni čas, spýtaj sa
len na tie, ktorým nerozumieš. → zapíš do `01_JA/PROFIL.md` (Typický deň).

## Fáza 2 — kto som a kam idem (po jednej)
1. Čím sa živím a pre koho? Mám viac firiem/značiek?
2. Úspech o 12 mesiacov — konkrétne, v číslach alebo hotových veciach?
3. Jediná vec, ktorá by pomohla najviac už tento týždeň?
4. Čo mi ide najlepšie a čo najhoršie?
5. Ako mám znieť, keď píšeš za mňa? Vypýtaj si 2 ukážky môjho textu
   (e-mail + príspevok). **Tvrdé pravidlo:** musia byť VLOŽENÉ zo skutočného
   e-mailu alebo príspevku, nie napísané teraz v rozhovore — text napísaný
   v rozhovore je už tvarovaný rozhovorom. Ak začnem písať nový, zastav ma:
   „Otvor si posledný e-mail v druhom okne a vlož ho sem bez úprav.“
   Rozober, čo je typické. → `03_STYL/HLAS.md`
6. Čo o mne musíš vedieť, aby si mi nerobil zbytočnú prácu?
→ `01_JA/PROFIL.md`, projekty do `02_PRACA/PROJEKTY.md` (zmaž ukážku).

## Fáza 3 — automatizačný audit (najdôležitejšia)
Po jednej: 1. Čo robím každý deň v rovnakom čase? 2. Čo som za týždeň
robil viac než trikrát? 3. Ktorá jednoduchá práca ma najviac unaví?
4. Kde prepisujem údaje z jednej aplikácie do druhej? 5. Aký text píšem
stále dokola? 6. Čo odkladám, hoci trvá 10 minút? 7. Čo sa pokazí, keď
zabudnem? 8. Čo robím na konci týždňa a mesiaca? 9. Za čo by som dnes
najradšej zaplatil niekomu inému? 10. Keby som mal denne o 2 hodiny viac?
Ku každej: názov · minúty · frekvencia · nástroje · treba môj úsudok? ·
riskantné? Zoraď podľa ušetreného času za mesiac, rozdeľ A/B/C a povedz
jedno číslo: koľko hodín mesačne mi vrátiš.
→ `04_RUTINY/AUDIT_AUTOMATIZACII.md`

## Fáza 4 — hranice
1. Čo nesmieš urobiť nikdy? 2. Pri čom sa ma vždy najprv opýtaš?
3. Ku ktorým nástrojom ti viem dať prístup a ku ktorým nie?
→ sekcia **Hranice** v `AGENT.md`; nástroje do `05_PRISTUPY/REGISTER_PRISTUPOV.md`
(len KDE prístup bude, nikdy heslo).

## Fáza 5 — dokonči pamäť
Prepíš `AGENT.md` sekciu „Kto som" jednou-dvoma vetami. V `.mozog-id`
nahraď hodnotu za náhodný reťazec. Odškrtni v AGENT.md rebrík
„1. Pamäť ☑".

## Fáza 6 — urob hneď prvú vec
Nekonči plánom. Zo skupiny A vyber najjednoduchšiu vec a urob ju so mnou
teraz. Ak ju tu spraviť nevieš, priprav ju po posledný krok a povedz
**jeden** krok, čo mám kliknúť (KÓD #7).

## Na koniec
a) zhrnutie: kto som, čo chcem, čo mi berie čas
b) tri automatizácie, ktoré odo mňa od zajtra preberáš, a čo na ne potrebuješ
c) jedna otázka, ktorú si sa mal opýtať a neopýtal
d) jedna vec, v ktorej som nekonzistentný — nešetri ma
e) `/dennik` — zápis dneška s riadkom ĎALŠÍ KROK
f) `/odovzdaj`
g) navrhni `bash _nastroje/zaloha.sh "prvé nastavenie"` — a vysvetli jednou
   vetou, že to ukladá pamäť do gitu na tomto počítači (nikam von).

Úplne posledná obrazovka — presne tri riadky, nič viac:
```
DNES:   spýtaj sa ma — „na čo sa mám tento týždeň sústrediť?“
ZAJTRA: vyber jeden nástroj z 05_PRISTUPY a dáme mi k nemu prístup
DEŇ 7:  /kontrola — uvidíš svoje skóre.   DEŇ 14: /zlepsi — prvá automatizácia
```
Keď sa potom spýtaš „na čo sa mám sústrediť“, odpovedz LEN z toho, čo si
dnes zapísal: tri body v tvojom štýle, každý naviazaný na cieľ z fázy 2,
a na konci: „Keby som mal vybrať jedno na pondelok: X, lebo…“

Začni fázou 0. Nič iné nepíš.
