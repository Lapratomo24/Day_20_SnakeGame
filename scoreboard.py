from turtle import Turtle
from food import Food


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.display_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", False, align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center")
