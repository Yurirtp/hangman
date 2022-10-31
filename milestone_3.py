# %%
import random




word_list = ["Pear", "Pineapple", "Apple", "Mango", "Melon"]

word = random.choice(word_list)
num_lives = 5

def check_guess():
            guess = input("Enter a single letter.")
            guess = guess.lower()  
            while True:
                    if guess in word:
                        print(f"Good guess! {guess} is in the word.")
                        break
                    else:
                        print(f"Sorry, {guess} is not in the word. Try again.")
                        break 

check = check_guess()

def ask_for_input(check):
        while True:
            guess = input("Enter a single letter.")
            if len(guess) != 1 and guess.isalpha() == bool(0):
                print("Invalid letter. Please, enter a single alphabetical character.")
                break
            return check_guess()            



ask_for_input(check)





                





