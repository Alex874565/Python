from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(x = -290, y = 260)
        self.level = 1
        self.speed(0)

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font = FONT)

    def game_over(self):
        self.setpos(y = 20, x = 0)
        self.write("Game Over!", font = FONT, align = "center")
        self.setpos(y = -20, x = 0)
        self.write(f"You have reached level {self.level}.", font = FONT, align = "center")

    def level_up(self):
        self.level += 1