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


tim.pensize(1)

tim.speed(550)

for a in range(int(360/5)):
    tim.circle(100)
    tim.color(my_colour())
    tim.setheading(tim.heading()+5)

screen= Screen()
screen.exitonclick()