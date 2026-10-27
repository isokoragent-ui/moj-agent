# Norsk innhold for sikkerhetsdatablad Isokor Junior (Baby Cleaner) – produktet finnes ikke i nettbutikken (kun til nedlasting)
# SK-originalen er identisk med Baderomsrens (tekst og tabeller); kun navnet er forskjellig.
import baderomsrens

PRODUCT = "Isokor Junior (Baby Cleaner)"
DATE = baderomsrens.DATE
PAGES = [p.replace(baderomsrens.PRODUCT, PRODUCT) for p in baderomsrens.PAGES]
assert sum(PRODUCT in p for p in PAGES) == 1
