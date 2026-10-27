# Norsk innhold for sikkerhetsdatablad Isokor Bilrens (SK: Na auto / Car Cleaner) – web: Isokor Bilrens
# SK-originalen er identisk med Baderomsrens (tekst og tabeller); kun navnet er forskjellig.
# I SK-originalen mangler overskriften til avsnitt 11 (tabellen står der) – beholdt i norsk versjon.
import baderomsrens

PRODUCT = "Isokor Bilrens (Car Cleaner)"
DATE = baderomsrens.DATE
PAGES = [p.replace(baderomsrens.PRODUCT, PRODUCT) for p in baderomsrens.PAGES]
assert sum(PRODUCT in p for p in PAGES) == 1
