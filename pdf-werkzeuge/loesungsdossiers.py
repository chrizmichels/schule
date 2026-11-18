# Lösungsdossiers Akte 01–03 (nur für die LP). Messwerte: MeteoSchweiz, Station Fluntern/Lugano/Zermatt, abgerufen am 18.11.2026 über /api/ogd.
from lib import render
CSS='''@page{size:A4;margin:11mm 14mm}
body{font-family:Inter,"Helvetica Neue",Arial,sans-serif;font-size:9.7pt;line-height:1.36;color:#14211f;margin:0}
.t{background:#1e7a8c;color:#fff;border-radius:3mm;padding:2.5mm 5mm;display:flex;justify-content:space-between;align-items:center}
.t small{display:block;font-size:8.5pt;opacity:.9}.t b{font-size:15pt}.lp{background:#fff;color:#b3302a;font-weight:700;font-size:8.5pt;border-radius:2mm;padding:1mm 2.5mm}
h2{font-size:11pt;margin:4mm 0 1mm;color:#1e7a8c}h2 span{display:inline-block;background:#1e7a8c;color:#fff;border-radius:1.5mm;padding:0 2mm;margin-right:2mm;font-size:9pt}
p{margin:1mm 0}ul{margin:1mm 0;padding-left:5mm}li{margin:.6mm 0}
table{border-collapse:collapse;margin:1.5mm 0;font-size:9.8pt}th,td{border:1px solid #9fb3b6;padding:.8mm 2.2mm;text-align:center}th{background:#e6f1f3}td.l{text-align:left;font-weight:700;background:#f6fafb}
.box{border:1px solid #1e7a8c;background:#eef6f7;border-radius:2mm;padding:1.5mm 3.5mm;margin:2mm 0}
.w{border-left:2mm solid #b3302a;background:#fbf1ef;border-radius:1.5mm;padding:1.5mm 3.5mm;margin:2mm 0}
.m{color:#44544f;font-size:9pt}svg{display:block;margin:1mm 0}'''
H=[8,10,12,14,16,18,20]
def tab(rows,head=None):
    h=head or ['Uhr']+[str(x) for x in H]
    s='<table><tr>'+''.join(f'<th>{x}</th>' for x in h)+'</tr>'
    for r in rows: s+='<tr><td class=l>'+r[0]+'</td>'+''.join(f'<td>{x}</td>' for x in r[1:])+'</tr>'
    return s+'</table>'
def f(x): return f'{x:.1f}'.replace('.',',')
def chart(series,w=420,h=150):
    L,R,T,B=34,10,8,22;lo,hi=3,11
    X=lambda hh:L+(hh-8)/12*(w-L-R);Y=lambda v:T+(hi-v)/(hi-lo)*(h-T-B)
    s=f'<svg viewBox="0 0 {w} {h}" width="{w*0.85}" font-family="Inter,Arial" font-size="9">'
    for v in range(lo,hi+1,2): s+=f'<line x1="{L}" x2="{w-R}" y1="{Y(v)}" y2="{Y(v)}" stroke="#d3dfe1"/><text x="{L-4}" y="{Y(v)+3}" text-anchor="end">{v}</text>'
    for hh in H: s+=f'<text x="{X(hh)}" y="{h-8}" text-anchor="middle">{hh}</text>'
    s+=f'<text x="{L-24}" y="{T+4}" font-size="8">°C</text>'
    for vals,col,dash in series:
        pts=' '.join(f'{X(hh)},{Y(v)}' for hh,v in zip(H,vals))
        s+=f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2" {"stroke-dasharray=4,3" if dash else ""}/>'
        s+=''.join(f'<circle cx="{X(hh)}" cy="{Y(v)}" r="2.6" fill="{col}"/>' for hh,v in zip(H,vals))
    return s+'</svg>'
