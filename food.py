from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        x_pos = random.randint(-260, 260)
        y_pos = random.randint(-260, 260)
        self.goto(x_pos, y_pos)