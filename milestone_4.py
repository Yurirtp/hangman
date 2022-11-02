#%%
import random
guess = input("Enter a single letter.")

class Hangman:
    def __init__(self, word_list=["pear", "pineapple", "apple", "mango", "melon"], num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.list_of_guesses = [] #making an empty list to then append later 
        self.word_guessed = len(self.word) * ["_"]
        self.num_letters = len(set(self.word).difference(set(self.word_guessed)))
        

    def check_guess(self, guess): # need to copy milestone 3 set up 
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
                self.num_letters = self.num_letters-1     
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word. Try again.") 
            print(f"You have {self.num_lives} lives left.")    
        self.list_of_guesses.append(guess)        


    def ask_for_input(self): 
        while True:
                guess = input("Enter a single letter.")
                guess = guess.lower()
                if len(guess) != 1 and guess.isalpha() == False:
                    print("Invalid letter. Please, enter a single alphabetical character.")
                    break
                elif guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.list_of_guesses.extend(guess)
                    self.check_guess(guess)                    
                    break
            
run = Hangman()
run.ask_for_input()




