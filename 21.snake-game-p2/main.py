from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# constants
REFRESH_SPEED = 0.03 # FPS, refresh of the screen
GROW_SPEED = 5 # (int) adding more segments to speed up the game, default 1
MOVE_DISTANCE = 5 # starting speed rate of snake

def main():
    # set up the screen
    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0) # automatical updating of the screen are turned off
    
    # creating initial objects
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    
    # snake movement
    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")
    screen.onkeypress(snake.up, "w")
    screen.onkeypress(snake.down, "s")
    screen.onkeypress(snake.left, "a")
    screen.onkeypress(snake.right, "d")
    
    # proper game
    game_on = True
    move_faster = 0
    while game_on:
        screen.update()
        time.sleep(REFRESH_SPEED)
        snake.move(MOVE_DISTANCE + move_faster)
        
        # Detect collision with food
        if snake.head.distance(food) < 15:
            # mechanism of new position for food eaten. while loop
            # is used for giving new position of food if it spawned inside
            # the body of the snake
            food_xcord, food_ycord = food.new_food_pos()
            for seg in snake.segments[1:]:
                if seg.distance(food_xcord, food_ycord) < 10:
                    food_xcord, food_ycord = food.new_food_pos()
            for i in range(GROW_SPEED):
                last_x, last_y = snake.read_pos() # unpack tuple of read cords of the last segment
                snake.create_segment(last_x, last_y)               
            scoreboard.score_up()
            # Every every specified score snake becomes faster
            if scoreboard.current_score() % 5 == 0 and scoreboard.current_score() > 1:
                move_faster += 1

        
        # Detect collision with a wall
        if (snake.head.xcor() > 295 or snake.head.xcor() < -295 or 
           snake.head.ycor() > 295 or snake.head.ycor() < -295):
            scoreboard.game_over()
            game_on = False
        
        # detect collision with a tail
        for seg in snake.segments[1:]:
            if snake.head.distance(seg) < 2:
                scoreboard.game_over()
                game_on = False
    screen.exitonclick()
    
        
if __name__ == "__main__":
    main()
