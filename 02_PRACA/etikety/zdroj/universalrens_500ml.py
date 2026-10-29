# Isokor Universalrens 500 ml (SK: Cleaner Home, koncentrát; do 29. 10. 2026 „Isokor Allrens for hjemmet“ — Luk premenoval) — nórske texty etikety. Všetko od výrobcu
# ostáva, len preklad (08_ROZHODNUTIA/2026-10-28_etikety_len_preklad.md).
from reportlab.lib.colors import CMYKColor

SOURCE = 'original_SK_Cleaner_Home_500ml.pdf'
OUT = 'Isokor_Universalrens_500ml_etikett_NO'

TITLE = ['UNIVERSALRENS']
CLAIMS = ['Miljøvennlig', 'Antimikrobiell', 'Biologisk nedbrytbar']

BODY = [
    ('ISOKOR® UNIVERSALRENS',
     'er et universelt, konsentrert og naturlig rensemiddel som kun består av naturlige stoffer, '
     'planteekstrakter og naturlige oljer. ISOKOR® Universalrens er testet for antimikrobielle '
     'egenskaper og har en sterk antioksidantvirkning ved ORP ned til –150&nbsp;mV.'),
    ('Bruksområde:',
     'ISOKOR® Universalrens er et konsentrert, naturlig rengjørings- og avfettingsmiddel med universell '
     'bruk på gulv, glass, keramikk, plast og metall, til rens av tepper og møbelstoff, i oppvaskmaskin og til '
     'klesvask. Egnet til rengjøring av overflater på kjøkken og bad. Ikke helseskadelig – holder overflatene '
     'på kjøkken og bad alltid hygienisk rene og trygge.'),
    ('Bruksanvisning:',
     'Fortynn ISOKOR® Universalrens i forholdet 1:5 til 1:100 og påfør på overflaten. Fordel middelet '
     'med en myk klut, eller bearbeid med pensel eller børste. La virke i ca.&nbsp;3–5&nbsp;minutter, og skyll '
     'deretter med vann. Brukes ved 15–35&nbsp;°C.'),
    ('Sammensetning:',
     'vann, mandelolje, sederolje, kanelolje, maisolje, geraniumolje, jojobaolje, sitrongressolje, soyaolje, '
     'ekstrakter av sukkerrør, saflorolje, natron, hvitløksekstrakt, organisk alkohol, havsalt, fruktsyrer. '
     'Inneholder ingen kjente farlige eller kreftfremkallende stoffer. Inneholder ikke SLES eller SLS, '
     'kunstige fargestoffer eller duftstoffer.'),
    ('Oppbevaring:',
     'Oppbevares i lukket originalemballasje ved 15–35&nbsp;°C. Må ikke utsettes for direkte sollys. '
     'Beskyttes mot frost. Oppbevares utilgjengelig for barn. Produktet kan endre farge og konsistens ved '
     'temperaturpåvirkning, men dette påvirker ikke egenskapene. Kun tom emballasje kan resirkuleres.'),
    ('Sikkerhetstiltak:',
     'Unngå kontakt med øynene – kan gi lett irritasjon, som ved bruk av såpe. Ved øyekontakt: hold øynene '
     'åpne og skyll straks med rent vann. Ved svelging: ikke fremkall brekninger, men drikk rikelig med '
     'væske. Oppbevares utilgjengelig for barn.'),
]

FOOT = [('Holdbarhet:', 'Se emballasjen'), ('Forbruk:', 'ca. 100 ml/m²')]

PRODUCER = {
    'head': 'Importør og distributør',
    'lines': ['Isokor Skandinavia AS', 'Org.nr. 922 112 975', 'Nærestadveien 1, 4985 Vegårshei',
              'Tlf. +47 486 42 178', 'www.isokor-skandinavia.no'],
    'tail': 'PRODUSERT I EU',
}

GREEN = CMYKColor(0.73, 0.07, 1, 0.34)        # pás, tvrdenia, 500ml
LAYOUT = {
    'regions': {
        'text':      (465, 60, 850, 397),
        'text2':     (465, 378, 700, 432),
        'logo':      (296, 96, 446, 140),
        'nazov':     (100, 185, 440, 250),
        'tvrdenia':  (300, 308, 440, 368),
        'vyrobca':   (476, 500, 650, 560),
    },
    'green': GREEN,
    'band': (75.5, 180.6, 449.5, 255.1),
    'claims': (434, (323, 342, 362), ['Khand-Regular', 'Khand-SemiBold', 'Khand-Regular'], [12.5, 10.5, 12.5]),
    'badges': [],
    'body': (480, 833, 66, 390),
    'producer': (533, 509, 7.2, 7.6),
    'icon': (487, 553, 32),
}
