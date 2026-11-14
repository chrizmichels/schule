src=open('akten11.py').read().split("render(doc(")[0]
exec(src)
extra='''
.hint{font-size:10.5pt;color:var(--muted);margin:0}
.need{background:#fbfaf6;border:1px solid var(--edge);border-left:2mm solid var(--ink);border-radius:2mm;padding:2mm 4mm;margin:3mm 0 1mm;font-size:11.5pt;line-height:1.45}
.q{margin:4.5mm 0 0;font-size:12.5pt;line-height:1.55}
.q .n{display:inline-block;background:var(--ink);color:#fbfaf6;font:700 9pt "CP";min-width:6.5mm;text-align:center;border-radius:1.5mm;padding:.4mm 0;margin-right:2mm}
.wb{display:inline-block;background:#f6edc8;border-radius:1.5mm;padding:.6mm 3mm;margin:0 1.5mm 0 0;font:700 11pt "AtkH"}
.sp{background:#fffdf2;border:1px solid var(--edge);border-left:2mm solid #b3302a;border-radius:1.5mm;padding:2mm 4mm;margin:2mm 0;font-size:11pt;line-height:1.4}
.sp p{margin:.8mm 0}
.star{font-weight:700;color:#8a5a00}
.lo td,.lo th{font-size:10.5pt}
.sol{font-size:11pt;line-height:1.4}.sol p{margin:1mm 0}
.sol h3{font:700 13pt "Zilla Slab";margin:3mm 0 1mm}
.lo2{width:100%;border-collapse:collapse;margin:1.5mm 0;font-family:"CP";font-size:10pt}
.lo2 th,.lo2 td{border:1px solid var(--edge);padding:1mm 1.5mm;text-align:center}.lo2 th{background:var(--folder)}
.lo2 td.l{text-align:left;font-weight:700;background:#fbfaf6}
.flag{background:#f6edc8;border-radius:1.5mm;padding:1.5mm 3mm;margin-top:2mm;font-size:10.5pt}
'''
def Q(n,t): return f'<p class=q><span class=n>{n}</span>{t}</p>'
def head(t,sub): return f'<div class=cover><span class=tabz>Wiederholung</span><div class=stamp>Fall<b>lösen</b>allein</div><div class=lbl>Kommissariat 4b · {sub}</div><h1>{t}</h1><div class=nm>Name:</div></div>'
red='<b style="color:#d62828">rote</b>';blue='<b style="color:#1d4ed8">blaue</b>'
f1=pg(head('Fall 1: Der warme Tag','Wiederholung'),
 f'<div class=need><b>Das brauchst du:</b> dein ausgefülltes <b>KM 54.2</b> (Tabelle und Kurven), deine <b>Akte 01</b> (Papier), ein Tablet und einen Stift. Du hast Fall 1 schon bearbeitet. Jetzt löst du ihn noch einmal und kontrollierst dich selbst.</div>',
 sec(1,'Allein lösen (ohne Tablet)'),
 f'<p class=ro>Du untersuchst <b>Tag 1: Freitag, 6. November</b>. Das ist deine {red} Zeile auf KM 54.2.</p>',
 Q(1,f'Am <b>wärmsten</b> war es um {bl(14)} Uhr: {bl(14)} °C.<br>Am <b>kältesten</b> war es um {bl(14)} Uhr: {bl(14)} °C.'),
 Q(2,f'Wie viel wärmer war es am wärmsten Zeitpunkt als um 8 Uhr?<br>Rechnung: {bl(56)} = {bl(14)} °C'),
 sec(2,'Mit dem Tablet kontrollieren'),
 app(1,'Hake die ersten Kästchen ab. Du hast das schon auf Papier gemacht.'),
 Q(3,f'Bei «Spuren sichern»: Vergleiche die Temperaturen in der App mit deiner Zeile <b>Tag 1</b> auf KM 54.2. Verbessere falsche Zahlen mit einer anderen Farbe.<br>{cb("Alle Zahlen haben gestimmt.")}<span class=cbx><i></i>Ich habe {bl(10)} Zahlen verbessert.</span>'),
 Q(4,f'Tippe auf <b>«Lösung zeigen»</b>. Vergleiche mit Schritt 1.<br>{cb("Meine Antworten stimmen.")}{cb("Ich habe sie verbessert.")}<br><b>Hat meine Vermutung in Akte 01 gestimmt?</b> {cb("Ja")}{cb("Fast")}{cb("Nein")}'),
 sec(3,'Beweisstück lesen, dann in eigenen Worten'),
 Q(5,'Lies in der App das <b>Beweisstück</b>. Lege dann das Tablet weg. Schreib <b>ohne abzuschreiben</b>: <b>Was macht die Luft warm? Warum war es am Morgen noch kalt?</b>')+ln(3,11))
