#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════
  FAKTURA — z krátkeho JSON zadania spraví PDF faktúru na tlač
═══════════════════════════════════════════════════════════════════════
PREČO: Luk fakturuje za Isokor - Skandinavia AS z Word šablóny (Faktura 19).
Agent drží vzhľad šablóny, Luk len povie klienta, riadky a dátumy.

POUŽITIE:
    python3 _nastroje/faktura.py nova            # → data/<ďalšie číslo>.json (kostra)
    python3 _nastroje/faktura.py 20              # → pdf/Faktura_20.pdf + aktualizuje ZOZNAM.md
    python3 _nastroje/faktura.py 20 --kontrola   # len prepočíta a vypíše, PDF nerobí
    python3 _nastroje/faktura.py zoznam          # prepíše ZOZNAM.md zo všetkých faktúr

DÁTA:
    02_PRACA/faktury/nastavenie.json  — firma, účet, ORG.NR., splatnosť
    02_PRACA/faktury/data/<číslo>.json:
    {"cislo": 20,
     "kunde": {"navn": "Lene Øglænd", "adresse": ["Christiesgate 13", "4307 Sandnes"]},
     "fakturadato": "2026-11-11",
     "forfallsdato": "2026-11-15",          # nepovinné → fakturadato + splatnost_dni
     "linjer": [{"beskrivelse": "Vask av belegningsstein", "pris": 240,
                 "antall": 43, "mva": 0}],   # mva v %, nepovinné → mva_predvolene
     "stav": "vystavená",                    # vystavená / odoslaná / zaplatená
     "poznamka": ""}                         # len pre nás, na faktúru nejde
