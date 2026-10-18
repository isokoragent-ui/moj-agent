---
name: kontrola
description: Zdravie mozgu — čo je zastarané, čo si protirečí, čo chýba, či nikde neleží kľúč, na ktorom stupni rebríka sme. Použi raz za týždeň-dva alebo keď človek povie „skontroluj mozog".
---

# /kontrola — zdravie pamäte

Výstup je **krátka správa + jeden navrhovaný krok**. Nie zoznam 20 vecí.

## Čo skontroluješ
1. `python3 _nastroje/over.py` — spusti a ukáž výsledok.
2. **Profil:** zostali v `01_JA/PROFIL.md` alebo `03_STYL/HLAS.md`
   „(zatiaľ nevyplnené)"? Ktoré?
3. **Čerstvosť:** posledný záznam v `06_DENNIK/` — koľko dní? Má riadok
   `ĎALŠÍ KROK`? `09_ODOVZDANIE/AKTUALNE.md` — súhlasí s denníkom?
4. **Projekty:** je v `02_PRACA/PROJEKTY.md` projekt bez zmeny stavu
   dlhšie ako 30 dní? Je tam ešte ukážkový?
5. **Protirečenia:** prečítaj `AGENT.md` + `00_KODY/` a nájdi dve pravidlá,
   ktoré si odporujú (model si pri protirečení vyberá náhodne).
6. **Schémy:** má každá sekciu „Pasce" s aspoň jednou položkou?
7. **Register prístupov:** nie je v `05_PRISTUPY/` niečo, čo vyzerá ako
   heslo alebo kľúč? Nie sú tam služby, ktoré už nepoužívam?
8. **Rebrík:** podľa zistení označ v `AGENT.md` stupne 1–4.
9. **Záloha:** `git log -1 --format=%cd` — kedy bola posledná?
10. **Sprievodca:** `bash _nastroje/sprievodca.sh stav` — koľko míľnikov, čo je
    preskočené a prečo (spýtaj sa, či sa k preskočenému vrátiť).
11. **Inbox:** leží v `_inbox/` niečo dlhšie ako 7 dní? (cintorín, nie inbox)

## Skóre 0–100 (dôkazy, nie priečinky)
Každá vrstva rebríka 0–25. Boduj len to, čo vieš **dokázať súborom alebo
volaním** — čerstvý balík má skóre blízko 0 a to je správne.
- **Pamäť (25):** profil bez „(zatiaľ nevyplnené)“ 10 · štýl s vloženými
  ukážkami 5 · denník za posledných 7 dní 5 · odovzdanie súhlasí s denníkom 5
- **Dosah (25):** každá služba v registri s prístupom, ktorý `over.py`
  potvrdil volaním — 25 ÷ počet služieb v registri (max 25)
- **Zručnosti (25):** každá schéma s pascami A s dátumom „naposledy prešla“
  za 30 dní — 8 bodov (max 25)
- **Autopilot (25):** naplánovaná úloha, ktorá preukázateľne bežala bez
  človeka 2× — 15; hlási zlyhanie (log/mail) — 5; dá sa vypnúť jedným
  príkazom a je to napísané — 5. Bez automatiky max 10.
Stupne: 0–24 nepreukázané · 25–49 základ · 50–69 funguje s dierami ·
70–84 spoľahlivé v overenom rozsahu · 85–100 udržiavané a dokázané.

Správu ulož do `09_ODOVZDANIE/kontroly/RRRR-MM-DD.md` a porovnaj
s predchádzajúcou: čo sa zlepšilo, čo je stále otvorené.

## Výstup
```
ZDRAVIE MOZGU — RRRR-MM-DD
✅ v poriadku: …
⚠️ pozor: … (max 3 najdôležitejšie)
Skóre: NN/100 (Pamäť N · Dosah N · Zručnosti N · Autopilot N) — stupeň
Oproti minule: +N / prvé meranie
ÚPRIMNE: 1–2 vety — čo sa fláka, čo sa opakuje, čo by som na tvojom mieste
prestal odkladať. Bez cukru.
NAVRHUJEM JEDEN KROK: …
```
Čakaj na „áno" a potom ten krok sprav.
