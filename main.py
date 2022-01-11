import os
from word_scrapping import scrap_5_letter_words
from wordle_simulator import Game
from wordle_player import *

if not os.path.isfile("5_letters_words.txt"):
    scrap_5_letter_words()

with open("5_letters_words.txt", "r") as f:
    word_list = [x[:-1] for x in f.readlines()]


game = Game(word_list)
player = Player1(word_list)
game.play(player)