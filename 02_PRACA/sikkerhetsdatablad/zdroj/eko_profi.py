# Norsk innhold for sikkerhetsdatablad Isokor Eko Profi – web: Isokor EKO Profi flisimpregnering
# SK-originalen er identisk med Isokor Lotos Profi (ikke klassifisert, ingen UFI, alle tabeller like); kun navnet er forskjellig.
import lotos_profi

PRODUCT = "Isokor Eko Profi"
DATE = lotos_profi.DATE
EXTRA_CSS = lotos_profi.EXTRA_CSS
PAGES = [p.replace("Isokor Lotos Profi", "Isokor Eko Profi") for p in lotos_profi.PAGES]
assert not any("Lotos" in p for p in PAGES) and any("Isokor Eko Profi</span>" in p for p in PAGES)
