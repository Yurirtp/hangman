# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Milestone 1 
Milestone 1 task: Set up the development environment. This included setting up a Github account, creating a repository for the Hangman project as well as using linking the respository to GIthub. This is so that, when you tell git to start keeping track of the files in a folder (or directory), you move the commits to a git repository, in which git stores the snapshots of the files in the working directory. Additionally, I learnt the essentials of Git.

Other tasks in Milestone 1 were to use Command line (Command Prompt), for file manipulation and running terminal commands.


# Milestone 2 
Milestone 2 task: Create a file named milestone_2.py. Create a list, and assign to a variable, then print out the newly created list.

The following is an example of the code written for each task:
creating list --> ["Pear", "Pineapple", "Apple", "Mango", "Melon"]
Assigning list to a variable --> word_list = ["Pear", "Pineapple", "Apple", "Mango", "Melon"]
print(word_list)




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
