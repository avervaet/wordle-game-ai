import random
from wordle_player import Player

class Game():
    def __init__(self, word_list):
        self.dictionnary = set(word_list)
    
    def play(self, player: Player):
        # Randomly pick a word
        secret_word = random.choice(tuple(self.dictionnary))
        #print(f"Secret word is: {secret_word}")

        guess_number = 1
        while True:
            # Enter a guess
            guess = player.guess()
            # Check that the guess exist in the dictionnary
            if guess not in self.dictionnary:
                print("Invalid word")
                continue
            
            # Check win
            if guess == secret_word:
                #print(f"Congratulation you win in {guess_number}")
                return guess_number
            else:
                hints = self.generate_hints(guess, secret_word)
                player.analyse_hints(guess, hints)
            guess_number += 1
            
    def generate_hints(self, guess, secret_word):
        hints = []
        for i,e in enumerate(guess):
            if e == secret_word[i]:
                hints.append("Valid")
            elif e in secret_word:
                hints.append("Present")
            else:
                hints.append("Absent")
        return hints
            