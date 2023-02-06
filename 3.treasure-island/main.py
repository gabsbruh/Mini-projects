print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
again = "yes"
while again == "yes":
    side = input("type: left or right?\n")
    if side == "left":
        what_to_do = input("type: swim or wait?\n")
        if what_to_do == "wait":
                door = input("type which door: red, blue, or yellow?\n")
                if door == "yellow":
                    print("\t***CONGRATULATIONS!***\n\tYou've found the treasure!")
                    break
                elif door == "red":
                    print("Burned by fire. \n\t***GAME OVER***")
                elif door == "blue":
                    print("Eaten by beasts. \n\t***GAME OVER***")
                else:
                    raise ValueError(door)
        elif what_to_do == "swim":
            print("Attacked by trout. \n\t***GAME OVER***")
        else:
            raise ValueError(what_to_do)
            
    elif side == "right":
        print("You fall into a hole. \n\t***GAME OVER***")
    else:
        print()
        raise ValueError(side)
    again = input('You want to try again? Type "yes" or "no"\n')
    

