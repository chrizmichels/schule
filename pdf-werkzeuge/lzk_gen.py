"""Lernzielkontrolle Wetter und Klima (6 Aufgaben, 12 Punkte) und Probe-Lernzielkontrolle.
Erzeugt je eine Aufgaben- und eine Lösungsversion:
  out/LZK_Wetter_und_Klima.pdf, out/LZK_Wetter_und_Klima_Loesung_LP.pdf
  out/Probe-LZK_Wetter_und_Klima.pdf, out/Probe-LZK_Wetter_und_Klima_Loesung.pdf
Nur ganze Zahlen (Mathe: noch keine Dezimalzahlen)."""
from lib import render

TEAL = '#1e7a8c'
INK = '#14211f'
GRN = '#1a7f37'
RED = '#d62828'

V = {
 'lzk': dict(
  name='Lernzielkontrolle', sub='NMG · Wetter und Klima · Lernzielkontrolle',
  read=[7, -3, 18], draw=[14, -4],
  who='Max und Tina messen in ihren Gärten die Temperatur. Max misst immer höhere Werte als Tina.',
  why='Wir messen jede Woche um 8:30 Uhr am gleichen Fenster. Warum ist das wichtig?',
  chart=[3, 5, 8, 9, 8, 6, 5], who_name='Sara',
  pts=[2, 6, 4], nachm='Warum ist es am Nachmittag oft wärmer als am Morgen?',
  orte=[('Lugano', 275), ('Zürich', 408), ('Zermatt', 1608)], coldest='Zermatt'),
 'probe': dict(
  name='Probe-Lernzielkontrolle', sub='NMG · Wetter und Klima · Probe-Lernzielkontrolle',
  read=[5, -6, 22], draw=[16, -2],
  who='Lena und Jonas messen in ihren Gärten. Lena misst immer tiefere Werte als Jonas.',
  why='Warum messen wir jedes Mal am gleichen Ort und zur gleichen Zeit?',
  chart=[1, 3, 5, 7, 6, 5, 4], who_name='Ben',
  pts=[3, 8, 6], nachm='Warum ist es am Morgen oft kälter als am Nachmittag?',
  orte=[('Locarno', 200), ('Bern', 540), ('Davos', 1560)], coldest='Davos'),
}

CSS = f'''
@page{{size:A4;margin:12mm 15mm 12mm 15mm}}
*{{box-sizing:border-box}}
body{{font-family:Inter,"Helvetica Neue",Arial,sans-serif;font-size:11pt;line-height:1.4;color:{INK};margin:0}}
.pg{{height:273mm;position:relative;page-break-after:always;overflow:hidden}}
.pg:last-child{{page-break-after:auto}}
.hd{{display:flex;gap:4mm;align-items:stretch;margin-bottom:5mm}}
.hd .t{{flex:1;background:{TEAL};color:#fff;border-radius:3mm;padding:2.5mm 5mm}}
.hd .t small{{display:block;font-size:8.5pt;opacity:.92}}.hd .t b{{font-size:17pt}}
.hd .p{{width:32mm;border:1.5px solid {TEAL};border-radius:3mm;padding:1.5mm 3mm;color:{TEAL};font-size:8.5pt;font-weight:700}}
.hd .p span{{display:block;text-align:right;font-size:13pt;color:{INK};font-weight:500;margin-top:1mm}}
.name{{border-bottom:1.5px solid {INK};padding:0 0 1mm;margin:0 0 5mm;font-size:10pt}}
.task{{display:flex;gap:3.5mm;margin:0 0 5mm}}
.task .n{{flex:none;width:7mm;height:7mm;border-radius:50%;background:{TEAL};color:#fff;font-weight:700;text-align:center;line-height:7mm;font-size:10pt}}
.task .b{{flex:1}}
.q{{display:flex;justify-content:space-between;gap:4mm;align-items:flex-start}}
.pill{{flex:none;border:1px solid {TEAL};color:{TEAL};border-radius:4mm;padding:0 2.6mm;font-size:8pt;font-weight:700;margin-top:.5mm;white-space:nowrap}}
.sub{{margin:2.5mm 0 0}}
.ln{{border-bottom:1px solid #9aa;height:10mm}}
.a{{color:{GRN};font-weight:700}}
.lab{{display:flex;justify-content:space-around;margin-top:1mm}}
.lab div{{width:50mm;text-align:center;font-size:11pt}}
.row{{display:flex;justify-content:space-around;align-items:flex-end}}
table.k{{border-collapse:collapse;margin:2mm 0}}
table.k td,table.k th{{border:1px solid #6b7c80;padding:1.2mm 5mm;text-align:center;font-size:10.5pt}}
table.k th{{background:#e6f1f3}}
.ft{{position:absolute;left:0;right:0;bottom:0;border-top:1px solid #ccd;padding-top:1.5mm;display:flex;justify-content:space-between;font-size:8pt;color:#667}}
.blank{{display:inline-block;min-width:14mm;border-bottom:1px solid {INK};text-align:center}}
'''


