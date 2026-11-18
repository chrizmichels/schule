# Lösungsdossier für Kinder, pro Akte 1 Blatt, im Stil der Papier-Akten (mit «GELÖST»-Stempel).
# Messwerte: MeteoSchweiz (Fluntern, Lugano, Zermatt), gleiche Quelle wie die App, abgerufen am 18.11.2026.
src=open('akten11.py').read().split("render(doc(")[0]
exec(src)
extra='''
.page{padding:9mm 16mm 0}
.ro{font-size:11.2pt;line-height:1.45}
.ro p,.ro{margin:0}
.lo2{width:100%;border-collapse:collapse;margin:1.5mm 0;font-family:"CP";font-size:10.5pt}
.lo2 th,.lo2 td{border:1px solid var(--edge);padding:1mm 1.5mm;text-align:center}.lo2 th{background:var(--folder)}
.lo2 td.l{text-align:left;font-weight:700;background:#fbfaf6}
.ok{background:#f6edc8;border-radius:1.5mm;padding:1.5mm 3.5mm;margin:2mm 0;font-size:11pt}
.sp{background:#fffdf2;border:1px solid var(--edge);border-left:2mm solid #b3302a;border-radius:1.5mm;padding:1.5mm 4mm;margin:2mm 0;font-size:10.5pt;line-height:1.4}
h2{margin:4mm 0 1.5mm}
.bw{margin:4mm 0 2mm}
svg.ch{display:block;margin:1mm 0}
'''
def lcov(n,t): return f'<div class=cover style="margin-top:4mm"><span class=tabz>Lösung zur Akte 0{n}</span><div class=stamp>Akte<b>GELÖST</b>Wetter</div><div class=lbl>Kommissariat 4b · Akte 0{n}</div><h1>{t}</h1><div class=nm>Name:</div></div>'
H=[8,10,12,14,16,18,20]
def fm(x): return f'{x:.1f}'.replace('.',',')
def table(rows,head=None):
    h=head or ['Uhr']+[str(x) for x in H]
    t='<table class=lo2><tr>'+''.join(f'<th>{x}</th>' for x in h)+'</tr>'
    for r in rows: t+='<tr><td class=l>'+r[0]+'</td>'+''.join(f'<td>{x}</td>' for x in r[1:])+'</tr>'
    return t+'</table>'
def chart(series,w=440,h=140):
    L,R,T,B=30,8,6,20;lo,hi=3,11
    X=lambda hh:L+(hh-8)/12*(w-L-R);Y=lambda v:T+(hi-v)/(hi-lo)*(h-T-B)
    s=f'<svg class=ch viewBox="0 0 {w} {h}" width="{w*0.78}" font-family="Courier Prime,monospace" font-size="9">'
    for v in range(lo,hi+1,2): s+=f'<line x1="{L}" x2="{w-R}" y1="{Y(v)}" y2="{Y(v)}" stroke="#d9cba3"/><text x="{L-4}" y="{Y(v)+3}" text-anchor="end">{v}</text>'
    for hh in H: s+=f'<text x="{X(hh)}" y="{h-6}" text-anchor="middle">{hh}</text>'
    for vals,col,dash in series:
        s+='<polyline points="'+' '.join(f'{X(hh)},{Y(v)}' for hh,v in zip(H,vals))+f'" fill="none" stroke="{col}" stroke-width="2.2" {"stroke-dasharray=5,3" if dash else ""}/>'
        s+=''.join(f'<circle cx="{X(hh)}" cy="{Y(v)}" r="2.8" fill="{col}"/>' for hh,v in zip(H,vals))
    return s+'<text x="2" y="9" font-size="8">°C</text></svg>'
