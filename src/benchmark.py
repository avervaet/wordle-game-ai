import os
from word_scrapping import scrap_5_letter_words
from wordle_simulator import Game
from wordle_player import *

NUMBER_OF_SIMULATION = 10000
DICTIONNARY_FILE = "dictionnaries/5_letters_words.txt"

if not os.path.isfile(DICTIONNARY_FILE):
    scrap_5_letter_words(DICTIONNARY_FILE)

with open(DICTIONNARY_FILE, "r") as f:
    word_list = [x[:-1] for x in f.readlines()]

# Test Random player
score = 0
for i in range(NUMBER_OF_SIMULATION):
    game = Game(word_list)
    player = Player(word_list)
    score += game.play(player)
print(f"Average number of guess for Random player: {score/NUMBER_OF_SIMULATION}")

# Test player 1
score = 0
for i in range(NUMBER_OF_SIMULATION):
    game = Game(word_list)
    player = Player1(word_list)
    score += game.play(player)
print(f"Average number of guess for Player1: {score/NUMBER_OF_SIMULATION}")