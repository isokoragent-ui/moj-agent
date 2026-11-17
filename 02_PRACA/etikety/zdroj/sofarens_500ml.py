# Isokor Sofarens 500 ml (SK: Sofa Cleaner) — nórske texty etikety. Všetko od výrobcu ostáva, len preklad
# (08_ROZHODNUTIA/2026-10-28_etikety_len_preklad.md). Odznaky: ÚČINNÝ → EFFEKTIV, NEUTRALIZUJE ZÁPACH →
# NØYTRALISERER LUKT, PRÍRODNÝ PRODUKT → NATURLIG PRODUKT. Rozloženie ako Car Cleaner (vektorový originál).
from reportlab.lib.colors import CMYKColor

SOURCE = 'original_SK_Sofa_Cleaner_500ml.pdf'
OUT = 'Isokor_Sofarens_500ml_etikett_NO'

TITLE = ['SOFARENS']
CLAIMS = ['Middel for rengjøring og dyprens', 'av polstrede møbler']

BODY = [
    ('ISOKOR® SOFARENS',
     'er et naturlig, miljøvennlig middel for dyprens av møbeltrekk, bilseter, setetrekk, tepper og sofaer. '
     'Fjerner effektivt smuss og flekker fra ulike typer tekstiler, slik at setene ser ut som nye. Rengjør '
     'svært godt vanskelige flekker på møbeltrekk (fra kaffe, juice, melk, urin osv.). Nøytraliserer '
     'ubehagelig lukt og etterlater en langvarig friskhet. Produktet er klart til bruk; vi fraråder '
     'fortynning eller blanding med andre stoffer. Isokor Sofarens er biologisk nedbrytbar.'),
    ('Bruksanvisning:',
     'Spray middelet på den tilsmussede overflaten fra ca.&nbsp;15&nbsp;cm avstand og vent 5–7&nbsp;minutter, '
     'slik at middelet kan virke på det tilsmussede tekstilet. Tørk av med en svamp, skyll og tørk med en '
     'klut. Gjenta ved behov.'),
    ('Sikkerhetstiltak:',
     'Unngå kontakt med øynene – kan gi lett irritasjon, som ved bruk av såpe. Ved øyekontakt: hold øynene '
     'åpne og skyll straks med rent vann. Ved svelging: ikke fremkall brekninger, men drikk rikelig med væske. '
     'Oppbevares utilgjengelig for barn. Oppbevares ved 15–35&nbsp;°C. Beskyttes mot frost og sollys.'),
    ('Sammensetning:',
     'Kan inneholde noen eller alle av følgende prosesserte ekstrakter og tilsetninger: organisk alkohol '
     '(97-99-4), mandelolje (8007-69-0), appelsinolje (8016-20-4), sederolje (8000-27-9), kanelolje '
     '(8007-80-5), maisolje (8001-30-7), geraniumolje (8000-46-2), jojobaolje (61789-91-1), sitrongressolje '
     '(8007-02-1), soyaolje (8001-22-7), prosessert *glukonsyre (526-95-4), prosesserte *ekstrakter av '
     'sukkerrør (57-50-1), ekstrakt av solsikkeolje (8001-23-8), natriumhydrogenkarbonat – natron '
     '(144-55-8), ammoniumbikarbonat av næringsmiddelkvalitet (1066-33-7), prosessert *havsalt '
     '(11062-32-1), hvitløksekstrakt (8008-99-9), fruktkjerneekstrakt (68916-04-1), vann. *lyofilisater '
     'eller konsentrater. INNEHOLDER INGEN KJENTE KREFTFREMKALLENDE STOFFER.'),
    ('Farlige stoffer:', 'Ingen.'),
    ('Oppbevaring:',
     'Oppbevares i lukket originalemballasje ved 15–35&nbsp;°C. Må ikke utsettes for direkte sollys. '
     'Beskyttes mot frost. Oppbevares utilgjengelig for barn. Produktet kan endre farge og konsistens ved '
     'temperaturpåvirkning, men dette påvirker ikke egenskapene. Kun tom emballasje kan resirkuleres.'),
]
# Zloženie presne podľa SK etikety Sofa Cleaner (poradie aj CAS; „olej z citrónovej trávy“ = sitrongressolje).

FOOT = [('Holdbarhet:', 'Se emballasjen'), ('Forbruk:', 'ca. 100 ml/m²')]

PRODUCER = {
    'head': 'Importør og distributør',
    'lines': ['Isokor Skandinavia AS', 'Org.nr. 922 112 975', 'Nærestadveien 1, 4985 Vegårshei',
              'Tlf. +47 486 42 178', 'www.isokor-skandinavia.no'],
    'tail': 'PRODUSERT I EU',
}

GREY = CMYKColor(0, 0, 0, 0.9)               # pás, podnadpis, odznaky EFFEKTIV a NØYTRALISERER LUKT
GOLD = CMYKColor(0.25, 0.25, 0.4, 0)         # odznak NATURLIG PRODUKT
LAYOUT = {
    'regions': {
        'text':      (465, 60, 850, 415),      # pod 415 vpravo začína V-label
        'text2':     (465, 400, 700, 450),     # Dátum spotreby, Výdatnosť
        'logo':      (296, 96, 446, 140),
        'nazov':     (100, 185, 440, 250),
        'podnadpis': (185, 265, 440, 312),
        'ucinny':    (385, 334, 426, 351),     # len text, fajka ostáva
        'zapach':    (370, 392, 442, 425),     # len text, para a čiara ostávajú
        'naturlig':  (713, 485, 751, 503),     # len text, kruh a list ostávajú
        'vyrobca':   (476, 516, 660, 580),
    },
    'green': GREY,
    'band': (75.5, 180.6, 449.5, 255.1),
    'claims': (428, (284.3, 305.2), 'Khand-SemiBold', 14),
    'badges': [],
    'texts': [
        ('EFFEKTIV', 405, 349.2, 'Khand-Bold', 8, GREY, 'c', 2.2),
        ('NØYTRALISERER', 405.5, 406.3, 'Khand-Bold', 8.6, GREY, 'c'),
        ('LUKT', 405.5, 422.2, 'Khand-Bold', 8.6, GREY, 'c'),
        ('NATURLIG', 732, 494.3, 'Khand-Bold', 6.6, GOLD, 'c'),
        ('PRODUKT', 732, 501.7, 'Khand-Bold', 6.6, GOLD, 'c'),
    ],
    'body': (472, 836, 66, 425),
    'producer': (533, 524, 6.9, 7.1),
    'icon': (487, 568, 32),
}
