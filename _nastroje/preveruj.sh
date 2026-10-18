#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════
#  PREVERUJ — povinná kontrola pred vetou „to nemáme / to neexistuje“
# ═══════════════════════════════════════════════════════════════════════
#  PREČO: agent tvrdil, že nemá prístup k firemnej pošte — hoci s ňou
#  pracoval denne a skripty ležali v priečinku. Príčina: povrchné hľadanie
#  + filter, ktorý odrezal výsledky.
#
#  PRAVIDLO: agent NESMIE povedať „nemáme to“, kým nespustí tento skript
#  a neukáže jeho výstup.
#
#  POUŽITIE:  bash _nastroje/preveruj.sh mail
#             bash _nastroje/preveruj.sh            # vypíše register prístupov
set -uo pipefail

HLADAJ="${1:-}"
MOZOG=$(bash "$(dirname "$0")/najdi_mozog.sh") || exit 1
REGISTER="$MOZOG/05_PRISTUPY/REGISTER_PRISTUPOV.md"
VYNECHAJ="site-packages|/venv/|node_modules|/Library/|\.app/|/\.cache/|/\.git/"

zelena() { printf "\033[32m%s\033[0m\n" "$1"; }
zlta()   { printf "\033[33m%s\033[0m\n" "$1"; }
siva()   { printf "\033[90m%s\033[0m\n" "$1"; }

if [ -z "$HLADAJ" ]; then
  echo "═══ REGISTER PRÍSTUPOV ═══"; cat "$REGISTER"; exit 0
fi

echo "═══════════════════════════════════════════"
echo "  PREVERUJEM: $HLADAJ"
echo "═══════════════════════════════════════════"; echo
NASLO_NIECO=0

zlta "▸ 1. REGISTER PRÍSTUPOV"
if grep -qi -- "$HLADAJ" "$REGISTER" 2>/dev/null; then
  grep -i -B1 -A2 -- "$HLADAJ" "$REGISTER" | sed 's/^/   /'
  zelena "   ✅ NÁJDENÉ V REGISTRI — prístup existuje!"; NASLO_NIECO=1
else siva "   (v registri nič)"; fi
echo

zlta "▸ 2. PAMÄŤ AGENTA (celý MOJ-AGENT)"
N=$(grep -ril -- "$HLADAJ" "$MOZOG" 2>/dev/null | grep -vE "$VYNECHAJ" | head -30)
if [ -n "$N" ]; then echo "$N" | sed 's/^/   📄 /'; NASLO_NIECO=1
else siva "   (nič)"; fi
echo

zlta "▸ 3. SKRIPTY A KONFIGURÁCIA (~/.config, ~/Documents)"
N2=$(grep -ril --include="*.py" --include="*.sh" --include="*.js" --include="*.json" \
     --include="*.md" --include="*.yaml" --include="*.yml" --include="*.toml" \
     -- "$HLADAJ" "$HOME/.config" "$HOME/Documents" 2>/dev/null | grep -vE "$VYNECHAJ" | head -20)
if [ -n "$N2" ]; then echo "$N2" | sed 's/^/   📄 /'; NASLO_NIECO=1
else siva "   (nič)"; fi
echo

zlta "▸ 4. NAPLÁNOVANÉ AUTOMATIKY"
LA=$( { ls -1 ~/Library/LaunchAgents/ 2>/dev/null; crontab -l 2>/dev/null; } | grep -i -- "$HLADAJ")
if [ -n "$LA" ]; then echo "$LA" | sed 's/^/   ⏰ /'; NASLO_NIECO=1
else siva "   (nič)"; fi
echo

if command -v security >/dev/null 2>&1; then
  zlta "▸ 5. HESLÁ V KEYCHAIN (macOS)"
  if security dump-keychain 2>/dev/null | grep -qi -- "\"svce\".*$HLADAJ"; then
    zelena "   🔑 v Keychain je položka, ktorej názov obsahuje „$HLADAJ“"; NASLO_NIECO=1
  else siva "   (nič)"; fi
  echo
fi

echo "═══════════════════════════════════════════"
if [ $NASLO_NIECO -eq 1 ]; then
  zelena "  ZÁVER: NIEČO SA NAŠLO. Prečítaj nájdené súbory, KÝM čokoľvek tvrdíš."
else
  echo "  ZÁVER: nič v žiadnom z miest. Až teraz smieš povedať, že prístup"
  echo "  zrejme neexistuje — a aj tak sa najprv opýtaj, kde by mohol byť."
fi
echo "═══════════════════════════════════════════"
