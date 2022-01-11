# wordle-game-ai

## Setup

`pip install -r requirement.txt`

## Run the benchmark

`cd src`
`python3 benchmark.py`

## Add a new player 

Your player should extend the Player class located [here](src/wordle_player.py).
A Player as at least two methods:
    -> guess() that predict a word
    -> analyse_hints(guess, hints) that gets hints regarding to your last guess

## Guessing

You can only guess word that exist in the game dictionnary

## Analyzing hints

Hints are an array filled with the following values: 
* "Valid" -> letter at the given position was correct
* "Present" -> letter at the given position exist inside the secret word but not at this position
* "Absent" -> letter does not exist inside the secret word

## Example

secret_word = "plane"
guess = "large"
hints = ["Present", "Present", "Absent", "Absent", "Valid"]


## Becnhmark scores
Average number of guess is calculated on 10000 random wordle game simulation.
This value fluctuate but it gives an order of idea of the performance for each method.

**RandomPlayer:**
Randomly return a word at every step. It can guess the same word multiple times.
* Average number of guess: 486.6

**Player1:**
Use hints to remove words from its pool. Randomly guess a word from its pool.
* Average number of guess: 3.778