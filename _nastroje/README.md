# Nástroje

| Skript | Načo | Kedy ho agent spustí |
|---|---|---|
| `preveruj.sh <téma>` | dôkaz pred vetou „to nemáme" (5 miest) | vždy pred popretím prístupu |
| `over.py [test]` | overí napojenia skutočným volaním | keď tvrdí, že niečo funguje; po pripojení služby pridá test |
| `zaloha.sh "správa"` | git commit (+push) so strážcom tajomstiev | pri `/odovzdaj`, po väčšej práci |
| `najdi_mozog.sh` | nájde priečinok podľa `.mozog-id` | volajú ho ostatné skripty |

Všetky sú bez závislostí (bash + Python 3 štandardná knižnica) a majú
v hlavičke „PREČO" — aby nikto neskôr nezrušil to, čo nás chráni.
- `tilsynslogg.py <chata.json>` — PDF záznam kontrol chaty pre poisťovňu (Hytteservice).
- `kjorebok.py <RRRR-MM>` — mesačná kniha jázd (Kjørebok) súkromným autom pre Isokor Skandinavia AS → PDF pre účtovníčku. Dáta v `02_PRACA/kjorebok/`.
- `faktura.py <číslo>|nova|zoznam` — faktúra Isokor - Skandinavia AS v PDF podľa Lukovej šablóny (Faktura 19). Dáta v `02_PRACA/faktury/`.
- `agenda.py den|tyzden|mesiac|kontrola` — agenda firmy AS: denné záznamy (výdavky, príjmy, aktivity) + raporty; berie aj faktúry a kjørebok. Dáta v `02_PRACA/agenda_as/`.
