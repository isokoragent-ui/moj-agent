# NOVÝ PRÍSTUP (kľúč, heslo, API)

**Kedy sa použije:** keď má agent po prvý raz siahnuť na novú službu —
e-mail, e-shop, platby, sociálna sieť, API nástroja.
**Naposledy prešla:** 3. 10. 2026

## Kroky

1. **Povedz nahlas, čo ten prístup umožní** a čo nie. Nie „pripojím Gmail",
   ale *„budem vedieť čítať a odosielať poštu z tejto adresy; mazať nie"*.
2. **Vlastná identita, nie moje heslo.** Kde sa dá, založ agentovi vlastný
   účet alebo vlastný kľúč. Navonok vystupuje ako „asistent <meno>", nikdy
   sa nepodpisuje ako ja.
3. **Najužšie oprávnenie, aké stačí.** Len na čítanie, kým zápis nie je
   nutný. Keď služba ponúka obmedzený token, vezmi ten obmedzený.
4. **Ulož mimo tohto priečinka.** Do `~/.config/<nazov>/` (`chmod 700`
   priečinok, `600` súbory) alebo do systémovej Keychain.
5. **Do `05_PRISTUPY/REGISTER_PRISTUPOV.md` zapíš len KDE to je a ako sa to
   zruší.** Nikdy samotný kľúč.
6. **Over skutočným volaním**, že prístup funguje — doplň test do
   `_nastroje/over.py`.
7. **Skús zrušenie nanečisto.** Vieš ten prístup odobrať jedným krokom?
   Keď nie, nastav ho inak.

## Pasce — čo nás už vypálilo

- ⚠️ **Kľúč zapísaný na Plochu skončil v cloude.** Plocha aj Dokumenty sa
  často synchronizujú. Tento priečinok tiež býva v gite — preto sem kľúč
  nepatrí ani omylom.
- ⚠️ **Kľúč nalepený do chatu je spálený.** Keď sa raz objaví v rozhovore,
  treba ho vymeniť, nie presunúť.
- ⚠️ **„Full access" je predvolené, nie potrebné.** Väčšina služieb ponúka
  užší rozsah, len ho treba hľadať.
- ⚠️ **Overuj, na ktorý účet prístup smeruje.** Dva účty u toho istého
  poskytovateľa sa zamieňajú ľahko a zistí sa to až pri škode.

## Čo agent spraví sám / kde čaká na moje „áno"

- **sám:** zistí, aký rozsah stačí, pripraví uloženie, zapíše register,
  napíše test
- **čaká:** na samotné vydanie kľúča a na prvé pripojenie k službe
