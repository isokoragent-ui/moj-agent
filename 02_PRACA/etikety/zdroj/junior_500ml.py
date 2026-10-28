# Isokor Junior 500 ml (SK: Baby Cleaner) — nórske texty etikety. Bezpečnostná karta: Isokor_Junior_Sikkerhetsdatablad_NO.pdf.
# Produkt zatiaľ nie je v e-shope (Luk 27. 10.) — názov „Junior“ podľa bezpečnostnej karty.
from reportlab.lib.colors import CMYKColor

SOURCE = 'original_SK_Baby_Cleaner_500ml.pdf'
OUT = 'Isokor_Junior_500ml_etikett_NO'

TITLE = ['JUNIOR']
CLAIMS = ['Rengjøring av leker', 'og barnemøbler']

BODY = [
    ('ISOKOR® JUNIOR',
     'er et naturlig rengjøringsmiddel for leker og andre overflater som barn kommer i kontakt med. '
     'Inneholder ingen kjente farlige eller kreftfremkallende stoffer. Produktet er dermatologisk testet. '
     'Leker og overflater rengjort med Isokor Junior er ikke forurenset med farlige kjemikalier og forblir '
     'rene. Barnet kan derfor trygt leke med dem rett etter bruk. Egnet til: barnemøbler, matstoler, '
     'stellematter, barnesenger, leker, potter, kurver og bokser til leker, flasker, barneservise og bestikk, '
     'rens av barnevogner, bilseter, madrasser, lekematter, tepper, gulv osv.'),
    ('Bruksanvisning:',
     'Rist i ca.&nbsp;5&nbsp;sekunder før bruk. Spray på, tørk av med en svamp og tørk deretter med en klut. '
     'Produktet trenger ikke skylles av med vann. Tekstiler som bilseter, barnevogner og tepper: tørk ganske '
     'enkelt av med en svamp.'),
    ('Sikkerhetstiltak:',
     'Unngå kontakt med øynene – kan gi lett irritasjon, som ved bruk av såpe. Ved øyekontakt: hold øynene '
     'åpne og skyll straks med rent vann. Ved svelging: ikke fremkall brekninger, men drikk rikelig med '
     'væske. Oppbevares utilgjengelig for barn.'),
    ('Sammensetning:',
     'Kan inneholde noen eller alle av følgende ekstrakter og tilsetninger: organisk alkohol (97-99-4), '
     'mandelolje (8007-69-0), appelsinolje (8016-20-4), jojobaolje (61789-91-1), sitronolje (8007-02-1), '
     'soyaolje (8001-22-7), prosessert *glukonsyre (526-95-4), prosesserte *ekstrakter av sukkerrør '
     '(57-50-1), ekstrakt av solsikkeolje (8001-23-8), natron, sederolje (8000-27-9), kanelolje '
     '(8007-80-5), maisolje (8001-30-7), geraniumolje (8000-46-2), hvitløksekstrakt (8008-99-9), '
     'fruktkjerneekstrakt (68916-04-1), ammoniumbikarbonat av næringsmiddelkvalitet (1066-33-7), '
     'bearbeidet havsalt (11062-32-1), vann. *lyofilisater eller konsentrater.'),
    ('Inneholder ikke:',
     'glyserol, parabener, silikoner, parafiner, ceresin, fosfater, SLES, SLS, kunstige fargestoffer, '
     'syntetiske dufter (terpener), syntetiske fortykningsmidler, petrokjemiske stoffer, stoffer av animalsk '
     'opprinnelse, metallforbindelser. Inneholder ingen kjente kreftfremkallende stoffer.'),
    ('Farlige stoffer:', 'Ingen.'),
    ('Oppbevaring:',
     'Oppbevares i lukket originalemballasje ved 15–35&nbsp;°C. Må ikke utsettes for direkte sollys. '
     'Beskyttes mot frost. Produktet kan endre farge og konsistens ved temperaturpåvirkning, men dette '
     'påvirker ikke egenskapene. Kun tom emballasje kan resirkuleres.'),
]
# VYNECHANÉ zo SK: „má vykonané skúšky na antimikrobiálne vlastnosti“ a odznak „ANTIMIKROBIÁLNE VLASTNOSTI“
# — biocídne tvrdenie (528/2012), bez povolenia nesmie byť na etikete (rovnako ako pri Fett- og flekkfjerner).
# Vynechaná aj zátvorka „(anti-kyanidíny)“ (nedáva zmysel), „hygienické a čisté“ → „rene“ (hygiena znie ako dezinfekcia).

FOOT = [('Holdbarhet:', 'Se emballasjen'), ('Forbruk:', 'ca. 100 ml/m²')]

PRODUCER = {
    'head': 'Importør og distributør',
    'lines': ['Isokor Skandinavia AS', 'Org.nr. 922 112 975', 'Nærestadveien 1, 4985 Vegårshei',
              'Tlf. +47 486 42 178', 'www.isokor-skandinavia.no'],
    'tail': 'PRODUSERT I EU',
}

CYAN = CMYKColor(0.516, 0, 0.13, 0)          # podnadpis
PINK = CMYKColor(0, 0.861, 0.47, 0)          # odznak „dermatologisk testet“
TEAL = CMYKColor(0.641, 0, 0.34, 0)          # odznak „naturlig produkt“
LAYOUT = {
    'regions': {
        'text':      (465, 60, 850, 452),
        'text2':     (465, 450, 600, 472),
        'logo':      (296, 96, 446, 140),
        'nazov':     (90, 188, 440, 250),
        'podnadpis': (230, 270, 442, 314),
        'antimikro': (330, 315, 442, 345),   # odznak ANTIMIKROBIÁLNE VLASTNOSTI (ikona aj text) — preč
        'derm':      (377, 357, 416, 373),
        'naturlig':  (659, 476, 691, 495),
        'vyrobca':   (476, 508, 650, 566),
    },
    'green': CYAN,
    'band': (75.5, 180.6, 449.5, 255.1),
    'claims': (439.2, (286.5, 308.5), 'Khand-SemiBold', 15),
    'badges': [],
    'texts': [
        ('DERMATOLOGISK', 396.7, 365, 'Khand-SemiBold', 4.3, PINK, 'c'),
        ('TESTET', 396.7, 371.3, 'Khand-SemiBold', 4.3, PINK, 'c'),
        ('NATURLIG', 661, 485, 'Arial-Bold', 3.8, TEAL, 'l'),
        ('PRODUKT', 661, 493.4, 'Arial-Bold', 3.8, TEAL, 'l'),
    ],
    'body': (480, 833, 67, 440),
    'producer': (533, 516, 7.2, 7.6),
}
