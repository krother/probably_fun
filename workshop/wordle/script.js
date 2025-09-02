const targetWord = "model"; // The word to guess; you can randomize this if desired.
const maxGuesses = 6;
let guessCount = 0;

function submitGuess() {
  const guessInput = document.getElementById("guess-input");
  const message = document.getElementById("message");
  const guess = guessInput.value.toLowerCase();

  if (guess.length !== 5) {
    message.textContent = "Please enter a 5-letter word.";
    return;
  }

  if (guessCount >= maxGuesses) {
    message.textContent = "You've reached the maximum guesses!";
    return;
  }

  displayGuess(guess);
  guessCount++;

  if (guess === targetWord) {
    message.textContent = "Congratulations! You've guessed the word!";
    guessInput.disabled = true;
  } else if (guessCount === maxGuesses) {
    message.textContent = `Out of guesses! The word was "${targetWord}".`;
    guessInput.disabled = true;
  } else {
    message.textContent = "";
  }

  guessInput.value = "";
}

function displayGuess(guess) {
  const guessContainer = document.getElementById("guess-container");

  for (let i = 0; i < 5; i++) {
    const letterDiv = document.createElement("div");
    letterDiv.classList.add("letter");

    if (guess[i] === targetWord[i]) {
      letterDiv.classList.add("correct");
    } else if (targetWord.includes(guess[i])) {
      letterDiv.classList.add("partial");
    } else {    
      letterDiv.classList.add("wrong");
    }

    letterDiv.textContent = guess[i].toUpperCase();
    guessContainer.appendChild(letterDiv);
  }
}
