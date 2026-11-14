# Klasse 4b – Apps und Druckmaterial (Übergabe)

Christian Michels, Fachlehrer (QUEST, PH Zürich), Klasse 4b, Living Space School Bühl, Kanton Zürich.
Dieses Repo enthält die Web-Apps für die Kinder und die Werkzeuge für die Papier-PDFs.

## Arbeitsweise (wichtig)
- **Sprache:** Deutsch (Schweizer Schreibweise: «ss», kein «ß»). Kurz und direkt. Strukturierte Antworten.
- **Kindermaterial:** sehr konkret, logisch, einfach. Kurze Sätze. Möglichst wenig Lehrerinnen-/Lehrertext, maximale Selbstständigkeit der Kinder.
- **Erst messen, dann verstehen:** Messen allein reicht nicht. Jede Akte braucht einen Schritt, in dem die Kinder ihre eigenen Zahlen erklären.
- **Nichts erfinden:** Keine erfundenen Messwerte oder Watt-Zahlen. Faktenquellen: Klexikon (klexikon.zum.de), Energiesparmeister, MeteoSchweiz, Stadt Zürich. Quellen bei Beweisstücken verlinken.
- Nach jeder Änderung testen (Playwright, Handybreite 420 px, keine JS-Fehler, `scrollWidth` = 420), dann committen und pushen. Vercel deployt automatisch aus `main`.

## Deployment
- GitHub: `chrizmichels/schule`, Branch `main`. Vercel-Projekt `freiday-4b`, Root Directory `landing/`, `cleanUrls: true`.
- Live: https://freiday-4b.vercel.app/ (Startseite), `/wetter`, `/detektive`, `/energie`, `/einsaetze`.
- Lokal testen: `cd landing && python3 -m http.server 8765`. JS-Syntax prüfen: letztes `<script>` extrahieren, `node --check`.
- `/api/ogd?st=SMA` (`landing/api/ogd.js`) liefert MeteoSchweiz-Messwerte (10-Min-Daten, ca. 21 Tage) als JSON-Zeilen `[zeit, temp, wind m/s, Böe, Richtung, Druck, Regen, Globalstrahlung, Luftfeuchte]`, neueste zuerst. Zeiten sind Zürcher Ortszeit (Quelle ist UTC).

## Apps (alles einzelne HTML-Dateien, Vanilla-JS, kein Build)
| Datei | Inhalt |
|---|---|
| `landing/index.html` | Startseite: Wetterstation, SOL-Fälle («kommissariat 4b»), FreiDay-Einsätze |
| `landing/wetter.html` | Wetterstation. Standard zeigt die letzte Messzeit **8:30** (vor 8:30 Uhr: gestern). Stationen: Zürich-Fluntern (MeteoSchweiz) und Mythenquai (tecdottir, oft verspätet) |
| `landing/detektive.html` | **Klimadetektive**, 3 Akten (Wetter): Akte 01–03 |
| `landing/energie.html` | **Energiedetektive**, 2 Akten: 01 «Warm und kalt» (Thermometer im Schulhaus), 02 «Strom und Watt» (Watt ablesen, Lampe beim Hausabwart erfragen) |
| `landing/einsaetze.html` | FreiDay-Einsätze (7 Stück, mit Geschichte, Logbuch) |

**Aufbau der Detektiv-Apps** (`detektive.html`, `energie.html`): State-Objekt `S` (`f1`, `f2`, … je Akte mit `c` = Häkchen, `show`, `res`, `self`), Render-Funktionen `viewF1`, `sol1` usw., Datenobjekte `BW[n]` (Beweisstück: `t`, `m` Merksätze, `s` Klexikon-Seiten, `x` Zusatz) und `KAP[n]` (Geschichte: `i` Einstieg, `a` Auflösung). Fortschritt in `localStorage` (`kd_solved` bzw. `ke_solved`). Ablauf jeder Akte: **1 Vermuten → 2 Spuren sichern → 3 Lösung → 4 Beweisstück lesen**. Zu jeder Akte gehört eine Papier-Akte (PDF) mit QR-Code zur App.

`energie.html` wurde aus `detektive.html` abgeleitet. Gemeinsame Hilfsfunktionen (`stepper`, `head`, `FB`, `box`, `ol`, `checks`, `selfBox`) sind in beiden Dateien kopiert. Änderungen daran in beiden Dateien nachziehen.

