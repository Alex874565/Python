# import turtle

# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)