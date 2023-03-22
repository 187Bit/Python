#Step 1 

import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list) # Randomly choses a word from the list word_list and assign the word to the variable chosen_word
# print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: \n").lower() # Asks the user to guess a letter and assign the letter to the variable guess

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word:
    
    if guess == letter:
        print("Right")
    else:
        print("Wrong")

# Alternative: (Only solves the todo, but is not helpful for later use)

if guess in chosen_word:
    print("It is in the word")
else:
    print("It is not in the word")