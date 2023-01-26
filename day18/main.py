from turtle import Turtle
from turtle import Screen

colour = ["blue", "indigo", "cyan", "bisque", "green", "lime", "red", "blue", "indigo"]
timmy=Turtle()
timmy.shape('turtle')
i=0
def drawsides(no_of_sides):
    ang = 360/no_of_sides
    for i in range(no_of_sides) :
        timmy.forward(80)
        timmy.right(ang)



for a in range(3,8):
    drawsides(a)
    timmy.pencolor(colour[a])





screen = Screen()
screen.exitonclick()