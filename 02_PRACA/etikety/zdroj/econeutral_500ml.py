# Isokor EcoNeutral 500 ml (SK: Anti Urine Cleaner) — nórske texty etikety; texty a fotky podľa Lukovej NO verzie.
# SK originál je iný typ súboru než Cleaner: pozadie je obrázok (150 dpi, RGB), texty sú písmo,
# názov a odznaky „Prírodný produkt“ sú zapečené v obrázku → pretierajú sa (LAYOUT band_fill, masks).
from reportlab.lib.colors import Color

SOURCE = 'original_SK_Anti_Urine_Cleaner_500ml.pdf'
OUT = 'Isokor_EcoNeutral_500ml_etikett_NO'

TITLE = ['ECONEUTRAL']
CLAIMS = ['Universell lukt-', 'og flekkfjerner']             # podnadpis pod pásom
BADGE = ['NATURLIG', 'PRODUKT']
ARC = 'NØYTRALISERER LUKT'                                   # oblúk pod ikonou (SK: NEUTRALIZUJE ZÁPACHY)

# Obsah podľa Lukovej nórskej verzie (Luk_NO_EcoNeutral_500ml.jpg, 28. 10.) — širšie použitie než SK originál
# (pot, posilňovne, šatne, obuv, auto); jazyk a štruktúra zjednotené s ostatnými etiketami.
BODY = [
    ('ISOKOR® ECONEUTRAL',
     'er et miljøvennlig og effektivt middel for fjerning av flekker og nøytralisering av ubehagelig lukt. '
     'Produktet er spesielt utviklet for å fjerne lukt fra svette, urin, oppkast, ekskrementer og annen '
     'organisk forurensning. Ideell for tekstiler, madrasser, tepper, møbelstoff og sko, samt i '
     'treningssentre, garderober og bilinteriør. Virker utmerket mot lukt fra både mennesker og dyr, '
     'også ved rengjøring av smådyrbur og liggeplasser. Produktet er dermatologisk testet og trygt for '
     'både mennesker og dyr. Naturlig og biologisk nedbrytbart. Etterlater en behagelig, frisk duft.'),
    ('Inneholder ikke:',
     'glyserol, parabener, silikoner, parafiner, ceresin, fosfater, SLES, SLS, kunstige fargestoffer, '
     'syntetiske dufter (terpener), syntetiske fortykningsmidler, petrokjemikalier, stoffer av animalsk '
     'opprinnelse eller metallforbindelser.'),
    ('Bruksanvisning:',
     'Rist flasken i ca.&nbsp;5&nbsp;sekunder før bruk. Spray middelet jevnt over overflaten. Tørk over med '
     'en svamp, og tørk deretter tørt med en klut. Produktet trenger ikke skylles av med vann. Tekstiler: '
     'spray på og tørk ganske enkelt av med en svamp eller klut.'),
    ('Oppbevaring:',
     'Oppbevares i lukket originalemballasje ved 15–35&nbsp;°C. Må ikke utsettes for direkte sollys. '
     'Beskyttes mot frost. Oppbevares utilgjengelig for barn. Produktet kan endre farge og konsistens ved '
     'temperaturpåvirkning, men dette påvirker ikke egenskapene. Kun tom emballasje kan resirkuleres.'),
    ('Sikkerhetstiltak:',
     'Unngå kontakt med øynene – kan gi lett irritasjon, som ved bruk av såpe. Ved øyekontakt: hold '
     'øynene åpne og skyll straks med rent vann. Ved svelging: ikke fremkall brekninger, men drikk '
     'rikelig med væske.'),
    ('Sammensetning:',
     'Kan inneholde noen eller alle av følgende prosesserte ekstrakter og tilsetninger: organisk alkohol '
     '(97-99-4), mandelolje (8007-69-0), appelsinolje (8016-20-4), jojobaolje (61789-91-1), sitronolje '
     '(8007-02-1), soyaolje (8001-22-7), prosessert *glukonsyre (526-95-4), prosesserte *ekstrakter av '
     'sukkerrør (57-50-1), ekstrakt av solsikkeolje (8001-23-8), natron (144-55-8), sederolje (8000-27-9), '
     'kanelolje (8007-80-5), maisolje (8001-30-7), geraniumolje (8000-46-2), hvitløksekstrakt (8008-99-9), '
     'fruktkjerneekstrakt (68916-04-1), ammoniumbikarbonat av næringsmiddelkvalitet (1066-33-7), '
     'bearbeidet havsalt (11062-32-1), vann. *lyofilisater eller konsentrater. Inneholder ingen kjente '
     'kreftfremkallende stoffer.'),
    ('Farlige stoffer:', 'Ingen.'),
]
# Oproti Lukovej verzii: „økologisk“ → „miljøvennlig“ (økologisk = certifikované bio), vynechané „(anti-cyanidiner)“,
# CAS 144-55-8 patrí k natron (v SK aj v Lukovej verzii omylom pri geraniumolje), doplnené Holdbarhet/Forbruk
# a Farlige stoffer (sú v SK origináli).

