# %%
import random 

guess = input("Enter a single letter.")

word_list = ["Pear", "Pineapple", "Apple", "Mango", "Melon"]

word = random.choice(word_list)
num_lives = 5

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.guessed = [] #making an empty list to then append later 
        self.lives = num_lives
        self.num_letters = len(set(self.word))

    def check_guess(self, guess):
        guess = guess.lower()  
        while True:
                if guess in word:
                    print(f"Good guess! {guess} is in the word.")
                    break
                else:
                    print(f"Sorry, {guess} is not in the word. Try again.")
                    break 

    def ask_for_input(self):
        check = self.check_guess
        while True:
                guess = input("Enter a single letter.")
                if len(guess) == 1 and guess.isalpha():
                    break
                else: 
                    print("Invalid letter. Please, enter a single alphabetical character.")
                    break
        check()
            
a = Hangman([word_list, num_lives])

a.ask_for_input()

        


                





