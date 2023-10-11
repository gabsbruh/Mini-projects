from turtle import Screen
from snake import Snake
import time

# constants
REFRESH_SPEED = 0.2

def main():
    # set up the screen
    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0) # automatical updating of the screen are turned off
    
    # creating initial snake
    snake = Snake()
    
    # snake movement
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    
    # proper game
    game_on = True
    while game_on:
        screen.update()
        time.sleep(REFRESH_SPEED)
        snake.move()
    screen.exitonclick()

    
if __name__ == "__main__":
    main()
