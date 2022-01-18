import random

class Player():
    def __init__(self, word_list):
        self.dictionnary = set(word_list)
    
    def guess(self):
        return random.choice(tuple(self.dictionnary))
    
    def analyse_hints(self, guess, hints):
        pass

class Player1(Player):
    """A basic player instance that randomly pick an available word
    and use hints to refine its pool"""
    def __init__(self, word_list):
        Player.__init__(self, word_list)
    
    def guess(self):
        return random.choice(tuple(self.dictionnary))
    
    def analyse_hints(self, guess, hints):
        for i,e in enumerate(hints):
            x = guess[i]
            if e == "correct":
                self.dictionnary = set([word for word in self.dictionnary if word[i] == x])
            elif e == "present":
                self.dictionnary = set([word for word in self.dictionnary if x in word and word[i] != x])
            elif e == "absent":
                self.dictionnary = set([word for word in self.dictionnary if x not in word])