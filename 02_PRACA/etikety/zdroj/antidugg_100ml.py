# Isokor Antidugg 100 ml (SK: Antifog 100 ml) — texty rovnaké ako 250/500 ml, menšia etiketa (124 × 80 mm + spadávka).
from antidugg_250_500ml import TITLE, CLAIMS, BODY, CLP, BURGUNDY

# Malá etiketa: „Holdbarhet“ ide na koniec textu namiesto samostatného riadku (o riadok väčšie písmo)
BODY = BODY + [('Holdbarhet:', 'Se emballasjen.')]
FOOT = []

SOURCE = 'original_SK_Antifog_100ml.pdf'
OUT = 'Isokor_Antidugg_100ml_etikett_NO'

PRODUCER = {
    'head': 'Importør og distributør',
    'lines': ['Isokor Skandinavia AS', 'Nærestadveien 1, 4985 Vegårshei', 'Tlf. +47 486 42 178',
              'www.isokor-skandinavia.no'],
    'tail': None,
}

LAYOUT = {
    'regions': {
        'text':      (290, 70, 575, 242),
        'text2':     (290, 240, 470, 277),       # spodné riadky textu vľavo od ikony 6M
        'logo':      (180, 74, 274, 106),
        'nazov':     (105, 124, 225, 158),
        'podnadpis': (130, 168, 272, 212),
        'vyrobca':   (288, 308, 425, 350),
    },
    'green': BURGUNDY,
    'band': (57.7, 119.7, 270.2, 161.9),
    'title_max': 26,
    'claims': (270, (179.5, 193, 206.5), ['Khand-Bold', 'Khand-Regular', 'Khand-Regular'], [10.5, 9.2, 9.2]),
    'badges': [],
    'body': (293, 505, 76, 240),
    'clp': (293, 468, 283),
    'producer': (333, 316, 5.2, 5.5),
    'logo': (226.5, 103, 74),
    'icon': (295, 347, 26),
    'a4_scale': 1.0,
}
