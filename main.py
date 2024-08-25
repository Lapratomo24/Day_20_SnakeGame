## Snake Game ##

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

x = [0, -20, -40]

for turtle in range(0,3):
    t = Turtle(shape="square")
    t.color("white")
    t.penup()
    t.goto(x=x[turtle], y=0)









screen.exitonclick()