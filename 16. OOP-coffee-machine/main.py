from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

order_name = input('What do you want to drink? (espresso/latte/cappucino):\n')
if order_name is 'report':
    maker.report()
else:
    item = menu.find_drink(order_name)
if not maker.is_resource_sufficient(item):
    print("Insufficent resources!")
print( f'Put ${item.cost} to the machine:')
money.report()
if money.make_payment(item.cost):
    maker.make_coffee(item)
else:
    print("Insufficent funds!")

    

    


