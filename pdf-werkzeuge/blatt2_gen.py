# Logbuch Blatt 2 (Plan, Fr 27.11.) für alle 7 Einsätze. Start: python3 blatt2_gen.py  (Ausgabe nach out/)
import re,sys
exec(open('einsatz_igel2.py').read().split("p1=pg(")[0])
exec(open('einsaetze_data.py').read())
exec("css="+open('einsatz_igel2.py').read().split("css=",1)[1].split("render(doc(")[0])
css+='.nm4::after{content:none!important}.t2{width:100%;border-collapse:collapse;margin:1mm 0 2mm}.t2 th,.t2 td{border:.3mm solid var(--g);padding:0 2mm;font-size:10pt;text-align:left}.t2 th{background:#e3f0e6;height:7mm}.t2 td{height:9.5mm}.t2 td.c{text-align:center;width:24mm}.it{margin:2.5mm 0 0}.it b.n{display:inline-block;width:5.2mm;height:5.2mm;border-radius:50%;background:var(--g);color:#fff;text-align:center;font-size:9pt;line-height:5.2mm;margin-right:2mm}.hint{font-size:9.5pt;margin:0 0 .5mm 7mm}.fz{border:.3mm solid var(--g);background:#eaf4ec;border-radius:2mm;padding:2mm 3mm;font-size:10.5pt;margin:1mm 0}.fz ul{margin:0;padding-left:5mm}'
E1={ # wo, wo-hinweis, fragen (Liste), zusätzliche Frage (optional), Ideen für die Tabelle
'igel':dict(wo='Wo im Schulgarten oder in der Nähe machen wir den Laubhaufen?',woh='Eine ruhige, trockene Ecke.',fr=['Hauswart oder zuständige Person für den Schulgarten: Dürfen wir hier einen Laubhaufen und Totholz hinlegen?','Ist die Ecke ruhig und trocken?'],idee='Laub · Totholz · Schild'),
'spatz':dict(wo='Wo machen wir den Asthaufen? Welche Hecke bleibt stehen?',woh='Eine ruhige Ecke, nah bei der Hecke.',fr=['Hauswart: Dürfen wir die Hecke stehen lassen und einen Asthaufen machen?','Wo bekommen wir Äste und Reisig?'],idee='Äste · Schild · Stift'),
'futter':dict(wo='Wo hängen wir die Meisenknödel auf?',woh='Schattig, sicher vor Katzen, vom Fenster gut zu sehen.',fr=['Hauswart: Wo dürfen wir die Meisenknödel aufhängen?','Wer schaut nach, ob noch Futter da ist? (Kein Plastiknetz verwenden!)'],idee='Pflanzenfett · Körner · Schnur'),
'znueni':dict(wo='Wo und wann kochen wir? Was gibt es?',woh='Zum Beispiel im Hort: Tee oder Porridge.',fr=['Hort: Dürfen wir die Küche benutzen? Helfen uns die Köchinnen beim Planen und Kochen?','Wissen wir, was jedes Kind essen darf? (Allergien)'],idee='Zutaten · Töpfe · Becher'),
'waerme':dict(wo='Wo hängen wir Schilder und Thermometer auf?',woh='Zum Beispiel an der Tür, am Fenster, im Gang.',fr=['Hauswart: Dürfen wir Schilder aufhängen?','Welche Thermometer haben wir? Wer hängt sie auf?'],idee='Schilder · Thermometer · Klebeband'),
'strom':dict(wo='Wo hängen wir Schilder oder Klebepunkte auf?',woh='Zum Beispiel bei den Lichtschaltern und an der Tür.',fr=['Hauswart: Dürfen wir Schilder und Klebepunkte bei den Schaltern anbringen?','Welche Räume dürfen wir beim Rundgang besuchen?'],idee='Papier · Stifte · Klebepunkte'),
'zuhause':dict(wo='Wo und wann füllen wir die Checkliste aus?',woh='Zu Hause, an einem Abend, mit den Eltern.',fr=['Eltern: Füllen wir die Checkliste zusammen aus? (Elternbrief)','Haben wir zu Hause eine Steckerleiste zum Ausprobieren?'],idee='Checkliste · Steckerleiste · Plakat')}
IGEL=dict(nr=1,t='Der Igel-Einsatz',col='#56c02b',satzs=['Ein Igel schläft im Winter in',''])
def item(n,t,note=''): return f"<p class='ro it'><b class=n>{n}</b><b>{t}</b> {note}</p>"
def b2(e,x):
    nr=e['nr'];ZEIT='Fr 27.11.'
    cover=f'<div class=cover><span class=tabz>Logbuch 4b · Blatt 2</span><div class=sun><b>Wir</b>verbessern<br>die Welt</div><div class=lbl>Einsatz 0{nr} · Blatt 2 · Unser Plan · {ZEIT}</div><h1>{e["t"]}</h1><div class=nm3>Unser Team <span style="font-weight:400;font-size:9.5pt">(A, B, C wie letzte Woche)</span></div><div class=nm3 style="margin-top:1.5mm">A: '+bl(30)+' &nbsp;B: '+bl(30)+' &nbsp;C: '+bl(30)+'</div></div>'
    satz0=e['satzs'][0].rstrip(':')
    tab=lambda rows:''.join(f'<tr><td>Idee {i}: </td><td class=c>☐</td><td class=c>☐</td><td class=c>☐</td></tr>' for i in range(1,4))
    p1=pg(cover,
     sec(3,'Plan',ZEIT),
     item(1,'Drei einfache Ideen','Was könnten wir tun?')+"<p class=hint>Einfach heisst: wenig Geld, wenig Material, wir schaffen es selbst in einer Lektion.</p>"+ln(4,9),
     item(2,'Welche Idee wählen wir?','Macht ein Häkchen, wenn die Antwort <b>Ja</b> ist.')+"<table class=t2><tr><th>Idee</th><th>Wenig Geld?</th><th>In einer Lektion?</th><th>Hilft es wirklich?</th></tr>"+tab(0)+"</table><p class=ro style='margin:0'><b>Wir wählen:</b> "+bl(120)+"</p>",
     item(3,'Wo machen wir es?',x['wo'])+f"<p class=hint>{x['woh']}</p>"+ln(2,8.5),
     item(4,'Wen müssen wir fragen?')+"<div class=fz><ul>"+''.join(f'<li>{q}</li>' for q in x['fr'])+"</ul></div>"+f"<p class=ro style='margin:1mm 0 0'>{cb('Wir haben gefragt. Antwort:')}</p>"+ln(3,9),
     f'<div class=ft2 style="position:absolute;left:12mm;right:12mm;bottom:6mm;font:700 8pt AtkH;color:var(--g);display:flex;justify-content:space-between"><span>Einsatz 0{nr} · Blatt 2 · {ZEIT}</span><span>Seite: 1/2</span></div>')
    p2=pg(bar_(f'Blatt 2 · {ZEIT}') if False else f"<div class=bar><span class=lbl>Einsatz 0{nr} · Blatt 2 · Plan (Fortsetzung)</span><span class=nm2>Team:</span></div>",
     item(5,'Was brauchen wir?','Wer besorgt es? Was kostet es?')+f"<p class=hint>Ideen: {x['idee']}</p>"+
     "<table class=t2><tr><th>Das brauchen wir</th><th style='width:42mm'>Wer besorgt es?</th><th style='width:24mm'>Kosten (CHF)</th></tr>"+'<tr><td></td><td></td><td></td></tr>'*5+"<tr><td colspan=2 style='text-align:right'><b>Total</b></td><td></td></tr></table>"+
     "<p class=ro style='margin:0'>Brauchen wir Geld? Dann fragen wir zuerst die Lehrperson. Wir suchen eine Lösung, die <b>wenig oder nichts</b> kostet.</p>",
     item(6,'Wer macht was bis Fr 18.12.?','Schreibt Namen oder Buchstaben dazu. Häkchen, wenn fertig.')+
     "<table class=t2>"+''.join(f"<tr><td style='width:20mm'><b>{d}</b></td><td></td><td class=c style='width:12mm'>☐</td></tr>" for d in ('Fr 4.12.','Fr 11.12.','Fr 18.12.'))+"</table>",
     item(7,'Wie zeigen wir es am Fr 18.12. der Klasse?')+f"<p class=ro style='margin:1mm 0 0 7mm'>{cb('Plakat')} &nbsp; {cb('Foto oder Bilder')} &nbsp; {cb('Kurzer Vortrag (2 Min.)')} &nbsp; {cb('Anderes:')} "+bl(40)+"</p>",
     "<div class=fz style='margin-top:4mm'><b>Legt dieses Blatt gut ab.</b> Am Fr 4.12. und Fr 11.12. arbeitet ihr nach diesem Plan.</div>",
     f'<div class=ft2 style="position:absolute;left:12mm;right:12mm;bottom:6mm;font:700 8pt AtkH;color:var(--g);display:flex;justify-content:space-between"><span>Einsatz 0{nr} · Blatt 2 · {ZEIT}</span><span>Seite: 2/2</span></div>')
    return p1+p2
FILES={'igel':'03_FreiDay_Igel_Logbuch_Blatt2_Plan_A4.pdf','spatz':'04_FreiDay_Spatzen_Logbuch_Blatt2_Plan_A4.pdf','futter':'05_FreiDay_Futterstelle_Logbuch_Blatt2_Plan_A4.pdf','znueni':'06_FreiDay_Znueni_Logbuch_Blatt2_Plan_A4.pdf','waerme':'07_FreiDay_Waerme_Logbuch_Blatt2_Plan_A4.pdf','strom':'08_FreiDay_Strom_Logbuch_Blatt2_Plan_A4.pdf','zuhause':'09_FreiDay_Zuhause_Logbuch_Blatt2_Plan_A4.pdf'}
if __name__=='__main__':
    D['igel']=IGEL
    for k,f in FILES.items():
        render(doc(b2(D[k],E1[k]),css),'out/'+f)
