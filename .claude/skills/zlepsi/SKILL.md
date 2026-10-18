---
name: zlepsi
description: Týždenný rituál — z toho, čo sa opakovalo, vyberie jednu vec a zautomatizuje ju (alebo pripraví po posledný krok). Použi raz týždenne alebo keď človek povie „čo by sme mohli zautomatizovať".
disable-model-invocation: true
---

# /zlepsi — jedna automatizácia týždenne

Nie zoznam nápadov. **Jedna vec, dotiahnutá.**

1. Prečítaj `04_RUTINY/AUDIT_AUTOMATIZACII.md` a posledné 2 týždne
   v `06_DENNIK/`.
2. Polož mi **po jednej** tieto tri otázky:
   - Čo si tento týždeň robil viac než trikrát?
   - Čo ťa najviac unavilo, hoci to bolo jednoduché?
   - Kde si prepisoval to isté z jedného miesta na druhé?
3. Doplň nové položky do tabuľky auditu (skupina A/B/C, minúty × frekvencia).
4. Vyber **jednu** položku s najväčším ušetreným časom, ktorú vieš dotiahnuť
   dnes. Povedz mi ju a prečo práve túto. Potom dve otázky, po jednej:
   - **Zruš najprv:** „Čo sa stane, keď to úplne prestaneme robiť?“ Ak nič —
     nezautomatizuj odpad. Zapíš to ako výhru do `08_ROZHODNUTIA` a skonči.
   - **Ktoré číslo to hýbe?** viac zákazníkov / vyššia hodnota zákazníka /
     nižšie náklady + konkrétna metrika (čas odpovede, chybovosť, minúty).
     Ak nevieme pomenovať číslo, nestaviame to.
   Počkaj na „áno“.
5. **Úroveň samostatnosti** — vyber NAJNIŽŠIU, ktorá problém rieši:
   L1 navrhne, ja rozhodnem · L2 pripraví, ja skontrolujem · L3 beží, ja
   občas skontrolujem · L4 beží samo. Nové veci začínajú na L1–L2; na L3+
   sa ide až po tom, čo nižšia úroveň týždeň fungovala. Ak rozhodnutie
   nemusí robiť AI, nenechaj ju.
6. Urob ju: skript do `_nastroje/` (hlavička PREČO, bez kľúčov v kóde,
   kľúče z `~/.config/`), alebo schéma do `07_SCHEMY/`, alebo naplánovaná
   úloha. Ak treba niečo klikať rukou — jeden krok naraz (KÓD #7).
7. Over skutočným volaním (`over.py` — pridaj test, ak je to služba).
8. Zapíš do „Čo už agent prebral“ (aj úroveň L1–L4) v audite + `/dennik`.
9. Povedz mi jedno číslo: koľko minút mesačne to vracia.
