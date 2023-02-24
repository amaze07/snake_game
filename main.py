import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

def restart():
    screen.reset()
    run_game()

def run_game():
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(restart, "r")

    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -295 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
            is_game_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for seg in snake.segments:
            if seg == snake.head:
                pass
            elif snake.head.distance(seg) < 10:
                is_game_on = False
                scoreboard.game_over()

run_game()
screen.exitonclick()
