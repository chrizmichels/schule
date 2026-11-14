from lib import *
import qrcode
LINK='425.co/k'; SHORT='425.co/k'
def qrsvg(txt,mm=19):
    m=qrcode.QRCode(border=0,error_correction=qrcode.constants.ERROR_CORRECT_M);m.add_data('https://'+txt);m.make();M=m.get_matrix();n=len(M)
    d=''.join(f'M{x},{y}h1v1h-1z' for y,r in enumerate(M) for x,v in enumerate(r) if v)
    return f'<svg width="{mm}mm" height="{mm}mm" viewBox="0 0 {n} {n}" shape-rendering="crispEdges"><path d="{d}" fill="#000"/></svg>'
QR=qrsvg(LINK)
def hc(n,t): return f'<div class=cover><span class=tabz>Aktenzeichen 4b.K.{n}</span><div class=stamp>Streng<b>GEHEIM</b>Wetter</div><div class=lbl>Kommissariat 4b · Akte 0{n}</div><h1>{t}</h1><div class=nm>Name:</div></div>'
cb=lambda t:f'<span class=cbx><i></i>{t}</span>'
ln=lambda k=1:'<div class=ln></div>'*k
bl=lambda w=18:f'<span class=bl style="min-width:{w}mm"></span>'
def app(n,txt): return f'<div class=app><div class=q>{QR}</div><div><span class=lbl>Spur</span><br><b>Öffne die App:</b> <span class=short>{SHORT}</span><br>Tippe auf <b>Akte 0{n}</b>.<br>{txt}</div></div>'
import sys
sys.path.insert(0,'.')
from kap import KAP
BW={1: {'t': 'Wer macht die Luft warm?', 'p': ['Spur gefunden! Der Täter ist <b>die Sonne</b>.', 'Ihre Strahlen treffen auf den Boden. Der Boden wird warm. Dann wärmt der warme Boden die Luft darüber. Warme Luft steigt auf.', 'Am Morgen ist der Boden noch kalt von der Nacht. Darum ist die Luft kühl. Mittags scheint die Sonne am stärksten. Der Boden wird noch weiter warm, auch nach dem Mittag. Darum ist es oft erst am <b>Nachmittag</b> am wärmsten. Am Abend scheint die Sonne kaum noch. Der Boden gibt Wärme ab. Die Luft wird kühler.'], 'src': ['Wind'], 'm': ['Die Sonne wärmt den Boden.', 'Der Boden wärmt die Luft.', 'Am wärmsten ist es oft am Nachmittag.']}, 2: {'t': 'Wolken, Wind und Nebel', 'p': ['Zwei Tage, zwei Kurven. Wer hat den Unterschied gemacht? Es gibt drei Verdächtige:', '<b>Wolken:</b> Sie bestehen aus winzigen Wassertröpfchen. Sie halten die Sonnenstrahlen ab. Dann kommt weniger Wärme zum Boden. Der Tag bleibt kühler.', '<b>Wind:</b> Er bringt Luft von anderswo. Kommt sie aus dem kalten Norden, wird es kälter. Kommt sie aus dem warmen Süden, wird es wärmer.', '<b>Nebel:</b> Nebel ist eine Wolke direkt am Boden. Im Herbst liegt oft Nebel über Zürich. Die Sonne kommt kaum durch. Dann bleibt es kühl.'], 'src': ['Wind', 'Wolke', 'Nebel'], 'm': ['Viel Sonne: wärmer. Wolken oder Nebel: kühler.', 'Der Wind bringt warme oder kalte Luft.']}, 3: {'t': 'Warum wird es oben kälter?', 'p': ['Drei Hinweise:', '<b>Hinweis 1:</b> Je höher du kommst, desto kleiner ist der Luftdruck: Es drückt weniger Luft von oben. Luft, die aufsteigt, dehnt sich darum aus. Dabei wird sie <b>kälter</b>. (Beim Velopumpen ist es umgekehrt: Wird Luft zusammengedrückt, wird sie warm.) Dazu kommt: Die Wärme kommt vom Boden. Oben ist die Luft dünner und behält weniger davon.', '<b>Hinweis 2:</b> Pro 100 Meter höher wird es etwa <b>0,6 °C</b> kälter. Von Lugano (273 m) bis Zermatt (1638 m) sind es etwa 1400 Meter. Das gibt rund <b>8 °C</b> Unterschied.', '<b>Hinweis 3:</b> Lugano liegt im Tessin, südlich der Alpen. Die Berge halten oft kalte Luft aus dem Norden ab. Darum ist es dort oft milder.'], 'src': ['Wolke', 'Atmosphäre'], 'm': ['Je höher, desto kälter.', 'Aufsteigende Luft dehnt sich aus und wird kälter.', 'Pro 100 m etwa 0,6 °C kälter.']}}
def bw(n,k):
    d=BW[k];return ('<div class=bw><span class=bwtag>Beweisstück %d</span><b class=bwh>%s</b>'%(n,d['t']))+''.join(f'<p>{x}</p>' for x in KAP[k]['a'])+'<div class=merk><b>Das merkst du dir:</b> '+' &nbsp;·&nbsp; '.join(d['m'])+'</div><p class=quelle>Mehr dazu im Klexikon (klexikon.zum.de), suche nach: <b>'+', '.join(d['src'])+'</b></p></div>'
