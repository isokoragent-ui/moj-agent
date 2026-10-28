# Isokor Bilrens 500 ml (SK: Car Cleaner) — nórske texty etikety. Všetko od výrobcu ostáva, len preklad
# (08_ROZHODNUTIA/2026-10-28_etikety_len_preklad.md). Odznaky: DODÁVA LESK → GIR GLANS, ÚČINNÝ → EFFEKTIV.
from reportlab.lib.colors import CMYKColor

SOURCE = 'original_SK_Car_Cleaner_500ml.pdf'
OUT = 'Isokor_Bilrens_500ml_etikett_NO'

TITLE = ['BILRENS']
CLAIMS = ['Middel for rengjøring', 'og beskyttelse av bil']

BODY = [
    ('ISOKOR® BILRENS',
     'er et miljøvennlig, skånsomt og naturlig rengjøringsmiddel for bilens interiør og eksteriør. Fjerner '
     'enkelt fettete urenheter, støv og insektrester, kvae fra trær på vinduer, lykter og speil, avleiringer '
     'på felger og smuss på seter og dashbord. Den rengjorte overflaten blir helt ren og uten striper. Takket '
     'være den naturlige sammensetningen er produktet helt trygt for trekk og skinn, aluminiumsfelger, stål, '
     'hjulkapsler og dekk. Fjerner svært godt inngrodde flekker på trekk (fra kaffe, juice, melk, urin osv.). '
     'Nøytraliserer ubehagelig lukt og etterlater en langvarig friskhet. Produktet er klart til bruk; vi '
     'fraråder fortynning eller blanding med andre stoffer.'),
    ('Bruksanvisning:',
     'Påfør en liten mengde av produktet på overflaten som skal rengjøres eller på en svamp, og poler deretter '
     'med sirkelbevegelser. Gjenta ved behov.'),
    ('Oppbevaring:',
     'Oppbevares i lukket originalemballasje ved 15–35&nbsp;°C. Må ikke utsettes for direkte sollys. '
     'Beskyttes mot frost. Oppbevares utilgjengelig for barn. Produktet kan endre farge og konsistens ved '
     'temperaturpåvirkning, men dette påvirker ikke egenskapene. Kun tom emballasje kan resirkuleres.'),
    ('Sikkerhetstiltak:',
     'Unngå kontakt med øynene – kan gi lett irritasjon, som ved bruk av såpe. Ved øyekontakt: hold øynene '
     'åpne og skyll straks med rent vann. Ved svelging: ikke fremkall brekninger, men drikk rikelig med væske.'),
    ('Sammensetning:',
     'Kan inneholde noen eller alle av følgende prosesserte ekstrakter og tilsetninger: organisk alkohol '
     '(97-99-4), mandelolje (8007-69-0), appelsinolje (8016-20-4), jojobaolje (61789-91-1), sitronolje '
     '(8007-02-1), soyaolje (8001-22-7), prosessert *glukonsyre (526-95-4), prosesserte *ekstrakter av '
     'sukkerrør (57-50-1), ekstrakt av solsikkeolje (8001-23-8), natron, sederolje (8000-27-9), kanelolje '
     '(8007-80-5), maisolje (8001-30-7), geraniumolje, ammoniumbikarbonat av næringsmiddelkvalitet '
     '(1066-33-7), bearbeidet havsalt (11062-32-1), vann. *lyofilisater eller konsentrater.'),
    ('Inneholder ikke:',
     'glyserol, parabener, silikoner, parafiner, ceresin, fosfater, SLES, SLS, kunstige fargestoffer, '
     'syntetiske dufter (terpener), syntetiske fortykningsmidler (anti-cyanidiner), petrokjemikalier, '
     'stoffer av animalsk opprinnelse, metallforbindelser.'),
]
# Zloženie presne podľa SK etikety Car Cleaner (bez cesnaku a výťažku zo semien, pelargónia bez CAS).

FOOT = [('Holdbarhet:', 'Se emballasjen'), ('Forbruk:', 'ca. 100 ml/m²')]

PRODUCER = {
    'head': 'Importør og distributør',
    'lines': ['Isokor Skandinavia AS', 'Org.nr. 922 112 975', 'Nærestadveien 1, 4985 Vegårshei',
              'Tlf. +47 486 42 178', 'www.isokor-skandinavia.no'],
    'tail': 'PRODUSERT I EU',
}

GREY = CMYKColor(0, 0, 0, 0.8)               # pás a podnadpis
RED = CMYKColor(0.083, 0.997, 0.99, 0.011)   # odznaky
LAYOUT = {
    'regions': {
        'text':      (465, 65, 850, 420),
        'text2':     (465, 400, 700, 436),
        'logo':      (296, 96, 446, 140),
        'nazov':     (100, 185, 440, 250),
        'podnadpis': (280, 268, 437, 310),
        'lesk':      (352, 346, 431, 359.5),   # len text v ovále, hviezdičky a ovál ostávajú
        'ucinny':    (378, 378, 428, 399.5),   # len text, rámik a fajka ostávajú
        'naturlig':  (746, 475, 775, 489),
        'vyrobca':   (476, 500, 650, 560),
    },
    'green': GREY,
    'band': (75.5, 180.6, 449.5, 255.1),
    'claims': (435, (285.5, 307.1), 'Khand-SemiBold', 14),
    'badges': [],
    'texts': [
        ('GIR GLANS', 391.5, 358.4, 'Arial-Bold', 10, RED, 'c'),
        ('EFFEKTIV', 375.5, 396.5, 'Arial-Bold', 9, RED, 'l'),
        ('NATURLIG', 747.5, 481.8, 'Arial-Bold', 3.6, RED, 'l'),
        ('PRODUKT', 747.5, 488.1, 'Arial-Bold', 3.6, RED, 'l'),
    ],
    'body': (480, 833, 78, 400),
    'producer': (533, 509, 7.2, 7.6),
    'icon': (487, 553, 32),
}
