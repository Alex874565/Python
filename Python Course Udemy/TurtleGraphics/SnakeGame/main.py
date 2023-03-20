from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width = 600, height = 600)
screen.title("Snake Game")
screen.tracer(0)

def start():
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.onkeypress(key = 'w', fun = snake.up)
    screen.onkeypress(key = 's', fun = snake.down)
    screen.onkeypress(key = 'a', fun = snake.left)
    screen.onkeypress(key = 'd', fun = snake.right)

    screen.listen()

    scoreboard.write_score()
    
    game_on = True

    while game_on:
        screen.update()
        time.sleep(1/15)
        
        snake.move()
        distance_to_food = snake.head.distance(food)
        
        # Detect collision with food
        if distance_to_food <= 15:
            snake.add_part()
            for part in snake.parts:
                if part.distance(food) <= 15:
                    food.refresh()
            scoreboard.score_up()
            scoreboard.write_score()

        # Detect collision with wall
        if snake.wall_collision():
            screen.clear()
            scoreboard.game_over()
            screen.update()
            game_on = False

        # Detect colision with itself
        if snake.self_collision():
            screen.clear()
            scoreboard.game_over()
            screen.update()
            game_on = False

screen.onkey(key = "space", fun = start)
screen.listen()

screen.exitonclick()