def kap(n): return f'<div class=kp><span class=kptag>Kapitel {n}</span><b class=bwh>{KAP[n]["t"]}</b>'+''.join(f'<p>{x}</p>' for x in KAP[n]['i'])+'</div>'
def sec(n,t): return f'<h2><span class=no>Schritt {n}</span>{t}</h2>'
hours=[8,10,12,14,16,18,20]
def grid(rows):
    t='<table class=mt><tr><th></th>'+''.join(f'<th>{h} Uhr</th>' for h in hours)+'</tr>'
    for lab,col in rows: t+=f'<tr><td class=lab style="color:{col}">{lab}</td>'+'<td class=v></td>'*7+'</tr>'
    return t+'</table>'
ln=lambda k=1,h=14:f'<div class=ln style="height:{h}mm"></div>'*k
def bar(n,t): return f'<div class=bar><span class=lbl>Akte 0{n} · {t}</span><span class=nm2>Name:</span></div>'
def pg(*x): return '<div class=page>'+''.join(x)+'</div>'
hours=[8,10,12,14,16,18,20]
def pg1(a,b): return a
a1f=pg(hc(1,'Der warme Tag'),
 kap(1),
 sec(1,'Vermuten'),
 f"<p class=ro>Wir untersuchen <b>Tag 1: Freitag, 6. November</b> (Zeile Tag 1 auf KM 54.2). Gemessen wurde von 8 bis 20 Uhr.<br><b>Um wie viel Uhr war es an Tag 1 am wärmsten?</b> Am Morgen, am Mittag oder am Abend?<br>Ich vermute: Um {bl(22)} Uhr, weil</p>{ln(6)}",
 sec(2,'Spuren sichern'),
 app(1,'Hake in der App die Vermutung ab. Lies die Temperaturen von <b>Tag 1</b> ab. Schreib sie auf <b>KM 54.2</b> in die Zeile <b>Tag 1</b>.'),
 f"<p class=ro>{cb('Ich habe die Temperaturen auf KM 54.2 eingetragen.')}</p>")
a1b=pg(bar(1,'Der warme Tag'),
 sec(3,'Kurve malen'),
 f"<p class=ro>Male auf <b>KM 54.2</b> deine <b style='color:#d62828'>rote Kurve</b> (Tag 1).<br>{cb('Ich habe sie auf KM 54.2 gemalt.')}</p>",
 f"<p class=ro>Dann in der App: <b>Lösung zeigen</b>.</p>",
 sec(4,'Die Lösung'),
 f"<p class=ro>Am wärmsten war es um {bl(20)} Uhr: {bl(18)} °C.</p>",
 f"<p class=ro><b>Hat meine Vermutung gestimmt?</b><br>{cb('Ja')} {cb('Fast')} {cb('Nein')}</p>",
 sec(5,'Beweisstück lesen, dann denk nach'),
 bw(1,1),
 f"<p class=ro><b>Was macht die Luft warm?</b> Schreib deine Antwort auf die Linien.</p>{ln(6)}")
a2f=pg(hc(2,'Zwei Tage'),
 kap(2),
 sec(1,'Vermuten'),
 f"<p class=ro>Du kennst <b>Tag 1</b> schon: Freitag, 6. November (rote Kurve). Neu ist <b>Tag 2</b>: Donnerstag, 12. November.<br><b>Tag 1 oder Tag 2: Welcher Tag war wärmer?</b><br>{cb('Tag 1')} {cb('Tag 2')} {cb('gleich warm')}</p><p class=ro>Ich vermute das, weil</p>{ln(6)}",
 sec(2,'Spuren sichern'),
 app(2,'Hake in der App die Vermutung ab. Lies die Temperaturen von <b>Tag 2</b> ab. Schreib sie auf <b>KM 54.2</b> in die Zeile <b>Tag 2</b>.'),
 f"<p class=ro>{cb('Ich habe die Temperaturen auf KM 54.2 eingetragen.')}</p>")
