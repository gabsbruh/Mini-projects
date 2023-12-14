from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import constants as c
import time

def main():
    # screen setup
    screen = Screen()
    screen.title('Pong Game')
    screen.setup(width=c.SCREEN_WIDTH, height=c.SCREEN_HEIGHT)
    screen.bgcolor('black')
    screen.tracer(0)  # automatic update of animations are turned off
    # paddle creator
    right_paddle = Paddle()
    right_paddle.position('right')
    left_paddle = Paddle()
    left_paddle.position('left')
    
    # add ball
    ball = Ball()
    
    # TODO zmien tak aby po jednym kliknieciu caly czas szlo w dol,
    # nie trzeba wtedy bedzie robic przyciskow jednoczesnych 
    # GENIALNY POMYSL 
    vs_cpu = False
    screen.listen()
    if vs_cpu:
        screen.onkeypress(left_paddle.up, "Up")
        screen.onkeypress(left_paddle.down, "Down")
        screen.onkeypress(left_paddle.up, "w")
        screen.onkeypress(left_paddle.down, "s")   
    else:
        screen.onkeypress(left_paddle.up, "w")
        screen.onkeypress(left_paddle.down, "s")            
        screen.onkeypress(right_paddle.up, "Up")
        screen.onkeypress(right_paddle.down, "Down") 
    
    
    # proper game
    game_on = True
    while game_on:
        screen.update()
        ball.move()
        time.sleep(c.REFRESH_SPEED)
        
    screen.exitonclick()
    
    
    

if __name__ == "__main__":
    main()