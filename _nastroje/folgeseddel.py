#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════
  FØLGESEDDEL — dodací list pri odovzdaní tovaru (Isokor - Skandinavia AS)
═══════════════════════════════════════════════════════════════════════
PREČO: Pri dodaní tovaru dostane zákazník dodací list, podpíše „Varene
mottatt" a až potom ide faktúra. Vzhľad podľa Lukovho papierového tlačiva
(02_PRACA/folgesedler/sablona/), dodávateľ je predvyplnený.

POUŽITIE:
    python3 _nastroje/folgeseddel.py nova             # → data/<ďalšie číslo>.json (kostra)
    python3 _nastroje/folgeseddel.py 1 --kontrola     # prepočíta a vypíše, PDF nerobí
    python3 _nastroje/folgeseddel.py 1                # → pdf/Folgeseddel_1.pdf + ZOZNAM.md
    python3 _nastroje/folgeseddel.py prazdny          # → pdf/Folgeseddel_prazdny.pdf (na ručné vypĺňanie)
    python3 _nastroje/folgeseddel.py 1 --faktura      # z podpísaného listu kostra faktúry
                                                      #   02_PRACA/faktury/data/<ďalšie č.>.json
    python3 _nastroje/folgeseddel.py zoznam           # prepíše ZOZNAM.md

DÁTA  02_PRACA/folgesedler/data/<číslo>.json:
    {"cislo": 1, "dato": "2026-11-24", "ekspedert_av": "Lukas Hric",
     "kjoper": {"navn": "Vegårshei kommune", "adresse": ["Molandsveien 11", "4985 Vegårshei"]},
     "linjer": [{"spesifikasjon": "Gravsteinvask 1 l", "antall": 6, "pris": 199, "mva": 25}],
                                       # pris = za kus BEZ MVA; mva nepovinné → 25 (od 6. 11. 2026)
     "uten_priser": false,             # true = list bez cien (len čo sa dodalo)
     "levert_til": "",                 # nepovinné — miesto dodania, ak iné ako adresa kupujúceho
     "stav": "vystavený",              # vystavený / podpísaný / fakturovaný
     "faktura": null,                  # číslo faktúry, keď sa z listu vystaví
     "poznamka": ""}                   # len pre nás, na list nejde
