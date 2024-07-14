
# Wahrscheinlichkeitsbäume

## Ablauf

1. Spielt in Kleingruppen Memory mit je 20 Karten.
2. zählt wie viele Züge ihr braucht
3. Zeichnet einen Wahrscheinlichkeitsbaum für 4 Paare
4. rechnet aus:

   - wie wahrscheinlich ist es, alle Paare hintereinander zu finden?
   - wie viele Züge braucht es im Schnitt bei einem perfekten Gedächtnis?
   - wie viele Züge braucht es, wenn das Gedächtnis nur in 50% der Fälle funktioniert?

## Schaubild:

2D Matrix:
- Zeilen == verbleibende Paare (zählt abwärts)
- Spalten == gesehene Karten

Jeder Zug hat eines der folgenden Ereignisse:

ERSTE KARTE
- neue Karte aufdecken: 1 Spalte nach rechts wenn p(Gedächtnis) erfolgreich

ZWEITE KARTE
- wenn erste Karte schon bekannt: 1 Zeile nach unten und 1 Spalte nach links
- ansonsten zweite Karte aufdecken


## Material

Ein Memory Spiel mit 20 Karten.