f2=pg(f'<div class=bar><span class=lbl>Fall 2 · Zwei Tage · Wiederholung</span><span class=nm2>Name:</span></div>',
 f'<div class=need style="margin-top:3mm"><b>Das brauchst du:</b> <b>KM 54.2</b>, deine <b>Akte 02</b> (Papier), ein Tablet und einen Stift.</div>',
 sec(1,'Allein lösen (ohne Tablet)'),
 f'<p class=ro>Du vergleichst {red} (Tag 1, Freitag 6. November) und {blue} (Tag 2, Donnerstag 12. November).</p>',
 Q(1,'<b>Welcher Tag war wärmer?</b> Vergleiche Spalte für Spalte, von 8 bis 20 Uhr.<br>Tag '+bl(12)+' war wärmer, an '+bl(10)+' von 7 Zeiten.'),
 Q(2,f'<b>Wie viele Grad Unterschied gibt es um 12 Uhr?</b><br>Tag 1: {bl(12)} °C &nbsp; Tag 2: {bl(12)} °C &nbsp; Unterschied: {bl(12)} °C'),
 sec(2,'Mit dem Tablet kontrollieren'),
 app(2,'Hake die ersten Kästchen ab. Du hast das schon auf Papier gemacht.'),
 Q(3,f'Vergleiche die Temperaturen von <b>Tag 2</b> in der App mit deiner {blue} Zeile auf KM 54.2. Verbessere falsche Zahlen mit einer anderen Farbe.<br>{cb("Alle Zahlen haben gestimmt.")}<span class=cbx><i></i>Ich habe {bl(10)} Zahlen verbessert.</span>'),
 Q(4,f'Tippe auf <b>«Lösung zeigen»</b>. Vergleiche mit Schritt 1 und mit deinen Kurven.<br>{cb("Meine Antworten stimmen.")}{cb("Meine Kurven sehen so aus.")}<br><b>Hat meine Vermutung in Akte 02 gestimmt?</b> {cb("Ja")}{cb("Fast")}{cb("Nein")}'),
 sec(3,'Spuren und Beweisstück, dann in eigenen Worten'),
 Q(5,'Lies in der App die <b>Spuren vom Wetter</b> und das <b>Beweisstück</b>. Lege dann das Tablet weg. Schreib <b>ohne abzuschreiben</b>:<br><b>Was war an den beiden Tagen anders? Was machen Wolken, Wind und Nebel mit der Temperatur?</b>')+ln(4,10.5))
def tab():
    t1=['4,2','5,3','5,7','6,7','6,5','6,1','6,3'];t2=['9,6','9,5','10,1','10,1','9,4','9,7','9,7']
    h='<table class=lo2><tr><th></th>'+''.join(f'<th>{x} Uhr</th>' for x in hours)+'</tr>'
    h+='<tr><td class=l style="color:#d62828">Tag 1 · Fr 6.11.</td>'+''.join(f'<td>{v}</td>' for v in t1)+'</tr>'
    h+='<tr><td class=l style="color:#1d4ed8">Tag 2 · Do 12.11.</td>'+''.join(f'<td>{v}</td>' for v in t2)+'</tr></table>'
    return h
s1=pg(f'<div class=bar><span class=lbl>Lösung · Fall 1 und 2 · Wiederholung</span><span class=nm2 style="border:0"></span></div>',
 '<div class=sol><p class=hint style="margin-top:2mm">Selbstkontrolle: mit einer anderen Farbe verbessern. Ein Wert darf um 0,1 °C abweichen (Anzeige rundet). Quelle der Zahlen: Wetter-Anzeige, Station Zürich-Fluntern (MeteoSchweiz).</p>'
 '<h3>Zahlen zum Vergleichen (KM 54.2)</h3>'+tab()+
 '<h3>Fall 1: Der warme Tag (Tag 1)</h3>'
 '<p><b>1.</b> Am wärmsten um <b>14</b> Uhr: <b>6,7</b> °C. Am kältesten um <b>8</b> Uhr: <b>4,2</b> °C.</p>'
 '<p><b>2.</b> 6,7 − 4,2 = <b>2,5 °C</b> wärmer.</p>'
 '<p><b>5. In eigenen Worten (Beispiel):</b> Die Sonne wärmt den Boden. Der Boden wärmt die Luft darüber. Am Morgen war der Boden noch kalt von der Nacht. Darum ist es oft erst am Nachmittag am wärmsten. <small>(Sinn zählt, nicht der genaue Wortlaut.)</small></p>'
 '<h3>Fall 2: Zwei Tage</h3>'
 '<p><b>1.</b> Tag <b>2</b> war wärmer, an <b>7</b> von 7 Zeiten.</p>'
 '<p><b>2.</b> Um 12 Uhr: Tag 1: <b>5,7</b> °C, Tag 2: <b>10,1</b> °C, Unterschied: <b>4,4 °C</b>.</p>'
 '<p><b>5. In eigenen Worten (Beispiel):</b> Die Sonne schien an beiden Tagen etwa gleich stark. An Tag 2 war es windiger. Der Wind bringt Luft von anderswo, hier warme Luft. Wolken halten die Sonnenstrahlen ab, dann bleibt es kühler. Nebel ist eine Wolke direkt am Boden, auch dann bleibt es kühler. <small>(Auch andere Begründungen mit den Spuren zählen.)</small></p></div>')
render(doc(f1+f2+s1,css+extra),'out/Klimadetektive_Wiederholung_Fall1-2_A4.pdf')
