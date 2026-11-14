from lib import *
css=open('akten_css.txt').read().replace("FILE:","fonts/node_modules/@fontsource/")
css+='''
@font-face{font-family:"Hand";font-weight:700;src:url(fonts/node_modules/@fontsource/caveat/files/caveat-latin-700-normal.woff2)}
:root{--g:#2c7a4b;--ink:#10301d;--edge:#8fc4a0;--sun:#f2c14e}
.page{padding:11mm 16mm 0;font-family:"AtkH",sans-serif;color:var(--ink);font-size:10pt;line-height:1.38;break-after:page}
h1{font:700 26pt "Hand";color:var(--g);margin:0;line-height:1}
.sub{font:700 8.5pt "CP";letter-spacing:.1em;text-transform:uppercase;color:#4d6657;margin:0 0 3mm}
h2{font:700 12.5pt "AtkH";margin:4mm 0 1.2mm;border-bottom:2px solid var(--sun);padding-bottom:.6mm}
table{border-collapse:collapse;width:100%;margin:1mm 0}
th,td{border:1px solid var(--edge);padding:1.2mm 2mm;vertical-align:top;text-align:left;font-size:9.3pt}
th{background:#def0e2}
ul{margin:.8mm 0 .8mm 4.5mm;padding:0}li{margin:.4mm 0}
.box{border:1.2px solid var(--g);border-left:2.5mm solid var(--g);border-radius:1.5mm;padding:1.8mm 3.5mm;margin:1.6mm 0;background:#f6fbf7;page-break-inside:avoid}
.warn{border-color:#c9661a;background:#fdf1e3}
.src{font-size:8.5pt;color:#3d5446}
b.k{color:var(--g)}
'''
p1='''<div class=page><h1>Lösungs-Logbuch: Igel-Einsatz, Freitag 20.11.</h1><p class=sub>Für die Lehrperson · Etappe 1 Hilferuf und Etappe 2 Forschen</p>
<h2>Ablauf am Freitag</h2>
<ul><li><b>Input (höchstens 5 Min.):</b> Geschichte aus der App vorlesen oder lesen lassen. Dann arbeiten die Teams selbständig.</li><li><b>Material:</b> 1 Tablet pro Team, Logbuch Blatt 1 (pro Team 1×, doppelseitig), SDG-Karten.</li><li><b>Tablet-Logistik:</b> Pro Runde sucht ein Kind (Tablet), eines schreibt, eines prüft. Die Rollen wechseln. So braucht es nur ein Tablet pro Team.</li><li><b>Hilfe:</b> Tipp 1 und 2 in der App. Das Lösungs-Logbuch erscheint in der App erst, wenn die Kinder angekreuzt haben, dass sie ihre Antwort geschrieben haben.</li></ul>
<h2>Etappe 1 · Hilferuf</h2>
<div class=box><b class=k>Das sehen wir:</b> klein, dünn, liegt im Laub, kein Nest in der Nähe. <b class=k>Vermutung:</b> Er findet nicht genug Futter und friert, der Winter wird schwer. <b class=k>SDG-Karte:</b> SDG 15 Leben an Land. SDG 13 (Klima) kann passen, wenn gut begründet.</div>
<h2>Etappe 2 · Forschen (3 Runden)</h2>
<table><tr><th>Runde</th><th>Auftrag</th><th>Lösung</th><th>Quelle · Wörter zum Finden im Text (vorgegeben) · Tipps (1 · 2)</th></tr>
<tr><td>1 Essen</td><td>Was frisst ein Igel? Warum im Herbst wichtig?</td><td>Vor allem Insekten, Käfer und Larven, Raupen, Regenwürmer, Schnecken. Im Herbst frisst er sich für den Winterschlaf einen Fettvorrat an, im Winter findet er kaum Futter.</td><td><b>Klexikon «Igel»:</b> fressen, Herbst · Tipps: Was braucht ein Tier, das lange nichts fressen kann? · Abschnitte «was fressen sie?» und «Soll man Igel füttern?»</td></tr>
<tr><td>2 Schlafen</td><td>Wo schläft ein Igel im Winter? Was passiert im Körper?</td><td>In einem Nest aus Laub und Ästen. Körpertemperatur sinkt, Atmung und Herzschlag werden langsamer, kaum Energieverbrauch.</td><td><b>Klexikon «Winterschlaf» + «Igel»:</b> Körpertemperatur, Herzschlag, Nest · Tipps: Was würdest du als Tier tun? · Körper: «Winterschlaf»; Schlafplatz: «Igel», Wörter Nest, Laub</td></tr>
<tr><td>3 Helfen</td><td>Wo suchen Igel einen Schlafplatz? Wie kann man helfen?</td><td>Erdmulden, unter Hecken, in Haufen aus Totholz, Reisig und Laub. Naturnaher Garten mit Verstecken. Füttern nur wenn nötig, nur Katzenfutter.</td><td><b>NABU «Unterschlupf für Igel im Winter»:</b> Winterquartier, Reisig, Totholz · Tipps: Wo würdest du dich als Igel verstecken? · Klexikon hat dazu fast nichts: NABU-Seite lesen, Wörter selbst im Text finden</td></tr></table>
<div class=box><b class=k>Unser Satz (Ziel von Freitag 1):</b> «Ein Igel schläft im Winter in einem Nest aus Laub, Totholz und Reisig, in einer ruhigen, geschützten Ecke. Dafür brauchen wir Laub, Totholz und Reisig und einen ruhigen Ort.» Dieser Satz ist der Einstieg für Freitag 2.</div>
<h2>Wohin es führt (nur für dich)</h2>
<ul><li><b>Fr 27.11. Plan:</b> Wo (Schulgarten neben der Schule klären), was wir brauchen (Laub, Totholz aus dem Wald, Reisig), wer bringt was. Idee für ein Erklärschild.</li><li><b>Fr 4.12. Umsetzen:</b> Totholz im Wald sammeln, Haufen im Schulgarten anlegen. <b>Fr 11.12.:</b> Schild und Prüfen. <b>Fr 18.12.:</b> Bericht.</li><li><b>Vorher klären:</b> Schulgarten und Erlaubnis (zuständige Person), ob dort schon ein Haufen oder Nest liegt. Totholz im Wald: Begleitung und Erlaubnis.</li></ul>
<div class="box warn"><b>Sicherheit:</b> Igel nie anfassen, sofort die Lehrperson holen. Ab Mitte November schlafen die meisten Igel (NABU). Bestehende Unterschlupfe im Winter nicht versetzen.</div>
<p class=src>Quellen: Klexikon «Igel» und «Winterschlaf» (klexikon.zum.de) · NABU: Unterschlupf für Igel im Winter (nabu.de/aktiv-werden/naturnah-gaertnern/tiere-im-garten/winterquartiere/unterschlupf-fuer-igel-im-winter)</p></div>'''
render(doc(p1,css),'out/FreiDay_Einsatz01_Loesungs-Logbuch_Fr20.11_LP.pdf')
