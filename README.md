# Phishing-URL-checker-
Bei diesem Projekt handelt es sich um ein einfaches Anfängerprojekt von einem IT-Sicherheitsstudenten, das häufige Phishing-Merkmale in einer URL überprüft und diese Markiert. 

## Übersicht 

Der Phishing Checker ist ein auf python basiertes Projekt das als portfolio Projekt aufgebaut wurde um sich mit Praktischen IT-Sicherheits Konzepten auseinander zusetzen. Es benutzt dabei eine von einem Benutzer eingegebene URL und überprüft typische Phishing Merkmale, liefert basierend darauf ein Risiko score, und dazu ein Ergebnis mit Passsender Begründung.

Das Ziel des Ganzen ist es ein erklärbares Werkzeug zu bauen das sicheres Denken sowie, einfache Gefahrenerkennung, Eingabevalidierung und saubere Dokumentation zeigt.

## Features

- Analyse einer benutzereingegebenen URL auf Phishing-Muster.
- Erkennung verschiedener Faktoren wie, verdächtige Symbole/Zahlen/Wörter, Verwendung von http statt https, Lookalikes (1 statt l) in der URl.
- Bewertung anhand eines Scores, mit verschiedenen Gewichtungen für jede Regel. Daraus folgt dann eine Ausgabe mit sicher, verdächtig, und sehr     verdächtig.
- Ausgabe eines Begründung die für jeden verständlich ist.
- Eine Benutzeroberfläche mit einer Eingabe für die Url und einer Ausgabe mit dem Ergebnis.
- Keep the logic modular so additional rules or APIs can be added later.

## Example Checks

The checker can include rules such as:

- URL uses an IP address instead of a domain.
- URL contains the `@` symbol.
- URL is unusually long.
- URL contains many subdomains.
- URL uses suspicious words such as `login`, `verify`, `secure`, `update`, or `account`.
- URL comes from a known shortening service.
- URL uses punycode or unusual character patterns.

## Project Structure

## Beschreibung

main.py ist der Checker ohne UI und funktioniert nur über die Komandozeile im Terminal.
app.py ist die Version mit der UI und läuft über den Browser, sie läuft mit flask in Kombination mit der html Datei für die Webseite.
in url_rules.py befinden sich die Regeln auf die die Url überprüft wird, sie liefert den score und die Begründung.
index.html ist die Webseite, style1.css ist für das Design verantwortlich.

```text
phishing-url-checker/
├── app.py
├── url_rules.py
├── main.py
├── static/style1.css
├── templates/index.html
└── README.md

