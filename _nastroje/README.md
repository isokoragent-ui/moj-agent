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
- `faktura.py <číslo>|nova|zoznam [--firma zivnost]` — faktúra v PDF podľa Lukovej šablóny. Bez prepínača = Isokor - Skandinavia AS (`02_PRACA/faktury/`, Faktura 19); `--firma zivnost` = Lukas Hric Liten Husservice (`02_PRACA/zivnost/faktury/`, Faktura 530).
- `agenda.py den|tyzden|mesiac|termin|prehlad|kontrola|rozpocet [--firma zivnost]` — agenda firmy: denné záznamy (výdavky, príjmy, aktivity) + raporty + návrh rozpočtu; berie aj faktúry (a pri AS kjørebok). Bez prepínača = AS (`02_PRACA/agenda_as/`), `--firma zivnost` = `02_PRACA/zivnost/agenda/`.
- `firmy.py` — jediné miesto, kde je určené, ktorá firma má ktoré priečinky (KÓD #25: nemiešať).