T1=[4.2,5.3,5.7,6.7,6.5,6.1,6.3]; T2=[9.6,9.5,10.1,10.1,9.4,9.7,9.7]
def page(n,titel,body):
    return f'<div class=t><div><small>Kommissariat 4b · Lösungsdossier Akte 0{n}</small><b>{titel}</b></div><span class=lp>nur für die LP</span></div>'+body
SRC='<p class=m>Messwerte: MeteoSchweiz, Station Zürich-Fluntern (556 m), 10-Minuten-Daten, abgerufen am 18.11.2026. Es sind dieselben Werte wie in der App (425.co/k).</p>'
a1=page(1,'Der warme Tag',f'''
<h2><span>1</span>Vermuten (Akte, Schritt 1)</h2>
<p>Die Kinder vermuten, um wie viel Uhr es an <b>Tag 1 (Fr 6.11.)</b> am wärmsten war: Morgen, Mittag oder Abend. Jede Vermutung mit Begründung ist gut. Es gibt kein falsch.</p>
<h2><span>2</span>Spuren sichern: Zeile Tag 1 auf KM 54.2</h2>
{tab([['Tag 1 · Fr 6.11.']+[f(x) for x in T1]])}<p class=m>Temperatur in °C. Die Kinder lesen die Werte in der App ab.</p>
<h2><span>3</span>Kurve malen (rot)</h2>{chart([(T1,'#d62828',0)])}
<p>0,5 °C genau reicht. Die Kurve steigt bis 14 Uhr und sinkt danach leicht. Um 20 Uhr ist es wieder etwas wärmer als um 18 Uhr. Das ist richtig so, kein Fehler.</p>
<h2><span>4</span>Lösung</h2>
<div class=box><b>Am wärmsten:</b> 14 Uhr, <b>6,7 °C</b>.<br><b>Am kältesten:</b> 8 Uhr, <b>4,2 °C</b>.<br><b>Unterschied (Wiederholung Fall 1, Frage 2):</b> 6,7 − 4,2 = <b>2,5 °C</b>.</div>
<p class=m>Feinwerte (nur LP): Das Maximum des Tages war 6,8 °C um 13:50 Uhr. Die App zeigt nur die Werte alle 2 Stunden.</p>
<h2><span>5</span>Beweisstück 1: «Wer macht die Luft warm?»</h2>
<p>Das muss in den eigenen Worten der Kinder stehen (Test-Lernziel «Warum ist es am Nachmittag am wärmsten?»):</p>
<ul><li>Die <b>Sonne</b> wärmt den <b>Boden</b>.</li><li>Der warme Boden wärmt die <b>Luft</b> darüber.</li><li>Am Morgen ist der Boden noch kalt von der Nacht. Der Boden wird auch nach dem Mittag noch wärmer. Darum ist es oft erst am <b>Nachmittag</b> am wärmsten.</li></ul>
<h2>KM 54.2, Frage 5: Stimmt unsere Messung vom 6.11. um 8:30?</h2>
<p>Station Fluntern um 8:30 Uhr: 4,4 °C (8:00 Uhr: 4,2 °C). Die Messung am Fenster darf abweichen (anderer Standort, anderes Thermometer). Bis etwa 1 °C Unterschied gilt «stimmt ungefähr». Um 11:45 Uhr: 5,9 °C (+1,5 °C).</p>
<div class=w><b>Stolpersteine:</b> Kinder tippen oft «Mittag». Das ist eine gute Vermutung, nur nicht die Lösung. Darum ist Schritt 5 wichtig: Sie erklären, <i>warum</i> der Boden Zeit braucht.</div>
{SRC}''')
a2=page(2,'Zwei Tage',f'''
<h2><span>1</span>Vermuten (Akte, Schritt 1)</h2>
<p>Die Kinder vermuten: Tag 1 (Fr 6.11., rot) oder Tag 2 (Do 12.11., blau) war wärmer. Mit Begründung.</p>
<h2><span>2</span>Spuren sichern: Zeile Tag 2 auf KM 54.2</h2>
{tab([['Tag 1 · Fr 6.11. (rot)']+[f(x) for x in T1],['Tag 2 · Do 12.11. (blau)']+[f(x) for x in T2]])}
<h2><span>3</span>Kurve malen (blau)</h2>{chart([(T1,'#d62828',0),(T2,'#1d4ed8',1)])}
<h2><span>4</span>Lösung</h2>
<div class=box><b>KM 54.2, Frage 3:</b> <b>Tag 2</b> war wärmer, an <b>7 von 7</b> Zeiten.<br><b>KM 54.2, Frage 4 (12 Uhr):</b> Tag 1: 5,7 °C · Tag 2: 10,1 °C · Unterschied <b>4,4 °C</b>.</div>
<p class=m>Weitere Zahlen (nur LP): Tag 2 war um 12 und um 14 Uhr gleich warm (10,1 °C). Der Unterschied war um 8 Uhr am grössten (5,4 °C) und um 16 Uhr am kleinsten (2,9 °C).</p>
<h2>Spuren vom Wetter (App, Station Fluntern, 8 bis 20 Uhr)</h2>
{tab([['Sonne (Strahlung, Ø W/m²)','39','38'],['Wind (Ø km/h)','3','6'],['Luftfeuchte (Ø %)','94','98'],['Regen (Summe mm)','1,3','5,7']],['','Tag 1 · Fr 6.11.','Tag 2 · Do 12.11.'])}
<p>In der App sehen die Kinder <b>Sonne</b>: an beiden Tagen etwa gleich stark, und <b>Wind</b>: Tag 2 war windiger (3 und 6 km/h). Luftfeuchte und Regen zeigt die App nicht. Beide Tage waren trüb (wenig Strahlung, Luftfeuchte über 87 %).</p>
<h2><span>5</span>Beweisstück 2: «Wolken, Wind und Nebel»</h2>
<ul><li><b>Wolken</b> halten Sonnenstrahlen ab. Es kommt weniger Wärme zum Boden.</li><li><b>Wind</b> bringt Luft von anderswo (kalte oder warme).</li><li><b>Nebel</b> ist eine Wolke am Boden. Die Sonne kommt kaum durch.</li></ul>
<div class=w><b>Wichtig für die Auswertung:</b> Die Sonne erklärt den Unterschied nicht, sie war an beiden Tagen gleich schwach. Der Wind war am Tag 2 stärker, die App zeigt aber nicht, woher er kam (am 12.11. bei Stichproben um 8, 12, 14 und 18 Uhr aus 36 bis 50°, also Nordost). Ein sicherer Grund lässt sich aus den Spuren darum <b>nicht</b> ablesen. Gute Kinderantworten begründen mit den Spuren: «Sonne war gleich, also nicht die Sonne. Der Wind war stärker, vielleicht brachte er wärmere Luft.» Wichtig ist die Begründung, nicht ein bestimmtes Wort.</div>
{SRC}''')
LUG1,ZUE1,ZER1=[10.1,9.3,10.2],[4.2,5.7,6.5],[2.2,5.9,3.9]
LUG2,ZUE2,ZER2=[10.7,11.4,11.3],[9.6,10.1,9.4],[5.2,5.9,4.3]
a3=page(3,'Drei Orte',f'''
<h2><span>1</span>Vermuten (Akte, Schritt 1)</h2>
<p>Die Kinder vermuten, wo es am kältesten ist (Lugano, Zürich oder Zermatt) und «Je höher der Ort, desto …».</p>
<h2><span>2</span>Spuren sichern: Messwerte der drei Orte</h2>
<p>Die App zeigt als Standard <b>Tag 1 (Fr 6.11.), 12 Uhr</b>. Die Kinder können (nur auf deine Anweisung) Tag und Zeit ändern.</p>
{tab([['Tag 1 · 8 Uhr','10,1','4,2','2,2'],['Tag 1 · <b>12 Uhr</b> (Standard)','9,3','<b>5,7</b>','5,9'],['Tag 1 · 16 Uhr','10,2','6,5','3,9'],['Tag 2 · 8 Uhr','10,7','9,6','5,2'],['Tag 2 · 12 Uhr','11,4','10,1','5,9'],['Tag 2 · 16 Uhr','11,3','9,4','4,3']],['Messzeitpunkt','Lugano (Höhe 273 m)','Zürich-Fluntern (556 m)','Zermatt (1638 m)'])}
<div class=w><b>Achtung, Ausnahme im Standard:</b> Am Fr 6.11. um 12 Uhr ist es in Zürich (5,7 °C) kälter als in Zermatt (5,9 °C). Die App zeigt dann «Heute passt es nicht ganz» und den Hinweis auf Nebel im Mittelland. Bei allen anderen Zeitpunkten in der Tabelle ist Zermatt am kältesten und die Reihenfolge stimmt. Entscheide vorher: Standard so lassen (gute Diskussion: «Warum hier nicht?») oder die Kinder auf 8 oder 16 Uhr stellen lassen.</div>
<h2><span>3</span>Lösung</h2>
<div class=box><b>Am kältesten:</b> in der Regel <b>Zermatt</b> (am höchsten). <b>Je höher der Ort, desto kälter.</b><br>Beispiel Fr 6.11., 8 Uhr: Lugano − Zermatt = 10,1 − 2,2 = <b>7,9 °C</b>. Beispiel Do 12.11., 12 Uhr: 11,4 − 5,9 = <b>5,5 °C</b>.</div>
<p class=m>Die Faustregel im Beweisstück (0,6 °C pro 100 m, rund 8 °C von Lugano bis Zermatt) ist ein Durchschnittswert. Einzelne Messungen weichen ab.</p>
<h2><span>4</span>Beweisstück 3: «Warum wird es oben kälter?» (Test-Lernziel)</h2>
<ul><li>Je höher man kommt, desto <b>geringer wird der Luftdruck</b>. Über einem hat es weniger Luft.</li><li>Steigt Luft auf, <b>dehnt sie sich aus</b>.</li><li>Dafür braucht sie Energie. Ihre Temperatur sinkt: <b>Die Luft wird kälter.</b></li><li>Pro 100 m höher etwa <b>0,6 °C</b> kälter. Das Fachwort (adiabatische Abkühlung) müssen die Kinder nicht kennen.</li><li>Zusatz: Lugano liegt südlich der Alpen. Die Berge halten oft kalte Luft aus dem Norden ab.</li></ul>
<h2>KM 54.3, Lösungen</h2>
<p><b>Aufgabe 1:</b> Lugano: Tessin, 275 m. Zürich: Zürich, 408 m. Zermatt: Wallis, 1608 m ü. M.<br><b>Aufgabe 2:</b> Wärmste / kälteste Temperatur / höchster Niederschlag: Lugano 27 °C / 1 °C / 190 mm · Zürich 24 °C / −2 °C / 130 mm · Zermatt 20 °C / −8 °C / 75 mm. Die zwei wärmsten Monate: Juli und August. Der kälteste Monat: Januar. Am meisten Niederschlag: Lugano.<br><b>Aufgabe 3:</b> Je höher ein Ort liegt, desto kälter ist es. Südlichere Orte sind tendenziell wärmer.</p>
<div class=w><b>Höhenangaben:</b> KM 54.3 nennt 275 m, 408 m und 1608 m (Orte). Die App zeigt die Höhen der <b>Messstationen</b> (Lugano 273 m, Fluntern 556 m, Zermatt 1638 m), weil die Temperatur dort gemessen wird. Wenn Kinder nachfragen: «Ort und Messstation liegen nicht auf genau gleicher Höhe.»</div>
{SRC}''')
for n,t,b in [(1,'Der_warme_Tag',a1),(2,'Zwei_Tage',a2),(3,'Drei_Orte',a3)]:
    render(f'<!doctype html><meta charset=utf-8><style>{CSS}</style><body>'+b,f'out/Loesungsdossier_Akte0{n}_{t}_LP.pdf')
