from turtle import Turtle

STARTING_POSITIONS = [(20, 0), (0,0), (-20,0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
SCREENMARGIN = 289

class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_part = Turtle(shape = "square")
            new_part.color("green")
            new_part.penup()
            new_part.setpos(position)
            self.parts.append(new_part)
        self.head = self.parts[0]
        self.head.color("darkgreen")
        self.tail = self.parts[2]

    def move(self):
        self.lastpos = self.tail.pos()
        for partindex in range(len(self.parts)-1, 0, -1):
            part = self.parts[partindex]
            nextpart = self.parts[partindex-1]
            part.setpos(x = nextpart.xcor(), y = nextpart.ycor())
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != LEFT and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading != DOWN and self.head.heading() != UP:
            self.head.setheading(DOWN)

    def wall_collision(self):
        xcor = self.head.xcor()
        ycor = self.head.ycor()
        if xcor > SCREENMARGIN or xcor < -SCREENMARGIN or ycor > SCREENMARGIN or ycor < -SCREENMARGIN:
            return True

    def self_collision(self):
        for part in self.parts[1:]:
                if part.distance(self.head) < 10:
                    return True

    def add_part(self):
        new_part = Turtle(shape = "square")
        new_part.color("green")
        new_part.penup()
        new_part.setpos(self.lastpos)
        self.parts.append(new_part)