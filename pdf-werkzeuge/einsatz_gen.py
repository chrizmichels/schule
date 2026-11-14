import re,sys
exec(open('einsatz_igel2.py').read().split("p1=pg(")[0])
exec(open('einsaetze_data.py').read())
exec("css="+open('einsatz_igel2.py').read().split("css=",1)[1].split("render(doc(")[0])
css+='.nm4::after{content:none!important}'
_ns={};exec(open('einsatz_loesung_fr1.py').read().split("p1='''")[0],_ns);lpcss=_ns['css']+'.page{padding-top:8mm}h2{margin:3mm 0 1mm}td,th{font-size:8.9pt;padding:1mm 1.8mm}.sub{margin:0 0 1mm}'
plain=lambda t:re.sub(r'<[^>]+>','',t)
def build(e):
    nr=e['nr']
    bar_=lambda t:f'<div class=bar><span class=lbl>Einsatz 0{nr} · {t}</span><span class=nm2>Team:</span></div>'
    cover=f'<div class=cover><span class=tabz>Logbuch 4b · Blatt 1</span><div class=sun><b>Wir</b>verbessern<br>die Welt</div><div class=lbl>Einsatz 0{nr} · Fr 20.11.</div><h1>{e["t"]}</h1><div class=nm3>Unser Team <span style="font-weight:400;font-size:9.5pt">(jedes Kind hat einen Buchstaben und behält ihn)</span></div><div class=nm3 style="margin-top:1.5mm">A: '+bl(30)+' &nbsp;B: '+bl(30)+' &nbsp;C: '+bl(30)+'</div></div>'
    app_=f'<div class=app><div class=q>{QR}</div><div><span class=lbl>App</span><br><b>Geschichte, Quellen und Tipps</b><br>{LINK}<br>Tippt auf <b>{e["t"]}</b>. Die Antworten findet ihr selbst.</div></div>'
    p1=pg(cover,sec(1,'Hilferuf','Fr 20.11.'),
     "<p class=ro><b>Das sehen wir</b> (2 Dinge):</p>"+ln(3,11),
     f"<p class=ro><b>Das vermuten wir:</b> {e['verm']}</p>"+ln(6,11),
     "<p class=ro><b>SDG-Karte:</b> Wir wählen die Karte Nr. "+bl(16)+"</p>",
     "<p class=ro><b>Warum passt diese Karte?</b></p>"+ln(3,11),
     f"<p class=ro>{cb('Wir haben die Karte und den Grund aufgeschrieben.')}</p>",app_)
    def runde(n,r,s_,w,pr):
        fm=lambda n:(lambda a,b:a+' «'+b+'»')(*n.split(': ',1))
        names=[]
        [names.append(fm(q[0])) for q in r['src'] if fm(q[0]) not in names]
        quelle=' und '.join(names)
        return (f'<div class=rl><div class=rh><span class=rb>{n}</span><b>Runde {n} · {r["t"]}</b><span class=nm4 style="margin-left:auto;font:700 9.5pt AtkH">Sucht: {s_} · Prüft: {pr} · Schreibt: {w}</span></div><p class=sm>{plain(r["auftrag"])}</p><p class=sm style="margin-top:1mm"><b>Quelle:</b> {quelle} &nbsp;·&nbsp; <b>Findet im Text:</b> {" · ".join(r["sw"])}</p>{ln(4,7.4)}</div>')
    F=e['felder'];rot=[('A','B','C'),('B','C','A'),('C','A','B')]
    p2=pg(bar_('Blatt 1 · Fr 20.11.'),sec(2,'Forschen','Fr 20.11.'),
     "<p class=ro style='font-size:11.5pt'>Ihr habt ein Tablet. Drei Runden. Die Aufgaben wechseln: <b>Sucht</b> (Quelle in der App öffnen, Wörter im Text finden), <b>Prüft</b> (liest mit: Steht <b>beides</b> aus der Frage im Text? Dann «Stopp, das ist es!»), <b>Schreibt</b> (Antwort ins Logbuch).</p>",
     *[runde(i+1,F[i],*rot[i]) for i in range(3)],
     f"<div class=idl style='margin-top:3mm'><b>Unser Satz:</b> {e['satzs'][0]}"+ln(2,8)+f"<b>{e['satzs'][1]}</b>"+ln(2,8)+"</div>",
     f"<p class=ro>{cb('Wir haben alle drei Runden gemacht und den Satz geschrieben.')}</p>",
     "<p class=sm style='margin-top:2mm'>Legt dieses Blatt gut ab. Am nächsten Freitag baut euer Plan auf eurem Satz auf.</p>")
    return p1+p2
def lp_page(e):
    rows=''.join(f"<tr><td>{i+1} {f['t']}</td><td>{f['auftrag']}</td><td>{f['loesung']}{('<br><span class=src>'+f['lp']+'</span>') if any(k in f['lp'] for k in ('steht nicht','NABU:','eigene Beobachtung')) else ''}</td><td><b>{' + '.join(q[0] for q in f['src'])}:</b> {', '.join(f['sw'])}<br><span class=src>Tipp 1: {f['tipp'][0]}</span></td></tr>" for i,f in enumerate(e['felder']))
    return f'''<div class=page><h1>Lösungs-Logbuch: {e['t']}, Freitag 20.11.</h1><p class=sub>Für die Lehrperson · Etappe 1 Hilferuf und Etappe 2 Forschen · {e['teams']} Team{'s' if e['teams']>1 else ''} (je 1 Logbuch Blatt 1, doppelseitig)</p>
<h2>Ablauf am Freitag</h2>
<ul><li><b>Input (höchstens 5 Min.):</b> Geschichte aus der App vorlesen. Dann arbeiten die Teams selbständig. <b>Material:</b> 1 Tablet pro Team, Logbuch Blatt 1, SDG-Karten.</li><li><b>Tablet-Logistik:</b> Pro Runde sucht ein Kind (Tablet), eines schreibt, eines prüft. Die Rollen wechseln. Das Lösungs-Logbuch erscheint in der App erst nach der eigenen Antwort.</li></ul>
<h2>Etappe 1 · Hilferuf</h2>
<div class=box><b class=k>Das sehen wir:</b> {e['lp_sehen']} <b class=k>Vermutung:</b> {e['lp_verm']} <b class=k>SDG-Karte:</b> {e['lp_sdg']}</div>
<h2>Etappe 2 · Forschen (3 Runden)</h2>
<table><tr><th>Runde</th><th>Auftrag</th><th>Lösung</th><th>Quelle · Wörter zum Finden im Text (vorgegeben) · Tipps (1 · 2)</th></tr>{rows}</table>
<div class=box><b class=k>Unser Satz (Ziel von Freitag 1), Beispiel:</b> «{e['satzl']}» Dieser Satz ist der Einstieg für Freitag 2.</div>
<h2>Wohin es führt (nur für dich)</h2><ul>{''.join('<li>'+x+'</li>' for x in e['lp_weiter'])}</ul>
<div class="box warn"><b>Sicherheit:</b> {e['lp_sicher']}</div>
<p class=src>Quellen: {e['lp_quellen']}</p></div>'''
if __name__=='__main__':
    for k,e in D.items():
        render(doc(build(e),css),'out/'+e['file'])
    render(doc(''.join(lp_page(e) for e in D.values()),lpcss),'out/FreiDay_Einsatz02-07_Loesungs-Logbuch_Fr20.11_LP.pdf')
