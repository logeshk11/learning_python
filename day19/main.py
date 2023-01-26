from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()


def move_forward():
    tim.forward(50)


# def move_back():
#     tim.back(5)
#
# def move_right():w
#     tim.right(90)
#
# def move_left():
#     tim.left(90)

screen.listen()
screen.onkey(key= "w", fun = move_forward)

screen.exitonclick()
