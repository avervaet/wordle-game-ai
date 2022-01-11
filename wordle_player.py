import random

class Player():
    def __init__(self, word_list):
        self.dictionnary = set(word_list)
    
    def guess(self):
        return random.choice(tuple(self.dictionnary))
    
    def analyse_hints(self, guess, hints):
        pass

class Player1(Player):
    def __init__(self, word_list):
        Player.__init__(self, word_list)
        self.remaining_words = set(word_list)
    
    def guess(self):
        return random.choice(tuple(self.remaining_words))
    
    def analyse_hints(self, guess, hints):
        for i,e in enumerate(hints):
            x = guess[i]
            if e == "Valid":
                self.remaining_words = set([word for word in self.remaining_words if word[i] == x])
            elif e == "Present":
                self.remaining_words = set([word for word in self.remaining_words if x in word])
            elif e == "Absent":
                self.remaining_words = set([word for word in self.remaining_words if x not in word])