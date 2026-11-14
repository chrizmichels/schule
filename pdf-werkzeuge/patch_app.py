import json,re
exec(open('einsaetze_data.py').read())
p='../landing/einsaetze.html'
s=open(p).read()
# 1) Igel: generische Felder ergänzen (einmalig)
if "foto:{" not in s:
    igel_extra="col:'#56c02b',foto:{e:'🦔',l:'🍂 🍂 🍂',cap:'Der Igel aus der Pause (Zeichnung)',aria:'Zeichnung: ein kleiner, dünner Igel im Laub'},verm:'Was könnte im Winter mit dem Igel passieren?',sdgl:'Die Karte <b>SDG 15: Leben an Land</b> passt am besten: Wir schützen Tiere und ihren Lebensraum an Land. Auch SDG 13 (Klimaschutz) kann passen, wenn ihr es gut begründet habt.',satzs:['Ein Igel schläft im Winter in','Dafür brauchen wir'],"
    a=" igel:{nr:1,"; assert a in s
    s=s.replace(a," igel:{"+igel_extra+"nr:1,")
    for k,t in [('A','Essen'),('B','Schlafen'),('C','Helfen')]: assert "{k:'%s',t:'%s'"%(k,t) in s
# 2) neue Einsätze: alles zwischen Igel und Ende des EINS-Objekts neu schreiben
m0=re.search(r",\n [a-z]+:\{\"nr\"",s)
if m0:
    m1=re.search(r"\n\};\nconst N=2;",s); s=s[:m0.start()]+s[m1.start():]
def js(d):
    d=dict(d)
    for key in ['file','short','lp_sehen','lp_verm','lp_sdg','lp_sicher','lp_weiter','lp_quellen','teams']: d.pop(key,None)
    for f in d['felder']: f.pop('lp',None)
    d['satz']={'loesung':d.pop('satzl')}
    return json.dumps(d,ensure_ascii=False)
add=''.join(",\n %s:%s"%(k,js(v)) for k,v in D.items())
m=re.search(r"\n\};\nconst N=2;",s); assert m
s=s[:m.start()]+add+s[m.start():]
# 3) View generisch
rep=[
("""h+=kap(id,1)+`<div class="foto" role="img" aria-label="Zeichnung: ein kleiner, dünner Igel im Laub"><span class="fe">🦔</span><span class="fl">🍂 🍂 🍂</span><small>Der Igel aus der Pause (Zeichnung)</small></div>`+""",
 """h+=kap(id,1)+`<div class="foto" role="img" aria-label="${e.foto.aria}"><span class="fe">${e.foto.e}</span><span class="fl">${e.foto.l}</span><small>${e.foto.cap}</small></div>`+"""),
("<b>Das vermuten wir:</b> Was könnte im Winter mit dem Igel passieren?'","<b>Das vermuten wir:</b> '+e.verm+'"),
("selbst(id,'sdg','Die Karte <b>SDG 15: Leben an Land</b> passt am besten: Wir schützen Tiere und ihren Lebensraum an Land. Auch SDG 13 (Klimaschutz) kann passen, wenn ihr es gut begründet habt.',","selbst(id,'sdg',e.sdgl,"),
("""`<table class="rtab"><tr><th>Runde</th><th>Sucht</th><th>Prüft</th><th>Schreibt</th></tr><tr><td>1 · Essen</td><td>A</td><td>C</td><td>B</td></tr><tr><td>2 · Schlafen</td><td>B</td><td>A</td><td>C</td></tr><tr><td>3 · Helfen</td><td>C</td><td>B</td><td>A</td></tr></table>`+""",
 """`<table class="rtab"><tr><th>Runde</th><th>Sucht</th><th>Prüft</th><th>Schreibt</th></tr>`+[['A','C','B'],['B','A','C'],['C','B','A']].map((r,i)=>`<tr><td>${i+1} · ${e.felder[i].t}</td><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join('')+`</table>`+"""),
("<p><b>Ein Igel schläft im Winter in ______. Dafür brauchen wir ______.</b></p>","<p><b>${e.satzs[0]} ______. ${e.satzs[1]} ______.</b></p>"),
("""<p class="sdgchip"><i style="background:#56c02b"></i>""","""<p class="sdgchip"><i style="background:${e.col}"></i>"""),
(" Mehr Einsätze folgen. Quelle für die Recherche: <a href=\"https://klexikon.zum.de\" target=\"_blank\" rel=\"noopener\">Klexikon</a>."," Quellen für die Recherche: <a href=\"https://klexikon.zum.de\" target=\"_blank\" rel=\"noopener\">Klexikon</a> und <a href=\"https://www.nabu.de\" target=\"_blank\" rel=\"noopener\">NABU</a>."),
]
for a,b in rep:
    if a in s: s=s.replace(a,b)
    elif b not in s: print('FEHLT:',a[:70])
open(p,'w').write(s)
print(len(s))
