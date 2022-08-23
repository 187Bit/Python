#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

game_over = False

while game_over == False:


    guess = input("Guess a letter: ").lower()

    position = 0

    #Check guessed letter
    for letter in chosen_word:
        
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

        position += 1

    if "_" not in display: # Checks if the "_" is not appearing in the display list
            game_over = True
            print("You win!")

    print(display)