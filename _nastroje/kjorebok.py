#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════
  KJØREBOK — z mesačného JSON záznamu jázd spraví PDF pre účtovníčku
═══════════════════════════════════════════════════════════════════════
PREČO: Luk jazdí súkromným autom pre Isokor Skandinavia AS. Kilometre
firma prepláca (kjøregodtgjørelse) len s knihou jázd. Luk diktuje,
agent zapisuje, raz mesačne z toho spraví PDF.

POUŽITIE:
    python3 _nastroje/kjorebok.py 2026-11          # → 02_PRACA/kjorebok/pdf/Kjorebok_2026-11.pdf
    python3 _nastroje/kjorebok.py 2026-11 --kontrola   # len skontroluje dáta, PDF nerobí

DÁTA:
    02_PRACA/kjorebok/nastavenie.json   — firma, vodič, auto, sadzba
    02_PRACA/kjorebok/jazdy/RRRR-MM.json — {"jazdy": [ {...}, ... ]}
    jazda: {"dato": "2026-11-11", "fra": "Vegårshei", "til": "Arendal",
            "formal": "Levering av varer", "besokt": "Kunde X",
            "km_start": 123456, "km_slutt": 123512, "km": 56,
            "tur_retur": false, "bom": 0, "parkering": 0, "merknad": ""}
    km sa dopočíta z km_start/km_slutt; ak tachometer chýba, stačí "km".
