# Norsk innhold for sikkerhetsdatablad Isokor Clinic (Cleaner Clinic) – web: Isokor Clinic rengjøring for helse og hygiene
# SK-originalen (Isokor Klinik) er identisk med Baderomsrens (tekst og tabeller); kun navnet er forskjellig.
# Avsnitt 9.2 mangler i originalen – beholdt som «Ingen» (obligatorisk underavsnitt).
import baderomsrens

PRODUCT = "Isokor Clinic (Cleaner Clinic)"
DATE = baderomsrens.DATE
PAGES = [p.replace(baderomsrens.PRODUCT, PRODUCT) for p in baderomsrens.PAGES]
assert sum(PRODUCT in p for p in PAGES) == 1
