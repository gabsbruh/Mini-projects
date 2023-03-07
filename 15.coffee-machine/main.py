## Cofee machine program
from data import MENU, capacity_of_resources, coins
import json

# adding resources from file
with open('resources.txt') as f:
    resources = f.read()
resources = json.loads(resources)

def ask_for_drink():
    for key in MENU:
        print(f"a\t-\t{key}\t-\t${MENU[key]['cost']}")
    answer = input("What would you like to drink? If you're maintainer of the machine, type 'fix' for more options")
    if answer == 'fix':
        print("Another options:")
        print("'off'\t-\t to turn off the machine")
        print("'report'\t-\t to check resources inside the machine")
        print("'refill'\t-\t to refill resources")
    if answer == 'a':
        espresso()
    elif answer == 'b':
        latte()
    elif answer == 'c':
        cappuccino()
    elif answer == 'off':
        print("Coffee Machine is turning off...")
        quit()
    elif answer == 'report':
        print("Current resource values:")
        print(resources)
    elif answer == 'refill':
        refill_resources()
    else:
        print("Wrong input!")
        ask_for_drink()
        
def put_coins():
    credit = 0
    for key in coins:
        coin_amount = int(input(f"How much {key} do you have?"))
        credit += coins[key] * coin_amount
    return credit

def make_coffee():
    pass

def refill_resources():
    print('maximum capacity of resources (in ml) containers is:')
    for key in capacity_of_resources:
        print(f'{key}\t-\t{capacity_of_resources[key]}')
    for key in resources:
        refill = float(input(f'How much {key} do you adding?'))
        if (resources[key] + refill) > capacity_of_resources[key]:
            print('Max capacity of container exceeded.')
            refill_resources()
        else:
            resources[key] += refill
    with open('resources.txt', 'w') as f:
        f.write(json.dumps(resources))
    pass

def main():
    # while True:
    #     ask_for_drink()
    #     put_coins()
    #     make_coffee()
    print(put_coins())
    
if __name__ == "__main__":
    main()