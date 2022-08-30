# Print logo 
# Count function 
# Random function

# Same scoes: Dealer wins
# Ace 1 or 11
# King, Jack or Queen equals to 10
# Dealer hand smaller than 17 then they must take another card

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import Blackjack_art
import random
import os

def Blackjack():

    print(Blackjack_art.logo)

    # all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    all_cards = [11, 2, 3, 4, 5, 6, 11]
    dealer_cards = []
    new_drawn_card = 0
    


    scores = {

        "Player": 0,
        "Dealer": 0,
        "Dealer_Full": 0,
    }

    cards = {
        "Player": [],
        "Dealer": [],
    }

    target = "Player"

    for i in range(0,4):

        if i >= 2:
            target = "Dealer"

        new_player_card = random.choices(all_cards)
        new_player_card_int =  new_player_card[0]
        cards[target].append(new_player_card_int)
    

    scores = calculate_score(cards)
    print(f"Scores are {scores}")
    player_score = scores["Player"]
    dealer_cards.append(cards["Dealer"][0])

    print(f"Your cards are: {cards['Player']} and your current score is: {player_score}.")
    print(f"The computer's first card is: {dealer_cards}")

    game = True
    

    while game:

        counter = 0

        if scores["Player"] > 21:

            if 11 in cards["Player"]:
                scores["Player"] -= 10
                print("triggered")
                for card in cards["Player"]:
                    if card == 11:
                        cards["Player"][counter] = 1
                        counter += 1
                    else:
                        counter += 1
                player_score = scores["Player"]
                print(f"Your cards are: {cards['Player']} and your current score is: {player_score}.")

                
        if scores["Dealer_full"] > 21:
            
            if 11 in cards["Dealer"]:
                scores["Dealer_full"] -= 10
                print("triggered")
                for card in cards["Dealer"]:
                    if card == 11:
                        cards["Dealer"][counter] = 1
                        counter += 1
                    else:
                        counter += 1

        
           
        
        want_new_card = input("Do you want to draw a new card? Type 'yes' for a new and 'no' for no new card.\n")

        if want_new_card == "yes":
            new_cards = draw_new_card(all_cards, cards, "Player", 2)
            cards = new_cards
            scores = calculate_score(cards)
            player_score = scores["Player"]
            dealer_cards = []
            for position in range(0, len(cards["Dealer"])-1):
                dealer_cards.append(cards["Dealer"][position])


            



            player_score = scores["Player"]
            dealer_score = scores["Dealer"]

            

            print(f"Your cards are: {cards['Player']} and your current score is: {player_score}.")
            print(f"The computer's cards are: {dealer_cards} and the current score is: {dealer_score}")
            

            
                    
        else:
            end_result(scores, all_cards, cards) # Check it after any turn instead of after no draw of a new card
            play_again = input("Do you want to play again?\n")
            if play_again == "no":
                game = False
                print("Have a good day!")
            else:
                game = False
                os.system('cls' if os.name == 'nt' else 'clear') #clear the terminal screen after an input
                Blackjack()
            
                   
                        



def calculate_score(cards):

    print(f"Current_cards: {cards}")


    calculated_score = {

        "Player": 0,
        "Dealer": 0,
        "Dealer_full":0,
    }
    for target in cards:
        
        list_to_count = cards[target]
        total_score = 0

        for number in list_to_count:
            total_score += number
        
        if target == "Dealer":
            calculated_score[target] = total_score - number
            calculated_score["Dealer_full"] = total_score
        else:
            calculated_score[target] = total_score
        

    return calculated_score

def draw_new_card(all_cards, new_cards, target, target_range):


    for i in range(0,target_range):

        if i >= 1:
            target = "Dealer"

        new_player_card = random.choices(all_cards)
        new_player_card_int =  new_player_card[0]
        new_cards[target].append(new_player_card_int)

    return new_cards

def end_result(scores, all_cards, cards):

    print(scores)

    difference_player = 0
    difference_dealer = 0


    if scores["Dealer_full"] < 17:
        new_cards = draw_new_card(all_cards, cards, "Dealer", 1)
        cards["Dealer"] = new_cards["Dealer"] #!
        scores = calculate_score(cards) #!
        dealer_cards = []

        for position in range(0, len(cards["Dealer"])-1):

                dealer_cards.append(cards["Dealer"][position])

        dealer_score = scores["Dealer"]
        print(f"The computer's cards are: {dealer_cards} and the current score is: {dealer_score}")

    difference_player = abs(21 - scores["Player"])
    difference_dealer = abs(21 - scores["Dealer_full"])

    dealer_cards = []

    for position in range(0, len(cards["Dealer"])):
        dealer_cards.append(cards["Dealer"][position])
        dealer_score = scores["Dealer_full"]
    
    if scores["Player"] > 21:
        print("You lose! You went over 21.")
        print(f"The computer's cards are: {dealer_cards} and the current score is: {dealer_score}")

    elif scores["Dealer_full"] > 21:
        print("You won! The Dealer went over 21.")
        print(f"The dealer's final hand was {dealer_cards} and the score was {dealer_score}.")

    elif difference_player < difference_dealer:
        print("You won!")
        print(f"The dealer's final hand was {dealer_cards} and the score was {dealer_score}.")
    elif scores["Player"] == scores["Dealer_full"]:
        print("It's a draw!")
        print(f"The dealer's final hand was {dealer_cards} and the score was {dealer_score}.")
    else:
        print("You lose!")
        print(f"The dealer's final hand was {dealer_cards} and the score was {dealer_score}.")
       

play_game = input("Do you want to play Black Jack? Type 'yes' or 'no'.\n")

if play_game == "yes":
    Blackjack()
else: 
    print("Bye!")