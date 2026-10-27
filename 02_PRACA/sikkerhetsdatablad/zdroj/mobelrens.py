# Norsk innhold for sikkerhetsdatablad Isokor Møbelrens (SK: Furniture Cleaner, eldre mal av 23.09.2021) – web: Isokor Møbelrens
# Innholdet i SK-originalen tilsvarer Baderomsrens (ikke klassifisert, ingen farlige bestanddeler, samme fysiske data).
# Rettet: manglende 1.1 Produktidentifikator lagt til, dobbel overskrift 4.3 og tekstrest i toppteksten fjernet.
import baderomsrens

PRODUCT = "Isokor Møbelrens (Furniture Cleaner)"
DATE = baderomsrens.DATE
OLD = "slovakisk sikkerhetsdatablad, versjon 1.0 av 15.01.2026. Endret i forhold til originalen: leverandøropplysninger (1.3), nødtelefonnummer (1.4) og nasjonalt regelverk (avsnitt 8, 13 og 15)."
NEW = "slovakisk sikkerhetsdatablad, versjon 1.0 av 23.09.2021. Endret i forhold til originalen: leverandøropplysninger (1.3), nødtelefonnummer (1.4) og nasjonalt regelverk (avsnitt 8, 13 og 15). Manglende produktidentifikator (1.1) er lagt til, og en dobbel overskrift (4.3) er fjernet."
PAGES = [p.replace(baderomsrens.PRODUCT, PRODUCT).replace(OLD, NEW) for p in baderomsrens.PAGES]
assert sum(PRODUCT in p for p in PAGES) == 1 and sum(NEW in p for p in PAGES) == 1
