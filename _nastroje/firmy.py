#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════
  FIRMY — kde ležia dáta ktorej firmy (jediné miesto s cestami)
═══════════════════════════════════════════════════════════════════════
PREČO: Luk má dve firmy s rovnakou adresou a podobným ORG.NR. (KÓD #25).
Faktúry, agenda a raporty sa NESMÚ miešať. Skripty faktura.py a agenda.py
sú spoločné, ale každá firma má vlastné priečinky, vlastné nastavenie
a vlastné číslovanie. Firmu vyberá prepínač --firma (predvolene AS,
aby staré príkazy fungovali ďalej).

    python3 _nastroje/faktura.py 531 --firma zivnost
    python3 _nastroje/agenda.py mesiac --firma zivnost
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
P = ROOT / "02_PRACA"

FIRMY = {
    "as": {
        "nazov": "Isokor - Skandinavia AS",
        "faktury": P / "faktury",
        "agenda": P / "agenda_as",
        "kjorebok": P / "kjorebok" / "jazdy",
    },
    "zivnost": {
        "nazov": "Lukas Hric Liten Husservice (živnosť)",
        "faktury": P / "zivnost" / "faktury",
        "agenda": P / "zivnost" / "agenda",
        "kjorebok": None,          # kniha jázd je vedená len pre AS
    },
}


def vyber(argv=None):
    """Vytiahne --firma X z argumentov. Vráti (kľúč, nastavenie, zvyšné argumenty)."""
    argv = list(sys.argv if argv is None else argv)
    kluc = "as"
    if "--firma" in argv:
        i = argv.index("--firma")
        if i + 1 >= len(argv) or argv[i + 1] not in FIRMY:
            sys.exit(f"--firma musí byť jedna z: {', '.join(FIRMY)}")
        kluc = argv[i + 1]
        del argv[i:i + 2]
    return kluc, FIRMY[kluc], argv
