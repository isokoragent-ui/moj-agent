# Norsk innhold for sikkerhetsdatablad Isokor SWB – (ikke i nettbutikken)
# SK-originalen er identisk med Isokor SW EKO (tekst og tabeller, H319); kun navn og UFI er forskjellige.
import sw_eko as eko

PRODUCT = "Isokor SWB"
DATE = eko.DATE
EXTRA_CSS = eko.EXTRA_CSS
PAGES = [p.replace('<span class="iv">Isokor SW EKO</span>', '<span class="iv">Isokor SWB</span>')
          .replace("0N20-102T-C00H-KMFA", "HR20-H0S6-P000-7Y1D") for p in eko.PAGES]
assert sum("HR20-H0S6-P000-7Y1D" in p for p in PAGES) == 2 and any("Isokor SWB</span>" in p for p in PAGES)
