from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.speed(0)
        self.setpos(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return 1
        else:
            return 0
