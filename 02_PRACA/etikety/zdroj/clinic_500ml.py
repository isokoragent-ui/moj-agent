# Isokor Clinic 500 ml (SK: Cleaner Clinic) — nórske texty etikety. Všetko od výrobcu ostáva, len preklad
# (08_ROZHODNUTIA/2026-10-28_etikety_len_preklad.md). Web: „Isokor Clinic rengjøring for helse og hygiene“.
from reportlab.lib.colors import CMYKColor

SOURCE = 'original_SK_Cleaner_Clinic_500ml.pdf'
OUT = 'Isokor_Clinic_500ml_etikett_NO'

TITLE = ['CLINIC']
CLAIMS = ['Miljøvennlig', 'Antimikrobielle egenskaper', 'Naturlig', 'Biologisk nedbrytbar']

BODY = [
    ('ISOKOR® CLINIC',
     'er et middel for avfetting og rengjøring av alle overflater, menneskehud og hender. Fjerner effektivt '
     'smuss. Gir overflatene en mild glans og etterlater en behagelig duft. Krever ikke skylling. '
     'Antimikrobielle egenskaper bekreftet ved testing. Naturlig og biologisk nedbrytbart. Trygt for '
     'menneskehud. Dermatologisk testet.'),
    ('BRUK 1:',
     'polert og upolert glass, keramikk, plast, lakkerte overflater, rustfritt stål, krom, tre, tekstiler, '
     'mineralske overflater; ideell til bruk både i hjemmet og i industrien.'),
    ('BRUK 2:', 'menneskehud, hender.'),
    ('Bruksanvisning:',
     'Påfør middelet på overflaten som skal rengjøres, og vent ca. 2–3&nbsp;minutter slik at produktet '
     'reagerer med smusset. Rengjør deretter med svamp eller klut. Du kan, men må ikke, skylle med vann. '
     'Gjenta ved behov.'),
    ('Sikkerhetstiltak:',
     'Unngå kontakt med øynene – kan gi lett irritasjon, som ved bruk av såpe. Ved øyekontakt: hold øynene '
     'åpne og skyll straks med rent vann.'),
    ('Inneholder ikke:',
     'glyserol, parabener, silikoner, ceresin, parafiner, fosfater, SLES, SLS, kunstige fargestoffer, '
     'syntetiske duftstoffer, syntetiske fortykningsmidler, petrokjemiske produkter, stoffer av animalsk '
     'opprinnelse, metallforbindelser, salter og eteriske oljer.'),
    ('Oppbevaring:',
     'Oppbevares ved 5–35&nbsp;°C. Beskyttes mot frost og sollys. Oppbevares utilgjengelig for barn.'),
    ('Sammensetning:',
     'Kan inneholde noen eller alle av følgende prosesserte ekstrakter og bestanddeler: organisk alkohol '
     '(97-99-4), mandelolje (8007-69-0), appelsinolje (8016-20-4), sederolje (8000-27-9), kanelolje '
     '(8007-80-5), maisolje (8001-30-7), geraniumolje (8000-46-2), jojobaolje (61789-91-1), sitrongressolje '
     '(8007-02-1), soyaolje (8001-22-7), prosessert *glukonsyre (526-95-4), prosesserte *ekstrakter av '
     'sukkerrør (57-50-1), ekstrakt av solsikkeolje (8001-23-8), natriumbikarbonat – natron (144-55-8), '
     'ammoniumbikarbonat av næringsmiddelkvalitet (1066-33-7), prosessert *havsalt (11062-32-1), '
     'hvitløksekstrakt (8008-99-9), fruktkjerneekstrakt (68916-04-1), vann. *lyofilisater eller konsentrater. '
     'INNEHOLDER INGEN KJENTE KREFTFREMKALLENDE STOFFER.'),
    ('Farlige stoffer:', 'Ingen.'),
]
# SK „(8001) -23-8“ = preklep → (8001-23-8). „Neobsahuje … éterické oleje“ ponechané ako u výrobcu.

FOOT = [('Holdbarhet:', 'Se emballasjen'), ('Forbruk:', 'ca. 100 ml/m²')]

PRODUCER = {
    'head': 'Importør og distributør',
    'lines': ['Isokor Skandinavia AS', 'Org.nr. 922 112 975', 'Nærestadveien 1, 4985 Vegårshei',
              'Tlf. +47 486 42 178', 'www.isokor-skandinavia.no'],
    'tail': 'PRODUSERT I EU',
}

BLUE = CMYKColor(1, 0.42, 0, 0)              # pás, tvrdenia, 500ml
CYAN = CMYKColor(1, 0.06, 0, 0)              # odznak „naturlig produkt“
LAYOUT = {
    'regions': {
        'text':      (465, 60, 850, 406),
        'text2':     (465, 395, 700, 436),
        'logo':      (296, 96, 446, 140),
        'nazov':     (100, 185, 440, 250),
        'tvrdenia':  (285, 265, 440, 340),
        'test':      (295, 360, 436, 413),
        'naturlig':  (720, 478, 758, 497),
        'vyrobca':   (476, 510, 650, 565),
    },
    'green': BLUE,
    'band': (75.5, 180.6, 449.5, 255.1),
    'claims': (435, (280.8, 298.7, 316.8, 334.6), 'Khand-SemiBold', 12),
    'badges': [],
    'texts': [
        ('Antimikrobielle egenskaper', 433, 375.7, 'Khand-SemiBold', 11, BLUE, 'r'),
        ('testet av SUJCHBO, V.V.I.,', 433, 392.4, 'Khand-SemiBold', 11, BLUE, 'r'),
        ('nr. 56/2015/LTL', 433, 409.1, 'Khand-SemiBold', 11, BLUE, 'r'),
        ('NATURLIG', 723.3, 487.2, 'Arial-Bold', 4.4, CYAN, 'l'),
        ('PRODUKT', 723.3, 495, 'Arial-Bold', 4.4, CYAN, 'l'),
    ],
    'body': (477, 831, 65, 398),
    'producer': (533, 519, 7.2, 7.6),
    'icon': (487, 563, 32),
}
