
# Screen
# Players + controls
# Ball + movement + wall,paddle collision
# Scoreboard + when_score + reset positions
# Game end + winner,loser

import time
import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
from ui import UI

screen = Screen()
screen.setup(height = 600, width = 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player1 = Paddle(1)
player2 = Paddle(2)
ball = Ball()
score1 = UI()
score2 = UI()
bg = UI()
bg.draw_middle()
score1.write_score(-40)
score2.write_score(40)

screen.update()

game_over = False

# Game_over func
def gameover(winnernr):
    global game_over, game_on
    ball.reset()
    player1.reset()
    player2.reset()
    bg.clear()
    score1.clear()
    score2.clear()
    game_over = True
    game_on = False
    bg.game_over(winnernr)

# Game
def game():
    MAXSCORE = 5
    # Players movement
    # Player 1
    screen.onkey(key = "w", fun = player1.move_up)
    screen.onkey(key = "s", fun = player1.move_down)
    # Player 2
    screen.onkey(key = "Up", fun = player2.move_up)
    screen.onkeypress(key = "Down", fun = player2.move_down)

    game_on = True
    while game_on:
        screen.update()
        time.sleep(1/144)

        # Move the ball
        ball.move()

        # Detect wall collision
        ball.detect_wall_collision()

        # Detect paddle collision
        ball.detect_paddle_collision(player1)
        ball.detect_paddle_collision(player2)

        # Detect out of bounds
        if ball.out_of_bounds():
            # Players movement
            # Player 1
            screen.onkey(key = "w", fun = None)
            screen.onkey(key = "s", fun = None)
            # Player 2
            screen.onkey(key = "Up", fun = None)
            screen.onkeypress(key = "Down", fun = None)
            if ball.out_of_bounds() == 1 and score1.score == MAXSCORE - 1:
                gameover(1)
            elif ball.out_of_bounds() == 2 and score2.score == MAXSCORE - 1:
                gameover(2)
            else:
                game_on = False
                if ball.out_of_bounds() == 1:
                    score1.score_up()
                else:
                    score2.score_up()
                ball.start_position()                
                player1.start_position()
                player2.start_position()
            screen.update()

# Game start

if game_over == False:
    screen.onkeypress(key = "space", fun = game)
screen.listen()

screen.exitonclick()