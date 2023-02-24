# guess the number app is based on finding the number which computer have chosen by guessing it number of times
# depends on the level you decided to play.
import random

# global variables
EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5

def defining_difficulty():
    """Allows user to choose the difficulty of the game

    Returns:
        int: number of lifes depending on chosen difficulty
    """
    global EASY_LEVEL_LIVES, HARD_LEVEL_LIVES 
    difficulty = input("Type 'h' if you want to play hard mode (5 chances ), or 'e' if u want to play on easy mode ( 10 chances ).\n")   
    if difficulty == 'h':
        return HARD_LEVEL_LIVES
    elif difficulty == 'e':
        return EASY_LEVEL_LIVES    
    else:
        print("Wrong input!")
        defining_difficulty()

def number_guessing(min, max, chosen_number):
    """Main mechanism of the game. checks if number is right, else loops over the end (if finds the right number of be out of the lifes) 

    Args:
        min (int): minimal number in range of guessing
        max (int): maximal number in range of guessing
        chosen_number (int): number which has been chosen
    """
    lifes = defining_difficulty()
    is_right_number = True
    while is_right_number and lifes > 0:
        print(f"\nIt's a number between {min} and {max}.")
        predict_number = int(input("Which number do you guess?:\t"))
        if predict_number == chosen_number:
            print("You find the right number!!!")
            is_right_number = False
        elif predict_number > chosen_number:
            print("the number you guessed is too big")
            max = predict_number
            lifes -= 1
            print(f"Lives left: {lifes}")
            
        else:
            print("the number you guessed is too small")
            min = predict_number
            lifes -= 1
            print(f"Lives left: {lifes}")
            
def game():
    print("Welcome to number guessing game!")
    chosen_number = random.randint(1,100)
    minimal = 1; maximal = 100
    number_guessing(minimal, maximal, chosen_number)
    print(f"The number you were looking for is {chosen_number}")
    
    
game()
    





