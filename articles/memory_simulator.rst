
.. _memory_simulator:

Memory Simulation
=================
   
.. figure:: ../images/memory.jpg
   :width: 800px

Have you ever wondered, how many turns it takes to match all pairs in a game of `Memory <https://en.wikipedia.org/wiki/Concentration_(card_game)>`__?
Let simulate many, many games in the computer and check how many turns they need.

The Simulation
--------------

.. raw:: html

   <p>
       <label for="nPairs">Number of Pairs:</label>
       <input type="number" id="nPairs" value="10">
   </p>
   <p>
       <label for="totalRuns">Simulation Runs:</label>
       <input type="number" id="totalRuns" value="100">
   </p>
   <p>
       <label for="memQuality">Memory retention [%]:</label>
       <input type="number" id="memQuality" value="100">
   </p>

    <button onclick="startSimulation()">Show Results</button>
   
   <div id="result"></div>
   
   <script>
   function shuffleArray(array) {
      // array.sort(() => Math.random() - 0.5); // was somehow biased
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
   }
   function rememberCard(cards, unveiled, newCard, memQuality) {
       // implement shaky retention
       if (Math.random() * 100 <= memQuality) {
           // memory works, remember the card forever
           unveiled.add(newCard);
        }
        else {
           cards.push(newCard);
           shuffleArray(cards); // reshuffle to avoid constant order
        }
   }

   function memoryGame(nPairs, memQuality) {
       // Step 1: Create cards
       let cards = [];
       for (let i = 1; i <= nPairs; i++) {
           cards.push(i, i);
       }
       shuffleArray(cards);
       let turns = 1;
       let unveiled = new Set();
       
       while (cards.length > 0) {
           // First card
           let first = cards.pop();
           if (unveiled.has(first)) {
               // Found a pair with a remembered card
               unveiled.delete(first);
           } else {
               // look at the second card
               let second = cards.pop();
               if (second === first) {
                   // Found a pair, great
               } else if (unveiled.has(second)) {
                   // Found already seen card, takes an extra turn to collect it
                   rememberCard(cards, unveiled, first, memQuality);
                   unveiled.delete(second);
                   turns++;
               } else {
                   // No pair
                   rememberCard(cards, unveiled, first, memQuality);
                   rememberCard(cards, unveiled, second, memQuality);
                   turns++;
               }
           }
       }
       return turns;
   }

   function startSimulation() {
       const nPairs = parseInt(document.getElementById('nPairs').value);
       const total_runs = parseInt(document.getElementById('totalRuns').value);
       const resultDiv = document.getElementById('result');
       const memQuality = parseInt(document.getElementById('memQuality').value);
       let result = [];
       for (let i = 0; i < total_runs; i++) {
           result.push(memoryGame(nPairs, memQuality));
       }
       result.sort((a, b) => a - b);
       const counter = {};
       result.forEach(turns => {
           counter[turns] = (counter[turns] || 0) + 1;
       });
   
       resultDiv.innerHTML = Object.entries(counter).map(([turns, count]) => `<p>${turns} turns: ${count*100 / total_runs}%</p>`).join('');
   }
   </script>

Notes
-----

- if the player unveils a pair, they get to check another two cards in the same turn.
- *100% retention* means the computer will never unveil the same card twice unless they know which other card to pair it with.
- *50% retention* means the computer will forget every second card on average.
- *0% retention* means the computer will not remember anything and can only find pairs by coincidence.
- once a card is remembered, the computer will remember it for the rest of the game.
- check out the :download:`Python version of the memory simulator <memory_simulator.py>`

.. seealso::

   `play memory online <https://krother.github.io/js_miniprojects/04-memory/memory.html>`__

.. card:: Probably Fun
   
   games to teach statistics

   .. figure:: ../images/title.png
      :width: 600px

   © 2024 `Dr. Kristian Rother <https://www.academis.eu>`__

   Usable under the conditions of the `Creative Commons Attribution Share-alike License 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`__.
