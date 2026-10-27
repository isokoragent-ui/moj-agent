# Norsk innhold for sikkerhetsdatablad Isokor Glass Profi – web: Isokor Glass Profi glassimpregnering
# SK-originalen er identisk med Isokor Polisher (= SW-innhold, bruk «impregnerings- og rengjøringsmiddel»); kun navn og UFI er forskjellige.
import polisher

PRODUCT = "Isokor Glass Profi"
DATE = polisher.DATE
EXTRA_CSS = polisher.EXTRA_CSS
PAGES = [p.replace('<span class="iv">Isokor Polisher</span>', '<span class="iv">Isokor Glass Profi</span>')
          .replace("CX00-W08V-700M-ASSW", "V310-W0NN-U00M-NFY1") for p in polisher.PAGES]
assert sum("V310-W0NN-U00M-NFY1" in p for p in PAGES) == 2 and any("Isokor Glass Profi</span>" in p for p in PAGES)
