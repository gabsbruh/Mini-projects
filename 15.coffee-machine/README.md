# Description in details of Coffee Machine Program
### 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.
### 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
### 3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.<br />
Water: 100ml<br />
Milk: 50ml<br />
Coffee: 76g<br />
Money: $2.5<br />
### 4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.<br />
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “ Sorry there is not enough water. ”<br />
c. The same should happen if another resource is depleted, e.g. milk or coffee.
### 5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.<br />
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01<br />
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
### 6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “ Sorry that's not enough money. Money refunded. ”.<br />
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.<br />
Water: 100ml<br />
Milk: 50ml<br />
Coffee: 76g<br />
Money: $2.5<br />
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.
### 7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:<br />
Water: 300ml<br />
Milk: 200ml<br />
Coffee: 100g<br />
Money: $0<br />
Report after purchasing latte:<br />
Water: 100ml<br />
Milk: 50ml<br />
Coffee: 76g<br />
Money: $2.5<br />
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.