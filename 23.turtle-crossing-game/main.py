import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def main():
    # customize the screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # create essential objects
    turtle = Player()
    scoreboard = Scoreboard()
    cars = CarManager()

    # binding 'Up' key to move forward
    screen.listen()
    screen.onkeypress(turtle.move, "Up")

    counter = 0
    print(turtle.turtlesize())
    
    # proper game
    game_is_on = True
    while game_is_on:
        time.sleep(0.04)
        screen.update()
        cars.move()   
        
        # posibility on new car can occur on the road is specified by possible_new()
        if cars.possible_new():    
            cars.new()
            cars.new()
            counter +=1

        # winning condition
        if turtle.ycor() >= 280:
            cars.next_level()
            scoreboard.next_level()
            turtle.starting_position()
            time.sleep(1)
            counter = 0
        
        # detect collision with car
        for car in cars.car_list:
            if turtle.distance(car) < 15:
                
                progress = turtle.progress()
                scoreboard.game_over(progress)
                game_is_on = False

    screen.exitonclick()

if __name__ == '__main__':
    main()