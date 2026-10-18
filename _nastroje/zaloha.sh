#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════
#  ZÁLOHA — uloží stav pamäte do gitu (a na GitHub, ak je nastavený)
# ═══════════════════════════════════════════════════════════════════════
#  POUŽITIE:  bash _nastroje/zaloha.sh "čo sa zmenilo"
#
#  Prvýkrát sám založí git a zapne strážcu (.githooks/pre-commit), ktorý
#  zastaví commit s prístupovým údajom. Push spraví len vtedy, keď existuje
#  remote „origin“ — ten si pridáš raz: git remote add origin <adresa>
#  (súkromný repozitár! pamäť je osobná).
#
#  PREČO: pamäť bez zálohy je jedna rozliata káva od straty. A pamäť
#  v gite = dva počítače majú ten istý mozog.
set -e
MOZOG=$(bash "$(dirname "$0")/najdi_mozog.sh") || exit 1
cd "$MOZOG"
SPRAVA="${1:-Aktualizácia pamäte — $(date '+%d. %m. %Y %H:%M')}"

if [ ! -d .git ]; then
  git init -q
  echo "🆕 založený git v $MOZOG"
fi
git config core.hooksPath .githooks       # strážca — vždy, aj po klonovaní

git add -A
if git diff --cached --quiet; then
  echo "✅ Nič nové na zálohovanie."; exit 0
fi
git commit -q -m "$SPRAVA" || { echo "⛔ Commit zastavený (pozri strážcu vyššie)."; exit 1; }
echo "✅ Uložené: $SPRAVA"

if git remote get-url origin >/dev/null 2>&1; then
  VETVA=$(git branch --show-current)
  git push -q -u origin "$VETVA" && echo "☁️  Odoslané na origin/$VETVA" \
    || echo "⚠️ Push zlyhal — over prístup na GitHub (git remote -v)."
else
  echo "ℹ️  Bez GitHubu (len lokálne). Pridaj: git remote add origin <adresa súkromného repozitára>"
fi
