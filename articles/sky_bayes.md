
Sky Bayes
=========

Goal
----

Students 

Time
----

90'

Concepts
--------

- Naive Bayes
- Bayes Theorem
- Odds ratio
- Prior
- Conditional probability

The Game: Sky Team
------------------

`Sky Team <>`__, the German `game of the year 2024 <>`__ is a cooperative game. Two teams (a pilot and a copilot) attempt to land a passenger plane over seven rounds.
They place dice that control the bearing and speed of the plane, activate flaps and landing gear.
Because the players are not allowed to communicate, there is quite a bit of intuition about the other players dice and intentions at play.

In the lesson, the class forms two teams. Use the simplest possible airport (Montreal) and no specials. With students forming two teams, many playing the game for the first time, they are bound to make terrible mistakes.

To make the game shorter, play 5 rounds instead of 7. Remove any planes on the first visible field.
Play with brakes fully activated.

To use the game in a classroom, you need a device to project the game board to the class (a document camera or phone in an according holder) or an electronic version of the game. A few extra dice would also help.

.. hint::

   If the class is doing well, have a flock of birds hit one of the engines, reducing its maximum output to two. Let's see what probabilities your students estimate.
 
.. hint::

   I want to make the implementation of a very similar game a project in my next programming course. Stay tuned!


How does the lesson work?
-------------------------

During the game, participants will estimate how well they are doing.
This estimate can directly be translated into an estimated probability using the approach described in `Bayes by Hand <>`__ by Laura Summer and Andy Kitchen.

The estimate is points on a decadic log-scale: 10 points difference mean a tenfold change in the odds ratio.
The starting point (prior) for a green airport is 10 points (we expect to win 10 out of 11 games).
The players estimate points for:

- how well landing gear and flaps are covered
- how well they are approaching the airport
- how well the team is communicating

Each estimate ranges from:

------ --------------------------------
points description
------ --------------------------------
+10    perfect
+ 5    going well
  0    nothing special
- 5    troublesome
-10    Houston, we have a problem
------ --------------------------------

Then you sum up the prior and the point estimates and convert them into the estimated probability to land the plane.


Key learnings of the lesson include:

- The relation between the log-points, odds ratio and probability
- How to get rid of the marginal probability in the Bayes equation
- Naive Bayes is really naive: for extreme cases it does not work very well


Lesson Plan
-----------

1. introduce the Bayes Theorem
2. derive the log probability equation
3. announce the goal: use 
3. explain the rules of the game very briefly
4. calculate an initial probability
2. form three teams of ideally 4 people (pilot, copilot and assesors)
3. play two rounds - the teams might briefly discuss which die to place
4. have the assessors assign a point estimate of the situation
5. sum the points and look up the probability in the table
6. play another two rounds and update the estimate
7. land the plane (hopefully)
8. unravel the math: where do the probabilities come from
9. go through the reflection questions

.. hint::

Reflection
----------

- what is a prior?
- how is the probability affected if any of the component probabilities is zero?


Further Reading
---------------

- `SkyTeam Soundtrack <https://www.youtube.com/watch?v=MYsvI8i0hTQ>`__
- somethin on fraud detection
