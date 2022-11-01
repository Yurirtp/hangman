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

Milestone 3 task is to continuously ask the user for a letter and validate it. Addtionally, the 



