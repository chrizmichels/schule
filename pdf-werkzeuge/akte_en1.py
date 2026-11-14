src=open('akten11.py').read().split("render(doc(")[0]
exec(src)

LINK='425.co/e'; SHORT='425.co/e'; QR=qrsvg(LINK)
def hc(n,t): return f'<div class=cover><span class=tabz>Aktenzeichen 4b.E.{n}</span><div class=stamp>Streng<b>GEHEIM</b>Energie</div><div class=lbl>Kommissariat 4b · Energie · Akte 0{n}</div><h1>{t}</h1><div class=nm>Name:</div></div>'
KAP[1]={'t':'Der Fall der verschwundenen Wärme','i':['Tim Thermo kommt aus dem Gang ins Kommissariat und reibt sich die Hände. «Chefin! Im Gang habe ich gefroren. Im Zimmer ist es warm. Aber die Heizung läuft doch überall!»','Klara Klima lächelt. «Gute Frage, Tim. <b>Wohin geht die Wärme?</b> Das müssen wir herausfinden. Wir messen im Schulhaus. Aber zuerst vermuten wir.»'],'a':['Klara Klima legt ihre Notizen auf den Tisch. «Ich weiss, wohin die Wärme geht. Sie geht immer dorthin, wo es <b>kälter</b> ist.»','«Die Heizung macht die Luft im Zimmer warm. Aber die Wärme bleibt nicht dort. Sie wandert durch Fenster, Wände und Türen nach draussen. Sie wandert auch durch die offene Tür in den kühleren Gang.»','«Und das Fenster?», fragt Tim. «Glas lässt Wärme leichter durch als eine Wand. Darum ist es am Fenster oft kühler. Ein <b>gekipptes Fenster</b> lässt den ganzen Tag Wärme hinaus. Die Wände kühlen dabei aus.»','«Was können wir tun?» «Zum Lüften das Fenster <b>ganz öffnen, kurz und kräftig</b>. Nach der Lektion einmal, dann wieder schliessen. Das heisst <b>Stosslüften</b>. Und bei Kälte: Türen zu.»','Tim schreibt in sein Heft: <b>Fall gelöst!</b>']}
BW[1]={'t':'Wohin geht die Wärme?','m':['Wärme geht immer dorthin, wo es kälter ist.','Durch offene Türen und gekippte Fenster geht viel Wärme verloren.','Stosslüften: ganz öffnen, kurz und kräftig, dann wieder schliessen.'],'src':['Thermometer','Energie']}
orte=['Klassenzimmer (Mitte)','bei der Heizung','beim Fenster','im Gang']
verm='<table class=mt><tr><th style="text-align:left">Ort</th><th style="width:60mm">Platz (1 = am kältesten, 4 = am wärmsten)</th></tr>'+''.join(f'<tr><td class=lab style="width:auto;font-family:AtkH;text-align:left">{o}</td><td class=v2 style="width:60mm;height:8mm"></td></tr>' for o in orte)+'</table>'
mess='<table class=mt><tr><th style="text-align:left">Ort</th><th style="width:45mm">Temperatur</th><th style="width:50mm">Platz (1 = am kältesten)</th></tr>'+''.join(f'<tr><td class=lab style="width:auto;font-family:AtkH;text-align:left">{o}</td><td class=v2 style="width:45mm;height:8.5mm;text-align:right;padding-right:4mm;font:12pt AtkH">°C</td><td class=v2 style="width:50mm;height:8.5mm"></td></tr>' for o in orte)+'</table>'
p1=pg(hc(1,'Warm und kalt'),kap(1),
 sec(1,'Vermuten'),
 f"<p class=ro><b>Wo im Schulhaus ist es am kältesten?</b> Ordne die vier Orte von 1 bis 4.</p>{verm}<p class=ro>Ich vermute das, weil</p>{ln(2,8)}",
 sec(2,'Spuren sichern'),
 app(1,'Hake die Vermutung ab. Die <b>Messregeln</b> stehen in der App. Ihr messt zu dritt mit <b>einem</b> Thermometer.'),
 f"<p class=ro style='margin-top:1mm'></p>{mess}",
 f"<p class=ro>{cb('Ich habe an allen vier Orten gemessen.')}</p>")
p2=pg(bar(1,'Warm und kalt'),
 sec(3,'Die Lösung'),
 f"<p class=ro>In der App: <b>Lösung zeigen</b>. Schau auf deine vier Zahlen.</p>",
 f"<p class=ro>Am kältesten war es {bl(52)}.<br>Am wärmsten war es {bl(52)}.<br>Unterschied: {bl(16)} °C.</p>",
 f"<p class=ro><b>Hat meine Vermutung gestimmt?</b><br>{cb('Ja')} {cb('Fast')} {cb('Nein')}</p>",
 sec(4,'Beweisstück lesen, dann denk nach'),
 bw(1,1),
 f"<p class=ro><b>Wohin geht die Wärme? Wie können wir Wärme sparen?</b> Schreib deine Antwort mit eigenen Worten auf die Linien.</p>{ln(5,11)}")
css=open('akten11.py').read().split("css='''")[1].split("'''")[0].replace("FILE:","fonts/node_modules/@fontsource/")
render(doc(p1+p2,css),'out/Energie_Akte01_Warm_und_kalt_A4.pdf')
