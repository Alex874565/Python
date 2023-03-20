from turtle import Screen
import pandas
from writer import Writer
from statecounter import Statecounter

screen = Screen()
screen.bgpic("Python Course Udemy/CSV/us-states-game-start/blank_states_img.gif")
screen.setup(height = 500, width = 700)
screen.title("U.S. States Game")

data = pandas.read_csv("Python Course Udemy/CSV/us-states-game-start/50_states.csv")

statesnames = data["state"].to_list()

writer = Writer()
statecounter = Statecounter(statesnames)

game_on = True
score = 0

while game_on:
    guessed = False
    guess = screen.textinput(title = "Enter state's name...", prompt = f"Score: {score}/50").title()
    if guess == "Exit":
        statecounter.create_report()
        writer.clear()
        score = 0
        del statecounter
        statecounter = Statecounter(statesnames)
    else:
        for name in statesnames:
            name = name
            if guess == name:
                guessed = True
                statecounter.state_guessed(guess)
                break

        if guessed:
            writer.write_state(guess, data)
            score += 1
        else:
            writer.game_over(score)
            game_on = False

        if score == 50:
            writer.game_won()
            game_on = False

screen.exitonclick()