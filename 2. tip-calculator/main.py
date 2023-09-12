#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("\tTip calculator\n")
total_bill = float(input("What was the total bill?\n$"))
tip = float(input("What percentage tip would you like to give for service?\n%"))
people_splitting = int(input("how many people should split the bill?\n"))
each_person_payment = round(((total_bill + total_bill * (tip/100)) / people_splitting), 3)
print(f"each person should pay ${each_person_payment} for the service.")
