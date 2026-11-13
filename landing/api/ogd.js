// Gibt die 10-Minuten-Werte einer MeteoSchweiz-Station als kleine JSON-Liste zurück.
// Der Server holt die Dateien nur alle paar Minuten bei MeteoSchweiz; alle Kinder bekommen dieselbe, zwischengespeicherte Antwort.
const MCH = 'https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/';
const OK = { sma: 1, lug: 1, zer: 1 };
const DAYS = 21;
const num = v => (v === undefined || v === '' || v === '-' || isNaN(+v)) ? null : +v;
const fmt = new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/Zurich', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' });
function zurichKey(ms) { const p = Object.fromEntries(fmt.formatToParts(new Date(ms)).map(x => [x.type, x.value])); return p.year + '-' + p.month + '-' + p.day + 'T' + p.hour + ':' + p.minute; }
function parseOGD(txt) {
  const L = txt.trim().split(/\r?\n/), H = L[0].split(';'), ix = n => H.indexOf(n);
  const c = { t: ix('tre200s0'), ws: ix('fkl010z0'), wk: ix('fu3010z0'), gs: ix('fkl010z1'), gk: ix('fu3010z1'), d: ix('dkl010z0'), p: ix('prestas0'), r: ix('rre150z0'), g: ix('gre000z0'), h: ix('ure200s0'), ts: ix('reference_timestamp') };
  const out = [];
  for (let i = 1; i < L.length; i++) {
    const a = L[i].split(';'), m = (a[c.ts] || '').match(/(\d+)\.(\d+)\.(\d+) (\d+):(\d+)/); if (!m) continue;
    const ms = Date.UTC(+m[3], +m[2] - 1, +m[1], +m[4], +m[5]);
    const ws = c.ws >= 0 && num(a[c.ws]) != null ? num(a[c.ws]) : (c.wk >= 0 && num(a[c.wk]) != null ? num(a[c.wk]) / 3.6 : null);
    const gs = c.gs >= 0 && num(a[c.gs]) != null ? num(a[c.gs]) : (c.gk >= 0 && num(a[c.gk]) != null ? num(a[c.gk]) / 3.6 : null);
    const r = [zurichKey(ms), num(a[c.t]), ws, gs, num(a[c.d]), num(a[c.p]), num(a[c.r]), num(a[c.g]), num(a[c.h])];
    if (r[1] != null || r[2] != null || r[7] != null || r[8] != null) out.push([ms, r]);
  }
  return out;
}
async function get(url) { const r = await fetch(url); if (!r.ok) throw new Error('HTTP ' + r.status); return r.text(); }
module.exports = async (req, res) => {
  const st = String((req.query && req.query.st) || 'sma').toLowerCase();
  if (!OK[st]) { res.status(400).json({ error: 'Station' }); return; }
  try {
    const base = MCH + st + '/ogd-smn_' + st + '_t_';
    const [now, recent] = await Promise.allSettled([get(base + 'now.csv'), get(base + 'recent.csv')]);
    if (now.status !== 'fulfilled' && recent.status !== 'fulfilled') throw new Error('keine Daten');
    const map = new Map();
    for (const s of [recent, now]) if (s.status === 'fulfilled') for (const [ms, r] of parseOGD(s.value)) map.set(ms, r);
    const limit = Math.max(...map.keys()) - DAYS * 864e5;
    const rows = [...map.entries()].filter(([ms]) => ms >= limit).sort((a, b) => b[0] - a[0]).map(x => x[1]);
    res.setHeader('Cache-Control', 'public, s-maxage=300, stale-while-revalidate=900');
    res.status(200).json(rows);
  } catch (e) {
    res.setHeader('Cache-Control', 'no-store');
    res.status(502).json({ error: String(e && e.message || e) });
  }
};
