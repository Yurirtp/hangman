# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain number of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
---
## Milestone 1 
Milestone 1 task: Set up the development environment. This included setting up a GitHub account, creating a repository for the Hangman project as well as using linking the repository to GitHub. This is so that, when you tell git to start keeping track of the files in a folder (or directory), you move the commits to a git repository, in which git stores the snapshots of the files in the working directory. Additionally, I learnt the essentials of Git.

Other tasks in Milestone 1 were to use Command line (Command Prompt), for file manipulation and running terminal commands.
---
## Milestone 2 
Milestone 2 task: Create a file named milestone_2.py. Create a list, and assign to a variable, then print out the newly created list.

The following is an example of the code written for each task:

- Creating a list --> ["Pear", "Pineapple", "Apple", "Mango", "Melon"]

- Assigning a list to a variable --> word_list = ["Pear", "Pineapple", "Apple", "Mango", "Melon"]


- Printing out list --> print(word_list)

Next, I imported 'random' module in the first line of the file. --> import random 

The random module is one of Python's built-in modules. It has a choice method which returns a random item from a given sequence.

random.choice method was used to then pass the word_list variable into the choice method. --> random.choice(word_list)

Then a randomly generated word was assigned to the varibale called word --> word = random.choice(word_list)

This was then printed out to the standard output. This was run multiple times to observe different word printed after each run. --> word = random.choice(word_list)      
print(word)

Use of the input function so user can enter a single letter. Futhermore, assigned this input to a variable. --> guess = input("Enter a single letter.") 

I then proceeded to create code which validates the users input by checking is the input is only a single letter and is an alphabetic chatacter. Uding an if statment I wrote the following code check code against this creiteria. --> 

guess = input("Enter a single letter.")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else: 
    print("Oops! That is not a valid input")

The last task of MIlestone 2 was to start documenting the experience of this project. Through this I have made sure that my GIthub is set up where I can upload/update the lasted versions of my working documents.

Below is all the code written for Milestone 2 -->

#%%
import random 


word_list = ["Pear", "Pineapple", "Apple", "Mango", "Melon"]

word = random.choice(word_list)

print(word)

guess = input("Enter a single letter.")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else: 
    print("Oops! That is not a valid input")


## MIlestone 3 

Milestone 3 task is to continuously ask the user for a letter and validate it. 

A new script called milestone_3.py saved. I created a while loop and set the condition to True. Setting this condition to True ensures that the code runs continuously. In the body of the loop, code for the function of guessing a letter was entered, here I assigned the variable called guess. In this function, I made sure that guess checked function checked that the guess is a single entry, and is an alphabetical character. I also ensured that, if the checks passed for the first if statment, it breaks out of the loop.

while True:
                guess = input("Enter a single letter.")
                if len(guess) == 1 and guess.isalpha():
                    break
                else: 
                    print("Invalid letter. Please, enter a single alphabetical character.")
                    

If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."

I also checked my code by making the code to make the user guesses letter "a" and the secret word is "apple", then the code will check if "a" is in "apple".

I then proceeded to create an if statement that checks if the guess is in the word. In the body of the if statement, I made the return print a message saying "Good guess! {guess} is in the word.". The format  of the string shows the actual guess instead of {guess}.I proceeded to create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.

 while True:
                if guess in word:
                    print(f"Good guess! {guess} is in the word.")
                    break
                else:
                    print(f"Sorry, {guess} is not in the word. Try again.")
                   


I then proceeded to create two functions which contained the code above in MIlesotne 3.
The two functions created are check_guess and ask_for_input functions which contain the code for those two things.

The functions are made by first defining the name of the function, and then created the return type of the function, which is what is returned which is shown in the code above. I also made sure to list inside parenthesis (), I listed parameters the function takes.
I also included the curly brackets {}, this code will run whenever the function is called. This is called the body of the function.

I defined a function called check_guess. I then passed in guess as a parameter for the function. Then I wrote the code for the following steps in the body of this function. ##Converting the guess into lower case, and then moving the code that to check if the guess is in the word into this function block.

