# Norsk innhold for sikkerhetsdatablad Isokor Gravsteinrens (Grave Cleaner)
# SK-originalen (Isokor Na hroby) er identisk med Baderomsrens (tekst og tabeller); kun navnet er forskjellig.
import baderomsrens

PRODUCT = "Isokor Gravsteinrens (Grave Cleaner)"
DATE = baderomsrens.DATE
PAGES = [p.replace(baderomsrens.PRODUCT, PRODUCT) for p in baderomsrens.PAGES]
assert sum(PRODUCT in p for p in PAGES) == 1
