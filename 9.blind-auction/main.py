from art import hammer
import os
print("Welcome to the auction!")
print(hammer)

# first variable defining end of while loof and second creating dictionary of bidders in the auction
end_of_bidders = 'no'
bids = {}
winning_bidder = {}
starting_offer = 0

def make_a_bid():
    """Function that adding a new bidder and his bid.
    """
    name = input("Name of bidder:   ")
    bid = float(input("What's your bid?:   "))
    bids[name] = bid
    print(f"{name} bidded ${bid}")
 
def ask_for_another_bidder():
    """Function that asking for another bidder.
       if 'yes', adding a new bidder by calling make_a_bid()
       if 'not' or wrong input, function are calling itself.
    """
    another_bidders = input("Type 'yes', if you want to add another bidder, or 'no' if no one wants to bid\n")
    if another_bidders == 'yes':
        os.system('cls')
        make_a_bid()
        ask_for_another_bidder()
    elif another_bidders == 'no':
        os.system('cls')
        print("End of auction!")
    else: 
        print("Wrong input!")
        ask_for_another_bidder()


def winner(bids : dict, highest_offer : float):
    """Function that pointing the winner of an auction.
       It's iterating on bids and finding the biggest one by replacing current with actual highest if it is bigger.
    Args:
        bids (dict): dictionary of bidders
        highest_offer (float): actual highest offer
    """
    highest_offer = 0
    for bidder in bids:
        if bids[bidder] > highest_offer:
            highest_offer = bids[bidder]
            winning_bidder = bidder
            
    print(f"The winner is: {winning_bidder} with a bid of ${highest_offer}")

#   RUN
make_a_bid()
ask_for_another_bidder()
winner(bids, starting_offer)