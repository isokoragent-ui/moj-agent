#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════
#  SPRIEVODCA — každý deň jeden ďalší krok, podľa toho, čo už je hotové
# ═══════════════════════════════════════════════════════════════════════
#  Pozrie sa na skutočný stav mozgu (súbory, nie domnienky), nájde prvý
#  nesplnený míľnik a ponúkne ho ako dnešný krok. Keď sú míľniky hotové,
#  ponúka striedavo tipy, čo skúsiť. Beží pri štarte rozhovoru (hook)
#  aj cez /sprievodca. Bez závislostí — bash.
#
#  POUŽITIE:  bash _nastroje/sprievodca.sh          # kompaktne (pre hook)
#             bash _nastroje/sprievodca.sh stav     # celý zoznam míľnikov
#             bash _nastroje/sprievodca.sh preskoc  # dnešný krok preskočiť
#
#  PREČO: prázdny mozog je ako prázdna telocvičňa — človek nevie, čím
#  začať, a po troch dňoch prestane chodiť. Sprievodca vždy vie, čo je
#  ďalšie, a hovorí len JEDNU vec (KÓD #7).

M=$(bash "$(dirname "$0")/najdi_mozog.sh") || exit 0
cd "$M" || exit 0
STAV_DIR="$M/09_ODOVZDANIE"; mkdir -p "$STAV_DIR/kontroly"
ZAC="$STAV_DIR/.zaciatok"; [ -f "$ZAC" ] || date +%Y-%m-%d > "$ZAC"
PRESKOC="$STAV_DIR/.sprievodca_preskocene"; touch "$PRESKOC"
UKAZANE="$STAV_DIR/.sprievodca_ukazane"
DNES=$(date +%Y-%m-%d)

# dni od začiatku (macOS aj Linux)
z=$(cat "$ZAC")
if date -j >/dev/null 2>&1; then zs=$(date -j -f %Y-%m-%d "$z" +%s); else zs=$(date -d "$z" +%s); fi
DEN=$(( ( $(date +%s) - zs ) / 86400 + 1 ))

