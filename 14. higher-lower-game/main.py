import accounts_data
import random
import os

def random_accounts():
    """ Randomly choose one of the account from data

    Returns:
        Dict: random account from accounts_data
    """
    account = random.choice(accounts_data.data)   
    return account


def which_bigger(account_1, account_2):
    """Funtion checking which account is bigger basing on the followe_count value. 

    Returns:
        Dict: bigger account
    """
    if account_1["follower_count"] > account_2["follower_count"]:
        return 1
    else:
        return 2


def print_accounts(account_1 = {}, account_2 = {}):
    print("Which account has more followers on Instagram?\n")
    print(f"{account_1['name']}, {account_1['description']}, from {account_1['country']} ")
    print("\tvs\t")
    print(f"{account_2['name']}, {account_2['description']}, from {account_2['country']} ")


def program():
    print("\t*** HIGHER-LOWER GAME ***\t")
    again = True
    while again:
        play = input("Do you want to play a game? Type 'y' or 'n': ")
        os.system('cls')
        if play == 'y':
            score = 0
            is_right = True
            while is_right:
                account_1 = random_accounts()
                account_2 = random_accounts()
                if account_1 == account_2 or account_1["follower_count"] == account_2["follower_count"]:
                    account_1 = random_accounts()
                    account_2 = random_accounts()   
                print_accounts(account_1, account_2)
                # check_choice(account_1, account_2)
                choice = int(input(f"\nType '1' if you choose {account_1['name']}, or '2' if you choose {account_2['name']}: "))
                os.system('cls')
                if choice == which_bigger(account_1, account_2):
                    # score up
                    score += 1
                    print("Good choice! Your actual score is " + str(score))
                    is_right = True
                else:
                    print(f"Wrong choice :(\nYour score: {score}")
                    is_right =  False
        elif play == 'n':
            again = False
            print("Goodbye!")
        else:
            print("Wrong input!")
            program()


def main():
    program()


# RUN
if __name__ == '__main__':
    main()
