# Kurzversion für Kinder: Spatzen-Rundgang (nach Vogelwarte Sempach, Unterrichtselement «Wie vogelfreundlich ist unser Schulgelände?»)
import re
exec(open('einsatz_igel2.py').read().split("p1=pg(")[0])
exec("css="+open('einsatz_igel2.py').read().split("css=",1)[1].split("render(doc(")[0])
css+='''.nm4::after{content:none!important}.t2{width:100%;border-collapse:collapse;margin:1mm 0 2mm}.t2 th,.t2 td{border:.3mm solid var(--g);padding:0 2.5mm;font-size:10.5pt;text-align:left}.t2 th{background:#e3f0e6;height:7mm}.t2 td{height:17.5mm}
.card{border:.3mm solid var(--g);border-left:3mm solid var(--g);border-radius:2mm;background:#f6faf6;padding:3mm 4.5mm;margin:3.6mm 0;font-size:13pt;line-height:1.35}
.card h3{margin:0 0 1mm;font:700 14pt AtkH;color:var(--g)}.card .su{font-size:12pt;margin-top:1.2mm}
.ft3{position:absolute;left:12mm;right:12mm;bottom:6mm;font:700 8pt AtkH;color:var(--g);display:flex;justify-content:space-between;border-top:.3mm solid var(--g);padding-top:1.5mm}
.ideen label{display:block;margin:2.4mm 0;font-size:12pt}.bx{display:inline-block;width:4.8mm;height:4.8mm;border:.4mm solid #000;border-radius:1mm;vertical-align:-1mm;margin-right:2.5mm}'''
def card(n,t,txt,such): return f"<div class=card><h3>{n} · {t}</h3>{txt}<div class=su><b>Das suchen wir:</b> {such}</div></div>"
cover='<div class=cover><span class=tabz>Logbuch 4b · Spatzen-Team</span><div class=sun><b>Wir</b>verbessern<br>die Welt</div><div class=lbl>Rundgang · Kurzversion der Vogelwarte Sempach</div><h1>Der Spatzen-Rundgang</h1><div class=nm3>Unser Team <span style="font-weight:400;font-size:9.5pt">(A, B, C)</span></div><div class=nm3 style="margin-top:1.5mm">A: '+bl(30)+' &nbsp;B: '+bl(30)+' &nbsp;C: '+bl(30)+'</div></div>'
ft=lambda n:f'<div class=ft3><span>Stand: 17.11.2026</span><span>Seite: {n}/2</span></div>'
p1=pg(cover,
 "<p class=ro style='font-size:12.5pt'><b>Ein Spatz braucht fünf Dinge zum Leben.</b> Lest sie durch. Danach sucht ihr sie auf unserem Schulhof.</p>",
 card(1,'Ein Nest','Spatzen wohnen gern an Häusern. Sie bauen ihr Nest in Löchern und Spalten: unter den Ziegeln, im Dach oder in der Hauswand.','Löcher, Spalten, Dachkante.'),
 card(2,'Material fürs Nest','Für das Nest brauchen Spatzen trockenes Gras, Stroh, Wolle und Federn. Dünne Äste helfen auch.','Gras, das stehen bleibt. Einen Haufen mit Ästen.'),
 card(3,'Futter und Wasser','Spatzen fressen am liebsten Körner und Samen. Im Winter finden sie weniger davon. Sie baden gern in Sand oder in Wasser.','Samen, Beeren, eine Sandstelle, einen Brunnen oder eine Pfütze.'),
 card(4,'Verstecke','Spatzen schlafen und verstecken sich in dichten Hecken und Büschen. Dort sind sie sicher vor Katzen und vor dem Sperber (ein Raubvogel).','Dichte Hecken, Büsche, Efeu.'),
 card(5,'Gefahren','Gefährlich sind grosse Fenster, in denen sich Bäume spiegeln: Vögel fliegen dagegen. Gefährlich sind auch Katzen, Abfall und Schnüre und Gift gegen Unkraut.','Grosse spiegelnde Fenster, Abfall, Katzen.'),
 "<p class=sm style='margin-top:3mm'><b>Quelle:</b> Schweizerische Vogelwarte Sempach: «Wie vogelfreundlich ist unser Schulgelände?» (Infoblatt 1 und Artporträt Haussperling), gekürzt und einfach erklärt. vogelwarte.ch</p>",ft(1))
rows=[('1 · Nest','Löcher, Spalten'),('2 · Material fürs Nest','Gras, Äste'),('3 · Futter und Wasser','Samen, Sand, Wasser'),('4 · Verstecke','Hecken, Büsche'),('5 · Gefahren','Fenster, Abfall, Katzen')]
tab="<table class=t2><tr><th style='width:44mm'>Das braucht ein Spatz</th><th>Das haben wir gefunden. Wo?</th><th style='width:50mm'>Wie gut ist es?</th></tr>"+''.join(f"<tr><td><b>{a}</b><br><span style='font-size:9pt'>{b}</span></td><td></td><td style='font-size:10pt'>{cb('gut')}<br>{cb('geht so')}<br>{cb('schlecht')}</td></tr>" for a,b in rows)+"</table>"
ideen=["Einen <b>Asthaufen</b> in einer ruhigen Ecke machen","<b>Laub</b> zu einem Haufen zusammenschieben","Einen Streifen <b>Gras stehen lassen</b>","Die <b>Hecke stehen lassen</b>. Büsche nur im Herbst oder Winter schneiden","<b>Zeichnungen</b> innen an das grosse Fenster kleben (es spiegelt weniger)","Nach der Pause den <b>Abfall einsammeln</b>","Den Hauswart fragen: <b>ohne Gift</b> arbeiten","Eigene Idee: "+bl(60)]
p2=pg(f"<div class=bar><span class=lbl>Spatzen-Rundgang · Unser Rundgang</span><span class=nm2>Team:</span></div>",
 "<p class=ro style='font-size:12pt'><b>1 · Geht über den Schulhof.</b> Sucht die fünf Dinge. Schreibt auf, was ihr findet und wo. Macht ein Häkchen.</p>",tab,
 "<p class=ro style='font-size:12pt;margin-top:3mm'><b>2 · Das können wir einfach ändern.</b> Macht ein Häkchen bei euren Ideen.</p>",
 "<div class=ideen>"+''.join(f"<label><span class=bx></span>{t}</label>" for t in ideen)+"</div>",
 "<div class=card style='margin-top:3mm'><h3>3 · Wir wählen eine Idee</h3>Prüft: Brauchen wir viel Geld? Schaffen wir es in einer Lektion? Hilft es wirklich?<br><b>Wir wählen:</b> "+bl(100)+"<br><b>Wen müssen wir fragen?</b> "+bl(80)+"</div>",
 "<p class=sm style='margin-top:2mm'>Quelle: Schweizerische Vogelwarte Sempach, Infoblatt 3 «Aufwertungsmöglichkeiten», gekürzt.</p>",ft(2))
if __name__=='__main__':
    render(doc(p1+p2,css),'out/10_FreiDay_Spatzen_Rundgang_Kurzversion_A4.pdf')
