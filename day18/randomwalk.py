import random
import turtle
from turtle import Screen
ang=[0, 90, 270, 360]
colour = ["blue", "indigo", "cyan", "bisque", "green", "lime", "red", "blue", "indigo"]
tim = turtle.Turtle()
turtle.colormode(255)

def my_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple=(r, g, b)
    return my_tuple

tim.speed(100)
tim.pensize(6)
tim.hideturtle()
for move in range(200):
    tim.forward(20)
    tim.setheading(random.choice(ang))
    tim.pencolor(my_colour())
screen= Screen()
screen.exitonclick()