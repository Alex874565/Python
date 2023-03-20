from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(x = 0, y = 270)
        self.score = 0
        with open("SnakeGame/highscore.txt", "r") as file:
            self.high_score = int(file.read())

    def write_score(self):
        self.clear()
        self.pendown()
        self.write(f"Score: {self.score} High score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def score_up(self):
        self.score += 1

    def game_over(self):
        self.penup()
        self.setpos(y = 20, x = 0)
        self.write("Game Over!", align = ALIGNMENT, font = ("Courier", 30, "normal"))
        self.setpos(y = -20, x = 0)
        self.write(f"Your score was {self.score}.", align = ALIGNMENT, font = ("Courier", 30, "normal"))
        self.change_high_score()

    def change_high_score(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("SnakeGame/highscore.txt", "w") as file:
                file.write(str(self.high_score))
