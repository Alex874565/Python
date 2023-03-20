import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 800, height = 600)
bet = screen.textinput(title = "Betting", prompt = "Which turtle do you bet on? (Turtle's names are their colors)")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

t1 = Turtle(shape = "turtle")
t2 = Turtle(shape = "turtle")
t3 = Turtle(shape = "turtle")
t4 = Turtle(shape = "turtle")
t5 = Turtle(shape = "turtle")
t6 = Turtle(shape = "turtle")

writer = Turtle()
writer.hideturtle()
writer.penup()
writer.speed(0)

turtles = [t1,t2,t3,t4,t5,t6]

startx = -380
starty = 75

for tutle in turtles:
    tutle.color(colors[turtles.index(tutle)])
    tutle.speed(10)
    tutle.penup()
    tutle.setpos(x = startx, y = starty)
    tutle.speed(0)
    starty -= 30

if bet:
    is_race_on = True

while is_race_on:
    for tutle in turtles:
        tutle.forward(random.randint(0, 10))
        if tutle.xcor() >= 370:
            winner = tutle.color()[1]
            if winner == bet:
                writer.pendown()
                writer.write("You won!", font = ("Arial", 24, "normal"), align = "center")
                print(f"You won! The {winner} turtle is the winner!")
            else:
                writer.pendown()
                writer.write("You lost.", font = ("Arial", 24, "normal"), align = "center")
                print(f"You lost. The {winner} turtle is the winner.")
            for tutle in turtles:
                if tutle.color()[1] != winner and tutle.color()[1] != bet:
                    pass
                else:
                    tutle.setpos(x = tutle.xcor(), y = tutle.ycor() - 7)
                    tutle.pendown()
                    tutle.pencolor("black")
                    if tutle.color()[1] == winner and winner != bet:
                        tutle.write("Winner:   ", align = "right")
                    elif tutle.color()[1] == winner and winner == bet:
                        tutle.write("Winner and your bet:   ", align = "right")
                    else:
                        tutle.write("Your bet:   ", align = "right")
                    tutle.penup()
                    tutle.setpos(x = tutle.xcor(), y = tutle.ycor() + 7)
            
            is_race_on = False
            break

screen.exitonclick()