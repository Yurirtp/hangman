# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
---
## Milestone 1 
Milestone 1 task: Set up the development environment. This included setting up a Github account, creating a repository for the Hangman project as well as using linking the respository to GIthub. This is so that, when you tell git to start keeping track of the files in a folder (or directory), you move the commits to a git repository, in which git stores the snapshots of the files in the working directory. Additionally, I learnt the essentials of Git.

Other tasks in Milestone 1 were to use Command line (Command Prompt), for file manipulation and running terminal commands.
---
## Milestone 2 
Milestone 2 task: Create a file named milestone_2.py. Create a list, and assign to a variable, then print out the newly created list.

The following is an example of the code written for each task:

- Creating a list --> ["Pear", "Pineapple", "Apple", "Mango", "Melon"]

- Assigning a list to a variable --> word_list = ["Pear", "Pineapple", "Apple", "Mango", "Melon"]


- Printing out list --> print(word_list)

Next I imported 'random' module in the first line of the file. --> import random 

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

A new script called milestone_3.py was created. I create a while loop and set the condition to True. Setting this condition to True ensures that the code run continuously. In the body of the loop, code for guess a letter was entered and I assigned this to a variable called guess. I made sure that guess checked the guess is a single, and is an alphabetical character. I also made it that if the checks passed, it breaks out of the loop.

while True:
                guess = input("Enter a single letter.")
                if len(guess) == 1 and guess.isalpha():
                    break
                else: 
                    print("Invalid letter. Please, enter a single alphabetical character.")
                    break

If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."

I also checked my code by making the code to make the user guesses letter "a" and the secret word is "apple", then the code will check if "a" is in "apple".

I then proceeded to create an if statement that checks if the guess is in the word. In the body of the if statement, I made the return print a message saying "Good guess! {guess} is in the word.". The format  of the string shows the actual guess instead of {guess}.I proceeded to create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.

 while True:
                if guess in word:
                    print(f"Good guess! {guess} is in the word.")
                    break
                else:
                    print(f"Sorry, {guess} is not in the word. Try again.")
                    break  






I then proceeded to create two functions which contained the code above in MIlesotne 3.
The two functions created are check_guess and ask_for_input functions which contain the code for those two things.

The functions are made by first defining the name of the function, and then created the return type of the function, which is what is returned which is shown in the code above. I also made sure to list inside parenthesis (), I listed parameters the function takes.
I also included the curly brackets {}, this code will run whenever the function is called. This is called the body of the function.

I defined a function called check_guess. I then passed in guess as a parameter for the function. Then I wrote the code for the following steps in the body of this function. ##Converting the guess into lower case, and then moving the code that to check if the guess is in the word into this function block.

I then proceeded to check the check_guess function, and made sure that it takes the guessed letter as an argument and check if the letter is in the word.

 def check_guess(self, guess):
        guess = guess.lower()  
        while True:
                if guess in word:
                    print(f"Good guess! {guess} is in the word.")
                    break
                else:
                    print(f"Sorry, {guess} is not in the word. Try again.")
                    break    



I then defined the function called ask_for_input. I moved the code that I wrote in the Iteratively check if the input is a valid guess task into this function block.I then added outside the while loop, within the function, which call the check_guess function to check if the guess is in the word. # I then made sure to pass in the guess as an argument to the method.

I then called the the function ask_for_input, to test your code.


    def ask_for_input(self, check):
        while True:
                guess = input("Enter a single letter.")
                if len(guess) == 1 and guess.isalpha():
                    break
                else: 
                    print("Invalid letter. Please, enter a single alphabetical character.")
                    break
        self.check_guess(guess)

run = Hangman(word_list,5)
run.ask_for_input(guess)

To help the write the code I created a class to initials these functions by using self:

#class Hangman:
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.guessed = [] #making an empty list to then append later 
        self.lives = num_lives
        self.guess = guess

#
run = Hangman(word_list,5)
run.ask_for_input(guess)
This allowed me to call the function ask_for_input. 
#