# ── kontroly stavu (0 = splnené) ─────────────────────────────────────
nevyplnene() { grep -q '(zatiaľ nevyplnené)' "$1" 2>/dev/null; }
subory_v() { ls -1 "$1"/*.md 2>/dev/null | grep -vE 'README|_SABLONA|NAPLANOVANA_ULOHA' | wc -l | tr -d ' '; }
riadky_tab() { # počet dátových riadkov tabuľky za nadpisom $2 v súbore $1
  sed -n "/$2/,\$p" "$1" 2>/dev/null | grep -E '^\| ' | grep -vE '^\| *(-|Od kedy|Služba|Meno|Kto|Činnosť|Dátum)' | grep -v 'ukážka' | grep -v 'zatiaľ nevyplnené' | wc -l | tr -d ' '; }

k_profil()   { ! nevyplnene 01_JA/PROFIL.md; }
k_hlas()     { ! nevyplnene 03_STYL/HLAS.md; }
k_dusa()     { ! nevyplnene 00_KODY/DUSA.md; }
k_dennik()   { ls 06_DENNIK/20*.md >/dev/null 2>&1; }
k_git()      { [ -d .git ]; }
k_register() { [ "$(riadky_tab 05_PRISTUPY/REGISTER_PRISTUPOV.md 'Register')" -ge 1 ]; }
k_over()     { [ "$(grep -cE '^    "[a-z_]+": \("' _nastroje/over.py)" -ge 4 ]; }
k_kontrola() { ls 09_ODOVZDANIE/kontroly/*.md >/dev/null 2>&1; }
k_schema()   { [ "$(subory_v 07_SCHEMY)" -ge 1 ]; }
k_rozhod()   { [ "$(subory_v 08_ROZHODNUTIA)" -ge 1 ]; }
k_auto()     { [ "$(riadky_tab 04_RUTINY/AUDIT_AUTOMATIZACII.md 'Čo už agent prebral')" -ge 1 ]; }
k_github()   { git remote get-url origin >/dev/null 2>&1; }
k_schemy3()  { [ "$(subory_v 07_SCHEMY)" -ge 3 ]; }
k_kontrola2(){ [ "$(ls 09_ODOVZDANIE/kontroly/*.md 2>/dev/null | wc -l | tr -d ' ')" -ge 2 ]; }
k_ludia()    { [ "$(riadky_tab 02_PRACA/LUDIA.md 'Ľudia')" -ge 1 ]; }
k_autopilot(){ grep -qE 'Naposledy prešla:\*\* *[0-9]' 07_SCHEMY/NAPLANOVANA_ULOHA.md 2>/dev/null; }

# id | kontrola | názov | ako na to (jedna veta)
MILNIKY=(
 "profil|k_profil|Agent ťa pozná|napíš /nastav — 20 minút rozhovoru, jedna otázka naraz"
 "hlas|k_hlas|Agent vie, ako znieš|vlož 2 skutočné texty (e-mail, príspevok) do 03_STYL/HLAS.md — nepísané pre AI, skopírované"
 "dusa|k_dusa|Agent má meno a tón|otvor 00_KODY/DUSA.md alebo povedz agentovi: vyber si meno a spýtaj sa ma na tón"
 "dennik|k_dennik|Prvý zápis v denníku|napíš /dennik — čo sme dnes urobili a čím zajtra začneme"
 "git|k_git|Pamäť je zálohovaná|povedz agentovi: spusti bash _nastroje/zaloha.sh — ukladá len do tohto počítača"
 "register|k_register|Prvý prístup k tvojmu nástroju|vyber JEDEN nástroj (pošta, kalendár, e-shop) a povedz: chcem ti dať prístup k … — agent ti povie jeden krok"
 "over|k_over|Prístup je overený volaním|povedz agentovi: pridaj do over.py test pre službu, ktorú sme pripojili, a spusti ho"
 "kontrola|k_kontrola|Prvé skóre|napíš /kontrola — dostaneš skóre 0–100 a jeden návrh"
 "schema|k_schema|Prvá schéma|keď sa dnes niečo podarí prvýkrát, napíš /schema — návod aj s pascami"
 "rozhod|k_rozhod|Prvé zapísané rozhodnutie|pri najbližšom „dobre, spravíme to takto“ povedz: zapíš to ako rozhodnutie"
 "auto|k_auto|Prvá vec, ktorú už nerobíš|napíš /zlepsi — jedna automatizácia, začne tým, či to vôbec treba robiť"
 "github|k_github|Mozog aj na druhom počítači|založ SÚKROMNÝ repozitár na GitHube a povedz agentovi adresu — zaloha.sh ho začne používať"
 "schemy3|k_schemy3|Tri schémy|ktoré tri veci robíš dokola? každú raz sprav s agentom a hneď /schema"
 "kontrola2|k_kontrola2|Druhé skóre — porovnanie|napíš /kontrola a pozri, o koľko si vyrástol od minula"
 "ludia|k_ludia|Agent pozná tvojich ľudí|povedz agentovi o troch ľuďoch, s ktorými pracuješ najviac — zapíše ich do 02_PRACA/LUDIA.md"
 "autopilot|k_autopilot|Prvá vec beží bez teba|otvor 07_SCHEMY/NAPLANOVANA_ULOHA.md a nechaj agenta naplánovať to, čo už 3× prešlo ručne"
)

TIPY=(
 "Pošli agentovi fotku obrazovky z programu, v ktorom sa strácaš, a povedz: veď ma jedným krokom."
 "Hoď do _inbox/ jeden dokument a povedz: spracuj inbox. Pozri, kam ho zaradil."
 "Nechaj agenta napísať odpoveď na skutočný e-mail v tvojom štýle — neposielaj, len porovnaj, či znie ako ty."
 "Spýtaj sa: čo o mne vieš, čo som ti nikdy nepovedal priamo? Zapíš to do 01_JA/VZORCE.md."
 "Povedz agentovi jednu chybu, ktorú si dnes urobil ty alebo on — a pridaj z nej KÓD do 00_KODY."
 "Spýtaj sa: ktorá vec v 04_RUTINY mi tento mesiac vráti najviac minút a ešte ju nerobíš?"
 "Nechaj agenta prečítať posledných 10 e-mailov a rozdeliť ich na: odpovedať / archivovať / počká. Nič neposielaj."
 "Spýtaj sa: čo som ti sľúbil a nesplnil? (číta denník a odovzdania)"
 "Otvor 05_PRISTUPY a spýtaj sa: ktorý prístup som ti dal a už som ho mesiac nepoužil?"
 "Povedz agentovi: prejdi všetky schémy a povedz, ktorá je zastaraná."
 "Spýtaj sa na začiatku týždňa: čo sú tri veci, ktoré keď sa stanú, bol to dobrý týždeň?"
 "Nechaj agenta navrhnúť, čo by z tvojej práce zvládol stážista — a či to nie je práve on."
 "Spýtaj sa: keby zajtra prišlo 10× viac zákazníkov, čo sa pokazí prvé?"
 "Nechaj agenta spísať z posledného mesiaca denníka jednu stranu: čo sa naozaj pohlo."
 "Skús deň bez zoznamu: ráno sa spýtaj „čo je dnes tá jedna vec?“ a rob len ju."
)

# ── vyhodnotenie ─────────────────────────────────────────────────────
HOTOVE=0; DALSI=""; ZOZNAM=""
for m in "${MILNIKY[@]}"; do
  IFS='|' read -r id fn nazov ako <<< "$m"
  if $fn; then HOTOVE=$((HOTOVE+1)); ZOZNAM+="  ✅ $nazov"$'\n'
  elif grep -qx "$id" "$PRESKOC"; then ZOZNAM+="  ⏭  $nazov (preskočené)"$'\n'
  else ZOZNAM+="  ☐  $nazov"$'\n'; [ -z "$DALSI" ] && DALSI="$id|$nazov|$ako"; fi
done
CELKOM=${#MILNIKY[@]}

if [ "${1:-}" = "preskoc" ]; then
  [ -n "$DALSI" ] && { echo "${DALSI%%|*}" >> "$PRESKOC"; n="${DALSI#*|}"; echo "Preskočené: ${n%%|*}"; } || echo "Nie je čo preskočiť."
  exit 0
fi

if [ -n "$DALSI" ]; then
  IFS='|' read -r _ NAZOV AKO <<< "$DALSI"; TYP="MÍĽNIK"
else
  i=$(( (DEN-1) % ${#TIPY[@]} )); NAZOV="Tip dňa"; AKO="${TIPY[$i]}"; TYP="TIP"
fi

# zapíš postup (pre človeka aj /kontrola)
{
  echo "# Sprievodca — kde som"
  echo; echo "*Deň $DEN od začiatku · $HOTOVE z $CELKOM míľnikov · aktualizuje sa samo pri každom štarte*"
  echo; printf '%s' "$ZOZNAM"
  echo; echo "**Dnešný krok:** $NAZOV — $AKO"
} > "$STAV_DIR/SPRIEVODCA.md"

if [ "${1:-}" = "stav" ]; then
  cat "$STAV_DIR/SPRIEVODCA.md"; exit 0
fi

# kompaktný výstup pre hook (raz za deň naplno, potom len riadok)
echo "═══ SPRIEVODCA · deň $DEN · $HOTOVE/$CELKOM míľnikov ═══"
if [ "$(cat "$UKAZANE" 2>/dev/null)" = "$DNES" ]; then
  echo "Dnešný krok už dnes zaznel ($NAZOV). Nevnucuj ho — spomeň ho len, ak sa človek spýta, čo ďalej."
else
  echo "$DNES" > "$UKAZANE"
  echo "➜ DNEŠNÝ KROK ($TYP): $NAZOV"
  echo "   Ako: $AKO"
  echo "Pokyn pre agenta: na KONCI prvej odpovede ponúkni tento krok JEDNOU vetou a spýtaj sa, či doň ideme. Nič viac. Ak človek povie nie, dnes ho už nespomínaj."
fi
