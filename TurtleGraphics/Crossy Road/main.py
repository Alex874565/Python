# Player 
    # Spawn
    # Move
    # Finish line
    # Hit by car

# Cars
    # Spawn - random location + color
    # Move
    # Level Up
    # Dissapear

# Scoreboard
    # Level
    # Game end + game over

import time
from turtle import Screen
from playermodule import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

carimage = "C:\Programare\PythonProjects\Python Course Udemy\TurtleGraphics\Crossy Road\Images\car.gif"

screen.addshape(carimage)

scoreboard = Scoreboard()
player = Player()
carmanager = CarManager()

scoreboard.write_level()

game_is_on = True
while game_is_on:
    time.sleep(1/60)
    screen.update()

    # Check collision
    for car in carmanager.cars:
        xdistance = abs(player.xcor() - car.xcor())
        ydistance = abs(player.ycor() - car.ycor())
        if xdistance <= 19.5 and ydistance <= 19.9:
            print(xdistance, ydistance)
            screen.clear()
            scoreboard.game_over()
            game_is_on = False
            screen.update()

    if game_is_on:
        # Player movement
        screen.onkeypress(key = "w", fun = player.move)
        screen.listen()

        # Create cars
        carmanager.create_car(carimage)

        # Move cars
        carmanager.movecars(scoreboard.level)

        # Destroy cars
        carmanager.destroy_unnecesary_cars()

        # Change level
        if player.finish_line():
            player.setpos(STARTING_POSITION)
            for car in carmanager.cars:
                car.hideturtle()
                car.setpos(300,300)
            carmanager.cars.clear()
            scoreboard.level_up()
            scoreboard.write_level()


screen.exitonclick()

    