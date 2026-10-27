# Norsk innhold for sikkerhetsdatablad Isokor Sofarens (Sofa Cleaner)
# SK-originalen (Isokor Na tepovanie) er identisk med Baderomsrens (tekst og tabeller); kun navnet er forskjellig.
import baderomsrens

PRODUCT = "Isokor Sofarens (Sofa Cleaner)"
DATE = baderomsrens.DATE
PAGES = [p.replace(baderomsrens.PRODUCT, PRODUCT) for p in baderomsrens.PAGES]
assert sum(PRODUCT in p for p in PAGES) == 1
