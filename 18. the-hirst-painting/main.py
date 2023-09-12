import colorgram as cg
import turtle as t

#adjustments
screen = t.Screen()
spark = t.Turtle()
spark.shape('circle')
spark.color('red')
spark.speed(11)


# finding colours from painting
colours = cg.extract('the_hirst_painting.jpg', 164)
in_rgb = []

for colr in colours:
    r = colr.rgb.r
    g = colr.rgb.g
    b = colr.rgb.b
    in_rgb.append((r,g,b))

print(in_rgb)
