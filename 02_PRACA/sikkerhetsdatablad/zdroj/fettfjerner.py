# Norsk innhold for sikkerhetsdatablad Isokor Cleaner – web: Isokor Fett- og flekkfjerner
# SK-originalen (Isokor Univerzál (Cleaner)) er identisk med Baderomsrens (tekst og tabeller); kun navnet er forskjellig.
import baderomsrens

PRODUCT = "Isokor Fett- og flekkfjerner (Cleaner)"
DATE = baderomsrens.DATE
PAGES = [p.replace(baderomsrens.PRODUCT, PRODUCT) for p in baderomsrens.PAGES]
assert sum(PRODUCT in p for p in PAGES) == 1
