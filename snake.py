from turtle import Turtle

POSITIONS = [0, -20, -40]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_block = []
        self.create_snake()
        self.snake_head = self.snake_block[0]

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
        self.snake_head.forward(20)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)