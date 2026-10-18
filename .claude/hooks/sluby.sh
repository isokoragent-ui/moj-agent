#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════
#  SĽUBY — keď v správe zaznie sľub, agent raz ponúkne, že ho zapíše
# ═══════════════════════════════════════════════════════════════════════
#  UserPromptSubmit hook. Číta správu človeka; ak vyzerá ako sľub niekomu
#  („pošlem ti to zajtra“, „ozvem sa Petrovi do piatku“), vloží agentovi
#  do kontextu pokyn: JEDENKRÁT ponúknuť zápis do 02_PRACA/LUDIA.md.
#  Nikdy nič nezapisuje sám. Nikdy neprerušuje, keď je to urgentné.
#  PREČO: sľub, ktorý nepristane v súbore, neexistuje — a práve tie
#  vyslovené mimochodom sa zabúdajú najčastejšie.

VSTUP=$(cat)
SPRAVA=$(printf '%s' "$VSTUP" | sed -n 's/.*"prompt": *"\(.*\)".*/\1/p' | head -c 2000)
[ -z "$SPRAVA" ] && exit 0

VZOR='(pošlem|posielam|ozvem sa|zavolám|napíšem (mu|jej|im|ti)|sľubujem|sľúbil som|dodám|pripravím (mu|jej|im|ti)|dám vedieť|vybavím)[^.!?]{0,60}(zajtra|dnes|do (pondelka|utorka|stredy|štvrtka|piatku|soboty|nedele|týždňa|konca|[0-9])|budúci|o [0-9]|večer|ráno|poobede)'
if printf '%s' "$SPRAVA" | grep -Eiq -- "$VZOR"; then
  echo "SĽUB? V správe zrejme zaznel sľub niekomu. Ak sa to hodí (nie uprostred súrnej veci), JEDNOU vetou ponúkni: „Mám si zapísať, že … — komu a dokedy?“ Zapíš až po „áno“ do 02_PRACA/LUDIA.md (Čo som sľúbil). Ak odmietne alebo neodpovie, pusti to."
fi
exit 0
