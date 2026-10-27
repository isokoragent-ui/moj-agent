# Norsk innhold for sikkerhetsdatablad Isokor Fasaderens (SK: Facade Eko / Facade) – web: Isokor Fasaderens
# SK-originalen er identisk med Baderomsrens (tekst og tabeller); kun navnet er forskjellig.
import baderomsrens

PRODUCT = "Isokor Fasaderens (Facade Eko)"
DATE = baderomsrens.DATE
PAGES = [p.replace(baderomsrens.PRODUCT, PRODUCT) for p in baderomsrens.PAGES]
assert sum(PRODUCT in p for p in PAGES) == 1