T1=[4.2,5.3,5.7,6.7,6.5,6.1,6.3];T2=[9.6,9.5,10.1,10.1,9.4,9.7,9.7]
Q='<p class=quelle style="font-size:9pt;color:#44544f;margin-top:3mm">Messwerte: MeteoSchweiz, Station Zürich-Fluntern. Es sind die gleichen Werte wie in der App.</p>'
d1=pg(lcov(1,'Der warme Tag'),
 sec(1,'Vermuten'),
 '<p class=ro>Hast du eine Vermutung mit «Um … Uhr, weil …» aufgeschrieben? Dann stimmt dein Schritt 1. Eine Vermutung darf falsch sein.</p>',
 sec(2,'Spuren sichern: Tag 1 (Freitag, 6. November)'),
 '<p class=ro>Vergleiche mit deiner Zeile <b>Tag 1</b> auf KM 54.2. Verbessere falsche Zahlen mit einer anderen Farbe.</p>',
 table([['Tag 1 (°C)']+[fm(x) for x in T1]]),
 sec(3,'Kurve malen'),
 chart([(T1,'#d62828',0)]),
 '<p class=ro>Deine <b style="color:#d62828">rote Kurve</b> soll so aussehen. Bis 0,5 °C genau ist gut. Die Kurve steigt bis 14 Uhr und sinkt dann ein wenig.</p>',
 sec(4,'Die Lösung'),
 '<div class=ok><b>Am wärmsten:</b> um <b>14 Uhr</b>, <b>6,7 °C</b>.<br><b>Am kältesten:</b> um <b>8 Uhr</b>, <b>4,2 °C</b>.<br><b>Unterschied:</b> 6,7 − 4,2 = <b>2,5 °C</b> wärmer als um 8 Uhr.</div>',
 sec(5,'Beweisstück: so kannst du es sagen'),
 '<div class=sp><b>Was macht die Luft warm? Warum war es am Morgen noch kalt?</b><br>Die Sonne wärmt den Boden. Der warme Boden wärmt die Luft. Am Morgen war der Boden noch kalt von der Nacht. Auch nach dem Mittag wird er noch wärmer. Darum ist es am <b>Nachmittag</b> am wärmsten.</div>',
 '<p class=ro><b>Hast du es mit eigenen Worten geschrieben?</b> Dann hast du das Beweisstück verstanden.</p>',
 '<div class=ok><b>Zusatz (KM 54.2, Frage 5):</b> Station Fluntern, 6.11., 8:30 Uhr: 4,4 °C. Weicht deine Messung bis etwa 1 °C ab, stimmt sie ungefähr (anderer Ort).</div>','<div class=sp><b>Nachlesen (Klexikon und mehr):</b><ul style="margin:1mm 0 0;padding-left:5mm"><li><a href="https://klexikon.zum.de/wiki/Sonne"><b>klexikon.zum.de/wiki/Sonne</b></a>: Die Sonne strahlt Licht und Wärme aus.</li><li><a href="https://klexikon.zum.de/wiki/Wetter"><b>klexikon.zum.de/wiki/Wetter</b></a>: Zum Wetter gehören Wind, Regen und Schnee. Das alles kommt durch die Sonne.</li><li><a href=\"https://www.meteoschweiz.admin.ch/wetter/wetter-und-klima-von-a-bis-z/temperatur/temperaturabnahme-mit-der-hoehe.html\"><b>MeteoSchweiz: Temperaturabnahme mit der Höhe</b></a>: Die Sonne erwärmt die Erdoberfläche. Die Erdoberfläche gibt die Wärme an die Luft ab.</li></ul></div>',Q)
d2=pg(lcov(2,'Zwei Tage'),
 sec(1,'Vermuten'),
 '<p class=ro>Hast du aufgeschrieben, welcher Tag wärmer war, und warum? Dann stimmt dein Schritt 1. Eine Vermutung darf falsch sein.</p>',
 sec(2,'Spuren sichern: Tag 1 und Tag 2'),
 '<p class=ro>Vergleiche mit deinen Zeilen auf KM 54.2. Verbessere falsche Zahlen mit einer anderen Farbe.</p>',
 table([['<span style="color:#d62828">Tag 1</span> · Fr 6.11.']+[fm(x) for x in T1],['<span style="color:#1d4ed8">Tag 2</span> · Do 12.11.']+[fm(x) for x in T2]]),
 sec(3,'Kurve malen'),
 chart([(T1,'#d62828',0),(T2,'#1d4ed8',1)]),
 '<p class=ro>Deine <b style="color:#1d4ed8">blaue Kurve</b> (Tag 2) liegt ganz über der <b style="color:#d62828">roten</b>.</p>',
 sec(4,'Die Lösung'),
 '<div class=ok><b>KM 54.2, Frage 3:</b> <b>Tag 2</b> war wärmer. An allen <b>7 von 7</b> Zeiten.<br><b>KM 54.2, Frage 4:</b> Um 12 Uhr war Tag 1 <b>5,7 °C</b> und Tag 2 <b>10,1 °C</b>. Unterschied: <b>4,4 °C</b>.</div>',
 '<h2 style="font-size:12pt">Spuren vom Wetter (aus der App)</h2>',
 '<div class=sp><b>Sonne:</b> An beiden Tagen schien die Sonne etwa gleich schwach. Sie erklärt den Unterschied nicht.<br><b>Wind:</b> Am Tag 2 war es windiger (Tag 1: 3 km/h, Tag 2: 6 km/h).</div>',
 sec(5,'Beweisstück: so kannst du es sagen'),
 '<div class=sp><b>Was war an den beiden Tagen anders?</b><br>Die Sonne war gleich. Also war es nicht die Sonne. Am Tag 2 war es windiger. Der Wind bringt Luft von anderswo. Vielleicht war das warme Luft. Ganz sicher wissen wir es nicht.<br><b>Wolken</b> halten Sonnenstrahlen ab, dann bleibt es kühler. <b>Nebel</b> ist eine Wolke am Boden.</div>',
 '<p class=ro><b>Wichtig:</b> Du musst mit den Spuren begründen. Es gibt nicht nur ein richtiges Wort.</p>','<div class=sp><b>Nachlesen (Klexikon und mehr):</b><ul style="margin:1mm 0 0;padding-left:5mm"><li><a href="https://klexikon.zum.de/wiki/Wolke"><b>klexikon.zum.de/wiki/Wolke</b></a>: Eine Wolke besteht aus sehr feinen Wassertröpfchen.</li><li><a href="https://klexikon.zum.de/wiki/Nebel"><b>klexikon.zum.de/wiki/Nebel</b></a>: Nebel ist eine Wolke am Erdboden.</li><li><a href="https://klexikon.zum.de/wiki/Wind"><b>klexikon.zum.de/wiki/Wind</b></a>: Wind ist bewegte Luft. Er entsteht durch Unterschiede im Luftdruck.</li></ul></div>',Q)
