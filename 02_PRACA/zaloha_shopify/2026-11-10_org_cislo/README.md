# Záloha pred zmenou org. čísla (2026-11-10)

Pôvodné HTML stránok a pravidiel obchodu pred prepnutím na **922 112 975 MVA**.
Na vrátenie: obsah súboru `page_*.html` vložiť späť do stránky (pageUpdate).

## Čo musí Luk spraviť ručne (agent nemá oprávnenie `write_legal_policies`)
Shopify admin → Nastavenia → Pravidlá (Policies):

**Kontaktné údaje** — nahradiť celé týmto:
```
Handelsnavn: Isokor Skandinavia AS
Telefonnummer: +47 48642178
E-postadresse: info@isokor-skandinavia.no
Fysisk adresse: Nærestadveien 1, 4985 Vegårshei, Norge
Organisasjonsnummer: 922 112 975 MVA
```
(oprava aj „Norsko“ → „Norge“ a „Isokor - skandinavia“ → „Isokor Skandinavia AS“)

**Právne upozornenie** — riadok `Organisasjonsnummer: 922112975` → `Organisasjonsnummer: 922 112 975 MVA`,
`Foretaksnavn: Isokor - Skandinavia AS` → `Foretaksnavn: Isokor Skandinavia AS`.

**Šablóna stránky Kontakt** (Online Store → Prispôsobiť → stránka contact → blok s adresou):
`Org nr.: 922 112 975` → `Org.nr. 922 112 975 MVA`. Živá šablóna je pre agenta zamknutá.
