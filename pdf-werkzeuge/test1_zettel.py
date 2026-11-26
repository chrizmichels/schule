from lib import render
ziele=[("",[
 "Ich kann ein Thermometer genau ablesen.",
 "Ich kann erklären, warum wir immer zur gleichen Zeit und am gleichen Ort messen.",
 "Ich kann erklären, warum es am Nachmittag am wärmsten ist.",
 "Ich kann in einem Temperatur-Diagramm die höchste Temperatur und die Uhrzeit ablesen.",
 "Ich kann aus einer Tabelle ein Liniendiagramm zeichnen.",
 "Ich kann Orte nach ihrer Höhe vergleichen: Je höher, desto kälter."])]
body=''.join((f'<h2>{t}</h2>' if t else '')+''.join(f'<div class=z><span class=cb></span>{x}</div>' for x in l) for t,l in ziele)
inner=f'''<div class=t><small>NMG · Wetter und Klima</small><b>Lernzielkontrolle: Wetter messen und verstehen</b></div>
<div class=w><b>Wann?</b> Freitag, 4. Dezember 2026, am Morgen (SOL)<br><b>Wie lange?</b> 25 Minuten, allein und ohne Heft<br><b>Wie viel?</b> 6 Aufgaben, 12 Punkte</div>
<p style="margin:0 0 1mm"><b>Das musst du können.</b> Hake ein Kästchen ab, wenn du es sicher kannst.</p>
{body}
<div class=u><b>So übst du:</b> Schau deine Blätter KM 54.1, 54.2, 54.3, deine Akten und dein Messprotokoll an. Zu Akte 01 bis 03 gibt es ein <b>Lösungsdossier</b>. In Schabi findest du eine <b>Probe-Lernzielkontrolle mit Lösungen</b>. Online üben mit sofortiger Rückmeldung: <b>425.co/detektive#lern</b></div>'''
html=f'''<!doctype html><meta charset=utf-8><style>
@page{{size:A4;margin:0}}
body{{font-family:Inter,"Helvetica Neue",Arial,sans-serif;font-size:11.5pt;line-height:1.4;color:#14211f;margin:0}}
.s{{height:148mm;box-sizing:border-box;padding:9mm 14mm 6mm;overflow:hidden}}
.cut{{height:0;border-top:1px dashed #888;position:relative}}
.cut::after{{content:"✂";position:absolute;left:4mm;top:-3.2mm;font-size:10pt;color:#666;background:#fff;padding:0 1mm}}
.t{{background:#1e7a8c;color:#fff;border-radius:3mm;padding:2.5mm 5mm}}.t small{{display:block;font-size:8.5pt;opacity:.9}}.t b{{font-size:15pt}}
.w{{background:#e6f1f3;border:1px solid #1e7a8c;border-radius:3mm;padding:2.5mm 5mm;margin:3mm 0;font-size:11pt}}
.z{{display:flex;gap:3mm;align-items:flex-start;margin:1.2mm 0;padding-left:1mm}}
.cb{{flex:none;width:4.2mm;height:4.2mm;border:1.5px solid #14211f;border-radius:1mm;margin-top:.5mm}}
.u{{border-top:1px dashed #888;margin-top:3mm;padding-top:2mm;font-size:10.5pt}}
</style><body><div class=s>{inner}</div><div class=cut></div><div class=s>{inner}</div>'''
open('_t.html','w').write(html)
render(html,'out/09_Ankuendigung_Lernzielkontrolle_Fr4.12.pdf')
