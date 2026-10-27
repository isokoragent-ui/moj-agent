# Norsk innhold for sikkerhetsdatablad Isokor FVP – web: Isokor FVP (solcellepaneler)
# SK-originalen er identisk med Isokor SW/Polisher (isopropanol, H225/H319/H336, UN 1219; alle tabeller like);
# forskjellig: navn, bruksområde «impregnačný prostriedok» og ingen UFI i originalen.
import sw_impregnering as sw

PRODUCT = "Isokor FVP"
DATE = sw.DATE
EXTRA_CSS = sw.EXTRA_CSS
PAGES = [p.replace('<span class="iv">Isokor SW</span>', '<span class="iv">Isokor FVP</span>')
          .replace('<p class="tight">UFI: YH30-20YS-E00G-6191</p>\n', '')
          .replace('<p class="sp"><b class="k6">UFI: YH30-20YS-E00G-6191</b></p>\n', '')
          .replace("Identifisert bruk: vannavstøtende impregnering (beskyttende belegg)", "Identifisert bruk: impregneringsmiddel")
          for p in sw.PAGES]
assert not any("YH30-20YS-E00G-6191" in p for p in PAGES)
assert any("Identifisert bruk: impregneringsmiddel" in p for p in PAGES) and any("Isokor FVP</span>" in p for p in PAGES)
