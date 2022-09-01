# Check everything and if the game has not ended yet, ask the user for a new card
# If the player does not want to draw a card anymore compare funtion

############### Blackjack Project #####################
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

from typing import final
import Blackjack_art
import random
import os



def blackjack():

    game = True
    above = ""
    global answer
    

    print(Blackjack_art.logo)

    cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    scores = {

            "Player": 0,
            "Dealer": 0,
            "Dealer_score_for_user": 0,
        }

    cards = {

            "Player": [],
            "Dealer": [],
        }

    for i in range(0,2):
         cards = draw_card(cards_list, cards)

    while game:

        new_scores = calculate_score(cards, scores, above)

        if new_scores == True or new_scores == False or new_scores == "Draw" or new_scores == "Player" or new_scores == "Dealer":
            game = False
            
            if new_scores == "Draw":
                print("It's a draw!")
            if new_scores == True:
                print("You won! You scored a blackjack!")
            elif new_scores == False:
                print("You lose! The dealer scored a blackjack!")
            elif new_scores == "Player":
                print("You won! The dealer went over 21!")
            elif new_scores == "Dealer":
                print("You lose! You went over 21!")
        else:
            scores = new_scores
            player_cards = cards["Player"]
            dealer_cards_for_user = cards["Dealer"]
            dealer_cards_for_user = dealer_cards_for_user[:-1]
            cards_dealer_after_minus = cards["Dealer"]
            player_score = scores["Player"]
            dealer_score = scores["Dealer_score_for_user"]
            print(f"Your cards are: {player_cards} and the current score is: {player_score}")
            print(f"The dealer's cards are: {dealer_cards_for_user} and the current score is: {dealer_score}")
            want_new_card = input("Do you want to draw a new card?\n")
            if want_new_card == "yes":
                cards = draw_card(cards_list, cards)
            else:
                game = False
                answer = no_new_card(scores, cards, cards_list, above)

    restart = input("Do you want to play again? Type 'yes' or 'no'.\n")
    if restart == "yes":
        blackjack()
    else:
        print("Have a good day!")

###Functions###

def draw_card(cards_list, cards):


    for target in cards:
        new_card = random.choice(cards_list)
        cards[target].append(new_card)
    
    return cards

def calculate_score(cards, scores, above):

    i = True

    while i:

        length_dealer_cards = len(cards["Dealer"]) - 1

        for target in cards:
            scores[target] = sum(cards[target])

        scores["Dealer_score_for_user"] = scores["Dealer"] - cards["Dealer"][length_dealer_cards]

        if scores["Player"] == 21 and scores["Dealer"] == 21:
            i = False
            return "Draw"
        elif scores["Player"] == 21:
            i = True
            return True
        elif scores["Dealer"] == 21:
            i = False
            return False
        elif scores["Player"] > 21:
            if 11 in cards["Player"]:
                cards["Player"].remove(11)
                cards["Player"].append(1)
            else:
                i = False
                above = "False"
                answer = compare(scores, cards, above)
                return answer
        elif scores["Dealer"] > 21:
            if 11 in cards["Dealer"]:
                cards["Dealer"].remove(11)
                cards["Dealer"].append(1)
            else:
                i = False
                above = "True"
                answer = compare(scores, cards, above)
                return answer
        else:
            i = False
    
    return scores

def no_new_card(scores, cards, cards_list, above):

    global answer

    answer = False

    """Checks if the dealer's total scores is below 17. If it is, the dealer keeps drawing until his score is equal or over 17. In addition it also calls the compare() function which compares both scores."""

    if scores["Dealer"] < 17:

        while scores["Dealer"] < 17:
            cards = draw_card(cards_list, cards)
            cards["Player"] = cards["Player"][:-1]
            calculate_score(cards, scores, above)
            dealer_cards = cards["Dealer"]
            dealer_score = scores["Dealer"]

    answer = compare(scores, cards, above)

    return answer
    
def compare(scores, cards, above):

    global answer

    if above != "True" and above != "False":

        difference_player = abs(21 - scores["Player"]) 
        difference_dealer = abs(21 - scores["Dealer"])

        if difference_player < difference_dealer:
            final_result = True
        elif difference_player == difference_dealer:
            final_result = "Draw"
        else:
            final_result = False
        
        if final_result == True:
            print("You won! You score is higher than the dealer's score.")
        elif final_result == "Draw":
            print("It is a draw!")
        else: 
            print("You lose! The dealer's score is highter than your score.")
    else:
        print("triggered")
        if above == "True":
            answer = "Player"
        elif above == "False":
            answer = "Dealer"

    player_cards = cards["Player"]
    player_score = scores["Player"]
    dealer_cards = cards["Dealer"]
    dealer_score = scores["Dealer"]

    print(f"Your final cards are: {player_cards} and the score is: {player_score}")
    print(f"The dealer's final cards are: {dealer_cards} and the score is: {dealer_score}")

    return answer


blackjack()