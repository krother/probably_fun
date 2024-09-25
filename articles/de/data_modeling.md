
# Data Modeling

Kopfzeile *Probably Fun: Lessons Plan for gamified statistics teaching*

Zeit: 90'

Spieler: 5-15

## Motivation

Datenmodellierung gehört zu den wichtigsten Tätigkeiten beim Entwickeln von IT-Systemen. Ein Datenmodell bestimmt, was für Daten gespeichert werden (Datentypen) und wie sie zueinander in Beziehung stehen (Relationen). Verwendet man eine Datenbank, steht am Anfang meist die Frage, welche Tabellen es geben soll und welche Spalten diese enthalten.

Oft gilt es zwischen mehreren Alternativen abzuwägen. Diese beeinflussen, wie schnell das System bestimmte Anfragen bearbeiten kann, wie leicht es zu ändern ist und welche Arten von Fehlern auftreten können.
Deshalb sollte man bei der Datenmodellierung etwas Sachkenntnis der Materie mitbringen.

## Unterrichtsziel

Die Spieler erstellen ein Datenmodell des Spiels **"Splendor"**, um den Spielstand in einer Datenbank abzubilden.

BILD SPLENDOR FLAVOR IMAGE

## Material

* Splendor (1 Box je 5 Spieler)
* Tafel oder Flipchart
* SQL-Datenbank

## Vorbereitung

Für die Implementierung in SQL müssen die Spieler eine SQL-Datenbank installiert haben.

## Ablauf

1. 5' Regeln von Splendor erklären (siehe Box)
2. 30' Spielen
3. 5' Problem vorstellen: wir möchten den Spielstand speichern. Welche Tabellen brauchen wir?
4. 20' Im Lehrgespräch ein Datenmodell an der Tafel entwickeln. Der Input sollte dabei überwiegend von den Teilnehmern kommen. Schreibe die Namen von Spalten und deren Datentyp auf.
5. 20' das fertige Datenmodell als `SQL CREATE TABLE` implementieren und ausführen
6. 10' Puffer und Fragen

BILD: Datenmodell

### Box: vereinfachte Regeln von Splendor

Die Regeln von Splendor wurden vereinfacht, um das Spiel zu beschleunigen.
Die Level-3-Karten und die VIPs werden komplett weggelassen.

Zieht nacheinander im Uhrzeigersinn. Ein Spieler am Zug darf eine der folgenden Aktionen durchführen:

- 3 Chips mit unterschiedlicher Farbe nehmen
- 2 Chips mit gleicher Farbe nehmen
- 1 Karte reservieren und 1 Gold nehmen
- 1 Karte kaufen (aus der Auslage oder eine reservierte)

Ein Spieler kann bis zu 8 Chips gleichzeitig haben.

Das Spiel endet sofort, sobald ein Spieler 10 Punkte hat.

## Fragen

- wie lässt sich abbilden, wem eine Karte gehört?
- sollte der Besitzer einer Karte als Zahl `spieler_id=3` oder als Text `besitzer="Maria Stuart"` definiert werden?
- wie werden Karten im Stapel und der Auslage unterschieden?
- wie lassen sich zwei identische Karten unterscheiden?
- ist es besser, für die Farbe einer Karte eine Spalte mit Text (farbe:"blau") oder 5 Spalten (blau:1, rot:0) anzulegen?
- was passiert bei Tippfehlern ("balu")?
- wie könnte man mehrere Partien speichern?

## Notizen

Das Splendor-Spiel ist eine ausgezeichnetes Priming, das domänenspezifisches Wissen aufbaut. Die Begrenzung auf einen klaren Anwendungsfall ("Spielstand speichern") erlaubt den Transfer in die Praxis.

Beim Formulieren des Datenmodells sollten mindestens zwei Tabellen entstehen. 
Das wichtigste Aha-Erlebnis ist, wenn die Gruppe realisiert, dass zwei Tabellen sinnvoll sind.

Für das Gelingen der Übung ist es unerheblich, ob die Tabellen eine `id`-Spalte enthalten.

Bei Vorkenntnissen läßt sich das Modellieren der Daten auch in Kleingruppen durchführen.

## Fortsetzung

Das Datenmodell kann als Startpunkt einer ganze Serie von Lektionen zu SQL dienen:

- C.R.U.D. Operationen
- Primärschlüssel
- Fremdschlüssel und Kardinalität
- SQL JOIN
- Constraints (CHECK, UNIQUE) 
- Normalisierung von Datenbanken

## Varianten

- die VIPs lassen sich als Hausaufgabe oder Wiederholungsübung modellieren
- das Spiel "Drecksau" lässt sich ebenfalls mit 2+ Tabellen sinnvoll modellieren. Das Datenmodell ist etwas einfacher, dafür ist das Spiel günstiger und einfacher zu transportieren.
- Als Einsteigervariante lässt sich eine Tabellnkalkulation statt SQL verwenden.
- Eine Programmiersprache sollte ebenfalls funktionieren.

## Spielhilfen

### Tabelle mit SQL-Datentypen
...

### Rezept zum Modellieren einer Tabelle

1. Name der Tabelle festlegen: lowercase_plural_nomen
2. Spalten festlegen
3. Datentyp für jede Spalte festlegen
4. id-Spalte hinzufügen (als SERIAL PRIMARY KEY)
5. Fremdschlüssel hinzufügen

### Musterlösung

...

## Links

- Splendor Brettspiel
- Splendor bei boardgamearena
- SQL w3schools
- Online-SQL-Editor
- gitpod SQL?
