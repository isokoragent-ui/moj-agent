---
name: odovzdaj
description: Na konci rozhovoru prepíše 09_ODOVZDANIE/AKTUALNE.md — čo je hotové, čo visí nedokončené, ďalší krok — aby zajtrajší rozhovor alebo druhý počítač vedeli pokračovať bez vysvetľovania. Použi vždy pred ukončením práce.
---

# /odovzdaj

Terminál a zajtrajšok nesmú byť dva oddelené svety.

0. **Najprv stiahni a zlúč `main`** (`git fetch origin main` + merge) — v iných
   oknách beží iná téma a mohla zapísať do tých istých súborov. Pri konflikte
   zachovaj obe strany. V `AKTUALNE.md` meň len body témy tohto okna.
1. Prepíš `09_ODOVZDANIE/AKTUALNE.md` v tejto štruktúre:
   ```
   # Kde sme skončili
   **Naposledy:** RRRR-MM-DD HH:MM, (názov počítača, ak ho vieš zistiť)
   ## Hotové naposledy
   - …
   ## Nedokončené — pokračovať tu
   1. … (čo presne chýba, kde je rozrobené, čo na to treba odo mňa)
   ## Pozor (čo by ďalšieho vypálilo)
   - … (pasca, rozbitá vec, čo nefunguje — ak nič, „(nič)“)
   ĎALŠÍ KROK: jedna veta
   ```
2. Nedokončené veci **nikdy nevynechaj** — aj tie, ktoré si odložil kvôli
   inej otázke (KÓD #13).
3. Aktualizuj stav projektov v `02_PRACA/PROJEKTY.md`, ak sa zmenil.
4. Ak dnes ešte nebol `/dennik`, sprav ho.
5. Spusti `bash _nastroje/zaloha.sh "krátky popis"` — ak je založený git.
   Ak nie je, spýtaj sa jednou vetou, či ho mám založiť (len lokálne).
6. Napíš mi dve vety: čo je hotové a čo čaká. Nič viac.
