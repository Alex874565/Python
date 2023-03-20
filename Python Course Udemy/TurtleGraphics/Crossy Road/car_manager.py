from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager():
    def __init__(self):
        self.cars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_car(self, shape):
        random_chance = random.randint(1, 12)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape(shape)
            new_car.setheading(180)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            ystart = random.randint(-240, 240)
            for car in self.cars:
                if car.xcor() >= 270: 
                    while abs(ystart - car.ycor()) <20:
                        ystart = random.randint(-240, 240)
            new_car.setpos(x = 300, y = ystart)
            new_car.speed(0)
            self.cars.append(new_car)

    def movecars(self, level):
        self.carspeed = STARTING_MOVE_DISTANCE
        speed_increment = MOVE_INCREMENT * (level - 1)
        if level > 4:
            speed_increment = MOVE_INCREMENT * 4 + MOVE_INCREMENT * (level - 4) * 0.5
        self.carspeed = STARTING_MOVE_DISTANCE + speed_increment
        for car in self.cars:
            car.forward(self.carspeed)

    def destroy_unnecesary_cars(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.hideturtle()
                self.cars.pop(0)
