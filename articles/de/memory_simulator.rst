
.. _memory_simulator_de:

Memory Simulation
=================

   
.. figure:: ../../images/memory.jpg

Hast du dich schon einmal gefragt, wie viele Züge es bei einer Partie `Memory <https://de.wikipedia.org/wiki/Memory_(Spiel)>`__ dauert, bis alle Paare gefunden sind?
Hier kannst du viele, viele Partien durch den Computer simulieren lassen und prüfen, wie viele Züge dieser benötigt.

Die Simulation
--------------

.. raw:: html

   <p>
       <label for="nPairs">Anzahl Paare:</label>
       <input type="number" id="nPairs" value="10">
   </p>
   <p>
       <label for="totalRuns">simulierte Partien:</label>
       <input type="number" id="totalRuns" value="100">
   </p>
   <p>
       <label for="memQuality">Retention (Gedächtnisleistung) [%]:</label>
       <input type="number" id="memQuality" value="100">
   </p>

    <button onclick="startSimulation()">Ergebnisse anzeigen</button>
   
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
   
       resultDiv.innerHTML = Object.entries(counter).map(([turns, count]) => `<p>${turns} Züge: ${count*100 / total_runs}%</p>`).join('');
   }
   </script>

Anmerkungen
-----------

- wenn der Computer ein Paar aufdeckt, darf er im gleichen Zug zwei weitere Karten aufdecken.
- bei *100% Retention* merkt sich der Computer alle Karten und deckt niemals die gleiche Karte ein zweites Mal auf, außer er kann ein Pärchen bilden.
- bei *50% Retention* vergisst der Computer im Schnitt jede zweite Karte gleich wieder.
- bei *0% Retention* merkt sich der Computer überhaupt nichts mehr und findet Paare nur durch Zufall.
- hat sich der Computer eine Karte erst einmal gemerkt, erinnert er sich die gesamte Partie hindurch an diese.
- Es gibt auch eine `Python-Version des Memory-Simulators <../memory_simulator.py>`__

.. seealso::

   `Memory online spielen <https://krother.github.io/js_miniprojects/04-memory/memory.html>`__

.. card:: Probably Fun
   
   games to teach statistics

   .. figure:: ../../images/title.png
      :width: 600px

   © 2024 `Dr. Kristian Rother <https://www.academis.eu>`__

   Nutzbar unter den Bedingungen der `Creative Commons Attribution Share-alike License 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`__.