"""
import json, sys
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
import firmy
import faktura as F          # spoločné: fonty A/AB, suma(), datum(), nastavenie AS

KOREN = firmy.FIRMY["as"]["folgesedler"]
FAKTURY = firmy.FIRMY["as"]["faktury"]
SEDA = colors.HexColor("#DADCDA")
TMAVA = colors.HexColor("#3A3A3A")
RIADKOV = 16                  # počet riadkov tabuľky (ako na tlačive)


def nast():
    return json.loads((FAKTURY / "nastavenie.json").read_text(encoding="utf-8"))


def vsetky_cisla():
    return sorted(int(p.stem) for p in (KOREN / "data").glob("*.json") if p.stem.isdigit())


def nacitaj(n):
    return json.loads((KOREN / "data" / f"{int(n)}.json").read_text(encoding="utf-8"))


def mva_plati(fs, n):
    od = n.get("mva_registrovana_od")
    return bool(od) and fs.get("dato", "") >= od


def prepocitaj(fs, n):
    chyby = []
    if not fs.get("kjoper", {}).get("navn"):
        chyby.append("chýba kupujúci (kjoper.navn)")
    try:
        date.fromisoformat(fs["dato"])
    except Exception:
        chyby.append("dato chýba alebo nie je RRRR-MM-DD")
    if not fs.get("linjer"):
        chyby.append("list nemá žiadne riadky (linjer)")
    netto = mva = 0.0
    for i, l in enumerate(fs.get("linjer", []), 1):
        if not l.get("spesifikasjon"):
            chyby.append(f"riadok {i}: chýba spesifikasjon")
        try:
            pris, antall = float(l.get("pris", 0)), float(l.get("antall", 1))
        except Exception:
            chyby.append(f"riadok {i}: pris/antall nie je číslo"); continue
        l["mva"] = float(l.get("mva", n.get("mva_predvolene", 0) if mva_plati(fs, n) else 0))
        l["belop"] = round(pris * antall, 2)
        netto += l["belop"]; mva += l["belop"] * l["mva"] / 100
    fs["netto"], fs["mva_spolu"] = round(netto, 2), round(mva, 2)
    fs["spolu"] = round(netto + mva, 2)
    return chyby


def text_riadku(l):
    a = float(l.get("antall", 1))
    t = l["spesifikasjon"]
    if a != 1 or l.get("pris"):
        t += f"   ({F.suma(a)} stk" + (f" à {F.suma(float(l['pris']))}" if l.get("pris") else "") + ")"
    return t


def kr_ore(x):
    """Rozdelí sumu na celé koruny a øre (ako stĺpce na tlačive)."""
    kr = int(round(x * 100)) // 100
    return f"{kr:,}".replace(",", " "), f"{int(round(x * 100)) % 100:02d}"


def kresli(fs, n, cesta, prazdny=False):
    W, H = A4
    c = canvas.Canvas(str(cesta), pagesize=A4)
    c.setTitle("Følgeseddel" + ("" if prazdny else f" {fs['cislo']}"))
    c.setAuthor(n["firma"])
    y = lambda t: H - t
    L, P = 40, W - 40                         # okraje
    c.setStrokeColor(TMAVA)

    # ─ LEVERANDØR (predvyplnený) — vľavo hore
    c.setLineWidth(0.8)
    c.roundRect(L, y(150), 250, 108, 6)
    c.setFont("AB", 7.5); c.drawString(L + 8, y(54), "LEVERANDØR")
    c.drawImage(str(FAKTURY / "sablona" / "logo.png"), L + 8, y(84), width=150, height=26,
                preserveAspectRatio=True, anchor="w", mask="auto")
    c.setFont("AB", 10); c.drawString(L + 8, y(100), n["firma"])
    c.setFont("A", 9)
    for i, r in enumerate(n["adresa"] + [f"Org.nr. {n['org_nr']}" + ("  MVA" if prazdny or mva_plati(fs, n) else ""),
                                         f"Tlf. {n['telefon']}"]):
        c.drawString(L + 8, y(113 + i * 10.5), r)

    # ─ nadpis + DATO / NR. / EKSP. AV — vpravo hore
    c.setFont("AB", 26); c.drawRightString(P, y(68), "FØLGESEDDEL")
    bx, bw = P - 200, 200
    c.setLineWidth(0.8); c.rect(bx, y(160), bw, 72)
    for i, (nadpis, hodnota) in enumerate((
            ("NR.", "" if prazdny else str(fs["cislo"])),
            ("DATO", "" if prazdny else F.datum(fs["dato"])),
            ("EKSP. AV", "" if prazdny else fs.get("ekspedert_av", "")))):
        top = 88 + i * 24
        if i: c.line(bx, y(top), P, y(top))
        c.setFont("AB", 7); c.drawString(bx + 6, y(top + 9), nadpis)
        c.setFont("A", 11); c.drawString(bx + 62, y(top + 17), hodnota)

    # ─ KJØPER — šedý box
    k = fs.get("kjoper", {}) if not prazdny else {}
    c.setFillColor(SEDA); c.roundRect(L, y(268), 250, 108, 6, stroke=1, fill=1)
    c.setFillColor(colors.black)
    c.setFont("AB", 7.5); c.drawString(L + 8, y(172), "KJØPER")
    if k:
        c.setFont("AB", 10.5); c.drawString(L + 8, y(192), k["navn"])
        c.setFont("A", 10)
        for i, r in enumerate(k.get("adresse", [])):
            c.drawString(L + 8, y(207 + i * 13), r)
    else:
        c.setStrokeColor(colors.HexColor("#9A9A9A")); c.setLineWidth(0.4)
        for i in range(4):
            c.line(L + 8, y(198 + i * 20), L + 242, y(198 + i * 20))
        c.setStrokeColor(TMAVA)
    if not prazdny and fs.get("levert_til"):
        c.setFont("AB", 7.5); c.drawString(bx, y(182), "LEVERT TIL")
        c.setFont("A", 9.5)
        for i, r in enumerate(simpleSplit(fs["levert_til"], "A", 9.5, bw)):
            c.drawString(bx, y(196 + i * 12), r)

    # ─ tabuľka SPESIFIKASJON | KRONER (kr . øre)
    T, rh = 290, 22                           # horný okraj, výška riadku
    kx, ox = P - 95, P - 28                   # začiatok stĺpca kroner, oddeľovač øre
    bez_cien = prazdny is False and fs.get("uten_priser")
    c.setLineWidth(1.2); c.rect(L, y(T + rh * (RIADKOV + 1)), P - L, rh * (RIADKOV + 1))
    c.setLineWidth(0.8); c.line(L, y(T + rh), P, y(T + rh))
    c.line(kx, y(T), kx, y(T + rh * (RIADKOV + 1)))
    c.setFont("AB", 8); c.drawString(L + 8, y(T + 14), "SPESIFIKASJON")
    c.drawString(kx + 8, y(T + 14), "KRONER")
    c.setLineWidth(0.4); c.setStrokeColor(colors.HexColor("#9A9A9A"))
    for i in range(2, RIADKOV + 1):
        c.line(L, y(T + rh * i), P, y(T + rh * i))
    c.setDash(1, 2); c.line(ox, y(T + rh), ox, y(T + rh * (RIADKOV + 1))); c.setDash()
    c.setStrokeColor(TMAVA)
    if not prazdny:
        r = 1
        for l in fs["linjer"]:
            riadky = simpleSplit(text_riadku(l) if not bez_cien else
                                 l["spesifikasjon"] + f"   ({F.suma(float(l.get('antall', 1)))} stk)",
                                 "A", 10, kx - L - 16)
            for j, t in enumerate(riadky):
                c.setFont("A", 10); c.drawString(L + 8, y(T + rh * (r + j) + 15), t)
            if not bez_cien:
                kr, ore = kr_ore(l["belop"])
                c.drawRightString(ox - 5, y(T + rh * r + 15), kr)
                c.drawString(ox + 6, y(T + rh * r + 15), ore)
            r += len(riadky)

    # ─ spodok: VARENE MOTTATT | BETALT | KRONER / MVA / TOTAL SUM
    B = T + rh * (RIADKOV + 1) + 18
    bh = 112
    sx = P - 150                              # súčtový box
    mx = L + 190                              # hranica VARENE MOTTATT | BETALT
    c.setLineWidth(1.2); c.rect(L, y(B + bh), P - L, bh)
    c.line(mx, y(B), mx, y(B + bh)); c.line(sx, y(B), sx, y(B + bh))
    c.setFont("AB", 8)
    c.drawString(L + 8, y(B + 14), "VARENE MOTTATT")
    c.drawString(mx + 8, y(B + 14), "BETALT")
    c.setFont("A", 8.5)
    c.setLineWidth(0.4)
    for i, t in enumerate(("Dato:", "Underskrift:", "Navn (blokkbokst.):")):
        yy = B + 42 + i * 26
        c.drawString(L + 8, y(yy), t); c.line(L + 88, y(yy + 2), mx - 10, y(yy + 2))
    for i, t in enumerate(("Dato:", "Underskrift:")):
        yy = B + 42 + i * 26
        c.drawString(mx + 8, y(yy), t); c.line(mx + 62, y(yy + 2), sx - 10, y(yy + 2))
    if not prazdny and fs.get("betalt_dato"):
        c.setFont("A", 10); c.drawString(mx + 66, y(B + 40), F.datum(fs["betalt_dato"]))
    sh = bh / 3
    c.setLineWidth(0.8)
    c.setFillColor(SEDA); c.rect(sx + 60, y(B + bh), P - sx - 60, sh, stroke=0, fill=1)
    c.setFillColor(colors.black)
    c.line(sx + 60, y(B), sx + 60, y(B + bh))
    for i, t in enumerate(("KRONER", "MVA", "TOTAL SUM")):
        if i: c.line(sx, y(B + sh * i), P, y(B + sh * i))
        c.setFont("AB", 7.5); c.drawString(sx + 6, y(B + sh * i + sh / 2 + 3), t)
    if not prazdny and not bez_cien:
        for i, (x, tuc) in enumerate(((fs["netto"], 0), (fs["mva_spolu"], 0), (fs["spolu"], 1))):
            c.setFont("AB" if tuc else "A", 11 if tuc else 10)
            c.drawRightString(P - 6, y(B + sh * i + sh / 2 + 4), F.suma(x))

    # ─ pätička
    c.setFont("A", 7.5); c.setFillColor(colors.HexColor("#555555"))
    pata = "Varene er mottatt i god stand når følgeseddelen er signert. Faktura sendes separat."
    c.drawCentredString(W / 2, y(B + bh + 22), pata)
    if n.get("web"):
        c.drawCentredString(W / 2, y(B + bh + 34), n["web"])
    c.showPage(); c.save()


def zoznam(n):
    riadky = [f"# Zoznam dodacích listov (følgesedler) — {n['firma']}", "",
              "*Generuje `python3 _nastroje/folgeseddel.py zoznam` — ručne neupravuj.*", "",
              "| Č. | Dátum | Kupujúci | Suma s MVA (kr) | Stav | Faktúra |", "|---|---|---|---:|---|---|"]
    for c in vsetky_cisla():
        fs = nacitaj(c); prepocitaj(fs, n)
        riadky.append(f"| {c} | {F.datum(fs['dato'])} | {fs['kjoper']['navn']} | "
                      f"{'—' if fs.get('uten_priser') else F.suma(fs['spolu'])} | {fs.get('stav', 'vystavený')} | "
                      f"{fs.get('faktura') or ''} |")
    (KOREN / "ZOZNAM.md").write_text("\n".join(riadky) + "\n", encoding="utf-8")


def nova(n):
    c = max(vsetky_cisla() + [0]) + 1
    cesta = KOREN / "data" / f"{c}.json"
    kostra = {"cislo": c, "dato": date.today().isoformat(), "ekspedert_av": "Lukas Hric",
              "kjoper": {"navn": "", "adresse": ["", ""]},
              "linjer": [{"spesifikasjon": "", "antall": 1, "pris": 0, "mva": n.get("mva_predvolene", 0)}],
              "uten_priser": False, "levert_til": "", "stav": "vystavený", "faktura": None, "poznamka": ""}
    cesta.write_text(json.dumps(kostra, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Kostra: {cesta}")


def na_fakturu(fs, n):
    """Z dodacieho listu kostra faktúry. PDF faktúry sa robí až po Lukovom „áno" (faktura.py)."""
    if fs.get("faktura"):
        sys.exit(f"Følgeseddel {fs['cislo']} už má faktúru {fs['faktura']}.")
    if fs.get("uten_priser"):
        print("POZOR: list je bez cien — ceny na faktúre treba doplniť.")
    F.nastav_firmu("as")
    cislo = max(F.vsetky_cisla() + [n.get("posledne_cislo_pred_agentom", 0)]) + 1
    f = {"cislo": cislo, "kunde": fs["kjoper"], "fakturadato": date.today().isoformat(), "forfallsdato": "",
         "linjer": [{"beskrivelse": l["spesifikasjon"], "pris": l.get("pris", 0),
                     "antall": l.get("antall", 1), "mva": l["mva"]} for l in fs["linjer"]],
         "referanse": f"Følgeseddel nr. {fs['cislo']} ({F.datum(fs['dato'])})",
         "stav": "vystavená", "poznamka": f"Z dodacieho listu č. {fs['cislo']}."}
    (FAKTURY / "data" / f"{cislo}.json").write_text(json.dumps(f, ensure_ascii=False, indent=2) + "\n",
                                                   encoding="utf-8")
    surovy = nacitaj(fs["cislo"]); surovy["faktura"] = cislo; surovy["stav"] = "fakturovaný"
    (KOREN / "data" / f"{fs['cislo']}.json").write_text(json.dumps(surovy, ensure_ascii=False, indent=2) + "\n",
                                                       encoding="utf-8")
    zoznam(n)
    print(f"Kostra faktúry {cislo}: 02_PRACA/faktury/data/{cislo}.json → over: "
          f"python3 _nastroje/faktura.py {cislo} --kontrola")


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    n = nast()
    a = sys.argv[1]
    if a == "nova":
        return nova(n)
    if a == "zoznam":
        zoznam(n); print("ZOZNAM.md aktualizovaný"); return
    if a == "prazdny":
        cesta = KOREN / "pdf" / "Folgeseddel_prazdny.pdf"
        kresli({}, n, cesta, prazdny=True); print(f"PDF: {cesta}"); return
    fs = nacitaj(a)
    chyby = prepocitaj(fs, n)
    print(f"[{n['firma']}] Følgeseddel {fs['cislo']} — {fs['kjoper'].get('navn')} — {F.datum(fs['dato'])}")
    for l in fs.get("linjer", []):
        print(f"  {l.get('spesifikasjon', '')[:45]:45} {F.suma(float(l.get('pris', 0))):>8} × "
              f"{F.suma(float(l.get('antall', 1))):>5}  mva {F.suma(l.get('mva', 0))}%  = {F.suma(l.get('belop', 0))}")
    print(f"  Kroner {F.suma(fs['netto'])} · MVA {F.suma(fs['mva_spolu'])} · TOTAL {F.suma(fs['spolu'])} kr")
    if chyby:
        print("CHYBY:"); [print("  ✗", ch) for ch in chyby]; sys.exit(2)
    if sum(len(simpleSplit(text_riadku(l), "A", 10, 400)) for l in fs["linjer"]) > RIADKOV:
        sys.exit(f"Priveľa riadkov — na jeden list sa zmestí {RIADKOV}. Rozdeľ na dva listy.")
    if "--kontrola" in sys.argv:
        return
    if "--faktura" in sys.argv:
        return na_fakturu(fs, n)
    cesta = KOREN / "pdf" / f"Folgeseddel_{fs['cislo']}.pdf"
    kresli(fs, n, cesta)
    zoznam(n)
    print(f"PDF: {cesta}")


if __name__ == "__main__":
    main()
