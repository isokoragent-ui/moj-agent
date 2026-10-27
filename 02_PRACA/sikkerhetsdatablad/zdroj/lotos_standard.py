# Norsk innhold for sikkerhetsdatablad Isokor Lotos Standard – web: Isokor Lotos Standard nanoimpregnering
# SK-originalen er identisk med Isokor SW (sammensetning, bruksområde og alle tabeller); forskjellig: navn og UFI.
import sw_impregnering as sw

PRODUCT = "Isokor Lotos Standard"
DATE = sw.DATE
EXTRA_CSS = sw.EXTRA_CSS
PAGES = [p.replace('<span class="iv">Isokor SW</span>', '<span class="iv">Isokor Lotos Standard</span>')
          .replace("YH30-20YS-E00G-6191", "4K30-K0P5-Q00Y-UCV3") for p in sw.PAGES]
assert sum("4K30-K0P5-Q00Y-UCV3" in p for p in PAGES) == 2 and any("Isokor Lotos Standard</span>" in p for p in PAGES)
