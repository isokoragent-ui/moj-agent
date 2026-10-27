# Norsk innhold for sikkerhetsdatablad Isokor Allrens for hjemmet (Cleaner Home)
# SK-originalen (Isokor Univerzál koncentrát) er identisk med Baderomsrens (tekst og tabeller); kun navnet er forskjellig.
import baderomsrens

PRODUCT = "Isokor Allrens for hjemmet (Cleaner Home)"
DATE = baderomsrens.DATE
PAGES = [p.replace(baderomsrens.PRODUCT, PRODUCT) for p in baderomsrens.PAGES]
assert sum(PRODUCT in p for p in PAGES) == 1