## PDF-Werkzeuge (`pdf-werkzeuge/`)
- Einmalig `./setup.sh` (Schriften via npm, Python: playwright, qrcode, pymupdf).
- HTML → PDF via Playwright/Chromium, A4. `akten11.py` ist der Stil der Papier-Akten (Deckblatt, Kapitel, Beweisstück, QR). `akte_en1.py` / `akte_en2.py` erzeugen die Energie-Akten, `akten_wdh.py` das Wiederholungsblatt Fall 1+2. `kap.py` enthält die Geschichten-Texte der Akten 1–3.
- Ausgabe nach `out/` (nicht im Git). Prüfen mit PyMuPDF: Inhalt muss auf A4 passen (unterste Textkante unter ca. 290 mm).
- `einsaetze_data.py` + `einsatz_gen.py`: Daten und Generator der Einsatz-Logbücher. `patch_app.py` schreibt die Einsatz-Daten in `landing/einsaetze.html`. Hinweis: `einsatz_gen.py` braucht weitere Einsatz-Vorlagen, die nicht alle im Repo sind. Bei Bedarf neu aufbauen.
- Namen der Akten-PDFs: `Energie_Akte01_Warm_und_kalt_A4.pdf`, `Energie_Akte02_Strom_und_Watt_A4.pdf`, `Klimadetektive_Wiederholung_Fall1-2_A4.pdf`.

## Ordner auf Christians Computer (OneDrive «Klasse 4b»)
- Druckdateien: `00 Drucken/<MMTT Wochentag>/`, z. B. `1127 Freitag`. Ersetzte Dateien nach `00 Drucken/_ersetzt` verschieben, nicht löschen.
- **Reihenfolge:** Zuerst in den Lektionsordner (`13 Freiday/5 Lektionsplanung/Wo5_…`), dann nach `00 Drucken`. Der Lektionsordner für Fr 20.11. und 27.11. existiert noch nicht.
- Aktuell: Energie Akte 01 → `00 Drucken/1127 Freitag/`, Energie Akte 02 → `00 Drucken/1211 Freitag/` (Termin vorläufig), Wiederholung Fall 1+2 → `00 Drucken/1120 Freitag/`.

## Offene Aufgaben
1. **Verstehen-Schritt für die Energie-Akten** (Christian: «messen und verstehen ist besser als messen und staunen»). Plan:
   - Akte 01: Temperaturen in der App eintippen (4 Orte), Lösung mit Balken aus den eigenen Zahlen. Danach Fragen mit sofortiger Rückmeldung: «Wohin wandert die Wärme?» (mit den eigenen Orten), «Fenster den ganzen Tag gekippt?», «Welche Lüftung ist besser?».
   - Akte 02: Rechnen mit den eigenen Zahlen (Watt × Stunden = Wattstunden, z. B. Beamer 2 h), Vergleich «Lampe 10 h gegen Beamer 1 h», Frage zu Standby. Der Beweisstück-Satz «Watt × Stunden = Wattstunden» ergänzen.
   - Auch die Papier-Akten um «5 · Verstehen» erweitern.
2. Akte 02: Hausabwart informieren (Kinder fragen selbst nach den Watt der Zimmerlampe). Bei Laptop-Netzteilen steht oft nur V und A, dann V × A.
3. Fotos für die Einsatz-Einstiege: echte Fotos statt Emoji (Wikimedia nicht erreichbar, eigene Schulfotos oder Commons-Dateinamen nötig). Fotos in `landing/img/` und in `einsaetze.html` über `foto.img` einbinden.
4. Lektionsplanung Fr 20.11. und 27.11. und Material in den Lektionsordner kopieren.
5. Offene Klärungen: Schulgarten/Hort/Hauswart-Erlaubnisse für die Einsätze; Wiederholung für Akte 03 «Drei Orte» (noch nicht bearbeitet, daher normaler Fall); Test 1 (Haltestelle 1+2) am 4.12.; Budget-Blatt für Fr 27.11.
6. Ermittlungsakten 1–3 (Papier) tragen noch «Klima-Kommissariat» auf dem Deckblatt (bereits gedruckt, bei Neudruck auf «Kommissariat 4b» ändern).

## Bekannte Stolpersteine
- Das Plakat «Heiz- und Stromtipps» (Energiesparmeister) stammt aus Deutschland. Richtwerte können in der Schweiz abweichen.
- Klexikon hat keine Standby-Seite. Das Beweisstück zu Standby ist eigener Text mit verlinkten Quellen.
- Thermometer-Anzahl und Angebot der Vogelwarte-Materialien sind ungeprüft.
- Mythenquai (tecdottir) liefert nachts teils Stunden alte Werte. Die Seite zeigt dann eine Verspätungs-Warnung.
