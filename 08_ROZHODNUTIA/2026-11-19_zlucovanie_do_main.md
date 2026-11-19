# Zlučovanie do main bez pýtania (2026-11-19)

**Rozhodol:** Luk, okno Šijacie stroje.
**Čo:** zmeny v tomto repozitári (pamäť agenta, projekty, výstupy) agent
zlučuje do `main` **rovno, bez pýtania** — cez PR z pracovnej vetvy
a hneď merge (cloudové prostredie pushuje na vlastnú vetvu).
**Prečo:** `main` je zdroj pravdy pre ďalšie okná; nezlúčená práca sa
v novom okne nenájde.
**Neplatí pre:** čokoľvek, čo ide von (zverejnenie, e-maily, e-shop, platby)
— tam stále najprv Lukovo „áno“.
