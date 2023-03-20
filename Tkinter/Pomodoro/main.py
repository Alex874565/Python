from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    countdown(WORK_MIN, 00)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(mins, secs):
    canvas.itemconfig(timer, text = f"{mins:02.00f}:{secs:02.00f}")
    canvas.grid(row = 1, column = 1)
    if mins or secs:
        if secs == 0:
            window.after(1000, countdown, mins-1, 59)
        else:    
            window.after(1000, countdown, mins, secs-1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, background = YELLOW)

tomato_img = PhotoImage(file = r"C:\Programare\PythonProjects\Python Course Udemy\Tkinter\Pomodoro\tomato.png")

canvas = Canvas(width = 200, height = 224)
canvas.create_image(100, 112, image = tomato_img)

timer = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))

canvas.config(background = YELLOW, highlightthickness=0)
canvas.grid(row = 1, column = 1)

phase_label = Label(text = "Timer", bg = YELLOW, fg = GREEN, font = (FONT_NAME, 40, "bold"))
phase_label.grid(row = 0, column = 1)

checks_label = Label(text = "✔", bg = YELLOW, fg = GREEN, font = (FONT_NAME, 15, "normal"))
checks_label.grid(row = 3, column = 1)

start_button = Button(text = "Start", command = start_timer, font = (FONT_NAME, 15, "bold"), borderwidth = 0, bg = YELLOW, activebackground=YELLOW, fg = RED, activeforeground=PINK, highlightthickness = 0)
start_button.grid(row = 2, column = 0)

reset_button = Button(text = "Reset", font = (FONT_NAME, 15, "bold"), borderwidth = 0, bg = YELLOW, activebackground=YELLOW, fg = RED, activeforeground=PINK, highlightthickness=0)
reset_button.grid(row = 2, column = 2)

window.mainloop()