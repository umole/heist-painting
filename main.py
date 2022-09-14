import turtle
import random

pen = turtle.Turtle()
turtle.colormode(255)
pen.speed("fastest")
pen.hideturtle()
#pen.width = 50

#rgb_color = []
#colors = colorgram.extract("20_001.jpg", 10)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.g
#    new_colors = (r, g, b)
#    rgb_color.append(new_colors)

#print(rgb_color)

colors = [(199, 175, 175), (124, 36, 36), (168, 106, 106), (222, 224, 224), (186, 158, 158), (6, 57, 57), (109, 67, 67)]

def clors():
  # for spec_color in colors:
    color = random.choice(colors)
    return color

def draw(space, x, y):
    #color = ()
    for i in range(y):
        for j in range(x):
            pen.dot(20, clors())
            pen.penup()
            #move forward by a specified distance "space"
            pen.forward(50)
            pen.pendown()
        pen.penup()
        pen.back(space * x)
        pen.lt(90)
        pen.forward(space)
        pen.rt(90)
        pen.pendown()


pen.setheading(225)
pen.penup()
pen.forward(7 * 50)
pen.setheading(0)
pen.pendown()

draw(50, 10, 10)
screen = turtle.Screen()
screen.exitonclick()