"""
import json, sys
from datetime import date
from pathlib import Path
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

KOREN = Path(__file__).resolve().parent.parent / "02_PRACA" / "kjorebok"
MESIACE = ["januar", "februar", "mars", "april", "mai", "juni", "juli",
           "august", "september", "oktober", "november", "desember"]

pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
registerFontFamily("DV", normal="DV", bold="DVB", italic="DV", boldItalic="DVB")


def kr(x):
    return f"{x:,.2f}".replace(",", " ").replace(".", ",") + " kr"


def nacitaj(mesiac):
    nast = json.loads((KOREN / "nastavenie.json").read_text(encoding="utf-8"))
    subor = KOREN / "jazdy" / f"{mesiac}.json"
    jazdy = json.loads(subor.read_text(encoding="utf-8")).get("jazdy", []) if subor.exists() else []
    return nast, sorted(jazdy, key=lambda j: (j.get("dato", ""), j.get("km_start") or 0))


def skontroluj(mesiac, jazdy):
    """Vráti zoznam problémov. Prázdny zoznam = v poriadku."""
    chyby = []
    for i, j in enumerate(jazdy, 1):
        n = f"jazda {i} ({j.get('dato', '?')})"
        if not str(j.get("dato", "")).startswith(mesiac):
            chyby.append(f"{n}: dátum nie je v mesiaci {mesiac}")
        for pole in ("fra", "til", "formal"):
            if not j.get(pole):
                chyby.append(f"{n}: chýba '{pole}'")
        ks, ke = j.get("km_start"), j.get("km_slutt")
        if ks is not None and ke is not None:
            if ke <= ks:
                chyby.append(f"{n}: km_slutt {ke} nie je väčší než km_start {ks}")
            elif j.get("km") not in (None, ke - ks):
                chyby.append(f"{n}: km {j['km']} ≠ tachometer {ke - ks}")
        elif not j.get("km"):
            chyby.append(f"{n}: chýba km aj stav tachometra")
    for a, b in zip(jazdy, jazdy[1:]):
        if a.get("km_slutt") and b.get("km_start") and b["km_start"] < a["km_slutt"]:
            chyby.append(f"{b.get('dato')}: tachometer ide dozadu ({a['km_slutt']} → {b['km_start']})")
    return chyby


def km_jazdy(j):
    if j.get("km_start") is not None and j.get("km_slutt") is not None:
        return j["km_slutt"] - j["km_start"]
    return j.get("km") or 0


def lag_pdf(mesiac, nast, jazdy, ut):
    rok, m = mesiac.split("-")
    obdobie = f"{MESIACE[int(m) - 1]} {rok}"
    st = getSampleStyleSheet()
    for s in st.byName.values():
        s.fontName = "DV"
    st["Title"].fontName = "DVB"
    liten = st["BodyText"].clone("liten", fontSize=8, leading=10)
    doc = SimpleDocTemplate(str(ut), pagesize=landscape(A4), leftMargin=12*mm, rightMargin=12*mm,
                            topMargin=12*mm, bottomMargin=12*mm, title=f"Kjørebok {obdobie}")
    f, bil = nast["firma"], nast["bil"]
    sats = nast.get("sats_per_km")
    hlava = [
        Paragraph(f"Kjørebok – {obdobie}", st["Title"]),
        Paragraph(f"<b>Firma:</b> {f['navn']}, org.nr. {f['orgnr']} &nbsp;&nbsp; "
                  f"<b>Sjåfør:</b> {nast['sjafor']} &nbsp;&nbsp; "
                  f"<b>Bil (privat):</b> {bil.get('merke') or '—'}, reg.nr. {bil.get('regnr') or '—'}",
                  st["BodyText"]),
        Spacer(1, 4*mm),
    ]
    rader = [["Dato", "Fra", "Til", "Formål med kjøringen", "Besøkt / kunde",
              "Km-stand\nstart", "Km-stand\nslutt", "Km", "Bom/\nparkering", "Merknad"]]
    sum_km = sum_bom = 0
    for j in jazdy:
        k = km_jazdy(j)
        bom = (j.get("bom") or 0) + (j.get("parkering") or 0)
        sum_km += k
        sum_bom += bom
        merk = j.get("merknad", "")
        if j.get("tur_retur"):
            merk = ("Tur/retur. " + merk).strip()
        rader.append([j["dato"], Paragraph(j.get("fra", ""), liten), Paragraph(j.get("til", ""), liten),
                      Paragraph(j.get("formal", ""), liten), Paragraph(j.get("besokt", ""), liten),
                      "" if j.get("km_start") is None else f"{j['km_start']:,}".replace(",", " "),
                      "" if j.get("km_slutt") is None else f"{j['km_slutt']:,}".replace(",", " "),
                      str(k), kr(bom) if bom else "", Paragraph(merk, liten)])
    if not jazdy:
        rader += [[""] * 10 for _ in range(12)]
    rader.append(["", "", "", "", "Sum", "", "", str(sum_km), kr(sum_bom) if sum_bom else "", ""])
    sirky = [20, 33, 33, 55, 38, 18, 18, 13, 20, 25]
    t = Table(rader, colWidths=[s*mm for s in sirky], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0, 0), (-1, -1), "DV", 8),
        ("FONT", (0, 0), (-1, 0), "DVB", 8),
        ("FONT", (0, -1), (-1, -1), "DVB", 8),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2f5d3a")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("BACKGROUND", (0, -1), (-1, -1), colors.HexColor("#e3ebe3")),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (5, 1), (8, -1), "RIGHT"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -2), [colors.white, colors.HexColor("#f2f5f2")]),
    ]))
    spolu = [Spacer(1, 6*mm)]
    suhrn = [["Kjørte km i perioden", f"{sum_km} km"]]
    if sats:
        suhrn += [[f"Sats per km ({nast.get('sats_kilde', '')})", kr(sats)],
                  ["Kjøregodtgjørelse", kr(sum_km * sats)]]
    if sum_bom:
        suhrn.append(["Bom og parkering (legg ved kvitteringer)", kr(sum_bom)])
    if sats:
        suhrn.append(["Til utbetaling i alt", kr(sum_km * sats + sum_bom)])
    ts = Table(suhrn, colWidths=[80*mm, 35*mm])
    ts.setStyle(TableStyle([("FONT", (0, 0), (-1, -1), "DV", 9),
                            ("FONT", (0, -1), (-1, -1), "DVB", 9),
                            ("ALIGN", (1, 0), (1, -1), "RIGHT"),
                            ("LINEABOVE", (0, -1), (-1, -1), 0.6, colors.black)]))
    spolu.append(ts)
    spolu += [Spacer(1, 12*mm),
              Paragraph(f"Dato: ____________________ &nbsp;&nbsp;&nbsp;&nbsp; "
                        f"Signatur sjåfør: ______________________________ &nbsp;&nbsp;&nbsp;&nbsp; "
                        f"Attestert (firma): ______________________________", st["BodyText"]),
              Spacer(1, 3*mm),
              Paragraph(f"Generert {date.today():%d.%m.%Y}. Kjøringen er utført med privat bil "
                        f"i tjeneste for {f['navn']}.", liten)]
    doc.build(hlava + [t] + spolu)
    return sum_km


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    mesiac = sys.argv[1]
    nast, jazdy = nacitaj(mesiac)
    chyby = skontroluj(mesiac, jazdy)
    for c in chyby:
        print("⚠️ ", c)
    print(f"{mesiac}: {len(jazdy)} jázd, {sum(km_jazdy(j) for j in jazdy)} km")
    if "--kontrola" in sys.argv:
        sys.exit(1 if chyby else 0)
    if chyby:
        print("PDF nerobím, kým nie sú dáta v poriadku.")
        sys.exit(1)
    ut = KOREN / "pdf" / f"Kjorebok_{mesiac}.pdf"
    ut.parent.mkdir(parents=True, exist_ok=True)
    lag_pdf(mesiac, nast, jazdy, ut)
    print("✅", ut)


if __name__ == "__main__":
    main()
