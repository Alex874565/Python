from turtle import Turtle

class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.pensize(10)
        self.speed(0)

    def draw_middle(self):
        self.penup()
        self.setpos(x = 0, y = 380)
        self.setheading(270)
        while self.ycor() >= -360:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(40)

    def write_score(self, pos):
        self.penup()
        self.xpos = pos
        self.setpos(y = 220, x = self.xpos)
        self.pendown()
        self.write("0", align = "center", font = ("New Courier", 60, "bold"))
        self.score = 0

    def score_up(self):
        self.score += 1
        self.clear()
        self.penup()
        self.setpos(y = 220, x = self.xpos)
        self.pendown()
        self.write(f"{self.score}", align = "center", font = ("New Courier", 60, "bold"))

    def game_over(self, playernr):
        self.setpos(0,0)
        self.write(f"Game Over!\n Player {playernr} wins!", align = "center", font = ("New Courier", 40, "bold"))