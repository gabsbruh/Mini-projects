## Cofee machine program
from data import MENU
from json import loads

# FIXME read from a file
with open('resources.txt') as f:
    resources = f.read()
resources = json.loads(resources)

# predefining variables
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

def ask_for_drink():
    for key in MENU:
        print(f"a\t-\t{key}\t-\t${MENU[key]['cost']}")
    answer = input("What would you like to drink?")
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
    pass

def make_coffee():
    pass

def refill_resources():
    # FIXME writes to a file and inputs how much refills before
    
    with open('resources.txt', 'w') as f:
     f.write(json.dumps(details))
    pass

def main():
    # while True:
    #     ask_for_drink()
    #     put_coins()
    #     make_coffee()
    print(resources)
        
    
if __name__ == "__main__":
    main()