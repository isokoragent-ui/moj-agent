#!/bin/bash
# Nájde priečinok MOJ-AGENT podľa podpisu .mozog-id — nech je kdekoľvek.
# Použitie:  MOZOG=$(bash _nastroje/najdi_mozog.sh)
#
# PREČO: cesta zapísaná natvrdo sa rozbije pri prvom presune priečinka
# (stalo sa — osem skriptov naraz). Podpis prežije presun aj premenovanie.
# Domov sa hľadá pred Plochou: Plocha býva v cloude a chránená systémom,
# naplánované úlohy sa k nej nedostanú.

rozvin() { (cd "$1" 2>/dev/null && pwd -P); }

# 1. priečinok, v ktorom tento skript leží
tu=$(rozvin "$(dirname "$0")/..")
[ -f "$tu/.mozog-id" ] && { echo "$tu"; exit 0; }

# 2. obvyklé miesta
for p in "$HOME/MOJ-AGENT" "$HOME/Documents/MOJ-AGENT" "$HOME/Desktop/MOJ-AGENT"; do
  [ -f "$p/.mozog-id" ] && { rozvin "$p"; exit 0; }
done

# 3. núdzové hľadanie
p=$(find "$HOME" -maxdepth 3 -name ".mozog-id" 2>/dev/null | head -1)
[ -n "$p" ] && { rozvin "$(dirname "$p")"; exit 0; }

echo "❌ Priečinok MOJ-AGENT sa nenašiel (chýba .mozog-id?)" >&2
exit 1
