from turtle import Turtle

class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
    
    def write_state(self, statename, data):
        row = data[data["state"] == statename]
        xpos = int(row["x"])
        ypos = int(row["y"])
        self.goto(x = xpos, y = ypos)
        self.write(statename, font = ("Arial", 8, "normal"), align = "center")

    def game_over(self, score):
        self.goto(y = 17, x = 0)
        self.pencolor("red")
        self.write("Game Over!", font = ("Arial", 24, "bold"), align = "center")
        self.goto(y = -17, x = 0)
        self.write(f"Your score was: {score}", font = ("Arial", 24, "bold"), align = "center")

    def game_won(self):
        self.goto(y = 17, x = 0)
        self.pencolor("red")
        self.write("Congratulations!", font = ("Arial", 24, "bold"), align = "center")
        self.goto(y = -17, x = 0)
        self.write(f"You won!", font = ("Arial", 24, "bold"), align = "center")
