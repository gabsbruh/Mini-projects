from turtle import Screen
from snake import Snake
import time



def main():
    # set up the screen
    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0) # automatical updating of the screen are turned off
    
    # creating initial snake
    snake = Snake()
    
    # proper game
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
    screen.exitonclick()

    
if __name__ == "__main__":
    main()
