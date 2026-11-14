src=open('akten11.py').read().split("render(doc(")[0]
exec(src)

LINK='freiday-4b.vercel.app/energie'; QR=qrsvg(LINK)
def hc(n,t): return f'<div class=cover><span class=tabz>Aktenzeichen 4b.E.{n}</span><div class=stamp>Streng<b>GEHEIM</b>Energie</div><div class=lbl>Kommissariat 4b · Energie · Akte 0{n}</div><h1>{t}</h1><div class=nm>Name:</div></div>'
KAP[2]={'t':'Der Fall der hungrigen Geräte','i':['Nach der Schule. Tim Thermo räumt im Kommissariat auf. Er schaut auf die Steckerleiste. «Chefin! Der Beamer ist aus. Aber ein rotes Lämpchen leuchtet noch.»','Klara Klima nickt. «Gute Beobachtung, Tim. Geräte brauchen Strom. Aber <b>welches Gerät braucht am meisten?</b> Das lesen wir ab. Auf jedem Gerät steht eine Zahl mit <b>W</b>. Aber zuerst vermuten wir.»'],'a':['Klara Klima legt vier Zettel nebeneinander. «Die Zahl mit W heisst <b>Watt</b>. Sie sagt, wie viel Strom ein Gerät braucht, wenn es läuft. Mehr Watt heisst: mehr Strom.»','«Und wenn das Gerät nur im Standby ist?», fragt Tim. «Auch dann brauchen viele Geräte noch Strom. Rund um die Uhr. Das rote Lämpchen zeigt es.»','«Es zählt auch, wie lange ein Gerät läuft», sagt Klara. «Wenig Watt und lange Zeit können viel Strom sein. Viel Watt und kurze Zeit auch.»','«Was können wir tun?» «Licht aus. Geräte <b>ganz</b> ausschalten. Ladegeräte aus der Steckdose ziehen. Bei vielen Geräten hilft eine Steckerleiste mit Schalter.»','Tim schreibt in sein Heft: <b>Fall gelöst!</b>']}
BW[2]={'t':'Strom, Watt und Standby','m':['Watt (W) sagt, wie viel Strom ein Gerät braucht, wenn es läuft. Mehr Watt heisst: mehr Strom.','Je länger ein Gerät läuft, desto mehr Strom braucht es. Mit gleich viel Strom kann man etwa 7 Stunden fernsehen oder 50 Stunden am Laptop arbeiten.','Auch im Standby brauchen Geräte Strom. Darum: ganz ausschalten oder den Stecker ziehen.'],'src':['Elektrizität','Stromkreis']}
geraete=['Lampe','Ladegerät','Computer','Beamer']
verm='<table class=mt><tr><th style="text-align:left">Gerät</th><th style="width:60mm">Platz (1 = am wenigsten Strom, 4 = am meisten)</th></tr>'+''.join(f'<tr><td class=lab style="width:auto;font-family:AtkH;text-align:left">{o}</td><td class=v2 style="width:60mm;height:8mm"></td></tr>' for o in geraete)+'</table>'
mess='<table class=mt><tr><th style="text-align:left">Gerät</th><th style="width:45mm">Zahl mit W</th><th style="width:50mm">Platz (1 = am wenigsten)</th></tr>'+''.join(f'<tr><td class=lab style="width:auto;font-family:AtkH;text-align:left">{o}</td><td class=v2 style="width:45mm;height:8.5mm;text-align:right;padding-right:4mm;font:12pt AtkH">W</td><td class=v2 style="width:50mm;height:8.5mm"></td></tr>' for o in geraete)+'</table>'
p1=pg(hc(2,'Strom und Watt'),kap(2),
 sec(1,'Vermuten'),
 f"<p class=ro><b>Welches Gerät braucht am meisten Strom?</b> Ordne die vier Geräte von 1 bis 4.</p>{verm}<p class=ro>Ich vermute das, weil</p>{ln(2,8)}",
 sec(2,'Spuren sichern'),
 app(2,'Hake die Vermutung ab. Die <b>Regeln</b> stehen in der App. Geh zur <b>Geräte-Station</b>. Lies bei <b>Ladegerät, Computer und Beamer</b> die Zahl mit <b>W</b> ab. <b>Nur ablesen.</b> Die <b>Lampe</b> hängt zu hoch: Frag den <b>Hausabwart</b> nach den Watt.'),
 f"<p class=ro style='margin-top:1mm'></p>{mess}",
 f"<p class=ro>{cb('Ich habe alle vier Zahlen und habe sie in der App eingetippt.')}</p>")
p2=pg(bar(2,'Strom und Watt'),
 sec(3,'Die Lösung'),
 f"<p class=ro>In der App: <b>Lösung zeigen</b>. Vergleiche mit deiner Tabelle.</p>",
 f"<p class=ro>Am meisten Strom braucht {bl(52)}.<br>Am wenigsten Strom braucht {bl(52)}.<br>Der grösste Wert ist etwa {bl(14)}-mal so gross wie der kleinste.</p>",
 f"<p class=ro><b>Hat meine Vermutung gestimmt?</b><br>{cb('Ja')} {cb('Fast')} {cb('Nein')}</p>",
 sec(4,'Beweisstück lesen, dann denk nach'),
 bw(2,2),
 f"<p class=ro><b>Was heisst W? Wie kann ich zu Hause Strom sparen?</b> Schreib deine Antwort mit eigenen Worten auf die Linien.</p>{ln(5,11)}")
css=open('akten11.py').read().split("css='''")[1].split("'''")[0].replace("FILE:","fonts/node_modules/@fontsource/")
render(doc(p1+p2,css),'out/Energie_Akte02_Strom_und_Watt_A4.pdf')
