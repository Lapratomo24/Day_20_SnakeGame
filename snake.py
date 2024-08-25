from turtle import Turtle

POSITIONS = [0, -20, -40]


class Snake:
    def __init__(self):
        self.snake_block = []
        self.create_snake()

    def create_snake(self):
        for position in range(0, 3):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(x=POSITIONS[position], y=0)
            self.snake_block.append(t)

    def move(self):
        # move third block to second block
        for block in range(len(self.snake_block) - 1, 0, -1):
            x_pos = self.snake_block[block - 1].xcor()
            y_pos = self.snake_block[block - 1].ycor()
            self.snake_block[block].goto(x_pos, y_pos)
        self.snake_block[0].forward(20)
