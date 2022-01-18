import os
import tqdm
from word_scrapping import scrap_5_letter_words_bestwordlist
from wordle_simulator import Game
from wordle_player import *

number_of_simulation = 1000
dictionnary_file = "../dictionnaries/5_letters_words.txt"

if not os.path.isfile(dictionnary_file):
    scrap_5_letter_words_bestwordlist(dictionnary_file)

with open(dictionnary_file, "r") as f:
    word_list = [x[:-1] for x in f.readlines()]

players = [Player, Player1]
for player in players:
    print(f"Benchmarking {player.__name__}")
    score = 0
    for i in tqdm.tqdm(range(number_of_simulation)):
        game = Game(word_list)
        player_instance = player(word_list)
        score += game.play(player_instance)
    print(f"Average number of guess for {player.__name__}: {score/number_of_simulation}")