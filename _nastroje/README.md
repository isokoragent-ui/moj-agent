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