def thermo(val=None, fill=False):
    y = lambda t: 156 - (t + 10) * 3.6
    s = ('<svg width="70" height="178" viewBox="0 0 70 178" xmlns="http://www.w3.org/2000/svg" '
         'font-family="Inter,Arial,sans-serif">')
    s += f'<rect x="8" y="6" width="12" height="150" rx="6" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
    if fill and val is not None:
        s += f'<rect x="11" y="{y(val):.1f}" width="6" height="{156 - y(val):.1f}" fill="{RED}"/>'
    s += f'<circle cx="14" cy="164" r="9" fill="{RED if fill else "#fff"}" stroke="{INK}" stroke-width="1.6"/>'
    for t in range(-10, 31):
        big = t % 5 == 0
        s += f'<line x1="{24}" x2="{30 if big else 28}" y1="{y(t):.1f}" y2="{y(t):.1f}" stroke="{INK}" stroke-width="{1 if big else .6}"/>'
        if big:
            s += f'<text x="33" y="{y(t) + 3:.1f}" font-size="9">{t}</text>'
    return s + '</svg>'


def chart(data=None, color=RED, pts=None):
    """Raster 0-10 °C, 8-20 Uhr. data: 7 Werte; pts: {Stunde: Wert} (Lösungslinie)."""
    W, H, L, R, T, B = 640, 250, 34, 30, 8, 26
    xs = lambda h: L + (h - 8) / 12 * (W - L - R)
    ys = lambda v: T + (10 - v) / 10 * (H - T - B)
    s = f'<svg width="100%" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Inter,Arial,sans-serif">'
    s += f'<text x="0" y="12" font-size="11" font-weight="700">°C</text>'
    for v in range(0, 11, 2):
        s += f'<line x1="{L}" x2="{W - R}" y1="{ys(v):.1f}" y2="{ys(v):.1f}" stroke="#c9d1d3" stroke-width="1"/>'
        s += f'<text x="{L - 6}" y="{ys(v) + 4:.1f}" font-size="11" text-anchor="end">{v}</text>'
    for h in range(8, 21, 2):
        s += f'<line x1="{xs(h):.1f}" x2="{xs(h):.1f}" y1="{T}" y2="{ys(0):.1f}" stroke="#e1e6e7" stroke-width="1"/>'
        s += f'<text x="{xs(h):.1f}" y="{H - 8}" font-size="11" text-anchor="middle">{h} Uhr</text>'
    if data:
        p = {8 + 2 * i: v for i, v in enumerate(data)}
    else:
        p = pts or {}
    if p:
        hs = sorted(p)
        s += '<polyline fill="none" stroke="%s" stroke-width="2.4" points="%s"/>' % (
            color, ' '.join(f'{xs(h):.1f},{ys(p[h]):.1f}' for h in hs))
        for h in hs:
            s += f'<circle cx="{xs(h):.1f}" cy="{ys(p[h]):.1f}" r="4" fill="{color}"/>'
    return s + '</svg>'


def task(n, body):
    return f'<div class=task><div class=n>{n}</div><div class=b>{body}</div></div>'


def qrow(text, pts):
    return f'<div class=q><div>{text}</div><span class=pill>{pts} P</span></div>'


def lines(n):
    return '<div class=ln></div>' * n


def sol(txt, sh):
    return f'<span class=a>{txt}</span>' if sh else ''


def page(n, inner, v, head=''):
    return f'<div class=pg>{head}{inner}<div class=ft><span>{v["sub"]}</span><span>Seite: {n}/2</span></div></div>'


