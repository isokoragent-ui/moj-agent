#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════
#  NA ZAČIATKU — vloží agentovi do kontextu, kde sme skončili
# ═══════════════════════════════════════════════════════════════════════
#  SessionStart hook. Čo vypíše na stdout, agent uvidí ako kontext —
#  aj keby zabudol prečítať AGENT.md. Volané s „po_skrateni“, keď sa
#  skrátil kontext (compact) — vtedy pripomenie len absolútne filtre.
#
#  PREČO: pravidlo „na začiatku si prečítaj odovzdanie“ v texte funguje
#  na 80 %. Toto funguje na 100 %.

KDE="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"

if [ "${1:-}" = "po_skrateni" ]; then
  echo "═══ KONTEXT BOL SKRÁTENÝ — pripomienka absolútnych filtrov ═══"
  sed -n '/^# ⭐ ABSOLÚTNE FILTRE/,/^# ĎALŠIE KÓDY/p' "$KDE/00_KODY/KODY_SPOLUPRACE.md" \
    | grep -E '^## ' | sed 's/^## /  /'
  echo "Plné znenie: 00_KODY/KODY_SPOLUPRACE.md. Nedokončené veci: 09_ODOVZDANIE/AKTUALNE.md"
  exit 0
fi

echo "═══ KDE SME SKONČILI (09_ODOVZDANIE/AKTUALNE.md) ═══"
[ -f "$KDE/09_ODOVZDANIE/AKTUALNE.md" ] && cat "$KDE/09_ODOVZDANIE/AKTUALNE.md"
echo

POSLEDNY=$(ls -1 "$KDE"/06_DENNIK/20*.md 2>/dev/null | sort | tail -1)
if [ -n "$POSLEDNY" ]; then
  echo "═══ POSLEDNÝ ZÁPIS V DENNÍKU ($(basename "$POSLEDNY")) ═══"
  awk '/^## /{blok=""} {blok=blok $0 "\n"} END{printf "%s", blok}' "$POSLEDNY"
  echo
fi

if grep -q '(zatiaľ nevyplnené)' "$KDE/01_JA/PROFIL.md" 2>/dev/null; then
  echo "⚠️ Profil ešte nie je vyplnený — navrhni spustiť /nastav."
fi

bash "$KDE/_nastroje/sprievodca.sh" 2>/dev/null
echo
echo "Začni vetou: „Naposledy sme skončili pri … Ideme ďalej?“ Ak niečo visí, povedz to."
