## Snake Game ##

from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.respawn()
        snake.extend_block()
        scoreboard.update_score()

    # detect collision with wall
    if snake.snake_head.xcor() < -290 or snake.snake_head.xcor() > 290 or snake.snake_head.ycor() < -290 or snake.snake_head.ycor() > 290:
        scoreboard.reset()
        snake.respawn()

    # detect collision with tail
    for block in snake.snake_block[1:]:
        if snake.snake_head.distance(block) < 10:
            scoreboard.reset()
            snake.respawn()

screen.exitonclick()
