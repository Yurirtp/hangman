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

def ask_for_input():
    check = check_guess()
    while True:
        guess = input("Enter a single letter.")
        if len(guess) == 1 and guess.isalpha():
            break
        else: 
            print("Invalid letter. Please, enter a single alphabetical character.")
        check(guess)



ask_for_input()





                





