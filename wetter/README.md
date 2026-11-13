# Wetter-Anzeige 4b

Einzelne HTML-Datei (`index.html`), keine Abhängigkeiten ausser der Schriftart Andika (Google Fonts).

Daten (Open Data, kein API-Key):
- Zürich-Fluntern: MeteoSchweiz (data.geo.admin.ch, 10-Minuten-Werte, Zeitstempel in UTC, Anzeige in Zürcher Zeit)
- Mythenquai: Stadt Zürich über Tecdottir (Reserve)

Standardmässig zeigt die Seite den Wert von 8:30 (Messzeit).
Bei fehlender Verbindung zeigt sie gespeicherte Beispieldaten (Badge «Beispieldaten»).


## Ansicht
- Es gibt nur noch eine Ansicht (immer mit «Tag verpasst?»). `?kompakt` und `?normal` werden nicht mehr gebraucht.

## Klimadetektive (detektive.html)
Kindgerechte, getrennte Version: `/detektive`. Drei Fälle (Tagesverlauf, zwei Tage vergleichen, drei Orte vergleichen). Ablauf: vermuten, Spur (Messwerte) prüfen, ins Heft schreiben. Nutzt denselben Daten-Weg wie die Wetter-Anzeige (`/api/ogd`, Fallback direkt MeteoSchweiz).

## Startseite (Ordner landing/, eigenes Vercel-Projekt freiday-4b)
`https://freiday-4b.vercel.app/` (Quelle: `landing/index.html`; `/start` hier leitet dorthin um): drei Bereiche mit gleichem Aufbau, aber eigener Farbe und Schrift: Wetterstation (blau, `/`), SOL-Fälle (Aktenbeige, `/detektive`), FreiDay (grün/gelb, `/einsaetze`). Die Wetter-Anzeige bleibt auf wetter-4b unter `/`, damit der gedruckte QR-Code weiter funktioniert. Jede Unterseite hat oben einen Link zurück zur Startseite. Die Kacheln dort haben ein «?» mit Link zum Klexikon (Temperatur, Wind, Wolke, Regen, Sonne, Nebel).

## Looks der drei Bereiche
- Wetterstation (`index.html`): blau, runde Formen, Messgerät-Symbol. Die vier grünen Kacheln zum Abschreiben bleiben grün.
- SOL (`detektive.html`): Aktenbeige, Stempel.
- FreiDay (`einsaetze.html`): grün und sonnengelb, Handschrift (Caveat), Geschichte der 4b-Kinder (kein Detektiv). Papier heisst dort «Einsatz-Logbuch».
