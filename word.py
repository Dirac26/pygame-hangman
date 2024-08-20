import random

with open("assets/words.txt") as f:
    words = f.read().splitlines()

class Word:
    def __init__(self):
        self.word = random.choice(words)
        print(self.word)
        self.guessed = []

    def guess(self, letter):
        if letter not in self.guessed:
            self.guessed.append(letter)
        print(self.guessed)
        return letter in self.word
    
    def is_guessed(self):
        return all([letter in self.guessed for letter in self.word])
    
    def display(self):
        return [letter if letter in self.guessed else '_' for letter in self.word]
    
