# Isokor Antidugg 250/500 ml (SK: Antifog) — nórske texty etikety. Web: „Isokor Antidugg for glass og visir“.
# Klasifikovaný výrobok (Eye Irrit. 2, H319 — bezpečnostná karta Isokor_Antidugg_Sikkerhetsdatablad_NO.pdf):
# na etikete musí byť po nórsky signálne slovo, H a P vety pri piktograme, UFI a dodávateľ s telefónom (CLP čl. 17).
# SK originál signálne slovo ani H/P vety nemá — doplnené z našej bezpečnostnej karty.
from reportlab.lib.colors import CMYKColor

SOURCE = 'original_SK_Antifog_250_500ml.pdf'
OUT = 'Isokor_Antidugg_250_500ml_etikett_NO'

TITLE = ['ANTIDUGG']
CLAIMS = ['Nanobeskyttelse mot dugg', 'glass, bilruter, briller', 'pleksiglass, plast']

BODY = [
    ('Isokor® Antidugg',
     'er et nanopartikkelbasert middel som hindrer dugg på glass, plast og pleksiglass og gir bedre sikt. '
     'Egnet til speil, vinduer, optisk utstyr som briller, bilruter og sidespeil på kjøretøy, overflater på '
     'bad og kjøkken, i treningssentre og badstuer, samt masker til airsoft og paintball og vernebriller.'),
    ('Bruksanvisning:',
     'Rist godt før bruk. Overflaten må rengjøres grundig, avfettes og tørkes før påføring – til avfetting '
     'anbefaler vi Isokor Fett- og flekkfjerner. Spray Isokor Antidugg på den tørre, rene og avfettede '
     'overflaten, 5–15&nbsp;ml per m². Fordel middelet med svært lett trykk med papirhåndkle eller en lite '
     'absorberende klut i sirkelbevegelser, slik at overflaten blir jevnt fuktig. Vent ca.&nbsp;3&nbsp;minutter '
     'og poler deretter med papirhåndkle. Beskytt overflaten mot vann og mekanisk slitasje i minst 1&nbsp;time '
     'etter polering. Etter 2&nbsp;timer er reaksjonen fullført, og effekten kan testes ved å puste på den '
     'behandlede flaten. Gjenta behandlingen 2&nbsp;ganger. Effekten er synlig og varer i 2–6&nbsp;uker. '
     'Gjenta behandlingen når effekten avtar.'),
    ('Førstehjelp:',
     'Ved kontakt med øynene: skyll med rennende vann. Fjern eventuelle kontaktlinser. Ved vedvarende '
     'irritasjon: kontakt lege. Vask hendene grundig etter bruk.'),
    ('Oppbevaring:',
     'Oppbevares i lukket originalemballasje ved 5–35&nbsp;°C. Må ikke utsettes for direkte sollys. '
     'Beskyttes mot frost. Oppbevares utilgjengelig for barn.'),
    ('Sammensetning:', 'vann, etanol, tilsetningsstoffer.'),
]
FOOT = [('Holdbarhet:', 'Se emballasjen')]

# CLP — znenie presne ako oddiel 2.2 bezpečnostnej karty
CLP = [
    ('ADVARSEL', ''),
    ('H319', 'Gir alvorlig øyeirritasjon.'),
    ('P102', 'Oppbevares utilgjengelig for barn.'),
    ('P305+P351+P338', 'VED KONTAKT MED ØYNENE: Skyll forsiktig med vann i flere minutter. Fjern eventuelle '
                       'kontaktlinser dersom dette enkelt lar seg gjøre. Fortsett skyllingen.'),
    ('P501', 'Innhold/beholder leveres i samsvar med nasjonale forskrifter.'),
    ('UFI:', '6W20-J050-9000-JN6H'),
]

PRODUCER = {
    'head': 'Importør og distributør',
    'lines': ['Isokor Skandinavia AS', 'Nærestadveien 1', '4985 Vegårshei',
              'Tlf. +47 486 42 178', 'www.isokor-skandinavia.no'],
    'tail': None,          # malá etiketa: bez org. č. a „Produsert i EU“ (nie sú povinné; adresa by narazila do čiarového kódu)
}

BURGUNDY = CMYKColor(0.09, 1.0, 0.32, 0.43)      # farba pásu a nápisov z originálu
LAYOUT = {
    'regions': {
        'text':      (310, 35, 580, 344),
        'logo':      (180, 40, 305, 80),
        'nazov':     (75, 120, 235, 165),
        'podnadpis': (70, 200, 301, 265),
        'vyrobca':   (318, 445, 462, 510),
    },
    'green': BURGUNDY,
    'band': (0, 107.3, 299.7, 178),
    'claims': (299, (215, 234, 258), ['Khand-Bold', 'Khand-Regular', 'Khand-Regular'], [15, 13, 13]),
    'badges': [],
    'body': (316, 576, 42, 318),
    'clp': (316, 516, 376),
    'producer': (365, 455, 6.3, 6.6),
    'logo': (242, 78, 92),
    'icon': (322, 502, 30),
    'a4_scale': 1.0,
}