"""
import json, sys
from datetime import date, timedelta
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

KOREN = Path(__file__).resolve().parent.parent / "02_PRACA" / "faktury"
LIB = "/usr/share/fonts/truetype/liberation/"
pdfmetrics.registerFont(TTFont("A", LIB + "LiberationSans-Regular.ttf"))   # metriky ako Arial
pdfmetrics.registerFont(TTFont("AB", LIB + "LiberationSans-Bold.ttf"))

SEDA = colors.HexColor("#E7E6E6")
CERVENA = colors.HexColor("#FF0000")


def suma(x):
    """Nórsky zápis: 10 320 alebo 10 320,50"""
    x = round(x + 0.0, 2)
    if x == int(x):
        return f"{int(x):,}".replace(",", " ")
    return f"{x:,.2f}".replace(",", " ").replace(".", ",")


def datum(s):
    d = date.fromisoformat(s)
    return f"{d.day}.{d.month}.{d.year}"


def nacitaj_nastavenie():
    return json.loads((KOREN / "nastavenie.json").read_text(encoding="utf-8"))


def nacitaj(cislo):
    return json.loads((KOREN / "data" / f"{int(cislo)}.json").read_text(encoding="utf-8"))


def vsetky_cisla():
    return sorted(int(p.stem) for p in (KOREN / "data").glob("*.json") if p.stem.isdigit())


def prepocitaj(f, nast):
    """Doplní forfallsdato, beløp na riadkoch a súčty. Vráti zoznam chýb."""
    chyby = []
    if not f.get("kunde", {}).get("navn"):
        chyby.append("chýba meno klienta (kunde.navn)")
    try:
        fd = date.fromisoformat(f["fakturadato"])
    except Exception:
        chyby.append("fakturadato chýba alebo nie je RRRR-MM-DD")
        fd = None
    if not f.get("forfallsdato") and fd:
        f["forfallsdato"] = (fd + timedelta(days=nast["splatnost_dni"])).isoformat()
    if f.get("forfallsdato") and fd and date.fromisoformat(f["forfallsdato"]) < fd:
        chyby.append("forfallsdato je pred fakturadato")
    if not f.get("linjer"):
        chyby.append("faktúra nemá žiadne riadky (linjer)")
    netto = mva = 0.0
    for i, l in enumerate(f.get("linjer", []), 1):
        if not l.get("beskrivelse"):
            chyby.append(f"riadok {i}: chýba beskrivelse")
        try:
            pris, antall = float(l["pris"]), float(l.get("antall", 1))
        except Exception:
            chyby.append(f"riadok {i}: pris/antall nie je číslo")
            continue
        sadzba = float(l.get("mva", nast.get("mva_predvolene", 0)))
        l["mva"] = sadzba
        l["belop"] = round(pris * antall, 2)
        netto += l["belop"]
        mva += l["belop"] * sadzba / 100
    f["netto"], f["mva_spolu"] = round(netto, 2), round(mva, 2)
    f["spolu"] = round(netto + mva, 2)
    return chyby


def kresli(f, nast, cesta):
    W, H = A4
    c = canvas.Canvas(str(cesta), pagesize=A4)
    c.setTitle(f"Faktura {f['cislo']}")
    c.setAuthor(nast["firma"])
    y = lambda top: H - top          # súradnice zhora, ako v šablóne
    P = 560                          # pravý okraj
    R = 325                          # ľavý okraj pravého stĺpca

    # ─ hlavička
    c.setFont("AB", 18)
    c.drawRightString(P - 30, y(37), f"Faktura   {f['cislo']}")
    c.setLineWidth(0.8)
    c.line(R, y(46), P, y(46))
    c.drawImage(str(KOREN / "sablona" / "logo.png"), 60, y(92), width=226, height=43,
                preserveAspectRatio=True, mask="auto")
    c.setFont("AB", 12); c.drawString(R, y(61), nast["firma"])
    c.setFont("A", 10.5)
    for i, r in enumerate(nast["adresa"]):
        c.drawString(R, y(77 + i * 15.6), r)

    # ─ klient
    k = f["kunde"]
    c.setFont("A", 10)
    for i, r in enumerate([k["navn"]] + k.get("adresse", [])):
        c.drawString(80, y(135 + i * 19), r)

    # ─ dátumy
    c.setFont("A", 10.5)
    c.drawString(R + 20, y(137), "Fakturadato:"); c.drawString(R + 108, y(137), datum(f["fakturadato"]))
    c.drawString(R + 20, y(158), "Forfallsdato:")
    c.setFont("AB", 10.5); c.setFillColor(CERVENA)
    c.drawString(R + 108, y(158), datum(f["forfallsdato"]))
    c.setFillColor(colors.black)

    # ─ tabuľka
    stl = {"pris": 352, "antall": 405, "mva": 455, "belop": 520}   # stredy stĺpcov
    top = 238
    c.setFillColor(SEDA); c.rect(30, y(top + 15), P - 30, 15, stroke=0, fill=1)
    c.setFillColor(colors.black); c.setFont("AB", 7.5)
    c.drawCentredString(180, y(top + 10.5), "BESKRIVELSE")
    for kl, t in (("pris", "PRIS"), ("antall", "ANTALL"), ("mva", "MVA"), ("belop", "BELØP")):
        c.drawCentredString(stl[kl], y(top + 10.5), t)
    c.setLineWidth(0.6); c.line(30, y(top + 15.5), P, y(top + 15.5))

    riadok_y = top + 26
    for l in f["linjer"]:
        riadky = simpleSplit(l["beskrivelse"], "A", 9, 270)
        c.setFont("A", 9)
        for j, t in enumerate(riadky):
            c.drawString(45, y(riadok_y + j * 11), t)
        c.drawCentredString(stl["pris"], y(riadok_y), suma(float(l["pris"])))
        c.drawCentredString(stl["antall"], y(riadok_y), suma(float(l.get("antall", 1))))
        c.drawCentredString(stl["mva"], y(riadok_y), suma(l["mva"]) + " %")
        c.drawCentredString(stl["belop"], y(riadok_y), suma(l["belop"]))
        riadok_y += 11 * len(riadky) + 5
    c.setFillColor(SEDA); c.rect(30, y(riadok_y + 1), P - 30, 4, stroke=0, fill=1)
    c.setFillColor(colors.black)

    # ─ súčty
    s = riadok_y + 18
    c.setFont("AB", 10.5)
    c.drawString(R, y(s), "Nettobeløp");      c.drawCentredString(485, y(s), suma(f["netto"]))
    c.drawString(R, y(s + 20), "Merverdiavgift"); c.drawCentredString(485, y(s + 20), suma(f["mva_spolu"]))
    c.setLineWidth(0.8); c.line(R, y(s + 27), P, y(s + 27))
    c.setFont("AB", 13.5)
    c.drawString(R, y(s + 44), "Å BETALE");      c.drawCentredString(485, y(s + 44), suma(f["spolu"]))

    # ─ platba
    p = max(s + 95, 398)
    c.setFont("AB", 10.5)
    c.drawString(35, y(p), "Husk å merke betalingen med fakturanummer!")
    c.drawString(35, y(p + 22), f"Bankkonto:  {nast['bankkonto']}")
    c.setFont("AB", 8); c.drawString(35, y(p + 53), nast["banka"])

    # ─ pätička
    c.setFont("A", 10)
    orgnr = nast["org_nr"] + ("  MVA" if f.get("mva_registrovana", nast.get("mva_registrovana")) else "")
    c.drawString(35, y(800), f"ORG.NR.  {orgnr}")
    c.drawCentredString(W / 2, y(800), f"TELEFON: {nast['telefon']}")
    c.drawRightString(P, y(800), nast["web"])
    c.showPage(); c.save()


def zoznam(nast):
    riadky = ["# Zoznam faktúr — Isokor - Skandinavia AS", "",
              "*Generuje `python3 _nastroje/faktura.py zoznam` — ručne neupravuj.*", "",
              "| Č. | Dátum | Splatné | Klient | Suma (kr) | Stav |", "|---|---|---|---|---:|---|"]
    for n in vsetky_cisla():
        f = nacitaj(n); prepocitaj(f, nast)
        riadky.append(f"| {n} | {datum(f['fakturadato'])} | {datum(f['forfallsdato'])} | "
                      f"{f['kunde']['navn']} | {suma(f['spolu'])} | {f.get('stav', 'vystavená')} |")
    (KOREN / "ZOZNAM.md").write_text("\n".join(riadky) + "\n", encoding="utf-8")


def nova(nast):
    cisla = vsetky_cisla()
    n = max(cisla + [nast.get("posledne_cislo_pred_agentom", 0)]) + 1
    cesta = KOREN / "data" / f"{n}.json"
    kostra = {"cislo": n, "kunde": {"navn": "", "adresse": ["", ""]},
              "fakturadato": date.today().isoformat(), "forfallsdato": "",
              "linjer": [{"beskrivelse": "", "pris": 0, "antall": 1, "mva": nast.get("mva_predvolene", 0)}],
              "stav": "vystavená", "poznamka": ""}
    cesta.write_text(json.dumps(kostra, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Kostra: {cesta}")


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    nast = nacitaj_nastavenie()
    if sys.argv[1] == "nova":
        return nova(nast)
    if sys.argv[1] == "zoznam":
        zoznam(nast); print("ZOZNAM.md aktualizovaný"); return
    f = nacitaj(sys.argv[1])
    chyby = prepocitaj(f, nast)
    print(f"Faktura {f['cislo']} — {f['kunde'].get('navn')} — {datum(f['fakturadato'])} → splatné {datum(f['forfallsdato'])}")
    for l in f["linjer"]:
        print(f"  {l['beskrivelse'][:45]:45} {suma(float(l['pris'])):>8} × {suma(float(l.get('antall', 1))):>5}  mva {suma(l['mva'])}%  = {suma(l['belop'])}")
    print(f"  Netto {suma(f['netto'])} · MVA {suma(f['mva_spolu'])} · Å BETALE {suma(f['spolu'])} kr")
    if chyby:
        print("CHYBY:"); [print("  ✗", ch) for ch in chyby]; sys.exit(2)
    if "--kontrola" in sys.argv:
        return
    cesta = KOREN / "pdf" / f"Faktura_{f['cislo']}.pdf"
    kresli(f, nast, cesta)
    zoznam(nast)
    print(f"PDF: {cesta}")


if __name__ == "__main__":
    main()
