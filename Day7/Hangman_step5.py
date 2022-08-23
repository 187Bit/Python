#Hangman project:
import random # import random module
import Hangman_word_list # import Hangman_word_list module
import Hangman_art # import Hangman_art module
# other alternative to just import one thing from another module:
# from hangman_words import word_list (Now you can just use word list instead of hangman_words.word_list)


chosen_word = random.choice(Hangman_word_list.word_list) # Randomly choses a word from the list word_list and assign the word to the variable chosen_word
word_length = len(chosen_word) # Assign the lentgh of the chosen_word variable to the world_length variable
already_guessed_letters = [] # Creates an empty list called already_guessed_letters

end_of_game = False # variable end_of_game set to false
lives = 6 # variable end_of_game set to false

print(Hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = [] # Creates an empty list called display
for _ in range(word_length): # Loop between 0 and the lenght of the chosen_word
    display.append("_") # Appends the "_" to the list display

while not end_of_game: # while loop until end_of game equals True
    guess = input("Guess a letter: ").lower() # Assign the users input to the variable guess
    position = 0 # Variable position set to 0

    if guess in already_guessed_letters: # Checks if the value stored in guess is in the list already_guessed_letters
        print(f"You have already guessed the letter: {guess}") 
    else: # If the value stored in guess is not in the list already_guessed_letters

        #Check guessed letter
        for letter in chosen_word: # For loop for the lentgh of the length of chosen_word

            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess: # Checks if the letter (from chosen_word) is equal to the value stored in the variable guess
                display[position] = letter # Assign the value stored in the variable letter to the list display at the value stored in the variable position

            position += 1 # Adds one to the variable position
            


        #Check if user is wrong.
        if guess not in chosen_word: # Checks if the value stored in the variable guess is not in the variable chosen_word
            print(f"The letter {guess} is not in the word. You lose a life!")
            lives -= 1 # Subtracts one from the variable lives

    print(f"{' '.join(display)}")   # Joins all the elements in the list and turns it into a String.

    already_guessed_letters.append(guess)   # Adds the guessed word to the already_guessed word list

    #Checks if the user has got all letters or is out of lives

    if "_" not in display:  # Checks if "_" is not in the list diplay
        end_of_game = True # Sets the variable (boolean) end_of_game to True
        print("You win.")
    elif lives == 0: # Checks if the user is out of lives, so the value in lives is equal to 0
        end_of_game = True # Sets the variable end_of_game to True
        print("You lose!")

    print(Hangman_art.stages[lives])