FOOT = [('Holdbarhet:', 'Se emballasjen'), ('Forbruk:', 'ca. 100 ml/m²')]

PRODUCER = {
    'head': 'Importør og distributør',
    'lines': ['Isokor Skandinavia AS', 'Org.nr. 922 112 975', 'Nærestadveien 1, 4985 Vegårshei',
              'Tlf. +47 486 42 178', 'www.isokor-skandinavia.no'],
    'tail': 'PRODUSERT I EU',
}

GREEN = Color(0.565, 0.784, 0.298)          # zelená nápisov z originálu (RGB)
LAYOUT = {
    'regions': {                            # texty sa mažú podľa počiatku riadku
        'text':     (470, 55, 852, 456),
        'logo':     (290, 95, 446, 140),
        'podnadpis': (280, 270, 456, 320),
        'vyrobca':  (470, 505, 650, 560),
    },
    'masks': [(378, 406, 416, 425), (735, 475, 766, 490),   # SK text v odznakoch (obrázok)
              (478, 503, 522, 540),                     # zvyšok starého loga v pozadí
              (372, 353, 380, 365), (426, 353, 438, 373)],  # konce starého oblúkového nápisu
    'green': GREEN,
    'band': (77.7, 180.7, 447.7, 254.7),
    'band_fill': Color(148 / 255, 200 / 255, 74 / 255),     # pás je v obrázku → pretrieť a napísať znova
    'claims': (450, (287, 310), 'Khand-Bold', 15),
    'badges': [(380, 414, (414.7, 423.3), 6.5), (737, 765, (481.7, 488.8), 4.6)],
    'arc': (403.56, 356.83, 22.6, 150, 9.0),   # kruh zmeraný z pôvodných písmen
    'body': (480, 850, 63, 405),
    'producer': (534, 513),
    'logo': (375, 140, 118),
    'icon': (486, 556, 32),
    # Lukove fotky (sofa, posilňovňa, tenisky, šteňa) z jeho JPG 300 dpi → presne do šesťuholníkov originálu
    'photos': [
        ('Luk_NO_EcoNeutral_500ml.jpg', (69, 345, 207, 464), [(85, 400.5), (118, 343), (184, 343), (217, 400.5), (184, 458), (118, 458)]),
        ('Luk_NO_EcoNeutral_500ml.jpg', (183, 412, 321, 532), [(194, 464.5), (227, 407), (293, 407), (326, 464.5), (293, 522), (227, 522)]),
        ('Luk_NO_EcoNeutral_500ml.jpg', (69, 475, 207, 596), [(85, 526), (118, 469), (184.5, 469), (217, 526), (184, 583), (118, 583)]),
        ('Luk_NO_EcoNeutral_500ml.jpg', (298, 478, 437, 600), [(304, 529), (337, 471), (403, 471), (437, 529), (404, 586), (337, 586)]),
    ],
}
