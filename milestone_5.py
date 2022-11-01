#%%
import random
guess = input("Enter a single letter.")

word_list = ["pear", "pineapple", "apple", "mango", "melon"]

word = random.choice(word_list)
num_lives = 5

class Hangman:
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.list_of_guesses = [] #making an empty list to then append later 
        self.num_lives = 5
        self.guess = guess
        self.word_guessed = len(self.word) * ['_']
        self.num_letters = len(set(self.word).difference(set(self.word_guessed)))
        

    def check_guess(self, guess):
        guess = guess.lower()  
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
                    print(self.word_guessed)
                    break
                self.num_letters = self.num_letters-1     
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word. Try again.") 
            print(f"You have {num_lives} lives left.")    
        self.list_of_guesses.extend(guess)        


    def ask_for_input(self):
        print(self.word_guessed)
        while True:
                guess = input("Enter a single letter.")
                if len(guess) != 1 and guess.isalpha() == False:
                    print("Invalid letter. Please, enter a single alphabetical character.")
                elif guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.list_of_guesses.extend(guess)
                    self.check_guess(guess)                    
                    break
                
    def play_game(self, word_list):
        game = Hangman(word_list,num_lives=5)
        game.ask_for_input()
        while True:
            if game.num_lives == 0:
                print("You lost!")
            elif game.num_letters > 0:
                game.ask_for_input()
            elif game.num_letters != 0 and game.num_letters == 0:
                print('Congratulations. You won the game!')
                break   
        

game = Hangman(word_list,num_lives=5)
game.play_game(word_list)
            




