from turtle import Turtle
import math
import random

XBALLSPEED = 3
YBALLSPEED = 3
SPEEDGROWTH = 0.5
SPEEDLIMIT = 17
SCREENMARGIN_X = 380
SCREENMARGIN_Y = 280

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.start_position()

    def start_position(self):
        self.x_pos = 0
        self.y_pos = 0
        self.ydirection = random.choice([-1, 1])
        self.xdirection = random.choice([-1, 1])
        self.setpos(x = self.x_pos, y = self.y_pos)
        self.xballspeed = XBALLSPEED
        self.yballspeed = YBALLSPEED

    def move(self):
        self.x_pos += self.xdirection * self.xballspeed
        self.y_pos += self.ydirection * self.yballspeed
        self.setpos(x = self.x_pos, y = self.y_pos)

    def detect_wall_collision(self):
        if self.ycor() > SCREENMARGIN_Y:
            self.ydirection = -1
        elif self.ycor() < -SCREENMARGIN_Y:
            self.ydirection = 1

    def detect_paddle_collision(self, paddle):
        if self.xcor() >= 330 and self.xcor() <= 350:
            if self.distance(paddle) <= 50:
                self.xdirection = -1
            if self.xballspeed < SPEEDLIMIT:
                self.xballspeed += SPEEDGROWTH
                self.yballspeed += SPEEDGROWTH
        elif self.xcor() <= -330 and self.xcor() >= -350:
            if self.distance(paddle) <= 50:
                self.xdirection = 1
            if self.xballspeed < SPEEDLIMIT:
                self.increase_speed()
    def increase_speed(self):
        self.xballspeed += self.xdirection * SPEEDGROWTH
        self.yballspeed += self.ydirection * SPEEDGROWTH

    def out_of_bounds(self):
        if self.xcor() > 360:
            return 1
        elif self.xcor() < -360:
            return 2
        else:
            return 0