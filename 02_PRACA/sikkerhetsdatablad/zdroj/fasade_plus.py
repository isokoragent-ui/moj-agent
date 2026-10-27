# Norsk innhold for sikkerhetsdatablad Isokor Facade Plus – web: Isokor Fasaderens Plus
# Eget innhold (SK versjon 2.0 av 26.09.2026, ny mal): Met. Corr. 1; H290, Skin Corr. 1A; H314, Eye Dam. 1; H318 –
# natriumhydroksid, kaliumhydroksid, natriummetasilikat, anionisk tensid, propan-1,2-diol. UN 3266, kl. 8, emb.gr. II.
# Rettet i forhold til SK-originalen: førstehjelp ved hudkontakt tilpasset H314; polske grenseverdier erstattet med norske
# (8.1) – verdiene for NaOH/KOH må verifiseres mot vedlegg 1 (Lovdata blokkert fra skyen); propan-1,2-diol ikke tatt med i 8.1.
import lms

PRODUCT = "Isokor Facade Plus"
DATE = lms.DATE
NA = "Ingen data tilgjengelig"
KR = lms.KR
LAB = lms.LAB
EXTRA_CSS = lms.EXTRA_CSS + """
table.tr td{font-size:8pt}
"""
UFI = "YX90-10RJ-E00V-TKR5"

