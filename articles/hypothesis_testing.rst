Bake Dice to test a Hypothesis
==============================

Lesson Goal:
------------

Students test whether a six-sided die is balanced.

Time Frame:
-----------

90’

Motivation
----------

|image6|

Ein didaktisches “Kochrezept” der besonderen Art: Ich habe Würfel (W6)
in den Backofen geschoben und bei 120-140 Grad für 10-20 Minuten
gebacken. Bei zu hoher Temperatur verwandelt sich der Würfel in ein
amorphes etwas, bei zu niedriger passiert nichts. Trifft man die
Bedingungen aber gut, verformt sich der Würfel so geringfügit, dass er
bestimmte Zahlen häufiger würfelt.

Ein solcherart gezinkter Würfel eignet sich fantastisch dazu die Frage
zu diskutieren: “Können wir beweisen, dass ein Würfel gezinkt ist?”. Die
Behandlung der Frage eröffnet auch eine tiefere Betrachtungsweise:
“Woher wissen wir überhaupt etwas?”.

Begriffe: **Hypothesentests**, **Konfidenz**, **p-Werte**,
**Epistemologie**

.. |image6| image:: ../images/chi2_auswertung.jpg


Key Concepts:
-------------

-  null hypothesis (H0)
-  alternative hypothesis
-  test statistic
-  Chi-square-test
-  significance threshold (alpha)
-  critical region
-  p-value
-  predictive power

Warmup:
-------

Dive right in: *“We want to know whether these dice are balanced”*

Hand out dice and have students do 120 dice rolls each, taking tick
marks about how often each number occurs.

Content Delivery:
-----------------

Present and go through the following recipe:

1. decide on a null hypothesis to test (*“the D6 follows a uniform
   distribution”*)
2. choose test statistic
3. decide on alpha
4. determine the critical region
5. calculate the test statistic
6. see whether the result is in the critical region
7. accept or reject H0

Collect the numbers from the dice rolls **only after** deciding on the
value for alpha. Write them into a table and ask with the class what
they think.

Only after that, calculate the test statistic:

:math:`\Chi^2 = \sum \frac{(O_i-E_i)^2}{E}`

where E would be 20 for 120 dice rolls.

Look up the critical values for the Chi-square test statistic using any
online tool. The number of degrees of freedom is five.

Material:
---------

Prepare forged dice:

-  buy a box of D6
-  bake them at 120°-140° for 10-20 minutes
-  then throw into ice water

The temperature in most ovens is not very stable, you may want to bake
one die at a time. If you have a strong group, make this a homework.

Comments:
---------

I skipped a lot of complicated stuff: other tests, error types,
predictive power, because this was the first exposure to hypothesis
testing.

Instead, I spent quite some time to attach huge warnings to the method
and gave examples for p-hacking and the reproducibility crisis.
