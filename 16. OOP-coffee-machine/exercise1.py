from turtle import Turtle, Screen

szymon = Turtle()
print(szymon)

szymon.shape("turtle")
szymon.color("black")
my_screen = Screen()

print(my_screen.canvheight)
szymon.forward(100)
my_screen.exitonclick()
