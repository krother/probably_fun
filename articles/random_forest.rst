
Animal Decision Tree
====================

Goal
----

Students construct decision trees to identify animals.

Time
----

60'

The Game: Twenty Questions
--------------------------

One player thinks of an animal. The others try to guess it by asking questions.
The first player only answers "yes" or "no":

::

    Q: can it fly?
    A: no

    Q: does it have 4 legs?
    A: no

    Q: is it a snake?
    A: yes

    Q: is it a Python?
    A: yes!

Decision Trees are machine learning models that identify questions to make efficient predictions. They are the computerized version of the twenty questions game.

To implent the tree model with a larger group, you should have a set of 8 different animals.
I used the material from the game `Tier auf Tier <https://www.haba-play.com/de-de/p/tier-auf-tier--2011189#variationId=2011189001>`__.
Any other animal figures should work as well. The first versions of the game worked with animals on paper cards.

Each group needs a bag with 8 different animals. They will pick 4 at random
Sheets of paper for drawing trees should also come in handy.

.. topic:: Instructions for students

   1. pick four animals. This is your training data
   2. draw a decision tree with yes/no questions that identifies the animals (see example)
   3. take all eight animals. This is your test data
   4. check what your decision tree would predict for all animals
   5. compare the predictions of multiple trees; train a second tree or use the ones from previous groups
   6. calculate an overall accuracy

Lesson Plan
-----------

Students should have a basic understanding of what machine learning and supervised learning are.

====== ==================================================================================== =======
step   description                                                                          time
====== ==================================================================================== =======
1.     Play a few rounds of "Twenty Questions" with the class. You pick the first animal,   5'
       students pick the next.
2.     Discuss components of a tree (see Figure in the linked chapter)                      5'
3.     ask students to construct decision trees                                             10'
4.     put the trees on display in class                                                    5'
5.     make predictions for all animals in the test set for all trees                       10'
6.     calculate the accuracy of each individual tree                                       10'
7.     make a consensus prediction (majority vote)                                          5'
8.     calculate the accuracy of the consensus                                              5'
====== ==================================================================================== =======


.. note::

    The choice of animals is crucial for how well the random forest works.
    The 8 animals simplify the model a bit, because not all target classes are used by all the trees.
    But it should get the idea across and allow you to follow up with theory.

Material
--------

.. seealso::

    - `Decision Trees <https://www.academis.eu/machine_learning/decision_trees/README.html>`__
    - `Random Forests <https://www.academis.eu/machine_learning/random_forests/README.html>`__