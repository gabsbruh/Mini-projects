import colorgram as cg
import turtle as t
import random


# finding colours from painting
colours = cg.extract('the_hirst_painting.jpg', 100)
in_rgb = []

for colr in colours:
    r = colr.rgb.r
    g = colr.rgb.g
    b = colr.rgb.b
    in_rgb.append((r,g,b))

# in rgb:
# [(240, 246, 243), (132, 166, 205), (221, 148, 106), 
# (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), 
# (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), 
# (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55),
# (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166),
# (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109),
# (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56),
# (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]

# code to run the turtle with drawing dots

def change_color(turtle):
    turtle.color(random.choice(in_rgb))

#adjustments
screen = t.Screen()
screen.colormode(255)
spark = t.Turtle()
spark.shape('arrow')
spark.speed(11)

spark.pu()
spark.setpos(-425, -425) # setting down-left to start an algorithm from the corner
for j in range(1,11):
    for i in range(10):
        change_color(spark)
        spark.pd()
        spark.begin_fill()
        spark.circle(20)
        spark.end_fill()
        spark.pu()
        spark.forward(90)
    spark.setpos(-425, (-425) + 90*j)  
       
screen.exitonclick()
    
        