d3=pg(lcov(3,'Drei Orte'),
 sec(1,'Vermuten'),
 '<p class=ro>Hast du aufgeschrieben, wo es am kältesten ist, und «Je höher der Ort, desto …»? Dann stimmt dein Schritt 1.</p>',
 sec(2,'Spuren sichern: Beispiele'),
 '<p class=ro>Deine Zahlen hängen vom Tag und von der Zeit ab. Vergleiche mit der passenden Zeile.</p>',
 table([['Tag 1 · 8 Uhr','10,1','4,2','2,2'],['Tag 1 · 12 Uhr','9,3','5,7','5,9'],['Tag 1 · 16 Uhr','10,2','6,5','3,9'],['Tag 2 · 8 Uhr','10,7','9,6','5,2'],['Tag 2 · 12 Uhr','11,4','10,1','5,9'],['Tag 2 · 16 Uhr','11,3','9,4','4,3']],['Temperatur (°C)','Lugano 273 m','Zürich 556 m','Zermatt 1638 m']),
 '<p class=ro style="font-size:9.5pt;color:#44544f">Die App zeigt die Höhe der Messstation. Sie kann etwas anders sein als auf KM 54.3.</p>',
 sec(3,'Die Lösung'),
 '<div class=ok><b>Am kältesten:</b> meistens <b>Zermatt</b>. Es liegt am höchsten.<br><b>Je höher der Ort, desto kälter.</b></div>',
 '<div class=sp><b>Ausnahme:</b> Am Freitag, 6. November um 12 Uhr war es in Zürich (5,7 °C) kälter als in Zermatt (5,9 °C). Das kommt vor, zum Beispiel bei Nebel im Mittelland. Meistens gilt aber: Je höher, desto kälter.</div>',
 '<p class=ro><b>Beispiel für den Unterschied:</b> Am Freitag, 6. November um 8 Uhr: Lugano 10,1 °C, Zermatt 2,2 °C. Unterschied: <b>7,9 °C</b>.</p>',
 sec(4,'Beweisstück: so kannst du es sagen'),
 '<div class=sp><b>Warum wird es oben kälter?</b><br>Je höher man kommt, desto geringer wird der Luftdruck. Über einem hat es weniger Luft. Steigt Luft auf, dehnt sie sich aus. Dabei sinkt ihre Temperatur: Die Luft wird kälter. Pro 100 Meter höher wird es etwa <b>0,6 °C</b> kälter.</div>',
 '<p class=ro><b>Hast du es mit eigenen Worten geschrieben?</b> Dann hast du das Beweisstück verstanden.</p>','<div class=sp><b>Nachlesen (Klexikon und mehr):</b><ul style="margin:1mm 0 0;padding-left:5mm"><li><a href="https://klexikon.zum.de/wiki/Atmosphäre"><b>klexikon.zum.de/wiki/Atmosphäre</b></a>: Die Luft hat ein Gewicht. Das spüren wir als Luftdruck.</li><li><a href="https://klexikon.zum.de/wiki/Wind"><b>klexikon.zum.de/wiki/Wind</b></a>: Hoher und niedriger Luftdruck: Wo sind viele, wo wenige Luftteilchen?</li><li><a href="https://klexikon.zum.de/wiki/Gebirge"><b>klexikon.zum.de/wiki/Gebirge</b></a>: Die Alpen sind ein Hochgebirge.</li><li><a href=\"https://www.meteoschweiz.admin.ch/wetter/wetter-und-klima-von-a-bis-z/temperatur/temperaturabnahme-mit-der-hoehe.html\"><b>MeteoSchweiz: Temperaturabnahme mit der Höhe</b></a>: Steigt Luft auf, dehnt sie sich wegen des abnehmenden Drucks aus. Das braucht Energie. Die Luft wird kühler.</li></ul></div>',Q)
render(doc(d1,css+extra),'out/Loesung_Akte01_Der_warme_Tag_A4.pdf')
render(doc(d2,css+extra),'out/Loesung_Akte02_Zwei_Tage_A4.pdf')
render(doc(d3,css+extra),'out/Loesung_Akte03_Drei_Orte_A4.pdf')
