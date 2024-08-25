## Snake Game ##

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

x = [0, -20, -40]
snake_block = []

for turtle in range(0,3):
    t = Turtle(shape="square")
    t.color("white")
    t.penup()
    t.goto(x=x[turtle], y=0)
    snake_block.append(t)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # move third block to second block
    for block in range(len(snake_block)-1, 0, -1):
        x_pos = snake_block[block-1].xcor()
        y_pos = snake_block[block-1].ycor()
        snake_block[block].goto(x_pos, y_pos)
    snake_block[0].forward(20)







screen.exitonclick()