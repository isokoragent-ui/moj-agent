#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════
  TILSYNSLOGG — z JSON záznamu návštev spraví PDF pre majiteľa chaty
═══════════════════════════════════════════════════════════════════════
PREČO: majiteľ potrebuje doklad o kontrolách pre poisťovňu. Luk fotí
a odfajkne, papiere robí agent.

POUŽITIE:
    python3 _nastroje/tilsynslogg.py 02_PRACA/hytteservice/logg/H01.json [vystup.pdf]

JSON (jeden súbor = jedna chata):
    {"kode": "H01", "eier": "Ola Nordmann", "hytte": "Vegårshei (H01)",
     "sesong": "2026/27",
     "besok": [{"dato": "2026-11-05", "tid": "10:30", "type": "Vintertilsyn",
                "temp": 8, "funn": "Alt i orden", "tiltak": "-", "bilder": 4}]}
Adresu chaty do JSON nepíš — stačí kód (KÓD #3).
"""
import json, sys
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))


def lag_pdf(data, ut):
    st = getSampleStyleSheet()
    for s in st.byName.values():
        s.fontName = "DV"
    st["Title"].fontName = "DVB"
    liten = st["BodyText"].clone("liten", fontSize=8, leading=10)
    doc = SimpleDocTemplate(str(ut), pagesize=A4, leftMargin=15*mm, rightMargin=15*mm,
                            topMargin=15*mm, bottomMargin=15*mm,
                            title=f"Tilsynslogg {data['kode']}")
    rader = [["Dato", "Kl.", "Type", "Temp. inne", "Funn", "Tiltak", "Bilder"]]
    for b in data.get("besok", []):
        temp = "" if b.get("temp") in (None, "") else f"{b['temp']} °C"
        rader.append([b.get("dato", ""), b.get("tid", ""), b.get("type", ""), temp,
                      Paragraph(b.get("funn", ""), liten), Paragraph(b.get("tiltak", ""), liten),
                      str(b.get("bilder", ""))])
    if len(rader) == 1:
        rader += [[""] * 7 for _ in range(14)]
    t = Table(rader, colWidths=[22*mm, 12*mm, 26*mm, 18*mm, 45*mm, 45*mm, 12*mm], repeatRows=1)
    t.setStyle(TableStyle([
        ("FONT", (0, 0), (-1, -1), "DV", 8),
        ("FONT", (0, 0), (-1, 0), "DVB", 8),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2f5d3a")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f2f5f2")]),
        ("TOPPADDING", (0, 1), (-1, -1), 4),
    ]))
    deler = [
        Paragraph("Tilsynslogg – Isokor Hytteservice", st["Title"]),
        Paragraph(f"<b>Hytte:</b> {data.get('hytte', '')} &nbsp;&nbsp; <b>Eier:</b> {data.get('eier', '')}"
                  f" &nbsp;&nbsp; <b>Sesong:</b> {data.get('sesong', '')}", st["BodyText"]),
        Spacer(1, 4*mm), t, Spacer(1, 6*mm),
        Paragraph("Tilsynet er utført av Isokor Skandinavia AS, org.nr. 922 112 975. Bilder fra hvert besøk "
                  "er sendt til eier og kan fremlegges på forespørsel. Kravene til tilsyn varierer mellom "
                  "forsikringsselskapene – eier er selv ansvarlig for å sjekke vilkårene i sin forsikring.", liten),
    ]
    doc.build(deler)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    inn = Path(sys.argv[1])
    ut = Path(sys.argv[2]) if len(sys.argv) > 2 else inn.with_suffix(".pdf")
    lag_pdf(json.loads(inn.read_text()), ut)
    print(f"✓ {ut}")
