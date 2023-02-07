rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

'''
I could do this task easier and more clearly on a dictionaries instead of listts,
but lesson content was aimed to the usage of lists and that's why I've done the task just like that.
'''

print("\t***ROCK PAPER SCISSORS GAME AGAINST CPU***\t")
# print("What do u choose? Type:\n 0 - for rock\n1 - for paper\n2 - for scissors")
import random
rock_num = 0
paper_num = 1
scissors_num = 2
things = [rock, paper, scissors]
my_score = 0
cpu_score = 0 

# max score
points = int(input("Type score at which player wins:\n"))

while points > my_score and points > cpu_score:
    # assigning my choice from console based on a numbers
    again_v2 = True # again to wrong 0/1/2 choose
    while again_v2 == True:
        my_choice = rock # default is rock
        my_choice_int = int(input("What do u choose? Type:\n 0 - for rock\n1 - for paper\n2 - for scissors\n\n"))
        if my_choice_int == rock_num:
            my_choice = things[0]
            print("You've chosen:\n")
            print(rock)
            again_v2 = False
            
        elif my_choice_int == paper_num:
            my_choice = things[1]
            print("You've chosen:\n")
            print(paper)
            again_v2 = False

        elif my_choice_int == scissors_num:
            my_choice = things[2]
            print("You've chosen:\n")
            print(scissors)
            again_v2 = False

        else:
            print("You typed wrong number!")
            again_v2 = True
        del my_choice_int
    # randomized CPU choice
    cpu_choice = random.choice(things)
    print("CPU has chosen:\n")
    print(cpu_choice)

            # game mechanism     
        # my wins
    if  (
            (my_choice == things[1] and cpu_choice == things[0]) or 
            (my_choice == things[2] and cpu_choice == things[1]) or 
            (my_choice == things[0] and cpu_choice == things[2])
        ):
        print("\n\tYou scores!")  
        my_score += 1
        
        # CPU wins
    elif  (
            (my_choice == things[0] and cpu_choice == things[1]) or 
            (my_choice == things[1] and cpu_choice == things[2]) or 
            (my_choice == things[2] and cpu_choice == things[0])
        ):
        print("\n\tCPU scores.")  
        cpu_score += 1
        
        # draws 
    else:
        print("\n\tDraw!") # there's 3**2 options, so the rest of 3 are draws

        # score
    print(f"\n\t\tSCORE:\nME\t{my_score}\t:\t{cpu_score}\tCPU\n")
    # del my_choice_int
    # del my_choice
    
print("\t\t FINAL SCORE \t\t")
print(f"\t*** ME\t{my_score}\t:\t{cpu_score}\tCPU***\t")
    
if my_score > cpu_score:
    print("\t*****  Y O U   W I N !  *****")
    print('''
          
          
          
          ''')
else:
    print("\t*****  Y O U   L O O S E :(  *****")