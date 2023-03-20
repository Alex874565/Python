class Statecounter():
    def __init__(self, allstates):
        self.missingstates = allstates[:]

    def state_guessed(self, state):
        self.missingstates.pop(self.missingstates.index(state))

    def create_report(self):
        with open(r"C:/Programare/PythonProjects/Python Course Udemy\CSV\us-states-game-start\missingstates.txt", "w") as file:
            for state in self.missingstates:
                file.write(f"{state}\n")
            