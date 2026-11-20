# 2026-11-20 — Agenda: oblasť a hodiny pri príjmoch

- **Luk „áno“ (okno Štúdium majetku):** k príjmom pridať 2 nepovinné polia — `oblast` a `hodiny`.
- **Prečo:** zákazníci platia za výsledok, nie za hodinu; aby sme videli, ktorá oblasť reálne zarába najviac na hodinu (cieľ ≥ 1 119 kr/h bez MVA, `10_STUDIUM_MAJETOK/08_HODINOVKA.md`).
- **Ako:** `_nastroje/agenda.py` (záznamy aj faktúry), `nastavenie.json` AS + živnosť → `oblasti`, `hranica_kr_h`; raport „Príjmy podľa oblasti“. Kontrola hlási neznámu oblasť / zlé hodiny.
