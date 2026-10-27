# Norsk innhold for sikkerhetsdatablad Isokor LMD (LM Descaling) – web: Isokor Kalkfjerner for bad
# SK-originalen er identisk med Isokor LMS (tekst og alle tabeller); kun navn og UFI er forskjellige.
import lms

PRODUCT = "Isokor LMD (LM Descaling)"
DATE = lms.DATE
EXTRA_CSS = lms.EXTRA_CSS
PAGES = [p.replace('<span class="iv">Isokor LMS</span>', '<span class="iv">Isokor LMD (LM Descaling)</span>')
          .replace("AV10-F0V7-M002-MJ6P", "7S10-Y05U-900K-X6MM") for p in lms.PAGES]
assert sum("7S10-Y05U-900K-X6MM" in p for p in PAGES) == 2 and any("Isokor LMD (LM Descaling)</span>" in p for p in PAGES)
