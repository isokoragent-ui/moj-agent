# Norsk innhold for sikkerhetsdatablad Isokor EcoDescal (SK: Odvápňovač / Eco Descal) – web: Isokor EcoDescal avkalker for vannkoker og kaffemaskin
# SK-originalen er identisk med Isokor LMS (tekst og alle tabeller); kun navn og UFI er forskjellige.
import lms

PRODUCT = "Isokor EcoDescal"
DATE = lms.DATE
EXTRA_CSS = lms.EXTRA_CSS
PAGES = [p.replace('<span class="iv">Isokor LMS</span>', '<span class="iv">Isokor EcoDescal</span>')
          .replace("AV10-F0V7-M002-MJ6P", "W120-G081-7002-X7CT") for p in lms.PAGES]
assert sum("W120-G081-7002-X7CT" in p for p in PAGES) == 2 and any("Isokor EcoDescal</span>" in p for p in PAGES)
