# Norsk innhold for sikkerhetsdatablad Isokor WhiteWood – (ikke i nettbutikken ennå)
# SK-originalen er identisk med Isokor LMS (tekst og alle tabeller); kun navn og UFI er forskjellige.
import lms

PRODUCT = "Isokor WhiteWood"
DATE = lms.DATE
EXTRA_CSS = lms.EXTRA_CSS
PAGES = [p.replace('<span class="iv">Isokor LMS</span>', '<span class="iv">Isokor WhiteWood</span>')
          .replace("AV10-F0V7-M002-MJ6P", "NY10-Y0JM-W00J-8VSR") for p in lms.PAGES]
assert sum("NY10-Y0JM-W00J-8VSR" in p for p in PAGES) == 2 and any("Isokor WhiteWood</span>" in p for p in PAGES)
