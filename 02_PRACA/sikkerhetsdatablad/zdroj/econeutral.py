# Norsk innhold for sikkerhetsdatablad Isokor EcoNeutral (SK: Proti zápachu / Anti Urine Cleaner) – web: Isokor EcoNeutral lukt- og flekkfjerner
# SK-originalen er identisk med Baderomsrens (tekst og tabeller); kun navnet er forskjellig.
import baderomsrens

PRODUCT = "Isokor EcoNeutral (Anti Urine Cleaner)"
DATE = baderomsrens.DATE
PAGES = [p.replace(baderomsrens.PRODUCT, PRODUCT) for p in baderomsrens.PAGES]
assert sum(PRODUCT in p for p in PAGES) == 1
