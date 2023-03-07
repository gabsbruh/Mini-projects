## Cofee machine program
from data import MENU, capacity_of_resources, coins, animation
import json
import time
import os

def ask_for_drink(coffee, resources):
    options = ['a','b','c']
    i=0
    for key in MENU:
        print(f"{options[i]}\t-\t{key}\t-\t${MENU[key]['cost']}")
        i+=1
    answer = input("What would you like to drink? (If you're maintainer of the machine, type 'fix' for more options)\n")
    if answer == 'fix':
        print("Another options:")
        print("'off'\t-\t to turn off the machine")
        print("'report'\t-\t to check resources inside the machine")
        print("'refill'\t-\t to refill resources\n")
        ask_for_drink(coffee, resources)
    if answer == 'a':
        return MENU['espresso']
    elif answer == 'b':
        return MENU['latte']
    elif answer == 'c':
        return MENU['cappuccino']
    elif answer == 'off':
        print("Coffee Machine is turning off...")
        quit()
    elif answer == 'report':
        os.system('cls')
        print_resources(resources)
        ask_for_drink(coffee, resources)
    elif answer == 'refill':
        os.system('cls')
        refill_resources(resources)
        ask_for_drink(coffee, resources)
    else:
        os.system('cls')
        print("Wrong input!")
        time.sleep(3)
        os.system('cls')
        ask_for_drink(coffee, resources)
        
def put_coins(credit):
    for key in coins:
        coin_amount = int(input(f"How much {key} do you have?\t"))
        credit += coins[key] * coin_amount
    return credit


def make_coffee(coffee, credit, resources):
    def decrease_resources(resources, coffee):
        for key in resources:
            resources[key] -= coffee["ingredients"][key]
        with open('resources.txt', 'w') as f:
            f.write(json.dumps(resources))
    def decrease_credits(credit, coffee):
        credit -= coffee["cost"]
        return credit
        
    def animation_of_coffee(coffee):
        print(f'Your coffee is making...')
        for t in range(10):
            print(animation[t])
            time.sleep(coffee['time']/10)
            print ("\033[A                             \033[A")
        print(coffee['art'])  
        print("Your coffee done!")
    
    def check_resources(resources, coffee):
        for res in resources:
            if resources[res] <= coffee['ingredients'][res]:
                print(f"Not enough {res} in machine. Ask for maintainer to refill.\n")
                ask_for_drink(coffee, resources)

    check_resources(resources, coffee)
    credit = float(put_coins(credit))
    print(f"${round(credit,3)} in total")
    if credit >= coffee["cost"]:
        decrease_resources(resources, coffee)
        credit = decrease_credits(credit, coffee)
        animation_of_coffee(coffee)
        return round(credit, 3)
    else:
        print("not enough money!\n\n")
        put_coins(credit)
               
def refill_resources(resources):
    print('maximum capacity of resources (in ml) containers is:')
    for key in capacity_of_resources:
        print(f'{key}\t-\t{capacity_of_resources[key]}  ({resources[key]} inside)')
    for key in resources:
        refill = float(input(f'How much {key} do you adding?\t'))
        if (resources[key] + refill) > capacity_of_resources[key]:
            print('Max capacity of container exceeded.')
            refill_resources(resources)
        else:
            resources[key] += refill
    with open('resources.txt', 'w') as f:
        f.write(json.dumps(resources))
    os.system('cls')
    print_resources(resources)

def print_resources(resources):
    print("Current resource values:")
    for key in resources:
        print(f"{key}\t-\t{resources[key]}")
    time.sleep(5)
    os.system('cls')

def main():
    credit = 0
    coffee = ''
    with open('resources.txt') as f:
        resources = f.read()
    
    # RUN
    resources = json.loads(resources)
    
    while True: # machine works all the
                # time, only maintainer can turn it off with 'off' button
        print(f"actually you have ${credit}")
        coffee = ask_for_drink(coffee, resources)
        credit = make_coffee(coffee, credit, resources)
    
if __name__ == "__main__":
    main()