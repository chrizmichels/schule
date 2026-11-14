from lib import *
import qrcode
LINK='freiday-4b.vercel.app/einsaetze'
def qrsvg(txt,mm=19):
    m=qrcode.QRCode(border=0,error_correction=qrcode.constants.ERROR_CORRECT_M);m.add_data('https://'+txt);m.make();M=m.get_matrix();n=len(M)
    d=''.join(f'M{x},{y}h1v1h-1z' for y,r in enumerate(M) for x,v in enumerate(r) if v)
    return f'<svg width="{mm}mm" height="{mm}mm" viewBox="0 0 {n} {n}" shape-rendering="crispEdges"><path d="{d}" fill="#000"/></svg>'
QR=qrsvg(LINK)
cb=lambda t:f'<span class=cbx><i></i>{t}</span>'
ln=lambda k=1,h=10.5:f'<div class=ln style="height:{h}mm"></div>'*k
bl=lambda w=18:f'<span class=bl style="min-width:{w}mm"></span>'
def sec(n,t,z): return f'<h2><span class=no>Etappe {n}</span>{t}<span class=zt>{z}</span></h2>'
def pg(*x): return '<div class=page>'+''.join(x)+'</div>'
def bar(t): return f'<div class=bar><span class=lbl>Einsatz 01 · {t}</span><span class=nm2>Team:</span></div>'
cover='<div class=cover><span class=tabz>Logbuch 4b</span><div class=sun><b>Wir</b>verbessern<br>die Welt</div><div class=lbl>Logbuch der 4b · Einsatz 01 · SDG 15</div><h1>Der Igel-Einsatz</h1><div class=nm3>Wir sind: &nbsp;A: '+bl(36)+' &nbsp;B: '+bl(36)+' &nbsp;C: '+bl(36)+'</div></div>'
app=f'<div class=app><div class=q>{QR}</div><div><span class=lbl>App</span><br><b>Geschichte, Klexikon und Tipps</b><br>{LINK}<br>Tippt auf <b>Einsatz 01</b>. Die Antworten findet ihr selbst.</div></div>'
def feld(k,t,auftrag):
    return (f'<div class=rl><div class=rh><span class=rb>{k}</span><b>{t}</b><span class=nm4>Name:</span></div><p class=sm>{auftrag}</p>{ln(4,7.4)}<p class=sm>Gefunden bei (Seite, Suchwort): {bl(70)}</p></div>')
p1=pg(cover,
 sec(1,'Hilferuf','Fr 20.11.'),
 "<p class=ro><b>Das sehen wir</b> (2 Dinge):</p>"+ln(2,8.5),
 "<p class=ro><b>Das vermuten wir:</b> Was könnte im Winter mit dem Igel passieren?</p>"+ln(4,8.5),
 "<p class=ro><b>Zusatz:</b> SDG-Karte, die passt: SDG "+bl(14)+" <b>Darum:</b></p>"+ln(3,8.5),
 f"<p class=ro>{cb('Wir haben unsere Vermutung geschrieben.')}</p>",
 sec(2,'Forschen','Fr 20.11.'),
 "<p class=ro>Jedes Kind forscht an einem Feld. Suche im Klexikon. Du wählst die Suchwörter.</p>",
 feld('A','Essen','Finde heraus: Was frisst ein Igel? Und warum ist das im Herbst besonders wichtig?'),
 app)
p2=pg(bar('Der Igel-Einsatz'),
 feld('B','Schlafen','Finde heraus: Wo schläft ein Igel im Winter? Was passiert dabei in seinem Körper?'),
 feld('C','Helfen','Finde heraus: Wo suchen Igel im Winter einen Schlafplatz? Wie kann man ihnen helfen?'),
 f"<p class=ro>{cb('Alle drei haben ihr Feld dem Team erklärt (1 Minute).')}</p>",
 sec(3,'Plan','Fr 27.11.'),
 "<p class=ro><b>Wie können wir dem Igel im Winter helfen?</b> Schreibt zwei Ideen. Warum hilft sie?</p>",
 "<div class=idl><b>Idee 1:</b>"+ln(2,8)+"<b>Warum hilft sie?</b>"+ln(2,8)+"</div>",
 "<div class=idl><b>Idee 2:</b>"+ln(2,8)+"<b>Warum hilft sie?</b>"+ln(2,8)+"</div>")
def v4(a,b,c,k=2): return f'<div class=v4><b>{a}</b> <small>{b}</small><p class=sm>{c}</p>{ln(k,8)}</div>'
p3=pg(bar('Der Igel-Einsatz'),
 f"<p class=ro><b>Wir entscheiden uns für:</b> {bl(110)}</p>",
 v4('Warum?','Unser Problem','Warum braucht der Igel Hilfe?'),
 v4('Wer?','Wem helfen wir? Wer macht was?','Wer im Team übernimmt welche Aufgabe?'),
 v4('Wie?','Das ist unsere Idee','Was machen wir genau? Wie sieht es aus? (Skizze auf die Rückseite)'),
 v4('Was?','Das machen wir konkret','Was brauchen wir? Wo? Wann? Wen müssen wir fragen?',3),
 '<div class=stp2><span class=lbl>Plan angeschaut (Lehrperson)</span></div>',
 sec(4,'Umsetzen','Fr 4.12.'),
 f"<p class=ro>Wir haben die Erlaubnis von: {bl(80)}</p>",
 f"<p class=ro>{cb('Wir haben nachgesehen: Dort liegt kein Haufen und kein Nest.')}<br>{cb('Wir haben unser Werk gemacht.')} {cb('Foto gemacht.')}</p>",
 "<div class=warn><b>Achtung:</b> Zieh Handschuhe an. Siehst du einen Igel: <b>nicht anfassen.</b> Sag es sofort deiner Lehrperson. Danach den Ort nicht mehr verändern.</div>")