def build(key, solution, lp):
    v = V[key]
    sh = solution
    title = v['name'] + (' · Lösung' if sh else '')
    hd = (f'<div class=hd><div class=t><small>NMG · Wetter und Klima</small><b>{title if sh else v["name"] + ": Wetter messen und verstehen"}</b></div>'
          f'<div class=p>Punkte<span>/ 12</span></div></div><div class=name>Name:</div>')
    g = lambda s_: f'<div class=a style="margin-top:1.5mm">{s_}</div>'
    ans = lambda x: f'<span class=a>{x}</span>' if sh else '<span class=blank></span>'
    # 1 Thermometer ablesen
    a1a = ''.join(
        f'<div>{thermo(x, fill=True)}<div style="text-align:center;margin-top:1mm">'
        + (f'<span class=a>{x} °C</span>' if sh else '<span class=blank style="min-width:16mm"></span> °C')
        + '</div></div>' for x in v['read'])
    t1 = task(1, qrow('<b>Thermometer.</b> Wie warm ist es? Schreibe die Temperatur mit der Einheit unter jedes Thermometer.', 2)
              + f'<div class=row>{a1a}</div>'
              + (g('3 richtig = 2 P, 2 richtig = 1 P') if sh else ''))
    # 2 Gleich messen
    t2 = task(2, qrow('<b>Gleich messen.</b> ' + v['who'], 2)
              + '<div class=sub>a) Nenne einen Grund.' + (' ' + sol('z. B. einer misst in der Sonne, der andere im Schatten / zu verschiedenen Zeiten / andere Thermometer (1 P)', sh) if sh else '') + '</div>' + ('' if sh else lines(2))
              + '<div class=sub>b) Was müssen die beiden ändern, damit sie gleich messen?' + (' ' + sol('z. B. gleiche Uhrzeit, gleicher Ort, gleiches Thermometer (1 P)', sh) if sh else '') + '</div>' + ('' if sh else lines(2)))
    # 3 Diagramm lesen
    d = v['chart']
    mx = max(d)
    hmx = 8 + 2 * d.index(mx)
    t3 = task(4, qrow(f'<b>Diagramm lesen.</b> {v["who_name"]} hat an einem Tag alle 2 Stunden die Temperatur gemessen.', 2)
              + chart(data=d, color=RED)
              + f'<div class=sub>a) Um wie viel Uhr war es am wärmsten? {ans(hmx)} Uhr <i>(1 P)</i></div>'
              + f'<div class=sub>b) Wie warm war es dann? {ans(str(mx) + " °C") if sh else "<span class=blank></span> °C"} <i>(1 P)</i></div>')
    # 4 Diagramm zeichnen
    p4 = v['pts']
    t4 = task(5, qrow('<b>Diagramm zeichnen.</b> Trage die drei Messwerte als Punkte ein (1 P). Verbinde die Punkte mit einer Linie (1 P).', 2)
              + f'<table class=k><tr><th>Zeit</th><th>8 Uhr</th><th>12 Uhr</th><th>16 Uhr</th></tr><tr><th>Temperatur</th><td>{p4[0]} °C</td><td>{p4[1]} °C</td><td>{p4[2]} °C</td></tr></table>'
              + chart(pts={8: p4[0], 12: p4[1], 16: p4[2]} if sh else None, color=RED))
    # 5 Warum ändert sich die Temperatur
    t5 = task(3, qrow('<b>Warum ändert sich die Temperatur?</b> ' + v['nachm'] + ' Schreibe zwei Sätze. Verwende diese Wörter: Sonne, Boden, Luft.', 2)
              + (g('1 P: Die Sonne wärmt den Boden. 1 P: Der Boden wärmt die Luft darüber.') if sh else lines(4)))
    # 6 Orte
    o = v['orte']
    tab = ('<table class=k><tr><th>Ort</th>' + ''.join(f'<th>{n_}</th>' for n_, _ in o) + '</tr><tr><th>Höhe</th>'
           + ''.join(f'<td>{h} m ü. M.</td>' for _, h in o) + '</tr></table>')
    t6 = task(6, qrow('<b>Orte und Höhe.</b> Schau dir die Orte und ihre Höhe an.', 2) + tab
              + f'<div class=sub>a) An welchem Ort ist es am kältesten? {ans(v["coldest"])} <i>(1 P)</i></div>'
              + f'<div class=sub>b) Je höher der Ort, desto {"<span class=a>kälter</span>" if sh else "<span class=blank style=\"min-width:30mm\"></span>"} ist es. <i>(1 P)</i></div>')
    html = ('<!doctype html><meta charset=utf-8><style>' + CSS + '</style><body>'
            + page(1, t1 + t2 + t5, v, hd) + page(2, t3 + t4 + t6, v))
    return html


if __name__ == '__main__':
    import pymupdf as m
    jobs = [('lzk', False, False, 'out/LZK_Wetter_und_Klima.pdf'),
            ('lzk', True, True, 'out/LZK_Wetter_und_Klima_Loesung_LP.pdf'),
            ('probe', False, False, 'out/Probe-LZK_Wetter_und_Klima.pdf'),
            ('probe', True, False, 'out/Probe-LZK_Wetter_und_Klima_Loesung.pdf')]
    for key, sol_, lp, out in jobs:
        render(build(key, sol_, lp), out)
        d = m.open(out)
        print(out, len(d), 'Seiten', [round(max(b[3] for b in p.get_text('blocks') if 'Seite:' not in b[4] and 'Lernzielkontrolle' not in b[4]) / 72 * 25.4) for p in d])
