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
