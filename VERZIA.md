# Štartovací mozog — verzia 2

**Vydané 3. 10. 2026.** Verzia 1 bola zabalená 14. 9. 2026.

## Čo je nové

### Kódy spolupráce: 23 → 29

Šesť nových pravidiel. Dve z nich stoja za zmienku najviac:

- **Nezapínaj vypnuté a nerob, čo neviem vrátiť** — bezpečnostné pravidlo
  postavené na skutočnej škode: zapnutý optimalizačný plugin položil e-shop
  na celý večer a cesty k súborom boli medzitým zablokované.
- **Maj názor a hovor pravdu** — mení agenta z prikyvovača na partnera.
  „Asistent bez názoru je vyhľadávač s krokmi navyše."

Ďalej pribudli: *Kontext vždy*, *Pozri sa, čo o sebe systém zistil*,
*Keď mám viac projektov, najprv zisti, o ktorý ide* a *Uč sa moje remeslo*.

**Podstatnejšie než počet:** pôvodné kódy dostali **„prečo"** — konkrétnu
chybu, z ktorej vznikli. Rozdiel medzi *„nikdy netvrď, že niečo funguje"*
a tým istým pravidlom s vetou *„API je zapnuté — usúdené z obrazovky.
Nebolo. Zistilo sa o deň neskôr pri chybe 403"* je rozdiel medzi frázou
a návodom.

### Tri hotové schémy namiesto prázdneho priečinka

`07_SCHEMY/` už nie je len šablóna. Každá z týchto schém vznikla zo
skutočnej chyby a pasce v nich sú tie, ktoré naozaj stáli čas alebo peniaze:

- **`ZALOHA_PRED_ZASAHOM.md`** — čo urobiť pred každou zmenou na živom webe
  či e-shope, a prečo sa ústupová cesta overuje VOPRED
- **`NOVY_PRISTUP.md`** — ako agentovi bezpečne dať kľúč k novej službe
- **`OBRAZKY_PRE_WEB.md`** — ako vyrobiť sadu AI obrázkov, ktoré držia spolu

### Vyplnené príklady namiesto prázdnych formulárov

Prázdny formulár väčšina vyplní na tri riadky a mozog potom nefunguje —
nie preto, že je zlý, ale preto, že nevie dosť. Preto sú pribalené úplne
vyplnené príklady jednej vymyslenej osoby:

- `01_JA/_PRIKLAD_PROFIL.md`
- `02_PRACA/_PRIKLAD_PROJEKTY.md`
- `05_PRISTUPY/_PRIKLAD_REGISTER.md`

Po vyplnení vlastných súborov ich môžeš zmazať.

## Čo sa nezmenilo a prečo

Nástroje (`over.py`, `preveruj.sh`, `najdi_mozog.sh`), hooky, skills aj
štruktúra priečinkov sú zhodné s verziou 1. Porovnávali sme ich
s rozpracovanými verziami a tie sa líšia len tým, že sú napísané na konkrétny
stroj a konkrétne služby — všeobecná verzia je už teraz schopnejšia.

Lepšie je povedať pravdu než predstierať upgrade tam, kde nie je.
