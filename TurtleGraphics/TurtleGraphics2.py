from turtle import Turtle, Screen
import random
from colorgram import extract, Color

screen = Screen()

screen.colormode(255)

turtle = Turtle()
turtle.speed(0)
turtle.hideturtle()

image = "hirst_complete_spot_paintings_1024x1024@2x.jpg"

def extract_colors(image, colornr):
    colors = extract(image, colornr)

    rgbs = []

    for color in colors:
        rgb = color.rgb
        rgbs.append((rgb.r, rgb.g, rgb.b))

    return rgbs

def dots_repartition(n):
    dots_vs_rows = n
    dots_per_row = n
    rows = 1
    for i in range(2, n//2 + 1):
        if n % i == 0 and abs(n//i - i) < dots_vs_rows:
            dots_vs_rows = abs(n//i - i)
            if i > n//i:
                dots_per_row = n//i
                rows = i
            else:
                dots_per_row = i
                rows = n//i

    return dots_per_row, rows




def draw(n, colornr, size):
    rgbs = extract_colors(image, colornr)
    dots_per_row, rows = dots_repartition(n) 
    startx = -(dots_per_row/2 * 3 * size)
    starty = -(rows/2 * 3 * size)
    for i in range(rows):
        x = startx
        y = starty
        for i in range(dots_per_row):
            turtle.penup()
            turtle.setpos((x, y))
            turtle.pendown()
            color = random.choice(rgbs)
            turtle.dot(size, color)
            x += 2*size 
        starty += 2*size


draw(40, 30, 50)
            


screen.exitonclick()
