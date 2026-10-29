# Norsk innhold for sikkerhetsdatablad Isokor Universalrens (Cleaner Home) — til 29.10.2026 «Isokor Allrens for hjemmet».
# SK-originalen (Isokor Univerzál koncentrát) er identisk med Baderomsrens (tekst og tabeller); kun navnet er forskjellig.
import baderomsrens

PRODUCT = "Isokor Universalrens (Cleaner Home)"
DATE = "29.10.2026"
VERSION = "1.1"
_REV_OLD = "Norsk versjon 1.0 (27.10.2026) er oversatt"
_REV_NEW = ("Norsk versjon 1.1 (29.10.2026): handelsnavnet er endret fra «Isokor Allrens for hjemmet» til "
            "«Isokor Universalrens»; innholdet er uendret. Norsk versjon 1.0 (27.10.2026) er oversatt")
PAGES = [p.replace(baderomsrens.PRODUCT, PRODUCT).replace(_REV_OLD, _REV_NEW)
         for p in baderomsrens.PAGES]
assert sum(PRODUCT in p for p in PAGES) == 1 and sum(_REV_NEW in p for p in PAGES) == 1
