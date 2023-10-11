import turtle as t
import random

# global variables
meta = 460
start = -480
screen = t.Screen()
screen.setup(1000, 400)

def check_pos(turtle):
    if turtle.xcor() >= meta:
        return True

def all_turtles_racing(turtle_list):
    return any(turtle.xcor() <= meta for turtle in turtle_list)

def random_forward(turtle):
    turtle.forward(random.randint(0,15))
    
def check_users_bet(race_winner):
    if bet == winner:
        return True
    else:
        return False

def turtle_creator(turtle, colr, ypos, bet, shap='turtle', xpos=start): 
    def starting_position(turtle, y, x=start):
        turtle.pu()
        turtle.setpos(x, y)
        
    turtle.color(colr)
    turtle.shape(shap)
    turtle.speed(2)
    starting_position(turtle, ypos, xpos)
    if bet == colr:
        turtle.dot(30)
    else:
        turtle.dot(10)

def print_winner(standings, bet):
    """defines does player's bet was correct and shows the standings"

    Args:
        standings (list): list of winners in order
        bet (string): betted winner
    """
    if bet == standings[0]:
        print(f"YOUR {bet} turtle WON!! Here's the standings:")
    else:
        print(f"Your {bet} turtle loose. Here's the standings:")
    
    for i in range(len(standings)):
        current_turtle = str(standings[i])
        if standings[i] is not bet:
            print(str(i+1) + '. ' + current_turtle)
        else:
            print(str(i+1) + '. ' + current_turtle.upper())
            
def create_a_meta():
    """visualize a meta on the center of 'meta' position
    """
    
    def black_rect():
        meta_creator.begin_fill()
        for rect in range(4):
            meta_creator.forward(10)
            meta_creator.right(90)
        meta_creator.end_fill()   
            
    def white_rect():
        for rect in range(4):
            meta_creator.forward(10)
            meta_creator.right(90)   
                  
    def set_pos():
        meta_creator.pu()
        meta_creator.right(90)
        meta_creator.forward(10)
        meta_creator.left(90)
        meta_creator.backward(10)    
        meta_creator.pd()
            
    meta_creator = t.Turtle()
    meta_creator.speed(100)
    meta_creator.ht()
    meta_creator.pu()
    meta_creator.setpos(meta,250)
    meta_creator.color('black')
    meta_creator.pd()
    
    for i in range(24):
        black_rect()
        meta_creator.forward(10)
        white_rect()
        set_pos()
        white_rect()
        meta_creator.forward(10)
        black_rect()
        set_pos()  
        

def main():
    create_a_meta()
        # assigning turtle objects to the list
    turtle_list = [None for i in range(6)]
    t_red = turtle_list[0] = t.Turtle()
    t_blue = turtle_list[1] =  t.Turtle()
    t_green = turtle_list[2] =  t.Turtle()
    t_orange = turtle_list[3] =  t.Turtle()
    t_purple = turtle_list[4] =  t.Turtle()
    t_brown = turtle_list[5] =  t.Turtle()
    
    bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color.\nChoose betweeen:\nred\nblue\ngreen\norange\npurple\nbrown")

        # Adjmustments for our turtles. Distances on y axis between turtles: 150, 90, 30, -30, -90, -150  
    turtle_creator(turtle_list[0], 'red', 150, bet)
    turtle_creator(turtle_list[1], 'blue', 90, bet)
    turtle_creator(turtle_list[2], 'green', 30, bet)
    turtle_creator(turtle_list[3], 'orange', -30, bet)
    turtle_creator(turtle_list[4], 'purple', -90, bet)
    turtle_creator(turtle_list[5], 'brown', -150, bet)
    
        # race loop
    standing = []
    while all_turtles_racing(turtle_list):
        random.shuffle(turtle_list) # to randomize the order of turtles going forward
        for turtle in turtle_list:
            if check_pos(turtle):
                standing.append(turtle.pencolor())
                turtle.color('yellow')
                turtle_list.remove(turtle)            
            else:
                random_forward(turtle)
    if len(turtle_list) > 0:   
        standing.append(turtle_list[0].pencolor())
    print_winner(standing, bet)
    screen.exitonclick()
    
if __name__ == '__main__':
    main()
