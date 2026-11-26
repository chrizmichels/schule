"""FreiDay: Pitch-Blatt (Mini-Plan) + Feedback-Karten. Ausgabe: out/FreiDay_Pitch-Blatt_Fr27.11_A4.pdf"""
from lib import render
T='#1e7a8c';INK='#14211f'
def ln(n=1,h=11): return ''.join(f'<div class=ln style="height:{h}mm"></div>' for _ in range(n))
CSS=f'''
@page{{size:A4;margin:12mm 15mm}}
*{{box-sizing:border-box}}
body{{font-family:Inter,"Helvetica Neue",Arial,sans-serif;font-size:11pt;line-height:1.35;color:{INK};margin:0}}
.pg{{height:273mm;overflow:hidden;page-break-after:always;position:relative}}.pg:last-child{{page-break-after:auto}}
.hd{{display:flex;gap:4mm;margin-bottom:3mm}}
.hd .t{{flex:1;background:{T};color:#fff;border-radius:3mm;padding:2.5mm 5mm}}.hd .t small{{display:block;font-size:8.5pt;opacity:.92}}.hd .t b{{font-size:17pt}}
.nm{{display:flex;gap:6mm;margin-bottom:3mm}}.nm div{{flex:1;border-bottom:1.5px solid {INK};padding-bottom:.5mm;font-weight:700}}
.q{{margin:3.2mm 0 0}}.q b{{display:block;margin-bottom:.5mm}}
.ln{{border-bottom:1px solid #9aa;}}
table{{width:100%;border-collapse:collapse;margin-top:1mm}}td,th{{border:1px solid {INK};padding:0 2mm;height:10.5mm;text-align:left;font-size:10pt}}th{{background:#e6f1f3}}
.box{{background:#e6f1f3;border:1px solid {T};border-radius:3mm;padding:2.5mm 4mm;margin:3.5mm 0}}
.box b{{color:{T}}}
.card{{border:1.5px solid {INK};border-radius:3mm;padding:3mm 4mm;margin-bottom:3mm}}
.card h3{{margin:0 0 1mm;font-size:12pt}}.card .r{{display:flex;gap:4mm;align-items:flex-end;margin-bottom:1mm}}
.card .r span{{white-space:nowrap}}.card .r i{{flex:1;border-bottom:1px solid #9aa;height:6mm;display:block}}
.c2{{display:flex;gap:4mm}}.c2>div{{flex:1}}

.nm2{{margin:0 0 1mm}}.nm2 div{{border-bottom:1.5px solid {INK};height:13mm;font-weight:700;font-size:14pt;padding-top:5mm}}
.big{{margin:5mm 0 0;font-size:13pt}}.big b{{display:block;margin-bottom:0}}
.fl{{font-weight:700;margin-top:1.5mm}}.card{{padding:2.5mm 4mm}}
small.h{{color:#4a5a58}}
'''
p1=f'''<div class=pg>
<div class=hd><div class=t><small>FreiDay · Fr 27.11. · Einsatz-Team</small><b>Unser Elevator-Pitch</b></div></div>
<div class=nm2><div>Team:</div></div><div class=nm2><div>Einsatz:</div></div>
<div class=box style="margin-top:3mm"><b>Elevator-Pitch:</b> Du hast nur <b>1 Minute</b>. Sag es kurz und klar. Übe es zuerst im Team.</div>
<div class=big><b>1 · Was machen wir?</b>{ln(3,16)}</div>
<div class=big><b>2 · Bis wann?</b>{ln(2,16)}</div>
<div class=big><b>3 · Warum ist das wichtig?</b>{ln(3,16)}</div>
<div class=box style="margin-top:8mm"><b>So sagst du es:</b><br><span style="font-size:13pt;line-height:1.8">«Wir machen ____________________ . Wir sind fertig bis ____________ . Das ist wichtig, weil ____________________ . Was meinst du?»</span></div>
</div>'''
def card(n): return f'''<div class=card><h3>Person {n}</h3>
<div class=r><span>Name:</span><i></i><span>Wer? (z. B. Lehrerin, Hauswart, Kind aus 6a):</span><i></i></div>
<div class=fl>👍 Das gefällt mir:</div>{ln(2,8)}
<div class=fl>💡 Das würde ich ändern:</div>{ln(2,8)}</div>'''
p2=f'''<div class=pg>
<div class=hd><div class=t><small>FreiDay · Fr 27.11. · Einsatz-Team</small><b>Feedback holen</b></div></div>
<div class=box><b>So geht es:</b> Suche 3 Personen im Schulhaus (nicht aus deinem Team). Frag höflich, ob sie 2 Minuten Zeit haben. Pitche deinen Plan. Die Person sagt dir ihre Meinung. <b>Du schreibst auf. Sag danke!</b></div>
{card(1)}{card(2)}{card(3)}
<div class=card style="border-color:{T}"><h3>Das ändern wir wegen dem Feedback:</h3>{ln(2,7)}</div>
</div>'''
render(f'<!doctype html><meta charset=utf-8><style>{CSS}</style><body>{p1}{p2}','out/FreiDay_Pitch-Blatt_Fr27.11_A4.pdf')
import pymupdf as m
d=m.open('out/FreiDay_Pitch-Blatt_Fr27.11_A4.pdf');print(len(d),[round(max(b[3] for b in p.get_text('blocks'))/72*25.4) for p in d])
for i,p in enumerate(d):p.get_pixmap(dpi=60).save(f'/tmp/pt{i}.png')
