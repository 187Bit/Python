# Who has more followers. Higher or lower game!

import random
import art
import game_data
import os 

def higher_lower():

    print(art.logo)
    total_score = 0
    game = True
    random_numbers = []

    for i in range(0,2):
        random_number = random_number_gen(game_data.data)
        random_numbers.append(random_number)

    first_account = game_data.data[random_numbers[0]]
    second_account = game_data.data[random_numbers[1]]

    while game:

        while first_account == second_account:
            random_number = random_number_gen(game_data.data)
            second_account = game_data.data[random_number]

        print(f"Compare A: {first_account['name']}, a {first_account['description']}, from {first_account['country']}")
        print(art.vs)
        print(f"Against B: {second_account['name']}, a {second_account['description']}, from {second_account['country']}")

        correct_answer = check_answer(first_account, second_account)

        user_input = input("Who has more followers? Type 'A' or 'B':\n").lower()

        os.system('cls' if os.name == 'nt' else 'clear')

        result = compare(user_input, correct_answer)
        # print(f"A: {first_account['follower_count']}, B: {second_account['follower_count']}")

        if result == True:
            total_score += 1
            print(f"You are right! Your current score is {total_score}.") 
            random_number = random_number_gen(game_data.data)
            first_account = second_account
            second_account = game_data.data[random_number]
        elif result == False:
            game = False
            print(f"You are wrong! Game over! Your score was {total_score}.")
        
        

        


def random_number_gen(game_data):

    random_number = random.randint(0, len(game_data)-1)
    
    return random_number

def compare(user_input, correct_answer):

    if user_input == correct_answer:
        return True
    else:
        return False

def check_answer(first_account, second_account):

    if first_account["follower_count"] > second_account["follower_count"]:
        return "a"
    else:
        return "b"




higher_lower()