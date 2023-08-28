#Number Guessing Game Objectives:

# Welcome the user
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# import number_guessing_art 
import random

# print(number_guessing_art.logo)

def number_guessing_game():

    """Function for number guessing game."""

    game = True

    print("Welcome to the number guessing game!")
    difficulty = input("On which difficulty do you want to play? 'Easy' or 'Hard'?\n").lower() # Asks the user to select a difficulty and stores it in the variable difficulty as a string
    if difficulty == "easy": # Checks if difficulty is equal to "easy"
        number_of_tries = 10 # Sets the constant number_of_tries to 10
    elif difficulty == "hard": # Checks if difficulty is equal to "hard"
        number_of_tries = 5 # Sets the constant number_of_tries to 5
    else: # The user entered a wrong input
        print("Wrong input!")
        game = False

    print(f"You are playing on difficulty {difficulty} and you have {number_of_tries} tries.")    
    random_number = random_number_gen() # Calls the function random_number_gen and stores the output in the variable random_number
    print("I am guessing a number between '0' and '100'.")

    while game: # While loop as long as game is True

        user_input = int(input("You can guess now!\n")) # Asks the user to guess a number and stores the value as an int inside the user_input function
        returned_answer = check_answer(user_input, random_number) # Calls the check_answer function with the arguments user_input and random_number and stores the output in the variable returned_answer

        if returned_answer == "Win": # Checks if the returned_answer is equal to "Win"
            print(f"You won! You guessed the right number. The number was {random_number}.")
            game = False
        elif returned_answer == "Too high": # Checks if the returned_answer is equal to "Too high"
            print("Your guess is too high.")
            number_of_tries -= 1 # Reduces the constant number_of_tries by 1
        elif returned_answer == "Too low": # Checks if the returned_answer is equal to "Too low"
            print("Your guess is too low.")
            number_of_tries -= 1 # Reduces the constant number_of_tries by 1
        elif returned_answer == "invalid": # Checks if the returned_answer is equal to "invalid"
            print("Your guess is out of range!")
            number_of_tries -= 1 # Reduces the constant number_of_tries by 1

        if number_of_tries == 0: # Checks if the value of the number_of_tries variable is equal to 0
            game = False
            print(f"You are out of tries. You lose! The number was {random_number}")

def random_number_gen():
    """Generates a random number in the range of 0 and 100 by using the random module and the randint function. Returns the generated number."""

    number = random.randint(0, 100) # Generates a random number in the range from 0 to 100 by using the randint() function from the random module and then stores the value in the variable number

    return number

def check_answer(user_input, random_number):

    """Checks the user_input variable if it is too high, too low, the exact number or out of range. Then return the statement. Has the positional arguments user_input and random_number."""

    if user_input == random_number: # Checks if value in the variable user_input is equal to the value in the variable random_number
        return "Win"
    elif user_input > random_number and user_input <= 100: # Checks if value in the variable user_input is higher to the value in the variable random_number
        return "Too high"
    elif user_input < random_number: # Checks if value in the variable user_input is lower to the value in the variable random_number
        return "Too low"
    elif user_input > 100: # Checks if value in the variable user_input is higher than 100
        return "invalid"

number_guessing_game()