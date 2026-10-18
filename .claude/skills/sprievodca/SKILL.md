---
name: sprievodca
description: Denný sprievodca nastavovaním — povie, kde človek je (deň, míľniky), aký je dnešný jeden krok, a urobí ho s ním. Použi, keď človek napíše /sprievodca, „čo mám dnes spraviť“, „čo ďalej“, „nevidím, kde som“. Argument „ďalej“ preskočí dnešný krok.
argument-hint: "[ďalej]"
---

# /sprievodca — čo je dnes ten jeden krok

Sprievodca **nikdy nedáva zoznam**. Jeden krok, urobený spolu, potom ďalší zajtra.

1. Ak `$ARGUMENTS` je „ďalej“ / „preskoč“: spusti `bash _nastroje/sprievodca.sh preskoc`,
   povedz jednou vetou, čo sa preskočilo, a spusti krok 2.
2. Spusti `bash _nastroje/sprievodca.sh stav` a prečítaj výstup.
3. Odpovedz **presne takto**, nič navyše:
   - jedna veta, kde sme: „Deň N, hotových H z C. Naposledy si spravil: …“
   - jedna veta, čo je dnešný krok a prečo práve ten (čo odomkne)
   - otázka: „Ideme do toho teraz?“
4. Keď povie áno — **urob ten krok s ním hneď**, nie návod naň. Ak to znamená
   spustiť skill (`/nastav`, `/dennik`, `/kontrola`, `/zlepsi`, `/schema`), spusti ho.
   Ak to znamená niečo klikať, veď ho jedným krokom (KÓD #7).
5. Po dokončení znova spusti `bash _nastroje/sprievodca.sh stav` a potvrď, že
   míľnik svieti ✅. Ak nesvieti, povedz prečo (čo ešte chýba) — nehádaj.
6. Zakonči jednou vetou: „Zajtra: …“ (ďalší nesplnený míľnik). Bez zoznamu.

Keď sú všetky míľniky hotové, sprievodca dáva **tipy** — každý deň iný. Aj tie
sa robia hneď, nie plánujú.
