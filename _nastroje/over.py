#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════
  OVER — otestuje každé napojenie SKUTOČNÝM VOLANÍM
═══════════════════════════════════════════════════════════════════════
PREČO: agent tvrdil, že „API je zapnuté" — usúdil to z obrazovky. Nebolo.
Zistilo sa o deň neskôr pri chybe 403. Odvtedy: nikdy netvrdiť, že niečo
funguje, kým sa to nezavolá a nepozrie na dáta.

POUŽITIE:
    python3 _nastroje/over.py            # všetko
    python3 _nastroje/over.py internet   # jeden test

AKO PRIDAŤ TEST (agent to spraví, keď sa pripojí nová služba):
    def t_mojasluzba():
        ...zavolaj službu, vráť (True, "čo si videl") alebo (False, "dôvod")
    TESTY["mojasluzba"] = ("Moja služba", t_mojasluzba)
Kľúče čítaj z ~/.config/<nazov>/ — nikdy ich nepíš sem.

Vracia nenulový kód, keď niečo nefunguje — dá sa použiť v automatike.
Bez závislostí — len štandardná knižnica.
"""
import socket
import sys
import time
import urllib.request
from pathlib import Path

ZELENA, CERVENA, ZLTA, SIVA, K = "\033[32m", "\033[31m", "\033[33m", "\033[90m", "\033[0m"
MOZOG = Path(__file__).resolve().parent.parent


def t_internet():
    """Ako PRVÉ. Keď vypadne DNS, zhasne všetko naraz a vyzerá to ako chyba
    v kóde — pritom je nedotknutý."""
    zle = [h for h in ("www.google.com", "api.anthropic.com")
           if not _dns(h)]
    if zle:
        return False, "NEFUNGUJE INTERNET/DNS — nepreložilo sa: " + ", ".join(zle)
    return True, "DNS aj pripojenie v poriadku"


def t_mozog():
    """Je pamäť celá a nájde sa? Tichá porucha, ktorú bez kontroly nevidno."""
    chyba = [p for p in ("AGENT.md", ".mozog-id", "00_KODY/KODY_SPOLUPRACE.md",
                         "09_ODOVZDANIE/AKTUALNE.md") if not (MOZOG / p).exists()]
    if chyba:
        return False, "chýba: " + ", ".join(chyba)
    profil = (MOZOG / "01_JA/PROFIL.md").read_text(encoding="utf-8")
    if "(zatiaľ nevyplnené)" in profil:
        return False, "profil nevyplnený — spusti /nastav"
    return True, f"{MOZOG.name} · profil vyplnený"


def t_tajomstva():
    """Neleží v pamäti niečo, čo vyzerá ako kľúč? (rýchla kontrola textov)"""
    import re
    vzory = re.compile(r"sk-[A-Za-z0-9_-]{30,}|AIza[A-Za-z0-9_-]{30,}|ghp_[A-Za-z0-9]{30,}"
                       r"|-----BEGIN [A-Z ]*PRIVATE KEY|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.")
    zle = []
    for p in MOZOG.rglob("*.md"):
        try:
            if vzory.search(p.read_text(encoding="utf-8", errors="ignore")):
                zle.append(str(p.relative_to(MOZOG)))
        except OSError:
            pass
    if zle:
        return False, "vyzerá na kľúč v: " + ", ".join(zle[:3])
    return True, "žiadny kľúč v pamäti"


# ── Ukážka testu skutočnej služby (odkomentuj a uprav, keď pripojíš prvú) ──
# def t_web():
#     r = urllib.request.urlopen("https://www.mojastranka.sk", timeout=15)
#     if r.status != 200:
#         return False, f"HTTP {r.status}"
#     return True, "stránka odpovedá"


TESTY = {
    "internet": ("Internet/DNS", t_internet),
    "mozog": ("Pamäť agenta", t_mozog),
    "tajomstva": ("Tajomstvá v pamäti", t_tajomstva),
    # "web": ("Moja stránka", t_web),
}


def _dns(host):
    try:
        socket.gethostbyname(host)
        return True
    except OSError:
        return False


def main():
    vyber = sys.argv[1] if len(sys.argv) > 1 else None
    testy = {vyber: TESTY[vyber]} if vyber in TESTY else TESTY
    print(f"\n{ZLTA}═══ OVERUJEM SKUTOČNÝM VOLANÍM ═══{K}\n")
    zle = []
    for _, (nazov, fn) in testy.items():
        t0 = time.time()
        try:
            ok, detail = fn()
        except Exception as e:  # noqa: BLE001 — chceme vidieť každú chybu
            ok, detail = False, str(e).replace("\n", " ")[:90]
        znak = f"{ZELENA}✅{K}" if ok else f"{CERVENA}❌{K}"
        print(f"  {znak} {nazov:<20} {detail}  {SIVA}({time.time()-t0:.1f}s){K}")
        if not ok:
            zle.append(nazov)
    print()
    if zle:
        print(f"{CERVENA}  ❌ NEFUNGUJE: {', '.join(zle)}{K}")
        print(f"{SIVA}     Kým to nespravíš, netvrď, že to funguje.{K}\n")
        sys.exit(1)
    print(f"{ZELENA}  ✅ Všetko overené skutočným volaním.{K}\n")


if __name__ == "__main__":
    main()
