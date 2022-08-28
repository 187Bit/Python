import os 
import Blind_auction_art

print(Blind_auction_art.logo)



# os.system('cls' if os.name == 'nt' else 'clear')

def auction():

    bidding_over = False
    bids = {}

    while bidding_over == False:
        name = input("What is your name?:\n")
        bid = int(input("What is you bid?:\n"))

        bids[name] = bid
        
        continue_auction = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if continue_auction == "no":
            bidding_over = True
            
    highest_bidder = ""
    highest_bid = 0
    
    for name_of_bidder in bids:

        if bids[name_of_bidder] > highest_bid:
            highest_bidder = name_of_bidder
            highest_bid = bids[name_of_bidder]

    
    print(f"The winner is {highest_bidder} with a bid of {highest_bid}€.")

        
auction()
