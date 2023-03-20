from tkinter import W
import turtle
from turtle import Turtle,Screen

turt = Turtle()
stats = Turtle()
stats.hideturtle()
writer = Turtle()
writer.hideturtle()
screen = Screen()

writer.speed(0)
writer.penup()
writer.setpos(y = screen.window_height()/2 - 20, x = -screen.window_width()/2 + 10)
writer.pendown()
writer.write(f'speed: ')
writer.penup()

stats.penup()
statsx = writer.xcor() + 40
statsy = writer.ycor()
stats.setpos(x = statsx, y = statsy)

turt.speed(10)

screen.tracer(0)

colors = ['black', 'grey', 'green', 'lime', 'blue', 'purple', 'pink', 'red', 'orange', 'yellow']
heading = 0
speed = 0.2
colorindex = 0
keypressed = False
fwd = False
bwd = False
right = False
left = False
penstate = True
changeddir = False


def key_not_pressed():
    global keypressed

def left_pressed():
    global left
    left = True
    print('left_pressed')

def left_not_pressed():
    global left
    left = False
    print('left_not_pressed')
    key_not_pressed()

def right_pressed():
    global right
    right = True
    print('right_pressed')

def right_not_pressed():
    global right
    right = False
    key_not_pressed()

def fwd_pressed():
    global fwd
    fwd = True
    print('fwd_pressed')

def fwd_not_pressed():
    global fwd
    fwd = False
    print('fwd_not_pressed')
    key_not_pressed()

def bwd_pressed():
    print('bwd_pressed')
    global bwd, changeddir, heading
#    if changeddir == False:
#        heading =  180 + heading
#        turt.setheading(heading)
    bwd = True
    changeddir = True

def bwd_not_pressed():
    print('bwd_not_pressed')
    global bwd, changeddir, heading 
#   if changeddir == True:
#        heading =  180 + heading
#        turt.setheading(heading)
    bwd = False
    changeddir = False
    key_not_pressed()

def move_forwards():
    print('moving_forwards')
    turt.forward(speed)

def move_backwards():
    global heading, changeddir
    print('moving_backwards')
#    turt.forward(speed)
    turt.backward(speed)

def turn_left():
    print('turning_left')
    global heading
#    if changeddir:
#        heading -= speed
#    else:
    heading += speed
    turt.setheading(heading)

def turn_right():
    print('turning_right')
    global heading
#    if changeddir:
#        heading += speed
#    else:
    heading -= speed
    turt.setheading(heading)

def clear_and_reset():
    global heading,speed,keypressed,colorindex,fwd,bwd,right,left,penstate,changeddir
    turt.clear()
    turt.penup()
    turt.home()
    turt.pendown()
    heading = 0
    speed = 0.2
    colorindex = 0
    turt.color(colors[colorindex])
    keypressed = False
    fwd = False
    bwd = False
    right = False
    left = False
    penstate = True
    changeddir = False

def color_up():
    global colorindex
    colorindex += 1
    if colorindex >= len(colors):
        colorindex = 0
    color = colors[colorindex]
    turt.color(color)

def color_down():
    global colorindex
    colorindex -= 1
    if colorindex <= 0:
        colorindex = len(colors) - 1
    color = colors[colorindex]
    turt.color(color)

def speed_up():
    global speed
    speed += 0.02
    speed = round(speed, 2)
    stats.clear()
    stats.setpos(x = statsx, y = statsy)
    stats.pendown()
    stats.write(f"{speed}")
    stats.penup()

def speed_down():
    global speed
    if speed > 0.0:
        speed -= 0.02
        speed = round(speed, 2)
    stats.clear()
    stats.setpos(x = statsx, y = statsy)
    stats.pendown()
    stats.write(f"{speed}")
    stats.penup()

def pen_up_down():
    global penstate
    penstate =  not penstate 

def main():
    global keypressed, fwd, bwd, left, right
    stats.pendown()
    stats.write(f"{speed}")
    stats.penup()
    keypressed = 1
    while True:
        screen.onkeypress(key = 'Right', fun = color_up)
        screen.onkeypress(key = 'Left', fun = color_down)

        screen.onkey(key = 'space' , fun = pen_up_down)
        screen.onkey(key = 'c', fun = clear_and_reset)

        screen.onkeypress(key = "w", fun = fwd_pressed)
        screen.onkeypress(key = "s", fun = bwd_pressed)
        screen.onkeypress(key = "d", fun = right_pressed)
        screen.onkeypress(key = "a", fun = left_pressed)

        screen.onkeyrelease(key = "w", fun = fwd_not_pressed)
        screen.onkeyrelease(key = "s", fun = bwd_not_pressed)
        screen.onkeyrelease(key = "d", fun = right_not_pressed)
        screen.onkeyrelease(key = "a", fun = left_not_pressed)

        screen.onkeypress(key = 'Up', fun = speed_up)
        screen.onkeypress(key = 'Down', fun = speed_down)
        
        if penstate:
            turt.pendown()
        else:
            turt.penup()

        if fwd:
            move_forwards()
            if left:
                turn_left()
            if right:
                turn_right()
        elif bwd:
            move_backwards()
            if left:
                turn_left()
            if right:
                turn_right()
        elif left:
            turn_left()
            if fwd:
                move_forwards()
            if bwd:
                move_backwards()
        elif right:
            turn_right()
            if fwd:
                move_forwards()
            if bwd:
                move_backwards()

        screen.update()
        screen.listen()


main()
screen.exitonclick()