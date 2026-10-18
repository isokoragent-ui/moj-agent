# NAPLÁNOVANÁ ÚLOHA — prvá vec, ktorá beží bez teba

**Kedy sa použije:** keď niečo prešlo s agentom ručne aspoň 3× čisto a chceš,
aby to bežalo samo (ranný prehľad, týždenný súhrn, kontrola skladu…).
**Naposledy prešla:** (ešte nie)

## Tri otázky PRED tým (ak jedna neprejde, nestaviaš)
1. Bežalo to ručne aspoň 3× bez opravy?
2. Je zlyhanie bezpečné? (vynechaný beh = nič; zle odoslaný e-mail = problém)
3. Píše to niečo von — pošta, platba, zverejnenie? → človek zostáva v slučke,
   úloha len PRIPRAVÍ.

## Kroky
1. Sprav zo skriptu jeden príkaz, ktorý sa dá spustiť z terminálu a skončí sám.
2. Spusti ho ručne raz z iného priečinka než z MOJ-AGENT — musí fungovať aj tak.
3. macOS: vytvor `~/Library/LaunchAgents/sk.mojagent.<nazov>.plist`
   (agent ho napíše; vzor nižšie). Windows: Plánovač úloh. Linux: `crontab -e`.
4. Načítaj: `launchctl load ~/Library/LaunchAgents/sk.mojagent.<nazov>.plist`
5. Počkaj na prvý naplánovaný beh. **Neber „načítané“ ako „beží“** — pozri log.
6. Zapíš do `05_PRISTUPY/REGISTER_PRISTUPOV.md` riadok: čo beží, kedy, kde je log,
   ako sa vypne (`launchctl unload …`). Do `08_ROZHODNUTIA` prečo.
7. Sem hore doplň „Naposledy prešla: dátum“.

## Pasce — čo nás už vypálilo
- ⚠️ **Naplánovaná úloha nemá tvoj shell.** Žiadne `~`, žiadne `$PATH`, žiadne
  premenné z profilu. Len absolútne cesty. Kľúče číta skript sám z `~/.config/`.
- ⚠️ **Plocha a Dokumenty sú chránené** — úloha sa k nim nedostane a ticho
  zlyhá. Preto MOJ-AGENT žije v domovskom priečinku.
- ⚠️ **Rozbitá naplánovaná úloha je horšia než žiadna** — nikto nevie, že
  neběží. Vždy log + `/kontrola` ho číta. Keď 2× zlyhá, vypni a oprav.
- ⚠️ **Strážca, ktorý blokuje donekonečna, nechráni** — zálohovanie raz stálo
  3 dni kvôli planému poplachu, nikto si nevšimol.
- ⚠️ `launchctl load` po zmene `.plist` nestačí — najprv `unload`, potom `load`.

## Čo agent spraví sám / kde čaká na „áno“
- sám: napíše skript, `.plist`, log, riadok do registra
- čaká: na `launchctl load` (spúšťaš ty — vidíš, čo sa zapína) a na každé
  „píše von“

## Vzor .plist (macOS) — každý pracovný deň 7:30
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>sk.mojagent.ranny-prehlad</string>
  <key>ProgramArguments</key><array>
    <string>/bin/bash</string>
    <string>/Users/MENO/MOJ-AGENT/_nastroje/moj_skript.sh</string>
  </array>
  <key>StartCalendarInterval</key><dict>
    <key>Hour</key><integer>7</integer><key>Minute</key><integer>30</integer>
  </dict>
  <key>StandardOutPath</key><string>/Users/MENO/MOJ-AGENT/_log/ranny.log</string>
  <key>StandardErrorPath</key><string>/Users/MENO/MOJ-AGENT/_log/ranny.err</string>
</dict></plist>
```
