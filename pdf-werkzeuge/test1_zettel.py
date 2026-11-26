from lib import render
ziele=[("",[
 "Ich kann ein Thermometer genau ablesen.",
 "Ich kann erklären, warum wir immer zur gleichen Zeit und am gleichen Ort messen.",
 "Ich kann erklären, warum es am Nachmittag am wärmsten ist.",
 "Ich kann in einem Temperatur-Diagramm die höchste Temperatur und die Uhrzeit ablesen.",
 "Ich kann aus einer Tabelle ein Liniendiagramm zeichnen.",
 "Ich kann Orte nach ihrer Höhe vergleichen: Je höher, desto kälter."])]
body=''.join((f'<h2>{t}</h2>' if t else '')+''.join(f'<div class=z><span class=cb></span>{x}</div>' for x in l) for t,l in ziele)
html=f'''<!doctype html><meta charset=utf-8><style>
@page{{size:A4;margin:14mm 16mm}}
body{{font-family:Inter,"Helvetica Neue",Arial,sans-serif;font-size:11.5pt;line-height:1.45;color:#14211f;margin:0}}
.t{{background:#1e7a8c;color:#fff;border-radius:3mm;padding:3mm 5mm}}.t small{{display:block;font-size:9pt;opacity:.9}}.t b{{font-size:17pt}}
.w{{background:#e6f1f3;border:1px solid #1e7a8c;border-radius:3mm;padding:3mm 5mm;margin:5mm 0}}
h2{{font-size:12pt;margin:5mm 0 1.5mm;color:#1e7a8c}}
.z{{display:flex;gap:3mm;align-items:flex-start;margin:1.6mm 0;padding-left:1mm}}
.cb{{flex:none;width:4.5mm;height:4.5mm;border:1.5px solid #14211f;border-radius:1mm;margin-top:.7mm}}
.u{{border-top:1px dashed #888;margin-top:6mm;padding-top:3mm}}
</style><body>
<div class=t><small>NMG · Wetter und Klima</small><b>Lernzielkontrolle: Wetter messen und verstehen</b></div>
<div class=w><b>Wann?</b> Freitag, 4. Dezember 2026, am Morgen (SOL)<br><b>Wie lange?</b> 25 Minuten. Du arbeitest allein und ohne Heft.<br><b>Wie viel?</b> 6 Aufgaben, 12 Punkte.</div>
<p><b>Lernziele.</b> Das musst du für die Lernzielkontrolle können. Hake ein Kästchen ab, wenn du es sicher kannst.</p>
{body}
<div class=u><b>So übst du:</b> Schau deine Blätter KM 54.1, KM 54.2, KM 54.3, deine Akten und dein Messprotokoll an. Zu Akte 01 bis 03 gibt es ein <b>Lösungsdossier</b> zum Lernen. In Schabi findest du eine <b>Probe-Lernzielkontrolle mit Lösungen</b>. Löse sie und kontrolliere danach. Online kannst du jederzeit auf <b>425.co/detektive#lern</b> üben. Dort bekommst du sofort die Rückmeldung.</div>'''
open('_t.html','w').write(html)
render(html,'out/09_Ankuendigung_Lernzielkontrolle_Fr4.12.pdf')
