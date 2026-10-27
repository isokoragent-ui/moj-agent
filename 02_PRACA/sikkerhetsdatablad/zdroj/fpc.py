# Norsk innhold for sikkerhetsdatablad Isokor FPC (alkalisk rengjøringsmiddel) – én liste per side
# Eget innhold: Met. Corr. 1; H290, Skin Corr. 1B; H314, Eye Dam. 1; H318 – natriumhydroksid, kaliumhydroksid, natriumhypokloritt.
# Rettet i forhold til SK-originalen: førstehjelp (4.1) og øyevern (8.2) tilpasset H314; 10.3 supplert med klorgass ved kontakt med syrer
# (produktet inneholder natriumhypokloritt); polske grenseverdier erstattet med norske (8.1) – verdiene må verifiseres mot vedlegg 1.
import lms

PRODUCT = "Isokor FPC"
DATE = lms.DATE
NA = lms.NA
KR = lms.KR
LAB = lms.LAB
EXTRA_CSS = lms.EXTRA_CSS
UFI = "5360-80PP-M00A-18S5"

PAGES = [
# ---------- 1 ----------
f"""
<h1>AVSNITT 1: Identifikasjon av stoffet/stoffblandingen og av selskapet/foretaket</h1>
<h3 class="inline">1.1 Produktidentifikator</h3><span class="iv">Isokor FPC</span>
<p class="tight">UFI: {UFI}</p>
<h3>1.2 Relevante identifiserte bruksområder for stoffet eller stoffblandingen og bruk som frarådes</h3>
<p class="sp">Identifisert bruk: rengjøringsmiddel</p>
<p class="tight">Bruk som frarådes: ikke spesifisert</p>
<h2>1.3 Opplysninger om leverandøren av sikkerhetsdatabladet</h2>
<p class="tight">Isokor Skandinavia AS<br>
Org.nr.: 922 112 975<br>
Nærestadveien 1, 4985 Vegårshei, Norge<br>
Tlf.: +47 486 42 178<br>
Nettside: www.isokor-skandinavia.no<br>
E-post: info@isokor-skandinavia.no</p>
<p class="tight small">Produsent: Rodinná firma, s.r.o., Raková 1631, 023 51 Raková, Slovakia</p>
<h2>1.4 Nødtelefonnummer</h2>
<p class="tight">113 (medisinsk nødtelefon)<br>
Giftinformasjonen (Helsedirektoratet): <b>22 59 13 00</b> – døgnåpen rådgivning ved akutte forgiftninger</p>
<h1>AVSNITT 2: Fareidentifikasjon</h1>
<h3>2.1 Klassifisering av stoffet eller stoffblandingen</h3>
<p class="tight"><u>I henhold til forordning (EF) nr. 1272/2008 (CLP):</u></p>
<p class="sp">Met. Corr. 1; H290</p>
<p class="sp">Skin Corr. 1B; H314</p>
<p class="sp">Eye Dam. 1; H318</p>
<p class="lbl">Helsefare:</p><p class="tight">Gir alvorlige etseskader på hud og øyne.</p>
<p class="lbl">Miljøfare:</p><p class="tight">Ingen.</p>
<p class="lbl">Fysiske/kjemiske farer:</p><p class="tight">Kan være etsende for metaller.</p>
""",
# ---------- 2 ----------
"""
<h2 class="first">2.2 Merkingselementer</h2>
<p class="sp"><b class="k6">Inneholder:</b> natriumhydroksid, kaliumhydroksid</p>
<p class="lbl b6 gap">Farepiktogrammer:</p>
<p class="pict"><img src="ghs05.svg"></p>
<p class="sp"><span class="k6">Varselord:</span> <b>Fare</b></p>
<p class="lbl b6 gap">Faresetninger:</p>
<p class="tight">H290 – Kan være etsende for metaller.<br>
H314 – Gir alvorlige etseskader på hud og øyne.</p>
<p class="lbl b6 gap">Sikkerhetssetninger:</p>
<p class="sp">P102 – Oppbevares utilgjengelig for barn.</p>
<p class="sp">P260 – Ikke innånd damp/aerosoler.</p>
<p class="sp">P280 – Benytt vernehansker/verneklær/vernebriller/ansiktsskjerm.</p>
<p class="sp">P301+P330+P331 – <i>VED SVELGING:</i> Skyll munnen. IKKE framkall brekninger.</p>
<p class="sp lh">P305+P351+P338 – <i>VED KONTAKT MED ØYNENE:</i> Skyll forsiktig med vann i flere minutter. Fjern eventuelle kontaktlinser dersom dette enkelt lar seg gjøre. Fortsett skyllingen.</p>
<p class="sp">P310 – Kontakt umiddelbart et GIFTINFORMASJONSSENTER/lege.</p>
<p class="sp">P501 – Innhold/beholder leveres i samsvar med nasjonale forskrifter.</p>
<h3 class="gap2">2.3 Andre farer</h3>
<p class="sp">Vedlegg XIII til REACH – Kriterier for identifisering av persistente, bioakkumulerende og giftige stoffer (PBT) og svært persistente og svært bioakkumulerende stoffer (vPvB): ikke relevant.</p>
<p class="sp">Stoffer med hormonforstyrrende egenskaper (i henhold til kriteriene i delegert kommisjonsforordning (EU) 2017/2100 og kommisjonsforordning (EU) 2018/605): ikke relevant.</p>
""",
# ---------- 3 ----------
"""
<h1 class="first">AVSNITT 3: Sammensetning/opplysninger om bestanddeler</h1>
<h2>3.1 Stoffer</h2><p class="tight">Ikke relevant.</p>
<h2>3.2 Stoffblandinger</h2><p class="tight">Farlige bestanddeler:</p>
<table class="comp" style="width:154mm">
<tr><th style="width:34%">Produktidentifikator</th><th>Innhold [%]</th><th>Fareklasse og -kategori</th><th>Faresetninger</th><th style="width:28%">Spesifikke konsentrasjonsgrenser, M-faktor, estimert akutt giftighet (ATE)</th></tr>
<tr><td>Natriumhydroksid*<br>CAS-nr.: 1310-73-2 · EF-nr.: 215-185-5<br>Indeksnr.: 011-002-00-6<br>REACH-reg.nr.: 01-2119457892-27-XXXX</td><td>1–&lt;5</td><td>Met. Corr. 1<br>Skin Corr. 1A<br>Eye Dam. 1</td><td>H290<br>H314<br>H318</td><td>Skin Corr. 1A; H314: C ≥ 5 %<br>Skin Corr. 1B; H314: 2 % ≤ C &lt; 5 %<br>Skin Irrit. 2; H315: 0,5 % ≤ C &lt; 2 %<br>Eye Irrit. 2; H319: 0,5 % ≤ C &lt; 2 %</td></tr>
<tr><td>Kaliumhydroksid*<br>CAS-nr.: 1310-58-3 · EF-nr.: 215-181-3<br>Indeksnr.: 019-002-00-8<br>REACH-reg.nr.: 01-2119487136-33-XXXX</td><td>1–&lt;5</td><td>Met. Corr. 1<br>Acute Tox. 4<br>Skin Corr. 1A<br>Eye Dam. 1</td><td>H290<br>H302<br>H314<br>H318</td><td>Skin Corr. 1A; H314: C ≥ 5 %<br>Skin Corr. 1B; H314: 2 % ≤ C &lt; 5 %<br>Skin Irrit. 2; H315: 0,5 % ≤ C &lt; 2 %<br>Eye Irrit. 2; H319: 0,5 % ≤ C &lt; 2 %</td></tr>
<tr><td>Natriumhypokloritt*<br>CAS-nr.: 7681-52-9 · EF-nr.: 231-668-3<br>Indeksnr.: 017-011-00-1<br>REACH-reg.nr.: 01-2119488154-34-XXXX</td><td>0,3–&lt;1</td><td>Met. Corr. 1<br>Skin Corr. 1B<br>STOT SE 3<br>Aquatic Acute 1<br>Aquatic Chronic 1</td><td>H290<br>H314<br>H335<br>H400<br>H410<br>EUH031</td><td>M = 10 (akutt)<br>M = 1 (kronisk)<br>EUH031: C ≥ 5 %</td></tr>
</table>
<p class="sp">Fullstendig ordlyd av H- og EUH-setningene: se avsnitt 16.</p>
<p class="tight">* stoff med fastsatt grenseverdi for eksponering på arbeidsplassen (se avsnitt 8)</p>
""",
# ---------- 4 ----------
"""
<h1 class="first">AVSNITT 4: Førstehjelpstiltak</h1>
<h3>4.1 Beskrivelse av førstehjelpstiltak</h3>
<h3>Generelt:</h3>
<p class="tight">Fjern tilsølte klær straks. Ved symptomer som gir grunn til bekymring: Kontakt lege. Vis dette sikkerhetsdatabladet eller etiketten.</p>
<h3>Innånding:</h3>
<p class="tight">Ved svimmelhet eller ubehag: Flytt personen ut i frisk luft.</p>
<h3>Øyekontakt:</h3>
<p class="tight">Skyll straks med rikelig vann i flere minutter, hold øyelokkene åpne. Fjern eventuelle kontaktlinser dersom dette enkelt lar seg gjøre. Fortsett skyllingen. Kontakt umiddelbart lege eller Giftinformasjonen (22 59 13 00).</p>
<h3>Hudkontakt:</h3>
<p class="tight">Fjern tilsølte klær. Skyll huden straks med rikelig vann. Ved irritasjon eller etseskader: Kontakt lege.</p>
<h3>Svelging:</h3>
<p class="tight">Skyll munnen og gi rikelig med vann å drikke. IKKE framkall brekninger. Kontakt umiddelbart lege eller Giftinformasjonen (22 59 13 00).</p>
<h3 class="gap">4.2 De viktigste symptomene og virkningene, både akutte og forsinkede</h3>
<p class="tight">Kan gi alvorlig irritasjon og etseskader på hud og øyne. Konsentrert damp kan irritere slimhinnene i luftveiene.</p>
<h3 class="gap">4.3 Angivelse av behov for øyeblikkelig legehjelp og spesialbehandling</h3>
<p class="tight">Symptomatisk behandling.</p>
<h1>AVSNITT 5: Brannslokkingstiltak</h1>
<h3>5.1 Slokkingsmidler</h3>
<p class="sp"><span class="k">Egnede slokkingsmidler:</span> Bruk slokkingsmetoder som er tilpasset forholdene i omgivelsene.</p>
<p class="sp"><span class="k">Uegnede slokkingsmidler:</span> Kraftig vannstråle.</p>
<h3>5.2 Særlige farer knyttet til stoffet eller stoffblandingen</h3>
<p class="tight">Ved forbrenning kan det dannes gasser og damper som inneholder helseskadelige karbonoksider, kloroksider og hydrogenklorid.</p>
<h3>5.3 Råd til brannmannskaper</h3>
<p class="sp lh">Beholdere i nærheten av brannen kjøles med vannstråle og fjernes om mulig fra faresonen. Ikke la slokkevann komme ut i overflatevann, grunnvann eller avløp.<br>
Ved brann i lukkede rom: Bruk verneklær og selvforsynt pusteapparat (trykkluftapparat).</p>
""",
# ---------- 5 ----------
"""
<h1 class="first">AVSNITT 6: Tiltak ved utilsiktede utslipp</h1>
<h3>6.1 Personlige forholdsregler, verneutstyr og nødprosedyrer</h3>
<p class="tight lh"><i>For personell som ikke er nødpersonell:</i> Varsle nødetatene om situasjonen. Personer som ikke deltar i håndteringen, skal holdes borte fra fareområdet.</p>
<p class="tight lh"><i>For nødpersonell:</i> Sørg for god ventilasjon, og bruk personlig verneutstyr. Unngå innånding av damp fra produktet.</p>
<h3>6.2 Miljømessige forholdsregler</h3>
<p class="tight">Hindre spredning og at større mengder kommer ut i avløp og vassdrag.</p>
<h3>6.3 Metoder og materialer for oppsamling og rengjøring</h3>
<p class="tight lh">Hindre spredning og samle opp med absorberende materiale (sand, sagflis, jord).<br>
Når forurenset materiale må kasseres (f.eks. diatoméjord, universalabsorbent), legges det i egnede, merkede beholdere for avfallsbehandling i samsvar med gjeldende regelverk.</p>
<h3>6.4 Henvisning til andre avsnitt</h3>
<p class="tight">Opplysninger om disponering av avfall fra produktet: se avsnitt 13 i sikkerhetsdatabladet.<br>
Opplysninger om personlig verneutstyr: se avsnitt 8 i sikkerhetsdatabladet.</p>
<h1>AVSNITT 7: Håndtering og lagring</h1>
<h3>7.1 Forholdsregler for sikker håndtering</h3>
<p class="tight lh">Brukes i godt ventilerte rom.<br>
Unngå kontakt med øynene.<br>
Unngå kontakt med huden.<br>
Unngå innånding av damp fra produktet.<br>
Følg gjeldende regler for sikkerhet og hygiene: ikke spis, drikk eller røyk i arbeidsområdet, vask hendene etter bruk, og fjern tilsølte klær og verneutstyr før du går inn i spiseområder.</p>
<h3>7.2 Vilkår for sikker lagring, herunder eventuelle uforenligheter</h3>
<p class="tight lh">Oppbevares kjølig, tørt og godt ventilert i tett lukket, korrekt merket originalemballasje.<br>
Unngå direkte sollys, varmekilder, varme overflater og åpen flamme.<br>
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
<tr><td>Klor (CAS: 7782-50-5)</td><td>0,5</td><td>1,5</td><td>T</td></tr>
</table>
<p class="sp small">T = takverdi (verdi som ikke skal overskrides).</p>
<p class="lbl gap">DNEL- og PNEC-verdier for bestanddeler:</p>
<div class="cols">
<div><p class="tight"><u>Natriumhydroksid</u><br>DNEL arbeidstaker, innånding, langtidseksponering, systemiske virkninger: 1 mg/m³<br>DNEL arbeidstaker, innånding, langtidseksponering, lokale virkninger: 1 mg/m³</p>
<p class="sp"><u>Kaliumhydroksid</u><br>DNEL arbeidstaker, innånding, langtidseksponering, lokale virkninger: 1 mg/m³</p></div>
<div><p class="tight"><u>Natriumhypokloritt</u><br>DNEL arbeidstaker, innånding, langtidseksponering, systemiske og lokale virkninger: 1,55 mg/m³<br>DNEL arbeidstaker, innånding, korttidseksponering, systemiske og lokale virkninger: 3,1 mg/m³<br>DNEL forbruker, innånding, langtidseksponering, systemiske og lokale virkninger: 1,55 mg/m³<br>DNEL forbruker, innånding, korttidseksponering, systemiske og lokale virkninger: 3,1 mg/m³<br>DNEL forbruker, oralt, langtidseksponering, systemiske virkninger: 0,26 mg/kg<br>PNEC ferskvann: 0,21 µg/l<br>PNEC sjøvann: 0,042 µg/l<br>PNEC sporadisk utslipp: 0,26 µg/l<br>PNEC renseanlegg: 0,03 mg/l</p></div>
</div>
""",
# ---------- 7 ----------
"""
<h3 class="first">8.2 Eksponeringskontroll</h3>
<p class="lbl">Egnede tekniske kontrolltiltak:</p>
<p class="tight lh">Følg generelle regler for sikkerhet og hygiene ved arbeid med kjemikalier.<br>
Unngå kontakt med øynene.<br>
Vask hendene i pauser og etter håndtering av produktet.<br>
Ikke spis, drikk eller røyk ved håndtering av produktet.<br>
Fjern tilsølte klær og vask dem før de brukes igjen.<br>
Sørg for lett tilgang til nøddusj og øyeskylleutstyr.</p>
<p class="lbl gap">Individuelle vernetiltak, som personlig verneutstyr:</p>
<p class="lbl">Øye-/ansiktsvern:</p>
<p class="tight">Bruk tettsittende vernebriller eller ansiktsskjerm i henhold til EN 166.</p>
<p class="lbl">Hudvern:</p><p class="tight it">Håndvern:</p>
<p class="tight">Bruk vernehansker i henhold til EN ISO 374.<br>
Anbefalt materiale: nitrilgummi · Tykkelse: &gt; 0,4 mm · Gjennombruddstid: &gt; 480 min.</p>
<p class="lbl">Hanskemateriale:</p>
<p class="tight lh">Valg av riktige hansker avhenger ikke bare av materialet, men også av merke og kvalitet, fordi det er forskjeller mellom produsentene. Hanskematerialets motstandsevne kan bare fastslås ved testing. Nøyaktig gjennombruddstid må oppgis av hanskeprodusenten.</p>
<p class="lbl">Annet:</p><p class="tight">Arbeidsklær.</p>
<p class="lbl">Åndedrettsvern:</p><p class="tight">Ved utilstrekkelig ventilasjon: Bruk åndedrettsvern.</p>
<p class="lbl">Termiske farer:</p><p class="tight">Ikke relevant.</p>
<p class="lbl">Begrensning og overvåking av miljøeksponering:</p><p class="tight">Hindre spredning i miljøet og at produktet kommer ut i avløp eller vassdrag.</p>
""",
# ---------- 8 ----------
f"""
<h1 class="first">AVSNITT 9: Fysiske og kjemiske egenskaper</h1>
<h3 class="gap">9.1 Opplysninger om grunnleggende fysiske og kjemiske egenskaper</h3>
<table class="props">
<tr><td>Aggregattilstand</td><td>Væske</td></tr>
<tr><td>Farge</td><td>Gul</td></tr>
<tr><td>Lukt</td><td>Karakteristisk</td></tr>
<tr><td>Smeltepunkt/frysepunkt<br><i>(gjelder ikke gasser)</i></td><td>{NA}</td></tr>
<tr><td>Kokepunkt eller startkokepunkt og kokepunktintervall</td><td>{NA}</td></tr>
<tr><td>Antennelighet <i>(gjelder gasser, væsker og faste stoffer)</i></td><td>Ikke brannfarlig produkt</td></tr>
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
<h3>10.1 Reaktivitet</h3><p class="tight">Kan være etsende for metaller.</p>
<h3 class="gap">10.2 Kjemisk stabilitet</h3><p class="tight">Stabilt under normale forhold for bruk, lagring og transport.</p>
<h3 class="gap">10.3 Mulighet for farlige reaksjoner</h3>
<p class="tight lh just">Natriumhydroksid: reagerer kraftig med aceton, kloroform, maleinsyreanhydrid, syrer, fosfor, nitriler, peroksider, brom, nitroforbindelser, nitrater, magnesium, kalsium og metallpulver.<br>
Kaliumhydroksid: eksplosjonsfare ved kontakt med tetrahydrofuran, organiske peroksider og selvspaltende stoffer, fluor, klor, fosfor og magnesium. Kraftige reaksjoner med mineralsyrer, organiske syrer, svovelsyre, syreklorider, aldehyder og alkoholer; farlige reaksjoner med aluminium og azider.<br>
Natriumhypokloritt: ved kontakt med syrer kan det frigjøres giftig klorgass.</p>
<h3 class="gap">10.4 Forhold som skal unngås</h3><p class="tight">Unngå høye temperaturer, åpen flamme, gnister og direkte sollys.</p>
<h3 class="gap">10.5 Uforenlige materialer</h3><p class="tight">Se avsnitt 10.3.</p>
<h3 class="gap">10.6 Farlige nedbrytningsprodukter</h3><p class="tight">Produktet brytes ikke ned ved anbefalte bruksforhold.</p>
""",
# ---------- 10 ----------
f"""
<h1 class="first">AVSNITT 11: Toksikologiske opplysninger</h1>
<h3 class="gap">11.1 Opplysninger om fareklasser som definert i forordning (EF) nr. 1272/2008</h3>
<table class="tox" style="margin-top:3mm">
<tr><td>Akutt giftighet</td><td>{KR}</td></tr>
<tr><td>Hudetsing/hudirritasjon</td><td>Gir alvorlige etseskader på hud og øyne.</td></tr>
<tr><td>Alvorlig øyeskade/øyeirritasjon</td><td>Gir alvorlige etseskader på hud og øyne.</td></tr>
<tr><td>Luftveis- eller hudsensibilisering</td><td>{KR}</td></tr>
<tr><td>Arvestoffskadelighet (kimcellemutagenitet)</td><td>{KR}</td></tr>
<tr><td>Kreftfremkallende egenskaper</td><td>{KR}</td></tr>
<tr><td>Reproduksjonstoksisitet</td><td>{KR}</td></tr>
<tr><td>Giftighet for bestemte organer – enkelteksponering</td><td>{KR}</td></tr>
<tr><td>Giftighet for bestemte organer – gjentatt eksponering</td><td>{KR}</td></tr>
<tr><td>Aspirasjonsfare</td><td>{KR}</td></tr>
</table>
<p class="lbl gap">Opplysninger om bestanddeler</p>
<div class="cols"><div><p class="tight"><u>Kaliumhydroksid</u><br>
LD50 (oralt, rotte): 333 mg/kg</p></div>
<div><p class="tight"><u>Natriumhypokloritt</u><br>
LD50 (oralt, rotte): &gt; 1100 mg/kg<br>
LD50 (hud, kanin): &gt; 2000 mg/kg<br>
LC50 (innånding, rotte): &gt; 10,5 mg/l, 1 t (klor)</p></div></div>
<h3 class="gap">11.2 Opplysninger om andre farer</h3>
<p class="lbl">Hormonforstyrrende egenskaper</p><p class="tight">Ingen.</p>
""",
# ---------- 11 ----------
"""
<h1 class="first">AVSNITT 12: Økologiske opplysninger</h1>
<h3>12.1 Giftighet</h3>
<p class="tight">Produktet er ikke klassifisert som miljøfarlig.</p>
<div class="cols"><div><p class="tight lh"><u>Natriumhydroksid</u><br>
Krepsdyr (Daphnia magna) EC50: 40,4 mg/l, 48 t</p></div>
<div><p class="tight lh"><u>Natriumhypokloritt</u><br>
Fisk (Salmo gairdneri) LC50, 96 t: verdi ikke oppgitt i kildedataene<br>
Fisk (Menidia peninsulae) NOEC: 0,04 mg/l, 96 t<br>
Krepsdyr (Daphnia magna) EC50: 0,141 mg/l, 48 t<br>
Alger NOEC: 0,0021 mg/l, 7 døgn<br>
Bakterier (aktivert slam) EC50: &gt; 3 mg/l, 3 t</p></div></div>
<h3 class="gap">12.2 Persistens og nedbrytbarhet</h3><p class="tight">Ingen data tilgjengelig for produktet.</p>
<h3>12.3 Bioakkumuleringsevne</h3><p class="tight">Ingen data tilgjengelig for produktet.</p>
<h3>12.4 Mobilitet i jord</h3><p class="tight">Ingen data tilgjengelig for produktet.</p>
<h3>12.5 Resultater av PBT- og vPvB-vurdering</h3><p class="tight">Produktet inneholder ingen bestanddeler som oppfyller kriteriene for PBT eller vPvB.</p>
<h3>12.6 Hormonforstyrrende egenskaper</h3><p class="tight">Produktet inneholder ingen stoffer med hormonforstyrrende egenskaper.</p>
<h3>12.7 Andre skadevirkninger</h3><p class="tight">Ingen data tilgjengelig.</p>
""",
# ---------- 12 ----------
"""
<h1 class="first">AVSNITT 13: Disponering</h1>
<h3>13.1 Metoder for avfallsbehandling</h3>
<p class="tight lh just">Rester av produktet er etsende og skal behandles som farlig avfall og leveres til godkjent mottak for farlig avfall. Rester oppbevares i originalemballasjen. Anbefalt disponering: forbrenning i egnede, godkjente forbrenningsanlegg. Tom emballasje skal disponeres, herunder materialgjenvinnes, i samsvar med gjeldende regelverk.</p>
<p class="sp lh just">Avfallskode (EAL) fastsettes av avfallsbesitteren i samsvar med avfallsforskriften (FOR-2004-06-01-930), kapittel 11 og vedlegg 1, ut fra hvordan avfallet har oppstått.</p>
<p class="sp"><u>Regelverk om avfall:</u></p>
<p class="tight">Europaparlaments- og rådsdirektiv 2008/98/EF av 19. november 2008 om avfall og om oppheving av visse direktiver; avfallsforskriften (FOR-2004-06-01-930).</p>
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
<tr><td>14.6 Særlige forsiktighetsregler for brukeren</td><td>–</td><td>–</td><td>–</td><td>–</td></tr>
<tr><td>14.7 Bulktransport til sjøs i henhold til IMOs instrumenter</td><td>Ikke relevant</td><td>Ikke relevant</td><td>Ikke relevant</td><td>Ikke relevant</td></tr>
</table>
""",
# ---------- 14 ----------
lms.PAGES[14],
# ---------- 15 ----------
"""
<h1 class="first">AVSNITT 16: Andre opplysninger</h1>
<p class="lbl">H- og EUH-setninger (bestanddeler, se avsnitt 3):</p>
<table class="h">
<tr><td>H290</td><td>Kan være etsende for metaller.</td></tr>
<tr><td>H302</td><td>Farlig ved svelging.</td></tr>
<tr><td>H314</td><td>Gir alvorlige etseskader på hud og øyne.</td></tr>
<tr><td>H315</td><td>Irriterer huden.</td></tr>
<tr><td>H318</td><td>Gir alvorlig øyeskade.</td></tr>
<tr><td>H319</td><td>Gir alvorlig øyeirritasjon.</td></tr>
<tr><td>H335</td><td>Kan forårsake irritasjon av luftveiene.</td></tr>
<tr><td>H400</td><td>Meget giftig for liv i vann.</td></tr>
<tr><td>H410</td><td>Meget giftig, med langtidsvirkning, for liv i vann.</td></tr>
<tr><td>EUH031</td><td>Ved kontakt med syrer utvikles giftig gass.</td></tr>
</table>
<p class="lbl gap">Forklaring av forkortelser og akronymer:</p>
<table class="abbr">
<tr><td>Met. Corr. 1</td><td>Etsende for metaller, kategori 1</td></tr>
<tr><td>Acute Tox. 4</td><td>Akutt giftighet, kategori 4</td></tr>
<tr><td>Skin Corr. 1A</td><td>Hudetsing, kategori 1A</td></tr>
<tr><td>Skin Corr. 1B</td><td>Hudetsing, kategori 1B</td></tr>
<tr><td>Skin Irrit. 2</td><td>Hudirritasjon, kategori 2</td></tr>
<tr><td>Eye Dam. 1</td><td>Alvorlig øyeskade, kategori 1</td></tr>
<tr><td>Eye Irrit. 2</td><td>Øyeirritasjon, kategori 2</td></tr>
<tr><td>STOT SE 3</td><td>Giftighet for bestemte organer – enkelteksponering, kategori 3</td></tr>
<tr><td>Aquatic Acute 1</td><td>Farlig for vannmiljøet – akutt fare, kategori 1</td></tr>
<tr><td>Aquatic Chronic 1</td><td>Farlig for vannmiljøet – kronisk fare, kategori 1</td></tr>
</table>
""",
# ---------- 16 ----------
"""
<table class="abbr first" style="margin-top:0">
<tr><td>DNEL</td><td>Avledet nivå uten virkning</td></tr>
<tr><td>PNEC</td><td>Beregnet konsentrasjon uten virkning</td></tr>
<tr><td>LD50</td><td>Median dødelig dose – statistisk fastsatt enkeltdose av et stoff som forventes å drepe 50 % av de eksponerte forsøksdyrene</td></tr>
<tr><td>LC50</td><td>Median dødelig konsentrasjon – statistisk fastsatt konsentrasjon av et stoff som forventes å drepe 50 % av de eksponerte organismene i løpet av eksponeringen eller en fastsatt periode etter eksponeringen</td></tr>
<tr><td>EC50</td><td>Median effektkonsentrasjon – statistisk beregnet konsentrasjon som gir en bestemt virkning hos 50 % av forsøksorganismene under fastsatte forhold</td></tr>
<tr><td>NOEC</td><td>Høyeste konsentrasjon uten observert virkning – konsentrasjonen der det ikke er noen vesentlig økning i hyppighet eller alvorlighet av virkninger sammenlignet med kontrollgruppen</td></tr>
<tr><td>vPvB</td><td>Svært persistent og svært bioakkumulerende stoff</td></tr>
<tr><td>PBT</td><td>Persistent, bioakkumulerende og giftig stoff</td></tr>
<tr><td>SVHC</td><td>Stoff som gir grunn til svært stor bekymring</td></tr>
<tr><td>EAL</td><td>Europeisk avfallsliste</td></tr>
<tr><td>UFI</td><td>Unik formelidentifikator</td></tr>
<tr><td>ADR</td><td>Europeisk avtale om internasjonal veitransport av farlig gods</td></tr>
<tr><td>RID</td><td>Regelverk for internasjonal jernbanetransport av farlig gods</td></tr>
<tr><td>ADN</td><td>Europeisk avtale om internasjonal transport av farlig gods på innlandsvannveier</td></tr>
<tr><td>IMDG</td><td>Internasjonalt regelverk for sjøtransport av farlig gods</td></tr>
<tr><td>IATA</td><td>Regelverk for lufttransport av farlig gods fra Den internasjonale luftfartsorganisasjonen IATA</td></tr>
</table>
<p class="lbl gap2">Grunnlag for klassifisering:</p>
<table class="basis">
<tr><td>Met. Corr. 1; H290</td><td>På grunnlag av bestanddelenes fysiske egenskaper</td></tr>
<tr><td>Skin Corr. 1B; H314</td><td>På grunnlag av innholdet av bestanddeler (beregningsmetode)</td></tr>
<tr><td>Eye Dam. 1; H318</td><td>På grunnlag av innholdet av bestanddeler (beregningsmetode)</td></tr>
</table>
""",
# ---------- 17 ----------
lms.PAGES[17]
  .replace("Førstehjelpstiltak (4.1) og personlig verneutstyr (8.2) er presisert i samsvar med klassifiseringen (H314) og sikkerhetssetningene i avsnitt 2.2.",
           "Førstehjelpstiltak (4.1) og personlig verneutstyr (8.2) er presisert i samsvar med klassifiseringen (H314) og sikkerhetssetningene i avsnitt 2.2. Avsnitt 10.3 er supplert med faren for klorgass ved kontakt med syrer.")
  .replace("AV10-F0V7-M002-MJ6P", UFI),
]
assert len(PAGES) == 17 and "AVSNITT 15" in PAGES[13] and "Opplæring" in PAGES[16] and "klorgass ved kontakt med syrer" in PAGES[16]
assert sum(UFI in p for p in PAGES) == 2 and not any("AV10-F0V7" in p or "melkesyre" in p for p in PAGES)