a2b=pg(bar(2,'Zwei Tage'),
 sec(3,'Kurve malen'),
 f"<p class=ro>Male auf <b>KM 54.2</b> deine <b style='color:#1d4ed8'>blaue Kurve</b> (Tag 2).<br>{cb('Ich habe sie auf KM 54.2 gemalt.')}</p>",
 f"<p class=ro>Dann in der App: <b>Lösung zeigen</b>.</p>",
 sec(4,'Die Lösung'),
 f"<p class=ro>Schreib die Antworten auf <b>KM 54.2</b>: <b>Frage 3</b> und <b>Frage 4</b>.<br>Die App zeigt dir, was richtig ist.</p>",
 f"<p class=ro><b>Hat meine Vermutung gestimmt?</b><br>{cb('Ja')} {cb('Fast')} {cb('Nein')}</p>",
 sec(5,'Beweisstück lesen, dann denk nach'),
 bw(2,2),
 f"<p class=ro><b>Was war an den Tagen anders? Sonne? Wolken? Wind?</b> Die App zeigt dir «Spuren vom Wetter».</p>{ln(5)}")
a3f=pg(hc(3,'Drei Orte'),
 kap(3),
 f"<p class=ro style='margin-top:3mm'>Zuerst: <b>KM 54.3, Aufgabe 1</b> (Kanton und Höhe).</p>",
 sec(1,'Vermuten'),
 f"<p class=ro><b>Wo ist es am kältesten?</b><br>{cb('Lugano')} {cb('Zürich')} {cb('Zermatt')}</p><p class=ro><b>Je höher der Ort, desto</b> {bl(40)} <small>(kälter / wärmer / gleich)</small></p><p class=ro>Ich vermute das, weil</p>{ln(2)}",
 sec(2,'Spuren sichern'),
 app(3,'Hake in der App beide Vermutungen ab. Dein Messzeitpunkt steht unten. Lies die Temperaturen der drei Orte ab. Schreib sie unten in die Tabelle in dieser Akte.'),
 f"<p class=ro>Messzeitpunkt: <b>Tag 1 · Freitag, 6. November · 12 Uhr</b></p>",
 """<table class=mt><tr><th>Ort</th><th>Höhe (von KM 54.3)</th><th>Temperatur</th></tr>
<tr><td class=lab>Lugano</td><td class=v2></td><td class=v2></td></tr>
<tr><td class=lab>Zürich</td><td class=v2></td><td class=v2></td></tr>
<tr><td class=lab>Zermatt</td><td class=v2></td><td class=v2></td></tr></table>""",
 f"<p class=ro>{cb('Ich habe die Temperaturen in meine Akte eingetragen.')}</p>")
a3b=pg(bar(3,'Drei Orte'),
 sec(3,'Die Lösung'),
 f"<p class=ro>In der App: <b>Lösung zeigen</b>.</p>",
 f"<p class=ro>Am kältesten ist es in {bl(30)}.<br>Je höher der Ort, desto {bl(30)}.</p>",
 f"<p class=ro><b>Haben meine Vermutungen gestimmt?</b><br>{cb('Ja')} {cb('Fast')} {cb('Nein')}</p>",
 sec(4,'Beweisstück lesen, dann denk nach'),
 bw(3,3),
 f"<p class=ro><b>Warum ist es oben anders als unten?</b> Das ist auch <b>Frage 3 auf KM 54.3</b>.</p>{ln(7)}")
