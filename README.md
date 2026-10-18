# MOJ-AGENT — štartovací mozog

Toto je pripravená pamäť pre tvojho osobného AI agenta. Namiesto dvoch týždňov
nastavovania máš od prvej minúty: pravidlá, ktoré vznikli z reálnych chýb,
strážcu tajomstiev, nástroje na overovanie a rytmus práce.

Všetko je obyčajný text. Nič sa nikam neodosiela. Vlastníš to ty.

## Jediný prvý krok

Otvor tento priečinok v Claude Code a napíš:

    /nastav

Agent sa ťa 15–25 minút pýta — jednu otázku naraz — a sám si vyplní pamäť.
Nič iné nerob. Ďalší krok ti povie on.

## Jedna veta, ku ktorej sa vzťahuje všetko vnútri

> *Kým nie si pri počítači, tvoj agent si všimne jednu skutočnú udalosť
> a spraví z nej výstup rýchlejšie a presnejšie, než by si to spravil ty.*

K tomu vedie cesta: **deň 1** `/nastav` → **deň 2** prvý prístup k nástroju →
**deň 7** `/kontrola` (skóre) → **deň 14** `/zlepsi` (prvá automatizácia) →
potom každý týždeň jedna. Prvé dva týždne budeš pomalší. Potom dvojnásobne rýchlejší.

## Čo je vnútri

- `AGENT.md` — manuál, ktorý agent číta ako prvý (`CLAUDE.md` naň odkazuje)
- `00_KODY/` — 22 pravidiel spolupráce, každé s dôvodom, prečo vzniklo
- `01`–`09` — priečinky pamäte (kto som → kde sme skončili)
- `00_KODY/DUSA.md` — kto je agent: meno, tón, v čo verí (má názor, je hosť, hovorí pravdu)
- `.claude/skills/` — príkazy `/nastav` `/rano` `/dennik` `/odovzdaj` `/schema` `/zlepsi` `/kontrola` `/tyzden` `/sprievodca`
- `.claude/hooks/sluby.sh` — keď napíšeš „pošlem ti to zajtra“, agent raz ponúkne, že to zapíše
- **Sprievodca** — pri každom štarte sa pozrie, čo už máš hotové, a ponúkne
  JEDEN ďalší krok (15 míľnikov, potom tipy). Nikdy zoznam. Postup vidíš
  v `09_ODOVZDANIE/SPRIEVODCA.md`.
- `.claude/hooks/` — strážca: zastaví tajomstvo v súbore a nebezpečný príkaz ešte pred vykonaním
- `.claude/settings.json` — oprávnenia: agent nesmie čítať `.env`, `~/.config`, `~/.ssh`,
  nesmie `rm -rf`, `sudo`, `git push --force`
- `_nastroje/` — `preveruj.sh` (dôkaz pred „to nemáme"), `over.py` (overenie volaním), `zaloha.sh`

## Kde má byť tento priečinok

Kdekoľvek — agent ho nájde podľa podpisu `.mozog-id`. Odporúčanie: `~/MOJ-AGENT`
(domovský priečinok), **nie Plocha ani Dokumenty**, ak sa ti synchronizujú do
iCloudu / OneDrive. Pamäť smie ísť do cloudu, ale heslá nikdy — a tie patria
mimo tohto priečinka, do `~/.config/<nazov>/`.

## Ak už máš MOJ-AGENT z lekcie 2.2

Nič nemaž. Spusti `/nastav` v TOMTO priečinku — agent tvoj starý MOJ-AGENT nájde
a prenesie z neho, čo už vieš.

## Windows

Skripty sú v bashi. Claude Code na Windows beží cez Git Bash, takže fungujú
rovnako. `over.py` potrebuje Python 3 (python.org, zaškrtni „Add to PATH").