PAGES = [
# ---------- 1 ----------
f"""
<h1>AVSNITT 1: Identifikasjon av stoffet/stoffblandingen og av selskapet/foretaket</h1>
<h3 class="inline">1.1 Produktidentifikator</h3><span class="iv">Isokor Facade Plus</span>
<p class="tight">UFI: {UFI}</p>
<h3>1.2 Relevante identifiserte bruksområder for stoffet eller stoffblandingen og bruk som frarådes</h3>
<p class="sp">Identifisert bruk: alkalisk rengjøringsmiddel</p>
<p class="tight">Bruk som frarådes: ikke spesifisert</p>
<h2>1.3 Opplysninger om leverandøren av sikkerhetsdatabladet</h2>
<p class="tight">Isokor Skandinavia AS<br>
Org.nr.: 922 112 975<br>
Nærestadveien 1, 4985 Vegårshei, Norge<br>
Tlf.: +47 486 42 178<br>
Nettside: www.isokor-skandinavia.no<br>
E-post: info@isokor-skandinavia.no</p>
<p class="tight small">Produsent: Rodinná firma, s.r.o., Okružná 236, 022 04 Čadca, Slovakia</p>
<h2>1.4 Nødtelefonnummer</h2>
<p class="tight">113 (medisinsk nødtelefon)<br>
Giftinformasjonen (Helsedirektoratet): <b>22 59 13 00</b> – døgnåpen rådgivning ved akutte forgiftninger</p>
<h1>AVSNITT 2: Fareidentifikasjon</h1>
<h3>2.1 Klassifisering av stoffet eller stoffblandingen</h3>
<p class="tight"><u>I henhold til forordning (EF) nr. 1272/2008 (CLP):</u></p>
<p class="sp">Met. Corr. 1; H290</p>
<p class="sp">Skin Corr. 1A; H314</p>
<p class="sp">Eye Dam. 1; H318</p>
<p class="lbl">Helsefare:</p><p class="tight">Gir alvorlige etseskader på hud og øyne. Gir alvorlig øyeskade.</p>
<p class="lbl">Miljøfare:</p><p class="tight">Ingen.</p>
<p class="lbl">Fysiske/kjemiske farer:</p><p class="tight">Kan være etsende for metaller.</p>
""",
# ---------- 2 ----------
"""
<h2 class="first">2.2 Merkingselementer</h2>
<p class="sp"><b class="k6">Inneholder:</b> natriumhydroksid, kaliumhydroksid, natriummetasilikat</p>
<p class="lbl b6 gap">Farepiktogrammer:</p>
<p class="pict"><img src="ghs05.svg"></p>
<p class="sp"><span class="k6">Varselord:</span> <b>Fare</b></p>
<p class="lbl b6 gap">Faresetninger:</p>
<p class="tight">H290 – Kan være etsende for metaller.<br>
H314 – Gir alvorlige etseskader på hud og øyne.</p>
<p class="lbl b6 gap">Sikkerhetssetninger:</p>
<p class="sp">P102 – Oppbevares utilgjengelig for barn.</p>
<p class="sp">P280 – Benytt vernehansker/verneklær/vernebriller/ansiktsskjerm.</p>
<p class="sp">P301+P330+P331 – <i>VED SVELGING:</i> Skyll munnen. IKKE framkall brekninger.</p>
<p class="sp lh">P303+P361+P353 – <i>VED HUDKONTAKT (eller håret):</i> Tilsølte klær må fjernes straks. Skyll huden med vann [eller dusj].</p>
<p class="sp lh">P305+P351+P338 – <i>VED KONTAKT MED ØYNENE:</i> Skyll forsiktig med vann i flere minutter. Fjern eventuelle kontaktlinser dersom dette enkelt lar seg gjøre. Fortsett skyllingen.</p>
<p class="sp">P310 – Kontakt umiddelbart et GIFTINFORMASJONSSENTER/lege.</p>
<p class="sp">P501 – Innhold/beholder leveres til egnede, merkede avfallsbeholdere i samsvar med nasjonale forskrifter.</p>
<p class="sp"><u>I henhold til forordning (EF) nr. 648/2004:</u> Inneholder: &lt; 5 % anioniske overflateaktive stoffer.</p>
<h3 class="gap2">2.3 Andre farer</h3>
<p class="sp">Vedlegg XIII til REACH – Kriterier for identifisering av persistente, bioakkumulerende og giftige stoffer (PBT) og svært persistente og svært bioakkumulerende stoffer (vPvB): stoffblandingen inneholder ingen stoffer som oppfyller PBT- eller vPvB-kriteriene.</p>
<p class="sp">Stoffer med hormonforstyrrende egenskaper (i henhold til kriteriene i delegert kommisjonsforordning (EU) 2017/2100 og kommisjonsforordning (EU) 2018/605): stoffblandingen inneholder ingen stoffer med hormonforstyrrende egenskaper.</p>
""",
# ---------- 3 ----------
"""
<h1 class="first">AVSNITT 3: Sammensetning/opplysninger om bestanddeler</h1>
<h2>3.1 Stoffer</h2><p class="tight">Ikke relevant.</p>
<h2>3.2 Stoffblandinger</h2><p class="tight">Farlige bestanddeler:</p>
<table class="comp" style="width:154mm">
<tr><th style="width:34%">Produktidentifikator</th><th>Innhold [%]</th><th>Fareklasse og -kategori</th><th>Faresetninger</th><th style="width:28%">Spesifikke konsentrasjonsgrenser, M-faktor, estimert akutt giftighet (ATE)</th></tr>
<tr><td>Alkoholer, C10–16, etoksylerte, sulfonerte, natriumsalter<br>CAS-nr.: 68585-34-2 · EF-nr.: 500-223-8<br>Indeksnr.: –<br>REACH-reg.nr.: –</td><td>1–&lt;5</td><td>Skin Irrit. 2<br>Eye Irrit. 2</td><td>H315<br>H319</td><td>–</td></tr>
<tr><td>Propan-1,2-diol*<br>CAS-nr.: 57-55-6 · EF-nr.: 200-338-0<br>Indeksnr.: –<br>REACH-reg.nr.: 01-2119456809-23-XXXX</td><td>1–&lt;5</td><td>–</td><td>–</td><td>–</td></tr>
<tr><td>Natriumhydroksid*<br>CAS-nr.: 1310-73-2 · EF-nr.: 215-185-5<br>Indeksnr.: 011-002-00-6<br>REACH-reg.nr.: 01-2119457892-27-XXXX</td><td>1–&lt;5</td><td>Met. Corr. 1<br>Skin Corr. 1A<br>Eye Dam. 1</td><td>H290<br>H314<br>H318</td><td>Skin Corr. 1A; H314: C ≥ 5 %<br>Skin Corr. 1B; H314: 2 % ≤ C &lt; 5 %<br>Skin Irrit. 2; H315: 0,5 % ≤ C &lt; 2 %<br>Eye Irrit. 2; H319: 0,5 % ≤ C &lt; 2 %</td></tr>
<tr><td>Kaliumhydroksid*<br>CAS-nr.: 1310-58-3 · EF-nr.: 215-181-3<br>Indeksnr.: 019-002-00-8<br>REACH-reg.nr.: 01-2119487136-33-XXXX</td><td>1–&lt;5</td><td>Met. Corr. 1<br>Acute Tox. 4<br>Skin Corr. 1A<br>Eye Dam. 1</td><td>H290<br>H302<br>H314<br>H318</td><td>Skin Corr. 1A; H314: C ≥ 5 %<br>Skin Corr. 1B; H314: 2 % ≤ C &lt; 5 %<br>Skin Irrit. 2; H315: 0,5 % ≤ C &lt; 2 %<br>Eye Irrit. 2; H319: 0,5 % ≤ C &lt; 2 %</td></tr>
<tr><td>Natriummetasilikat<br>CAS-nr.: 6834-92-0 · EF-nr.: 229-912-9<br>Indeksnr.: 014-010-00-8<br>REACH-reg.nr.: 01-2119449811-37-XXXX</td><td>1–&lt;5</td><td>Skin Corr. 1B<br>STOT SE 3</td><td>H314<br>H335</td><td>–</td></tr>
</table>
<p class="sp">Fullstendig ordlyd av H-setningene: se avsnitt 16.</p>
<p class="tight">* stoff med fastsatt grenseverdi for eksponering på arbeidsplassen i SK-originalen (se avsnitt 8)</p>
""",
# ---------- 4 ----------
"""
<h1 class="first">AVSNITT 4: Førstehjelpstiltak</h1>
<h3>4.1 Beskrivelse av førstehjelpstiltak</h3>
<h3>Hudkontakt:</h3>
<p class="tight">Fjern tilsølte klær straks. Skyll huden straks med rikelig vann (eventuelt dusj). Ved etseskader eller vedvarende irritasjon: Kontakt lege.</p>
<h3>Øyekontakt:</h3>
<p class="tight">Skyll øynene i ca. 15 minutter med rikelig vann, hold øyelokkene godt åpne. Unngå kraftig vannstråle på grunn av fare for skade på hornhinnen. Kontakt lege umiddelbart.</p>
<h3>Innånding:</h3>
<p class="tight">Flytt personen ut i frisk luft. Kontakt lege dersom tilstanden ikke raskt bedres.</p>
<h3>Svelging:</h3>
<p class="tight">IKKE framkall brekninger. Kontakt umiddelbart lege eller Giftinformasjonen (22 59 13 00).</p>
<h3 class="gap">4.2 De viktigste symptomene og virkningene, både akutte og forsinkede</h3>
<p class="tight lh"><i>Innånding:</i> kan gi sterk irritasjon av de øvre luftveiene, tørrhoste, pustevansker, hodepine og svimmelhet.<br>
<i>Hudkontakt:</i> kjemiske etseskader, rødhet, smerte.<br>
<i>Øyekontakt:</i> smerte, tåkesyn, kraftig tåreflod, fare for alvorlig øyeskade.<br>
<i>Svelging:</i> etseskader i spiserør, svelg og andre deler av fordøyelseskanalen, fare for perforasjon og blødning.</p>
<h3 class="gap">4.3 Angivelse av behov for øyeblikkelig legehjelp og spesialbehandling</h3>
<p class="tight">Behandling avgjøres av lege etter vurdering av den skadedes tilstand.</p>
<h1>AVSNITT 5: Brannslokkingstiltak</h1>
<h3>5.1 Slokkingsmidler</h3>
<p class="sp"><span class="k">Egnede slokkingsmidler:</span> skum, slokkepulver, karbondioksid, vanntåke. Bruk slokkingsmetoder som er tilpasset forholdene i omgivelsene.</p>
<p class="sp"><span class="k">Uegnede slokkingsmidler:</span> Kraftig vannstråle.</p>
<h3>5.2 Særlige farer knyttet til stoffet eller stoffblandingen</h3>
<p class="tight">Ved brann frigjøres giftige nedbrytningsprodukter (karbonoksider og svoveloksider).</p>
<h3>5.3 Råd til brannmannskaper</h3>
<p class="sp lh">Beholdere i brannområdet kjøles med vannspray og fjernes om mulig fra faresonen. Hindre at slokkevann kommer ut i overflatevann, grunnvann eller avløp.<br>
Ved brann i lukkede rom: Bruk verneklær og selvforsynt pusteapparat (trykkluftapparat).</p>
""",
# ---------- 5 ----------
"""
<h1 class="first">AVSNITT 6: Tiltak ved utilsiktede utslipp</h1>
<h3>6.1 Personlige forholdsregler, verneutstyr og nødprosedyrer</h3>
<p class="tight lh"><i>For personell som ikke er nødpersonell:</i> Varsle nødetatene. Personer som ikke deltar i håndteringen, skal holdes borte fra fareområdet. Unngå kontakt med utsølt produkt.</p>
<p class="tight lh"><i>For nødpersonell:</i> Sørg for tilstrekkelig ventilasjon. Bruk personlig verneutstyr (se avsnitt 8).</p>
<h3>6.2 Miljømessige forholdsregler</h3>
<p class="tight">Hindre spredning og at produktet kommer ut i avløp og vassdrag. Dersom dette ikke kan hindres, varsle lokale myndigheter.</p>
<h3>6.3 Metoder og materialer for oppsamling og rengjøring</h3>
<p class="tight lh">Hindre spredning og samle opp med ikke-brennbart absorberende materiale (sand, sagflis, universalabsorbent).<br>
Forurenset materiale legges i egnede, merkede beholdere for avfallsbehandling i samsvar med gjeldende regelverk.</p>
<h3>6.4 Henvisning til andre avsnitt</h3>
<p class="tight">Disponering av avfall fra produktet: se avsnitt 13.<br>
Personlig verneutstyr: se avsnitt 8.</p>
<h1>AVSNITT 7: Håndtering og lagring</h1>
<h3>7.1 Forholdsregler for sikker håndtering</h3>
<p class="tight lh">Sørg for tilstrekkelig ventilasjon.<br>
Unngå kontakt med øynene. Unngå langvarig eller gjentatt kontakt med huden. Unngå innånding av damp fra produktet. Bruk personlig verneutstyr (se avsnitt 8).<br>
Følg gjeldende regler for sikkerhet og hygiene: ikke spis, drikk eller røyk i arbeidsområdet, vask hendene etter bruk, og fjern tilsølte klær og verneutstyr før du går inn i spiseområder.</p>
<h3>7.2 Vilkår for sikker lagring, herunder eventuelle uforenligheter</h3>
<p class="tight lh">Oppbevares kjølig, tørt og godt ventilert i tett lukket, korrekt merket originalemballasje.<br>
Unngå kontakt med uforenlige materialer (se avsnitt 10).</p>
<h3>7.3 Særlig(e) sluttbruk(er)</h3>
<p class="tight">Bruk som angitt i avsnitt 1.2 – ingen ytterligere anbefalinger.</p>
""",
# ---------- 6 ----------
"""
<h1 class="first">AVSNITT 8: Eksponeringskontroll/personlig verneutstyr</h1>
<h3>8.1 Kontrollparametere</h3>
<p class="sp just lh">Grenseverdier for forurensning i arbeidsatmosfæren i henhold til forskrift om tiltaks- og grenseverdier (FOR-2011-12-06-1358), vedlegg 1, med senere endringer.</p>
<p class="sp">Bestanddeler med grenseverdier for eksponering:</p>
<table class="oel">
<tr><th>Kjemisk navn og CAS-nr.</th><th>Grenseverdi (ppm)</th><th>Grenseverdi (mg/m³)</th><th>Anm.</th></tr>
<tr><td>Natriumhydroksid (CAS: 1310-73-2)</td><td>–</td><td>2</td><td>T</td></tr>
<tr><td>Kaliumhydroksid (CAS: 1310-58-3)</td><td>–</td><td>2</td><td>T</td></tr>
</table>
<p class="sp small">T = takverdi (verdi som ikke skal overskrides).</p>
<p class="lbl gap">DNEL- og PNEC-verdier for bestanddeler:</p>
<div class="cols">
<div><p class="tight"><u>Propan-1,2-diol</u><br>DNEL arbeidstaker, innånding, langtidseksponering, systemiske virkninger: 168 mg/m³<br>DNEL arbeidstaker, innånding, langtidseksponering, lokale virkninger: 10 mg/m³<br>DNEL forbruker, innånding, langtidseksponering, systemiske virkninger: 50 mg/m³<br>DNEL forbruker, innånding, langtidseksponering, lokale virkninger: 10 mg/m³<br>DNEL forbruker, hud, langtidseksponering, systemiske virkninger: 213 mg/kg<br>DNEL forbruker, oralt, langtidseksponering, systemiske virkninger: 85 mg/kg</p></div>
<div><p class="tight"><u>Propan-1,2-diol</u><br>PNEC ferskvann: 260 mg/l<br>PNEC sjøvann: 26 mg/l<br>PNEC ferskvannssediment: 572 mg/kg<br>PNEC sjøvannssediment: 57,2 mg/kg<br>PNEC sporadisk utslipp: 183 mg/l<br>PNEC renseanlegg: 20 000 mg/l<br>PNEC jord: 50 mg/kg</p></div>
</div>
<h3 class="gap">8.2 Eksponeringskontroll</h3>
<p class="lbl">Egnede tekniske kontrolltiltak:</p>
<p class="tight lh">Følg generelle regler for sikkerhet og hygiene ved arbeid med kjemikalier.<br>
Unngå kontakt med øynene.<br>
Vask hendene i pauser og etter håndtering av produktet.<br>
Ikke spis, drikk eller røyk ved håndtering av produktet.<br>
Fjern tilsølte klær og vask dem før de brukes igjen.<br>
Sørg for lett tilgang til nøddusj og øyeskylleutstyr.</p>
""",
# ---------- 7 ----------
"""
<p class="lbl first">Individuelle vernetiltak, som personlig verneutstyr:</p>
<p class="tight">Personlig verneutstyr velges ut fra farene på arbeidsplassen, i samsvar med forordning (EU) 2016/425 og relevante CEN-standarder.</p>
<p class="lbl">Øye-/ansiktsvern:</p>
<p class="tight">Bruk tettsittende vernebriller eller ansiktsskjerm (EN ISO 16321-1).</p>
<p class="lbl">Hudvern:</p><p class="tight it">Håndvern:</p>
<p class="tight">Bruk kjemikaliebestandige vernehansker i henhold til EN ISO 374.<br>
Anbefalt materiale: butylgummi · Tykkelse: 0,7 mm · Gjennombruddstid: 480 min.</p>
<p class="lbl">Hanskemateriale:</p>
<p class="tight lh">Valg av riktige hansker avhenger ikke bare av materialet, men også av merke og kvalitet, som varierer mellom produsentene. Hanskematerialets motstandsevne kan fastslås ved testing. Nøyaktig gjennombruddstid må oppgis av hanskeprodusenten.</p>
<p class="lbl">Annet:</p><p class="tight">Bruk arbeidsklær og vask dem regelmessig.</p>
<p class="lbl">Åndedrettsvern:</p><p class="tight">Ved utilstrekkelig ventilasjon: Bruk åndedrettsvern – maske med filter mot damp.</p>
<p class="lbl">Termiske farer:</p><p class="tight">Ikke relevant.</p>
<p class="lbl">Begrensning og overvåking av miljøeksponering:</p><p class="tight">Hindre spredning i miljøet og at produktet kommer ut i avløp eller vassdrag.</p>
""",
# ---------- 8 ----------
f"""
<h1 class="first">AVSNITT 9: Fysiske og kjemiske egenskaper</h1>
<h3 class="gap">9.1 Opplysninger om grunnleggende fysiske og kjemiske egenskaper</h3>
<table class="props">
<tr><td>Aggregattilstand</td><td>Væske</td></tr>
<tr><td>Farge</td><td>Fargeløs</td></tr>
<tr><td>Lukt</td><td>Karakteristisk</td></tr>
<tr><td>Smeltepunkt/frysepunkt<br><i>(gjelder ikke gasser)</i></td><td>{NA}</td></tr>
<tr><td>Kokepunkt eller startkokepunkt og kokepunktintervall</td><td>{NA}</td></tr>
<tr><td>Antennelighet <i>(gjelder gasser, væsker og faste stoffer)</i></td><td>Produktet er ikke brannfarlig</td></tr>
<tr><td>Nedre og øvre eksplosjonsgrense <i>(gjelder ikke faste stoffer)</i></td><td>{NA}</td></tr>
<tr><td>Flammepunkt <i>(gjelder ikke gasser, aerosoler og faste stoffer)</i></td><td>{NA}</td></tr>
<tr><td>Selvantennelsestemperatur <i>(gjelder kun gasser og væsker)</i></td><td>{NA}</td></tr>
<tr><td>Spaltningstemperatur <i>(gjelder kun selvreaktive stoffer og stoffblandinger, organiske peroksider og andre stoffer og stoffblandinger som kan spaltes)</i></td><td>Ikke relevant</td></tr>
<tr><td>pH <i>(gjelder ikke gasser)</i></td><td>13–14</td></tr>
<tr><td>Kinematisk viskositet <i>(gjelder kun væsker)</i></td><td>{NA}</td></tr>
<tr><td>Løselighet</td><td>Løselig i vann</td></tr>
<tr><td>Fordelingskoeffisient n-oktanol/vann (log-verdi)</td><td>Ikke relevant – stoffblanding</td></tr>
<tr><td>Damptrykk</td><td>{NA}</td></tr>
<tr><td>Tetthet og/eller relativ tetthet <i>(gjelder kun væsker og faste stoffer)</i></td><td>{NA}</td></tr>
<tr><td>Relativ damptetthet <i>(gjelder kun gasser og væsker)</i></td><td>{NA}</td></tr>
<tr><td>Partikkelegenskaper <i>(gjelder kun faste stoffer)</i></td><td>Ikke relevant</td></tr>
</table>
<h3 class="gap">9.2 Andre opplysninger</h3>
<p class="tight">Ingen.</p>
""",
# ---------- 9 ----------
"""
<h1 class="first">AVSNITT 10: Stabilitet og reaktivitet</h1>
<h3>10.1 Reaktivitet</h3><p class="tight">Produktet inneholder natriumhydroksid og kaliumhydroksid, sterkt reaktive stoffer som er etsende for metaller.</p>
<h3 class="gap">10.2 Kjemisk stabilitet</h3><p class="tight">Produktet er stabilt under normale forhold for bruk, lagring og transport.</p>
<h3 class="gap">10.3 Mulighet for farlige reaksjoner</h3><p class="tight">Ved kontakt med syrer kan det oppstå eksoterme reaksjoner.</p>
<h3 class="gap">10.4 Forhold som skal unngås</h3><p class="tight">Oppvarming, direkte sollys.</p>
<h3 class="gap">10.5 Uforenlige materialer</h3><p class="tight">Lettmetaller (aluminium, sink, nikkel, kobber og kobberlegeringer), syrer, oksidasjonsmidler, organiske materialer.</p>
<h3 class="gap">10.6 Farlige nedbrytningsprodukter</h3><p class="tight">Produktet brytes ikke ned ved anbefalte forhold for bruk og lagring. Termiske nedbrytningsprodukter: se avsnitt 5.</p>
""",
# ---------- 10 ----------
f"""
<h1 class="first">AVSNITT 11: Toksikologiske opplysninger</h1>
<h3 class="gap">11.1 Opplysninger om fareklasser som definert i forordning (EF) nr. 1272/2008</h3>
<table class="tox" style="margin-top:3mm">
<tr><td>Akutt giftighet</td><td>{KR}</td></tr>
<tr><td>Hudetsing/hudirritasjon</td><td>Gir alvorlige etseskader på hud og øyne.</td></tr>
<tr><td>Alvorlig øyeskade/øyeirritasjon</td><td>Gir alvorlig øyeskade.</td></tr>
<tr><td>Luftveis- eller hudsensibilisering</td><td>{KR}</td></tr>
<tr><td>Arvestoffskadelighet (kimcellemutagenitet)</td><td>{KR}</td></tr>
<tr><td>Kreftfremkallende egenskaper</td><td>{KR}</td></tr>
<tr><td>Reproduksjonstoksisitet</td><td>{KR}</td></tr>
<tr><td>Giftighet for bestemte organer – enkelteksponering</td><td>{KR}</td></tr>
<tr><td>Giftighet for bestemte organer – gjentatt eksponering</td><td>{KR}</td></tr>
<tr><td>Aspirasjonsfare</td><td>{KR}</td></tr>
</table>
<p class="lbl gap">Opplysninger om bestanddeler</p>
<p class="tight"><u>Propan-1,2-diol</u><br>
LD50 (oralt, rotte): &gt; 20 000 mg/kg<br>
LD50 (hud, kanin): &gt; 2000 mg/kg<br>
LC50 (innånding, kanin): 317 042 mg/l, 2 t (aerosol) – verdi som oppgitt i kildedataene</p>
""",
# ---------- 10b ----------
"""
<p class="lbl first">Opplysninger om sannsynlige eksponeringsveier</p>
<p class="tight lh"><i>Innånding:</i> kan gi sterk irritasjon av de øvre luftveiene, tørrhoste, pustevansker, hodepine og svimmelhet.<br>
<i>Hudkontakt:</i> kjemiske etseskader, rødhet, smerte.<br>
<i>Øyekontakt:</i> smerte, tåkesyn, kraftig tåreflod, fare for alvorlig øyeskade.<br>
<i>Svelging:</i> etseskader i spiserør, svelg og andre deler av fordøyelseskanalen, fare for perforasjon og blødning.</p>
<p class="tight lh gap">Symptomer knyttet til fysiske, kjemiske og toksikologiske egenskaper; forsinkede og umiddelbare virkninger og kroniske virkninger ved kort- og langtidseksponering; interaktive virkninger: ingen data tilgjengelig.</p>
<h3 class="gap">11.2 Opplysninger om andre farer</h3>
<p class="lbl">Hormonforstyrrende egenskaper</p><p class="tight">Ingen.</p>
""",
# ---------- 11 ----------
"""
<h1 class="first">AVSNITT 12: Økologiske opplysninger</h1>
<h3>12.1 Giftighet</h3>
<p class="tight">Stoffblandingen er ikke klassifisert som miljøfarlig. Hindre at produktet kommer ut og spres i jord, avløp, grunnvann og vassdrag.</p>
<p class="sp lh"><u>Propan-1,2-diol</u><br>
LC50, fisk (Oncorhynchus mykiss): &gt; 1000 mg/l, 96 t<br>
EC50, krepsdyr (Mysidopsis bahia): &gt; 1000 mg/l, 48 t<br>
EC50, alger (Selenastrum capricornutum): &gt; 1000 mg/l, 72 t<br>
EC0, mikroorganismer (Pseudomonas putida): &gt; 1000 mg/l, 18 t<br>
NOEC, krepsdyr (Ceriodaphnia dubia): 13 020 mg/l, 7 døgn</p>
<h3 class="gap">12.2 Persistens og nedbrytbarhet</h3>
<p class="tight lh">Ingen data tilgjengelig for stoffblandingen.<br>
Propan-1,2-diol: bionedbrytning 81,7 % i løpet av 28 døgn (OECD 301F); 90,6 % i løpet av 64 døgn (OECD 306).<br>
De overflateaktive stoffene i dette produktet oppfyller kriteriene for biologisk nedbrytbarhet i forordning (EF) nr. 648/2004 om vaskemidler. Alle underlagsdata er tilgjengelige for vedkommende myndigheter og vil bli fremlagt på deres anmodning eller på anmodning fra vaskemiddelprodusenten.</p>
<h3>12.3 Bioakkumuleringsevne</h3><p class="tight">Ingen data tilgjengelig for stoffblandingen. Propan-1,2-diol: log Pow −1,07; BCF 0,09.</p>
<h3>12.4 Mobilitet i jord</h3><p class="tight">Ingen data tilgjengelig for stoffblandingen. Propan-1,2-diol: Koc &lt; 1.</p>
<h3>12.5 Resultater av PBT- og vPvB-vurdering</h3><p class="tight">Stoffblandingen inneholder ingen bestanddeler som oppfyller kriteriene for PBT eller vPvB.</p>
<h3>12.6 Hormonforstyrrende egenskaper</h3><p class="tight">Stoffblandingen inneholder ingen stoffer med hormonforstyrrende egenskaper.</p>
<h3>12.7 Andre skadevirkninger</h3><p class="tight">Ingen data tilgjengelig.</p>
""",
# ---------- 12 ----------
"""
<h1 class="first">AVSNITT 13: Disponering</h1>
<h3>13.1 Metoder for avfallsbehandling</h3>
<p class="tight lh just">Rester av produktet er etsende og skal behandles som farlig avfall og leveres til godkjent mottak for farlig avfall. Rester oppbevares i originalemballasjen. Tom, rengjort emballasje leveres til behandling, herunder materialgjenvinning, i samsvar med gjeldende regelverk.</p>
<p class="sp lh just">Avfallskode (EAL) fastsettes av avfallsbesitteren i samsvar med avfallsforskriften (FOR-2004-06-01-930), kapittel 11 og vedlegg 1, ut fra hvordan avfallet har oppstått.</p>
<p class="sp"><u>Regelverk om avfall:</u></p>
<p class="tight lh">Europaparlaments- og rådsdirektiv 2008/98/EF av 19. november 2008 om avfall og om oppheving av visse direktiver, med senere endringer; avfallsforskriften (FOR-2004-06-01-930).<br>
Europaparlaments- og rådsforordning (EU) 2025/40 av 19. desember 2024 om emballasje og emballasjeavfall.</p>
""",
# ---------- 13 ----------
f"""
<h1 class="first">AVSNITT 14: Transportopplysninger</h1>
<table class="tr">
<tr><td></td><td><b>ADR/RID</b></td><td><b>ADN</b></td><td><b>IMDG</b></td><td><b>IATA</b></td></tr>
<tr><td>14.1 FN-nummer eller ID-nummer</td><td>UN 3266</td><td>UN 3266</td><td>UN 3266</td><td>UN 3266</td></tr>
<tr><td>14.2 FN-forsendelsesnavn</td><td>ETSENDE VÆSKE, BASISK, UORGANISK, N.O.S. (natriumhydroksid, kaliumhydroksid)</td><td>ETSENDE VÆSKE, BASISK, UORGANISK, N.O.S. (natriumhydroksid, kaliumhydroksid)</td><td>CORROSIVE LIQUID, BASIC, INORGANIC, N.O.S. (sodium hydroxide, potassium hydroxide)</td><td>CORROSIVE LIQUID, BASIC, INORGANIC, N.O.S. (sodium hydroxide, potassium hydroxide)</td></tr>
<tr><td>14.3 Transportfareklasse(r)</td><td>8<br>Fareseddel: 8{LAB}</td><td>8<br>Fareseddel: 8{LAB}</td><td>8<br>Fareseddel: 8{LAB}</td><td>8<br>Fareseddel: 8{LAB}</td></tr>
<tr><td>14.4 Emballasjegruppe</td><td>II</td><td>II</td><td>II</td><td>II</td></tr>
<tr><td>14.5 Miljøfarer</td><td>Nei</td><td>Nei</td><td>Nei</td><td>Nei</td></tr>
<tr><td>14.6 Særlige forsiktighetsregler for brukeren</td><td>Klassifiseringskode: C5<br>Begrensede mengder (LQ): 1 l<br>Unntatte mengder: E2<br>Transportkategori: 2<br>Farenummer: 80<br>Tunnelrestriksjonskode: E</td><td>Klassifiseringskode: C5<br>Begrensede mengder (LQ): 1 l<br>Unntatte mengder: E2</td><td>EmS: F-A, S-B<br>Begrensede mengder (LQ): 1 l<br>Unntatte mengder: E2<br>Stuing og håndtering: kategori B, SW2<br>Segregering: SG35</td><td>Passasjerfly: emballeringsinstruks 851 (LQ: Y840, maks. 0,5 l per kolli); maks. netto mengde per kolli: 1 l<br>Kun fraktfly: emballeringsinstruks 855; maks. 30 l<br>Spesialbestemmelse: A3</td></tr>
<tr><td>14.7 Bulktransport til sjøs i henhold til IMOs instrumenter</td><td colspan="4">Ingen data tilgjengelig</td></tr>
</table>
""",
# ---------- 14 ----------
"""
<h1 class="first">AVSNITT 15: Regelverksmessige opplysninger</h1>
<h3 class="gap">15.1 Særskilte bestemmelser/særskilt lovgivning om sikkerhet, helse og miljø for stoffet eller stoffblandingen</h3>
<ol class="laws" style="line-height:1.5">
<li>Europaparlaments- og rådsforordning (EF) nr. 1907/2006 (REACH), med senere endringer – gjennomført i norsk rett ved REACH-forskriften (FOR-2008-05-30-516).</li>
<li>Kommisjonsforordning (EU) 2020/878 av 18. juni 2020 om endring av vedlegg II til forordning (EF) nr. 1907/2006 (REACH).</li>
<li>Europaparlaments- og rådsforordning (EF) nr. 1272/2008 (CLP), med senere endringer – gjennomført i norsk rett ved CLP-forskriften (FOR-2012-06-16-622).</li>
<li>Europaparlaments- og rådsforordning (EF) nr. 648/2004 om vaskemidler, med senere endringer. Produktet oppfyller kravene til vaskemidler; merking i henhold til artikkel 11.</li>
<li>Europaparlaments- og rådsforordning (EU) 2016/425 om personlig verneutstyr.</li>
<li>Lov om kontroll med produkter og forbrukertjenester (produktkontrolloven) av 11. juni 1976 nr. 79.</li>
<li>Forskrift om begrensning i bruk av helse- og miljøfarlige kjemikalier og andre produkter (produktforskriften) (FOR-2004-06-01-922).</li>
<li>Forskrift om gjenvinning og behandling av avfall (avfallsforskriften) (FOR-2004-06-01-930); direktiv 2008/98/EF om avfall; forordning (EU) 2025/40 om emballasje og emballasjeavfall.</li>
<li>Lov om arbeidsmiljø, arbeidstid og stillingsvern mv. (arbeidsmiljøloven) av 17. juni 2005 nr. 62.</li>
<li>Forskrift om utførelse av arbeid (FOR-2011-12-06-1357) og forskrift om tiltaks- og grenseverdier (FOR-2011-12-06-1358).</li>
<li>Forskrift om landtransport av farlig gods (FOR-2009-04-01-384), med ADR/RID.</li>
</ol>
<p class="sp lh">Seveso-direktivet 2012/18/EU (storulykkeforskriften): ikke omfattet.<br>
Biocidprodukter – forordning (EU) nr. 528/2012: ikke omfattet.<br>
Prekursorer for eksplosiver – forordning (EU) 2019/1148: ikke omfattet.<br>
Narkotikaprekursorer – forordning (EF) nr. 273/2004: ikke omfattet.<br>
Vedlegg XIV til REACH (godkjenning), SVHC-kandidatlisten og vedlegg XVII til REACH (begrensninger): ikke relevant.</p>
<h3 class="gap">15.2 Kjemikaliesikkerhetsvurdering</h3>
<p class="tight">Det er ikke utført kjemikaliesikkerhetsvurdering for stoffblandingen.</p>
""",
# ---------- 15 ----------
"""
<h1 class="first">AVSNITT 16: Andre opplysninger</h1>
<p class="lbl">H-setninger (bestanddeler, se avsnitt 3):</p>
<table class="h">
<tr><td>H290</td><td>Kan være etsende for metaller.</td></tr>
<tr><td>H302</td><td>Farlig ved svelging.</td></tr>
<tr><td>H314</td><td>Gir alvorlige etseskader på hud og øyne.</td></tr>
<tr><td>H315</td><td>Irriterer huden.</td></tr>
<tr><td>H318</td><td>Gir alvorlig øyeskade.</td></tr>
<tr><td>H319</td><td>Gir alvorlig øyeirritasjon.</td></tr>
<tr><td>H335</td><td>Kan forårsake irritasjon av luftveiene.</td></tr>
</table>
<p class="lbl gap">Forklaring av forkortelser og akronymer:</p>
<table class="abbr">
<tr><td>Met. Corr. 1</td><td>Etsende for metaller, kategori 1</td></tr>
<tr><td>Acute Tox. 4</td><td>Akutt giftighet, kategori 4</td></tr>
<tr><td>Skin Corr. 1A / 1B</td><td>Hudetsing, kategori 1A / 1B</td></tr>
<tr><td>Skin Irrit. 2</td><td>Hudirritasjon, kategori 2</td></tr>
<tr><td>Eye Dam. 1</td><td>Alvorlig øyeskade, kategori 1</td></tr>
<tr><td>Eye Irrit. 2</td><td>Øyeirritasjon, kategori 2</td></tr>
<tr><td>STOT SE 3</td><td>Giftighet for bestemte organer – enkelteksponering, kategori 3</td></tr>
<tr><td>ATE</td><td>Estimert akutt giftighet</td></tr>
<tr><td>DNEL</td><td>Avledet nivå uten virkning</td></tr>
<tr><td>PNEC</td><td>Beregnet konsentrasjon uten virkning</td></tr>
<tr><td>BCF</td><td>Biokonsentrasjonsfaktor</td></tr>
<tr><td>LD50</td><td>Median dødelig dose – statistisk fastsatt enkeltdose som forventes å drepe 50 % av de eksponerte forsøksdyrene</td></tr>
<tr><td>LC50</td><td>Median dødelig konsentrasjon – statistisk fastsatt konsentrasjon som forventes å drepe 50 % av de eksponerte organismene</td></tr>
<tr><td>EC50</td><td>Median effektkonsentrasjon – konsentrasjon som gir en bestemt virkning hos 50 % av forsøksorganismene</td></tr>
<tr><td>NOEC</td><td>Høyeste konsentrasjon uten observert virkning</td></tr>
<tr><td>vPvB / PBT</td><td>Svært persistent og svært bioakkumulerende stoff / persistent, bioakkumulerende og giftig stoff</td></tr>
<tr><td>UFI</td><td>Unik formelidentifikator</td></tr>
<tr><td>ADR / RID / ADN</td><td>Regelverk for transport av farlig gods på vei / jernbane / innlandsvannveier</td></tr>
<tr><td>IMDG / IATA</td><td>Regelverk for transport av farlig gods til sjøs / med fly</td></tr>
</table>
""",
# ---------- 16 ----------
f"""
<p class="lbl first">Grunnlag for klassifisering:</p>
<table class="basis">
<tr><td>Met. Corr. 1; H290</td><td>På grunnlag av bestanddelenes fysiske egenskaper</td></tr>
<tr><td>Skin Corr. 1A; H314</td><td>På grunnlag av innholdet av bestanddeler (beregningsmetode)</td></tr>
<tr><td>Eye Dam. 1; H318</td><td>På grunnlag av innholdet av bestanddeler (beregningsmetode)</td></tr>
</table>
<p class="lbl gap">Endringer i forhold til forrige versjon (SK-originalen):</p>
<p class="tight">Avsnitt 3: endret sammensetning · Avsnitt 8, 11, 12: utfyllende opplysninger om bestanddel · Avsnitt 13, 15: oppdatert regelverk.</p>
<p class="lbl gap">Opplæring:</p>
<p class="tight lh just">Arbeidstakere som håndterer produktet, skal få nødvendig opplæring i farene ved kjemikaliet og sikker bruk, jf. forskrift om utførelse av arbeid. Risikovurdering av kjemisk helsefare på arbeidsplassen skal gjennomføres og dokumenteres, og arbeidstakerne skal gjøres kjent med resultatet.</p>
<h3 class="gap ref">REFERANSEMATERIALE</h3>
<p class="sp">Vedlegg til kommisjonsforordning (EU) 2020/878 av 18. juni 2020.<br>
Regelverk angitt i avsnitt 15 i sikkerhetsdatabladet.</p>
<p class="sp just lh">Opplysningene i dette sikkerhetsdatabladet gjelder kun produktet som er angitt i navnet. Opplysningene skal utelukkende betraktes som et hjelpemiddel for sikker bruk av produktet. Siden forholdene for lagring, transport og bruk ligger utenfor vår kontroll, kan de ikke anses som en garanti i juridisk forstand. Gjeldende lovbestemmelser og eventuelle rettigheter tilhørende tredjepart skal alltid overholdes. Dette sikkerhetsdatabladet utgjør ikke en risikovurdering av arbeidsplassen. Produktet skal ikke brukes til andre formål enn dem som er angitt i avsnitt 1, uten forutgående konsultasjon med leverandøren.</p>
<p class="lbl gap">Revisjonsopplysninger</p>
<p class="tight just lh">Norsk versjon 1.0 (27.10.2026) er oversatt og tilpasset norske forhold på grunnlag av slovakisk sikkerhetsdatablad, versjon 2.0 av 26.09.2026. Endret i forhold til originalen: leverandøropplysninger (1.3), nødtelefonnummer (1.4), nasjonale grenseverdier og regelverk (avsnitt 8, 13 og 15). Førstehjelpstiltak ved hudkontakt (4.1) er presisert i samsvar med klassifiseringen (H314).</p>
<p class="sp">Norsk oversettelse og tilpasning: Isokor Skandinavia AS, <u>www.isokor-skandinavia.no</u></p>
<p class="sp"><b class="k6">UFI: {UFI}</b></p>
""",
]
assert len(PAGES) == 17 and sum(UFI in p for p in PAGES) == 2