def pf(i): return f'<div class=pf><b>{i}.</b> Frage: {bl(105)}<br>Antwort vom Gast: {bl(100)}</div>'
p4=pg(bar('Der Igel-Einsatz'),
 sec(5,'Prüfen','Fr 11.12.'),
 "<p class=ro>Woran erkennen wir, dass unser Werk gut ist? Schreibt <b>drei Prüffragen</b>. Ein Gast antwortet.</p>",
 pf(1),pf(2),pf(3),
 "<p class=ro><b>Das ist gut:</b> "+bl(120)+"</p>","<p class=ro><b>Das verbessern wir:</b> "+bl(105)+"</p>",
 f"<p class=ro>{cb('Wir haben eine Sache verbessert.')}</p>",
 sec(6,'Bericht','Fr 18.12.'),
 "<p class=ro>Stichworte für den Bericht. Jedes Kind sagt etwas (höchstens 2 Minuten).</p>",
 *[f"<p class=ro style='margin-top:1.5mm'><b>{t}</b></p>"+ln(2,7.5) for t in ['Das haben wir gefragt:','Das haben wir herausgefunden:','Das haben wir gemacht:','Das haben wir geprüft:','Das haben wir gelernt:']],
 f"<p class=ro>{cb('Wir haben der Klasse berichtet.')}</p>")
css=open('akten_css.txt').read().replace("FILE:","fonts/node_modules/@fontsource/")
css+='''
@font-face{font-family:"Hand";font-weight:700;src:url(fonts/node_modules/@fontsource/caveat/files/caveat-latin-700-normal.woff2)}
:root{--folder:#def0e2;--edge:#8fc4a0;--ink:#10301d;--muted:#4d6657;--stamp:#2c7a4b;--g:#2c7a4b;--sun:#f2c14e}
.cover{background:#fff;border:1.4px solid var(--g);border-radius:1mm 4mm 12mm 4mm}
.tabz{background:var(--g);color:#fff;border:0;font:700 8.5pt "AtkH";letter-spacing:.06em}
.cover h1{font:700 36pt "Hand";color:var(--g);line-height:.95}
.sun{position:absolute;right:6mm;top:3mm;width:26mm;height:26mm;border-radius:50%;background:var(--sun);border:1.2mm solid var(--g);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font:700 7.5pt "AtkH";line-height:1.1;transform:rotate(8deg)}
.sun b{font:700 15pt "Hand"}
.bar{background:var(--folder);border-color:var(--edge)}
.no{background:var(--g)}
.zt{margin-left:auto;font:700 9pt "AtkH";color:var(--g);border:1.2px solid var(--g);border-radius:99px;padding:.3mm 3mm}
h2{font:700 15pt "AtkH"}
.qq{font-size:11pt}
.nm3{margin-top:2mm;font:11pt "AtkH";font-weight:700}
.nm2{font:700 12pt "AtkH";border-bottom:1px solid var(--ink);width:70mm;height:6mm;display:inline-block}
.app{background:#fff;border-color:var(--edge);border-left-color:var(--g)}
.rl{border:1.3px solid var(--g);border-radius:2mm 2mm 6mm 2mm;padding:1.5mm 4mm 1mm;margin:2mm 0;background:#fff}
.rh{display:flex;align-items:center;gap:3mm;font-size:12pt}.rb{display:inline-flex;width:8mm;height:8mm;border-radius:50%;background:var(--g);color:#fff;align-items:center;justify-content:center;font:700 14pt "Hand"}
.nm4{margin-left:auto;font:10pt "AtkH"}.nm4::after{content:" ______________________"}
.sm{font-size:10pt;margin:.5mm 0;color:#3d5446}
.v4{border:1.3px solid var(--g);border-radius:2mm 2mm 6mm 2mm;padding:1.5mm 4mm 0;margin:2mm 0;background:#fff}.v4 b{font:700 17pt "Hand";color:var(--g)}.v4 small{font:700 8.5pt "AtkH";text-transform:uppercase;letter-spacing:.06em;color:#3d5446}
.idl{border:1.3px dashed var(--g);border-radius:2mm;padding:1.5mm 4mm 0;margin:2mm 0;font-size:11.5pt;background:#fff}
.stp2{border:1.3px dashed var(--ink);border-radius:2mm;height:11mm;padding:1.5mm 3mm;margin:2mm 0}
.warn{border:1.3px solid #c9661a;background:#fdf1e3;border-radius:2mm;padding:2mm 4mm;margin:2mm 0;font-size:11pt}
.pf{font-size:11.5pt;line-height:2;margin:1.2mm 0;border-bottom:1px dotted var(--edge)}
.page{break-after:page}
'''
render(doc(p1+p2+p3+p4,css),'out/FreiDay_Einsatz01_Igel_Logbuch_A4.pdf')