css='''
@font-face{font-family:"Zilla Slab";font-weight:600;src:url(FILE:zilla-slab/files/zilla-slab-latin-600-normal.woff2)}
@font-face{font-family:"Zilla Slab";font-weight:700;src:url(FILE:zilla-slab/files/zilla-slab-latin-700-normal.woff2)}
@font-face{font-family:"AtkH";font-weight:400;src:url(FILE:atkinson-hyperlegible/files/atkinson-hyperlegible-latin-400-normal.woff2)}
@font-face{font-family:"AtkH";font-weight:700;src:url(FILE:atkinson-hyperlegible/files/atkinson-hyperlegible-latin-700-normal.woff2)}
@font-face{font-family:"CP";font-weight:400;src:url(FILE:courier-prime/files/courier-prime-latin-400-normal.woff2)}
@font-face{font-family:"CP";font-weight:700;src:url(FILE:courier-prime/files/courier-prime-latin-700-normal.woff2)}
:root{--folder:#e7d6ae;--edge:#cdb886;--ink:#1c2420;--muted:#5b6660;--stamp:#b3302a;--desk:#eef0ed}
.page{padding:12mm 18mm 0;font-family:"AtkH",sans-serif;color:var(--ink)}
.cover{position:relative;background:var(--folder);border:1px solid var(--edge);border-radius:1mm 4mm 4mm 4mm;padding:3.5mm 7mm 3mm;margin-top:6mm}
.tabz{position:absolute;top:-6.2mm;left:-.2mm;background:var(--folder);border:1px solid var(--edge);border-bottom:0;border-radius:2.5mm 2.5mm 0 0;padding:1mm 4mm .6mm;font:8.5pt "CP"}
.lbl{font:700 8.5pt "CP";letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.cover h1{font:700 28pt "Zilla Slab",serif;margin:0;line-height:1.05}
.stamp{position:absolute;right:7mm;top:5mm;border:1.3mm solid var(--stamp);color:var(--stamp);font:700 8.5pt "CP";letter-spacing:.12em;padding:1mm 3mm;border-radius:1.5mm;transform:rotate(-8deg);text-align:center;line-height:1.15;opacity:.85}
.stamp b{display:block;font-size:17pt;letter-spacing:.04em}
.bar{display:flex;justify-content:space-between;align-items:center;background:var(--folder);border:1px solid var(--edge);border-radius:2mm 4mm 4mm 4mm;padding:3mm 6mm;margin-top:2mm}
.nm2{font:700 12pt "AtkH";border-bottom:1px solid var(--ink);width:70mm;height:6mm;display:inline-block}
.nm{margin:2mm 0 0;font:700 12pt "AtkH";border-bottom:1px solid var(--ink);width:100mm;height:6mm}
h2{font:700 15pt "Zilla Slab",serif;margin:3.5mm 0 1mm;display:flex;align-items:center;gap:3mm}
.no{display:inline-block;background:var(--ink);color:#fbfaf6;font:700 8pt "CP";letter-spacing:.1em;text-transform:uppercase;padding:1mm 2.5mm;border-radius:1.5mm}
.ro{font-size:12.5pt;line-height:1.55;margin:0}
.cbx{display:inline-flex;align-items:center;gap:2mm;margin-right:6mm;white-space:nowrap}
.cbx i{display:inline-block;width:6mm;height:6mm;border:1.5px solid var(--ink);border-radius:1.2mm;background:#fff}
.bl{display:inline-block;border-bottom:1.5px solid var(--ink);height:7mm;vertical-align:bottom;margin:0 1mm}
.ln{border-bottom:1px solid var(--ink);height:12.5mm}
.app{display:flex;gap:4mm;align-items:center;background:#fbfaf6;border:1px solid var(--edge);border-left:2mm solid var(--ink);border-radius:2mm;padding:2mm 4mm;margin:1mm 0 2mm;font-size:11.5pt;line-height:1.4}
.app .q{flex:none;line-height:0}
.short{font-weight:700;font-size:18pt;letter-spacing:.4pt;border:.6mm solid var(--ink);border-radius:1.5mm;padding:0 2mm;background:#fff;white-space:nowrap}
.bw{position:relative;background:#fbfaf6;border:1px solid var(--edge);border-left:2mm solid #b3302a;border-radius:1.5mm;padding:4mm 4mm 2.5mm;margin:5mm 0 3mm;font-size:10.5pt;line-height:1.4}
.bw p{margin:1.2mm 0}.bwh{display:block;font:700 13pt "Zilla Slab";margin-bottom:1mm}
.bwtag{position:absolute;right:3mm;top:-3.2mm;background:#fbfaf6;border:1.2px solid #b3302a;color:#b3302a;font:700 8pt "CP";letter-spacing:.1em;text-transform:uppercase;padding:0 2mm;border-radius:1mm;transform:rotate(-2deg)}
.kp{position:relative;background:#fffdf2;border:1px solid var(--edge);border-left:2mm solid var(--ink);border-radius:1.5mm;padding:3.5mm 4mm 1.5mm;margin:5mm 0 2mm;font-size:10.5pt;line-height:1.35}
.kp p{margin:1mm 0}
.kptag{position:absolute;right:3mm;top:-3.2mm;background:var(--ink);color:#fbfaf6;font:700 8pt "CP";letter-spacing:.1em;text-transform:uppercase;padding:0 2mm;border-radius:1mm}
.quelle{margin:2mm 0 0;font-size:9.5pt;color:#44544f}
.merk{background:#f6edc8;border-radius:1.5mm;padding:1.5mm 3mm;margin-top:2mm}
.mt{width:100%;border-collapse:collapse;margin:2mm 0;font-family:"CP"}
.mt th{font-size:10pt;height:8mm;padding:1mm;border:1px solid var(--edge);background:var(--folder)}
.mt td{border:1px solid var(--edge)}
.mt td.lab{font-size:10.5pt;font-weight:700;padding:1mm 2mm;width:28mm;background:#fbfaf6}
.mt td.v{height:20mm}.mt td.v2{height:13mm;width:50mm}.mt td.c{text-align:center;font-size:12pt}
'''.replace("FILE:","fonts/node_modules/@fontsource/")
render(doc(a1f+a1b+a2f+a2b+a3f+a3b,css),'out/Klimadetektive_Ermittlungsakten_A4.pdf')
