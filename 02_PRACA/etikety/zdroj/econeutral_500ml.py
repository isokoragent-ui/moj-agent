# Isokor EcoNeutral 500 ml (SK: Anti Urine Cleaner) — nórske texty etikety.
# SK originál je iný typ súboru než Cleaner: pozadie je obrázok (150 dpi, RGB), texty sú písmo,
# názov a odznaky „Prírodný produkt“ sú zapečené v obrázku → pretierajú sa (LAYOUT band_fill, masks).
from reportlab.lib.colors import Color

SOURCE = 'original_SK_Anti_Urine_Cleaner_500ml.pdf'
OUT = 'Isokor_EcoNeutral_500ml_etikett_NO'

TITLE = ['ECONEUTRAL']
CLAIMS = ['Lukt- og flekkfjerner', 'mot urin og dyrelukt']   # podnadpis pod pásom
BADGE = ['NATURLIG', 'PRODUKT']
ARC = 'NØYTRALISERER LUKT'                                   # oblúk pod ikonou (SK: NEUTRALIZUJE ZÁPACHY)

BODY = [
    ('ISOKOR® ECONEUTRAL',
     'er et miljøvennlig middel for effektiv fjerning av flekker og lukt etter urin, avføring og oppkast. '
     'Egnet til vask og rens av madrasser, tepper, møbelstoff, barnesenger og gulv, og til vask av '
     'liggeunderlag og små bur for dyr. Produktet er dermatologisk testet. Trygt for mennesker og dyr. '
     'Naturlig og biologisk nedbrytbart. Etterlater en behagelig, frisk duft.'),
    ('Inneholder ikke:',
     'glyserol, parabener, silikoner, parafiner, ceresin, fosfater, SLES, SLS, kunstige fargestoffer, '
     'syntetiske dufter (terpener), syntetiske fortykningsmidler, petrokjemiske stoffer, stoffer av '
     'animalsk opprinnelse, metallforbindelser.'),
    ('Bruksanvisning:',
     'Rist flasken i ca.&nbsp;5&nbsp;sekunder før bruk. Spray slik at hele overflaten dekkes. Tørk av med '
     'en svamp, og tørk deretter med en klut. Produktet trenger ikke skylles av med vann. På tekstiler: '
     'tørk ganske enkelt av med en svamp.'),
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
# SK „syntetické zahusťovadlá (anti-kyanidíny)“ — zátvorka nedáva zmysel (antokyanidíny sú farbivá), vynechaná.
# SK „pelargóniový olej (8000-46-2) (144-55-8)“ — 144-55-8 je CAS sódy bikarbóny → presunuté k natron.

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
}
