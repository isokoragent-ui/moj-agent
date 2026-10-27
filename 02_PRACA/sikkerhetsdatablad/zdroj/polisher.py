# Norsk innhold for sikkerhetsdatablad Isokor Polisher – web: Isokor Polish for blanke overflater
# SK-originalen er identisk med Isokor SW (sammensetning og alle tabeller); forskjellig: navn, bruksområde og UFI.
import sw_impregnering as sw

PRODUCT = "Isokor Polisher"
DATE = sw.DATE
EXTRA_CSS = sw.EXTRA_CSS
PAGES = [p.replace('<span class="iv">Isokor SW</span>', '<span class="iv">Isokor Polisher</span>')
          .replace("YH30-20YS-E00G-6191", "CX00-W08V-700M-ASSW")
          .replace("Identifisert bruk: vannavstøtende impregnering (beskyttende belegg)", "Identifisert bruk: impregnerings- og rengjøringsmiddel")
          for p in sw.PAGES]
assert sum("CX00-W08V-700M-ASSW" in p for p in PAGES) == 2
assert any("impregnerings- og rengjøringsmiddel" in p for p in PAGES) and any("Isokor Polisher</span>" in p for p in PAGES)
