import os
from word_scrapping import scrap_5_letter_words
from wordle_simulator import Game
from wordle_player import *

NUMBER_OF_SIMULATION = 1000

if not os.path.isfile("5_letters_words.txt"):
    scrap_5_letter_words()

with open("5_letters_words.txt", "r") as f:
    word_list = [x[:-1] for x in f.readlines()]

# Test Random player
score = 0
for i in range(NUMBER_OF_SIMULATION):
    game = Game(word_list)
    player = Player(word_list)
    score += game.play(player)
print(f"Average score for Random player: {score/NUMBER_OF_SIMULATION}")

# Test player 1
score = 0
for i in range(NUMBER_OF_SIMULATION):
    game = Game(word_list)
    player = Player1(word_list)
    score += game.play(player)
print(f"Average score for Player1: {score/NUMBER_OF_SIMULATION}")