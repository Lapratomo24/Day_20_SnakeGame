from turtle import Turtle
from food import Food


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.display_score()

    def update_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} --- HighScore: {self.highscore}", False, align="center")

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.display_score()

    # def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", False, align="center")
