rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

random.seed()


random_number = random.randint(0,2)

options_list = ["rock", "paper", "scissors"]




user_input = input("What do you want to choose? Rock, paper or scissors?\n").lower()

display = " "

if user_input == "rock":
    display = rock
elif user_input == "paper":
    display = paper
elif user_input == "scissors":
    display = scissors


print(display)

print("The computer chose:")

computer_choice = options_list[random_number]

print(computer_choice)

if computer_choice == "rock":
    display = rock
elif computer_choice == "paper":
    display = paper
else:
    display = scissors

print(display)


if user_input == "rock" and computer_choice == "paper":
    print("You lose!")
elif user_input == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_input == "paper" and computer_choice == "rock":
    print("You won!")
elif user_input == "paper" and computer_choice == "scissors":
    print("You lose!")
elif user_input == "scissors" and computer_choice == "paper":
    print("You win!")
elif user_input == "scissors" and computer_choice == "rock":
    print("You lose!")
elif user_input == "scissors" and computer_choice == "rock":
    print("You lose!")
elif user_input == computer_choice:
    print("It is a draw!")
else: 
    print("Not allowed word. You lose! Haha, you can not even type!")