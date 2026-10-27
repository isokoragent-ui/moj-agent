# Norsk innhold for sikkerhetsdatablad Isokor Antifog (SK: Proti roseniu) – web: Isokor Antidugg for glass og visir
# SK-originalen er identisk med Isokor SW EKO (H319, tabeller); forskjellig: navn, UFI og 6.1 (uten setning om antennelseskilder).
import sw_eko as eko

PRODUCT = "Isokor Antidugg (Antifog)"
DATE = eko.DATE
EXTRA_CSS = eko.EXTRA_CSS
PAGES = [p.replace('<span class="iv">Isokor SW EKO</span>', '<span class="iv">Isokor Antidugg (Antifog)</span>')
          .replace("0N20-102T-C00H-KMFA", "6W20-J050-9000-JN6H")
          .replace("Varsle nødetatene om situasjonen. Ikke delta i håndteringen av hendelsen, og forlat fareområdet. Fjern mulige antennelseskilder.",
                   "Varsle nødetatene om situasjonen. Personer som ikke deltar i håndteringen av hendelsen, skal holdes borte fra fareområdet.")
          for p in eko.PAGES]
_all = "".join(PAGES)
assert _all.count("6W20-J050-9000-JN6H") == 2 and "Isokor Antidugg (Antifog)</span>" in _all
assert "antennelseskilder" not in _all.split("6.2 Miljømessige")[0].split("6.1 Personlige")[1]
