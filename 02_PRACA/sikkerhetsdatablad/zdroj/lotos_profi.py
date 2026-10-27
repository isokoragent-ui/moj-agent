# Norsk innhold for sikkerhetsdatablad Isokor Lotos Profi – web: Isokor Lotos Profi nanoimpregnering
# SK-originalen følger Isokor SW EKO (avsnitt 5–16), men blandingen er IKKE klassifisert (isopropylalkohol 5–<10 %),
# har EUH210, fargeløs, ingen pH-data og ingen UFI. Sidene som avviker, er skrevet om her.
import sw_eko as eko

PRODUCT = "Isokor Lotos Profi"
DATE = eko.DATE
EXTRA_CSS = eko.EXTRA_CSS
NA, KR = eko.NA, eko.KR
P = list(eko.PAGES)

P[0] = (P[0].replace('<span class="iv">Isokor SW EKO</span>', '<span class="iv">Isokor Lotos Profi</span>')
        .replace('<p class="tight">UFI: 0N20-102T-C00H-KMFA</p>\n', '')
        .replace('<u>I henhold til forordning (EF) nr. 1272/2008 (CLP):</u><br>Eye Irrit. 2; H319',
                 '<u>I henhold til forordning (EF) nr. 1272/2008 (CLP):</u><br>Stoffblandingen er ikke klassifisert som farlig.')
        .replace('<p class="lbl">Helsefare:</p><p class="tight">Gir alvorlig øyeirritasjon.</p>',
                 '<p class="lbl">Helsefare:</p><p class="tight">Ingen.</p>'))

P[1] = """
<h2 class="first">2.2 Merkingselementer</h2>
<p class="lbl b6">Farepiktogrammer:</p><p class="tight">Ingen.</p>
<p class="lbl b6">Varselord:</p><p class="tight">Ingen.</p>
<p class="lbl b6">Faresetninger:</p><p class="tight">Ingen.</p>
<p class="lbl b6">Sikkerhetssetninger:</p><p class="tight">Ingen.</p>
<p class="sp gap"><span class="k6">EUH210:</span> Sikkerhetsdatablad kan fås ved henvendelse.</p>
<h3 class="gap2">2.3 Andre farer</h3>
<p class="sp">Vedlegg XIII til REACH – Kriterier for identifisering av persistente, bioakkumulerende og giftige stoffer (PBT) og svært persistente og svært bioakkumulerende stoffer (vPvB): ikke relevant.</p>
<p class="sp">Stoffer med hormonforstyrrende egenskaper (i henhold til kriteriene i delegert kommisjonsforordning (EU) 2017/2100 og kommisjonsforordning (EU) 2018/605): ikke relevant.</p>
<h1 class="gap2">AVSNITT 3: Sammensetning/opplysninger om bestanddeler</h1>
<h2>3.1 Stoffer</h2><p class="tight">Ikke relevant.</p>
"""

P[2] = P[2].replace('<td>5–10</td>', '<td>5–&lt;10</td>')

P[3] = (P[3].replace('Varsle nødetatene om situasjonen. Ikke delta i håndteringen av hendelsen, og forlat fareområdet. Fjern mulige antennelseskilder.',
                     'Varsle nødetatene om situasjonen. Personer som ikke deltar i håndteringen, skal holdes borte fra fareområdet.'))

P[6] = (P[6].replace('<td>Farge</td><td>Hvit</td>', '<td>Farge</td><td>Fargeløs</td>')
        .replace('<td>pH <i>(gjelder ikke gasser)</i></td><td>6–7</td>', f'<td>pH <i>(gjelder ikke gasser)</i></td><td>{NA}</td>'))

P[8] = P[8].replace('<td>Alvorlig øyeskade/øyeirritasjon</td><td>Gir alvorlig øyeirritasjon.</td>', f'<td>Alvorlig øyeskade/øyeirritasjon</td><td>{KR}</td>')

P[13] = (P[13].replace('''<table class="basis">
<tr><td>Eye Irrit. 2; H319</td><td>På grunnlag av innholdet av bestanddeler (beregningsmetode)</td></tr>
</table>''', '<p class="tight">Stoffblandingen er ikke klassifisert som farlig.</p>')
         .replace('''<p class="tight lh just">Arbeidstakere som håndterer produktet, skal få nødvendig opplæring i farene ved kjemikaliet og sikker bruk, jf. forskrift om utførelse av arbeid. Risikovurdering av kjemisk helsefare på arbeidsplassen skal gjennomføres og dokumenteres, og arbeidstakerne skal gjøres kjent med resultatet.</p>''',
                  '<p class="tight">Ikke nødvendig.</p>')
         .replace('<p class="sp"><b class="k6">UFI: 0N20-102T-C00H-KMFA</b></p>\n', ''))

PAGES = P
_all = "".join(PAGES)
assert "SW EKO" not in _all and "0N20" not in _all and "Hvit" not in _all and "6–7" not in _all
assert "EUH210" in _all and "5–&lt;10" in _all and "Ikke nødvendig." in _all and "Varsle nødetatene om situasjonen. Personer" in _all
assert _all.count("Gir alvorlig øyeirritasjon.") == 1  # kun H319 i avsnitt 16
