# %%
import random 

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.guesses = [] #making an empty list to then append later 
        self.lives = num_lives
        self.num_letters = len(set(self.word))

        while True:
            guess = input("Enter a single letter.")
            if len(guess) == 1 and guess.isalpha():
                break
            else: 
                print("Invalid letter. Please, enter a single alphabetical character.")

guess = input("Enter a single letter.")

word_list = ["Pear", "Pineapple", "Apple", "Mango", "Melon"]

word = random.choice(word_list)

while True:
    if guess in word:
        print(f"Good guess! {guess} is in the word.")

        break
    
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

        break 

