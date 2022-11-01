import random
guess = input("Enter a single letter.")

word_list = ["Pear", "Pineapple", "Apple", "Mango", "Melon"]

word = random.choice(word_list)
num_lives = 5

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.list_of_guesses = [] #making an empty list to then append later 
        self.lives = num_lives
        self.guess = guess
        self.num_letters = len(set(self.word))
        self.word_guessed = len(self.word) * ["_"]



