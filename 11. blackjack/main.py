############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def add_cards(score : list):
    score.append(random.choice(cards))
  
def current_score(score : list):
    summary = sum(score)
    if summary > 21 and cards[0] in score: # changing 11 to a 1 if needed (ace)
        summary - 10
    return summary

def print_scores(my_cards, my_score, cpu_cards, cpu_score):
    """printing scores and cards which every player got.

    """
    print(f"your cards is {my_cards}")
    print(f"Your final score is: {my_score}\n")
    print(f"CPU cards is {cpu_cards}")    
    print(f"Computer final score is: {cpu_score}") 
    print("\n")             

def end_of_game():
    """Check if there's winner yet. Calculates score of player and score of cpu and look for condition who can ends
    the game. If there's not, passes trough.

    Returns:
        bool: True if game ends, default False
    """
    my_score = current_score(my_cards)
    cpu_score = current_score(cpu_cards)
    if my_score > 21:
        print_scores(my_cards, my_score, cpu_cards, cpu_score)
        print("Your bust !!")
        print("*** CPU wins. ***")
        return False
    elif cpu_score > 21:
        print_scores(my_cards, my_score, cpu_cards, cpu_score)
        print("CPU bust !!")
        print("*** Y O U   W I N !! ***")   
        return False 
    else:
        return True
        
def ask_for_card():
    """asking user would he like to take another card. If not, directs to check_final_score() function.
    """
    ask = input("Do you want to take another card? Type 'y' or 'n'\n")
    if ask == 'y':
        add_cards(my_cards)
        os.system('cls')
    elif ask == 'n':
        os.system('cls')
        check_final_score()
    else:
        print("Wrong input!")
        ask_for_card()
        
def start():
    """Main function that holds an interface of the app.
    """
    print(f"Your current cards are {my_cards}")
    print(f"Your score is: {current_score(my_cards)}")
    print(f"CPU's first card is {cpu_cards[0]}")
    
def end_of_play():
    """Function that checking if user wants to end the whole game.
    
    """
    is_game_end = input("Type 'y' if you want to play again, or 'n' to end\n")
    if is_game_end == 'y':
        return True
    elif is_game_end == 'n':
        print("Goodbye!")
        return False 

def cpu_intelligence(cpu_cards):
    """system deciding if computer should add a card or not. Bettwen score 14 and 17 it's randomized.

    Args:
        cpu_cards (list): cards of cpu
    """
    cpu_score = current_score(cpu_cards)
    while cpu_score < 14:
        if cpu_score > 17:
            pass
        elif cpu_score > 14:
            if random.randint(1,4) > 2:
                add_cards(cpu_cards)
            break
        else:
            add_cards(cpu_cards)
        cpu_score = current_score(cpu_cards)
    
def check_final_score():
    """Calculates the final score if user won't take another card. Calls by add_to_card() function,
    and calling cpu_intelligence() function
    """
    cpu_intelligence(cpu_cards)
    if end_of_game() == False:      # checking if end og game which is omre prioritized wasn't before
        pass
    else:
        check_final_score.has_been_called = True
        my_score = current_score(my_cards)
        cpu_score = current_score(cpu_cards)
        print_scores(my_cards, my_score, cpu_cards, cpu_score)
        if my_score > cpu_score:
            print("*** Y O U   W I N !! ***") 
        elif my_score < cpu_score: 
            print("*** CPU wins. ***")
        else: 
            print("*** draw! ***")
        return True

# RUN
while end_of_play():
    my_cards = []
    cpu_cards = []
    check_final_score.has_been_called = False # checker if check final score has been called to end a while loop
    os.system('cls')
    print("Welcome to the blackjack game!") 
    add_cards(my_cards)
    add_cards(my_cards)
    add_cards(cpu_cards)
    while end_of_game():
        start()
        ask_for_card()
        if check_final_score.has_been_called == True:
            break
        os.system('cls') # prevent by doubling final output