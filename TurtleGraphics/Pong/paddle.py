from turtle import  Turtle

PADDLESPEED = 50

class Paddle(Turtle):

    def __init__(self, playernum):
        self.playernum = playernum
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len = 5)

        self.setheading(90)
        self.penup()

        self.start_position()

    def start_position(self):
        if self.playernum == 1:
            self.x_pos = -350
            self.y_pos = 0
        elif self.playernum == 2:
            self.x_pos = 350
            self.y_pos = 0

        self.setpos(x = self.x_pos, y = self.y_pos)
        self.color("white")

    def move_up(self):
        self.y_pos += PADDLESPEED
        self.setpos(x = self.x_pos, y = self.y_pos)

    def move_down(self):
        self.y_pos -= PADDLESPEED
        self.setpos(x = self.x_pos, y = self.y_pos)