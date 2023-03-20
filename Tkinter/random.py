from tkinter import *

window = Tk()


def button_clicked():
    my_label.config(text = f"{input.get()}")

window.title("Title")
window.minsize(width = 500, height = 300)
window.config(padx = 100, pady = 200)

my_label = Label(text = "text")
my_label.grid(column = 0, row = 0)
my_label.config(padx = 50, pady = 50)

button1 = Button(text = "Click Me", command = button_clicked)
button1.grid(row = 1, column = 1)

button2 = Button(text = "New Button")
button2.grid(row = 0, column = 2)

input = Entry(width = 30)
input.grid(row = 2, column = 3)

window.mainloop()
