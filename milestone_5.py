#%%
import random

class Hangman:
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.list_of_guesses= [] #making an empty list to then append later 
        self.word_guessed = len(self.word) * ["_"]
        self.num_letters = len(set(self.word).difference(set(self.word_guessed)))
        print(self.word_guessed)

    def check_guess(self, guess):  
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = letter     
            self.num_letters -=1
            print(self.word_guessed)     
        else:
            letter = guess
            self.num_lives -=1
            print(f"Sorry, {letter} is not in the word.") 
            print(f"You have {self.num_lives} lives left.")
            return print(self.word_guessed) 
                             


    def ask_for_input(self): 
        while True:
                guess = input("Enter a single letter.")
                guess = guess.lower()
                if len(guess) != 1 and guess.isalpha() == False:
                    print("Invalid letter. Please, enter a single alphabetical character.")
                elif guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.list_of_guesses.append(guess)
                    self.check_guess(guess)  
                    break                  

                
    
def play_game(word_list = ["pear", "pineapple", "apple", "mango", "melon"]):
    game = Hangman(word_list,num_lives=5)
    game.ask_for_input()
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif not game.num_letters >0 and game.num_lives != 0:
            print('Congratulations. You won the game!')
            break           


play_game()






