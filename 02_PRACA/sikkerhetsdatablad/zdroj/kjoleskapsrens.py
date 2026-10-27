# Norsk innhold for sikkerhetsdatablad Isokor Kjøleskapsrens (SK: Fridge Cleaner, eldre mal av 23.09.2021) – web: Isokor Kjøleskapsrens
# SK-originalen er identisk med Furniture Cleaner (= Baderomsrens-innhold); kun navnet er forskjellig.
import mobelrens

PRODUCT = "Isokor Kjøleskapsrens (Fridge Cleaner)"
DATE = mobelrens.DATE
PAGES = [p.replace(mobelrens.PRODUCT, PRODUCT) for p in mobelrens.PAGES]
assert sum(PRODUCT in p for p in PAGES) == 1 and not any("Møbelrens" in p for p in PAGES)
