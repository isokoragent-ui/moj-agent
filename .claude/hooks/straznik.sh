#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════
#  STRÁŽCA — zastaví nebezpečný krok ESTE PRED vykonaním
# ═══════════════════════════════════════════════════════════════════════
#  Claude Code ho spustí pred každým Bash / Write / Edit (PreToolUse).
#  Na vstupe dostane JSON s tým, čo sa chystá urobiť.
#  exit 2 = ZASTAV (dôvod na stderr uvidí agent a upraví sa)
#  exit 0 = bez námietok, ďalej rozhoduje bežný systém oprávnení
#
#  PREČO: pravidlo v texte si agent môže nevšimnúť. Toto sa stane vždy.
#  Bez závislostí — len bash a grep, aby to bežalo na každom počítači.

VSTUP=$(cat)

# ── 1. Tajomstvá — vzory skutočných kľúčov (nie slovo „secret“ v texte)
TAJNE=(
  'sk-[A-Za-z0-9_-]{30,}'                 # OpenAI / Anthropic / Stripe
  'sk_(live|test)_[A-Za-z0-9]{20,}'       # Stripe
  'gsk_[A-Za-z0-9]{40,}'                  # Groq
  'AIza[A-Za-z0-9_-]{30,}'                # Google API key
  'ya29\.[A-Za-z0-9_-]{30,}'              # Google OAuth token
  'ghp_[A-Za-z0-9]{30,}'                  # GitHub
  'xox[baprs]-[A-Za-z0-9-]{20,}'          # Slack
  'ck_[a-f0-9]{32,}|cs_[a-f0-9]{32,}'     # WooCommerce
  'eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.'  # JWT
  '-----BEGIN [A-Z ]*PRIVATE KEY'         # súkromný kľúč
  '(postgres|postgresql|mysql|mongodb|redis)://[^:/ ]+:[^@ ]+@'   # heslo v adrese databázy
  '(heslo|password|passwd|api[_-]?key|secret|token)[ ]*[:=][ ]*["'"'"']?[A-Za-z0-9_./+-]{12,}'  # heslo = hodnota
)
# Zástupné hodnoty v návodoch — nie sú tajomstvo, strážca ich pustí.
VYNIMKY='(TVOJ_|<[^>]+>|your_|example|PRIKLAD|xxx+|\.\.\.|\$\{?[A-Z_]+\}?)'
for v in "${TAJNE[@]}"; do
  if printf '%s' "$VSTUP" | grep -Eo -- "$v" | grep -Evq -- "$VYNIMKY"; then
    echo "STRÁŽCA: v tomto kroku je niečo, čo vyzerá ako prístupový kľúč ($v)." >&2
    echo "Kľúče nepatria do súborov v MOJ-AGENT ani do príkazov. Ulož ho do ~/.config/<nazov>/ a sem daj len odkaz." >&2
    exit 2
  fi
done

# ── 2. Nebezpečné príkazy (len pre Bash)
if printf '%s' "$VSTUP" | grep -q '"tool_name": *"Bash"'; then
  NEBEZPECNE=(
    'rm -rf? +[/~]'          # mazanie od koreňa alebo domova
    'rm -rf? +\*'            # rm -rf *
    'sudo '
    'git push[^|;&]*(--force(-with-lease)?|-f)([ "]|$)'
    'git reset --hard'
    '--no-verify'            # obchádza strážcu v gite
    'chmod -R 777'
    'curl [^|;&]*\| *(ba)?sh' # curl | sh
    '> */dev/sd'
    'mkfs\.'
  )
  for v in "${NEBEZPECNE[@]}"; do
    if printf '%s' "$VSTUP" | grep -Eq -- "$v"; then
      echo "STRÁŽCA: príkaz zodpovedá nebezpečnému vzoru ($v). Nezvratné veci sa robia až po výslovnom „áno“ — a aj potom radšej ručne." >&2
      exit 2
    fi
  done
fi

exit 0
