import asyncio
from playwright.async_api import async_playwright
def hd(title,sub='Bildung für nachhaltige Entwicklung - Frei Day R 4'):
    return f'<div class="hd"><div class="logo"><img src="img-000.png"></div><div><h1>{title}</h1><small>{sub}</small></div></div>'
def ft(n,t,src='Projekt-Finder FreiDay (MNWeG), SDG-Dossier',stand='30.10.2026'):
    return f'<div class="ft"><div class="l"><img src="img-000.png"><div>Bereitgestellt von: Christian Michels<br>Stand: {stand}<br>Quelle: {src}</div></div><div class="m">Seite: {n}/{t}</div></div>'
def doc(body,css=''):
    return f'<!doctype html><meta charset=utf-8><link rel=stylesheet href=style.css><style>{css}</style><body>{body}'
async def _r(pairs,land):
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page()
        for html,out in pairs:
            open('_t.html','w').write(html); await pg.goto('file://'+__import__('os').path.abspath('_t.html')); await pg.wait_for_timeout(300)
            await pg.pdf(path=out,prefer_css_page_size=True,print_background=True)
        await b.close()
def render(html,out): asyncio.run(_r([(html,out)],False))
