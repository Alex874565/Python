from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        xspawn = random.randint(-270, 270)
        yspawn = random.randint(-270,270)
        self.setpos(x = xspawn, y = yspawn)
