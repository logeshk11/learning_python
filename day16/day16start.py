from turtle import Turtle, Screen

def print_msg(msg):
    print(f"Hi {msg}")

def run_turtle():
    timmy= Turtle()
    print(timmy)
    timmy.shape("turtle")
    timmy.fillcolor("blue")
    myscreen = Screen()
    print(myscreen.canvheight)
    timmy.forward(120)
    timmy.right(90)
    myscreen.exitonclick()

if __name__ == '__main__':
    run_turtle()