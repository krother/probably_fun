
The Entropy of Wordle
=====================

|image2|

Wordle eignet sich als Aufwärmspiel für Unterricht (als Idee von
Christina übernommen). Fantastisch für Statistik, da sich hier die
Themen **bedingte Wahrscheinlichkeit** und **Kombinatorik** illustrieren
lassen. Ein programmiertechnischer Exkurs könnte die absoluten
Wahrscheinlichkeiten anhand der SOWPODS-Liste (offizielle Liste aller
erlaubten englischsprachigen Scrabble-Wörter) berechnen und so eine
optimale Auswahlstrategie entwickeln (GINI-Score).

geeignete Wörter: RANGE, PIVOT, BAYES

.. |image2| image:: ../images/wordle.jpg

1. download the SOWPODS list [LINK]
2. calculate the entropy of one position
3. calculate the overall entropy (??)
4. apply a condition, calculate entropy again
5. count frequent combinations of characters
6. calculate mutual info of two columns
7. strategy to find the best guess