I then proceeded to check the check_guess function, and made sure that it takes the guessed letter as an argument and check if the letter is in the word.

def check_guess(guess): 
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")




I then defined the function called ask_for_input. I moved the code that I wrote in the Iteratively check if the input is a valid guess task into this function block. I then added outside the while loop, within the function, which call the check_guess function to check if the guess is in the word. I then made sure to pass in the guess as an argument to the method "check_guess(guess)". 

I then called the the function ask_for_input, to test your code.

def ask_for_input():
    while True:
        guess = input("Enter a single letter.")
        guess = guess.lower() 
        if len(guess) == 1 and guess.isalpha():
            break
        else: 
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)


# %%
import random 

guess = input("Enter a single letter.")

word_list = ["pear", "pineapple", "apple", "mango", "melon"]

word = random.choice(word_list)
num_lives = 5
   
def check_guess(guess): 
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    while True:
        guess = input("Enter a single letter.")
        guess = guess.lower() 
        if len(guess) == 1 and guess.isalpha():
            break
        else: 
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)
            
ask_for_input()


# %%

# Milestone 4 

Method is a function that is defined inside a class.
To help the write the code I created a class initialisation block, which is a block of statments preceded by static keywords that are introduced in the class body. When the class loads these statments are executed, for this self is used as an instance of the class, so we can access the attributes and methods of the class in python when we call upon it, the reason we use self is because pythons syntax does use the @ syntax to refer to instance attributes:

Hangman is a game where the user has to guess a word by guessing the letters in the word.
The game is over when the number of lives is 0 or the number of letters left to guess is 0.


The class Hangman is created with the following attributes, parameters and methods:

Parameters:
    word_list: a list of words to choose from
    num_lives: the number of lives the user has; default is 5

Attributes:
    word: the word to guess
    word_guessed: the word with the letters guessed
    num_letters: the number of letters left to guess
    num_lives: the number of lives left
    word_list: the list of words to choose from
    list_of_guesses: the list of letters guessed

Methods:
    check_guess: checks if the guess is in the word and updates the word_guessed.

    ask_for_input: asks the user for a letter and calls the check_guess method

There are two methods: one asking for the input (ask_for_input) and another checking if the supplied letter is in the "word" (check_guess). "Ask_for_input_ method calls "check_guess" method whenever the user input matches the condition that it is a single alphabetical character.

In case the supplied letter is not part of the "word" the number of lives attributes is reduced by one. Otherwise if the letter is guessed correctly, word_guessed and num_letters attributes are respectively updated.

Below is the code written in milestone 4 

#%%
import random

#%%
import random

class Hangman:
    def __init__(self, word_list=["pear", "pineapple", "apple", "mango", "melon"], num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.list_of_guesses= [] #making an empty list to then append later 
        self.word_guessed = len(self.word) * ["_"]
        self.num_letters = len(set(self.word).difference(set(self.word_guessed)))

    def check_guess(self, guess): 
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = letter     
            self.num_letters -=1     
        else:
            letter = guess
            self.num_lives -=1
            print(f"Sorry, {letter} is not in the word.") 
            print(f"You have {self.num_lives} lives left.")              


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
            
run = Hangman()
run.ask_for_input()

For this run was used, and is later known as the variable (game). 



# Milestone 5 

Milestone 5 leverages on the Milestone 4 Hangman class and preserves all methods and attributes detailed in Milestone 4.

The addition of this Milestone is a python play_game() function which defines the logic of the game:

The game stops in the case that the number of lives attribute is 0 (the player loses) or number of letters attribute is 0 (the player wins).
the game continues otherwise, which is implemented by calling ask_input() method. 

   
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
       
As discussed, This function plays the game, and the logic follows the following rules:
if the number of lives is 0, that means that the has lost the game.
if the number of lettters is greater than 0, keep asking the user for the input
if the number of lives is not 0 and the number of letters is not greater than 0, that means that the user has won the game.

Parameters:
   word_list: a list of words to choose from, which is seen in the firs line of def play_game. 



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

