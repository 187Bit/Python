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

def Blackjack():
    """Two player Blackjack game."""

    print(Blackjack_art.logo)

    all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # List named all_cards
    dealer_cards = [] # Empty list called dealer_cards

    scores = { # Dictionary "score" with 3 key and values to store the score of the player and the dealer

        "Player": 0, # Score of the player
        "Dealer": 0, # Score of the dealer that is shown to the player
        "Dealer_Full": 0. # Full score of the dealer
    }

    cards = { # Dictionary "cards" with 2 key and values
        "Player": [], # Key "Player" with empty list
        "Dealer": [], # Key "Dealer" with empty list
    }

    target = "Player"

### Draws the two starting cards for thep player and the dealer: ###

    for i in range(0,4): # For loop in range from 0 to 3 (4 in total)

        if i >= 2: # Checks if the target is
            target = "Dealer" # Sets the target to dealer after i is 2

        new_player_card = random.choices(all_cards) # randomly choses a value from the list "all_cards" and stores this value in the variable new_player_cards
        new_player_card_int =  new_player_card[0] # Converts the list into an int
        cards[target].append(new_player_card_int) # Appends the value stored in the variable new_player_cards_int in the dictionary cards at the corresponding position (player or dealer)
    

    scores = calculate_score(cards) # calls the function calculate_score() with the argument "cards" and stores the output (return value) in the variable "score"
    player_score = scores["Player"] # Updates the player_score by assigning it to a variable called player_score by using the dictionary scores an the key "Player"
    dealer_cards.append(cards["Dealer"][0]) # Updates the dealer cards by appending the first position in the dictionary cards with the key "Dealer" at the position 0

    print(f"Your cards are: {cards['Player']} and your current score is: {player_score}.")
    print(f"The computer's first card is: {dealer_cards}")

    game = True
    
    while game:

        
        want_new_card = input("Do you want to draw a new card? Type 'yes' for a new and 'no' for no new card.\n") # Ask the user if he wants to draw a new card and stores it in the variable want_new_card

        if want_new_card == "yes": # Checks if the value stored in want_new_card is equal to "yes"
            new_cards = draw_new_card(all_cards, cards, "Player", 2) # calls the draw_new_card function with the arguments "all_cards", "cards", "Player", "2" and assigns the output to the variable new_cards
            cards = new_cards # sets the dictionary cards to new_cards (cards attains the values of new_cards)
            scores = calculate_score(cards) # Calculates the new score with the new cards
            player_score = scores["Player"] # Updates the player score
            dealer_cards = [] # Resets the dealer cards list
            for position in range(0, len(cards["Dealer"])-1): # for loop in range of 0 and the length (number of cards) of the list in the dictionary cards at the postion dealer minus 1
                dealer_cards.append(cards["Dealer"][position]) # Appends the new cards of the dealer to the dealer_cards list

            player_score = scores["Player"] # Updates the player score
            dealer_score = scores["Dealer"] # Updates the dealer score

            print(f"Your cards are: {cards['Player']} and your current score is: {player_score}.")
            print(f"The computer's cards are: {dealer_cards} and the current score is: {dealer_score}")
            

            if scores["Player"] > 21: # Checks if the score of the "Player" is higher than 21
                if 11 in cards["Player"]: # Checks if an 11 is in the cards of the player
                    scores["Player"] -= 10
                else:
                    print("You went over. You lose!")
                    print(f"The computer's final cards are: {dealer_cards} and the score was: {dealer_score}")
                    play_again = input("It's a draw. Do you want to play again?\n")
                    if play_again == "no":
                        game = False
                
            if scores["Dealer_full"] > 21: # Checks if the score of the "Dealer" is higher than 21
                if 11 in cards["Dealer"]: # Checks if an 11 is in the cards of the player
                    scores["Dealer_full"] -= 10
                else:
                    print("You went over. You lose!")
                    print(f"The computer's final cards are: {dealer_cards} and the score was: {dealer_score}")
                    play_again = input("It's a draw. Do you want to play again?\n")
                    if play_again == "no":
                        game = False

        else:
            end_result(scores, all_cards, cards)
            game = False

def calculate_score(cards):

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

    difference_player = 0
    difference_dealer = 0
    
    if scores["Dealer_full"] < 17:
        new_cards = draw_new_card(all_cards, cards, "Dealer", 1)
        cards["Dealer"] = new_cards["Dealer"]
        scores = calculate_score(cards)
        dealer_cards = []

        for position in range(0, len(cards["Dealer"])-1):

                dealer_cards.append(cards["Dealer"][position-1])

        # player_score = scores["Player"]
        dealer_score = scores["Dealer"]
        print(f"The computer's cards are: {dealer_cards} and the current score is: {dealer_score}")
    
    
    dealer_cards = []

    for position in range(0, len(cards["Dealer"])):
        dealer_cards.append(cards["Dealer"][position-1])
        dealer_score = scores["Dealer_full"]

    if scores["Dealer_full"] > 21:
        print("You won!")
        print(f"The dealer's final hand was {dealer_cards} and the score was {dealer_score}.")
        play_again = input("It's a draw. Do you want to play again?")
        if play_again == "yes":
            Blackjack()
        else:
            print("Have a good day!")

    difference_player = abs(21 - scores["Player"])
    difference_dealer = abs(21 - scores["Dealer_full"])
    print(f"Dealer: {difference_dealer}")
    print(f"Player: {difference_player}")

    if scores["Player"] == scores["Dealer_full"]:
        play_again = input("It's a draw. Do you want to play again?")
        if play_again == "yes":
            Blackjack()
        else:
            print("Have a good day!")
    elif difference_player < difference_dealer:
        print("You won!")
        
        
        print(f"The dealer's final hand was {dealer_cards} and the score was {dealer_score}.")
        play_again = input("Do you want to play again?")
        if play_again == "yes":
            Blackjack()
        else:
            print("Have a good day!")
    else:
        print("You lose!")
        print(f"The dealer's final hand was {dealer_cards} and the score was {dealer_score}.")
        play_again = input("Do you want to play again?")
        if play_again == "yes":
            Blackjack()
        else:
            print("Have a good day!")
        
play_game = input("Do you want to play Black Jack? Type 'yes' or 'no'.\n")

if play_game == "yes":
    Blackjack()
else: 
    print("Bye!")