# Norsk innhold for sikkerhetsdatablad Isokor Muggfjerner (SK: Na pleseň / Mold Cleaner) – web: Isokor Muggfjerner
# SK-originalen er identisk med Baderomsrens (tekst og tabeller); kun navnet er forskjellig.
import baderomsrens

PRODUCT = "Isokor Muggfjerner (Mold Cleaner)"
DATE = baderomsrens.DATE
PAGES = [p.replace(baderomsrens.PRODUCT, PRODUCT) for p in baderomsrens.PAGES]
assert sum(PRODUCT in p for p in PAGES) == 1
