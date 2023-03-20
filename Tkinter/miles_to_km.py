from tkinter import *

def calculate():
    result = float(input_box.get()) * 1.609344
    labels["output"].config(text = f"{result:0.2f}")

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(height = 20, width = 20)
window.config(padx = 20, pady = 30, background="white")

input_box = Entry(width = 20)
input_box.grid(row = 0, column = 1)

labels = {}

labels["Miles"] = Label(text = "Miles", background="white")
labels["Miles"].grid(row = 0, column = 2)

labels["is_equal_to"] = Label(text = "is equal to", background="white")
labels["is_equal_to"].grid(row = 1,  column = 0)

labels["output"] = Label(text = "0", background="white")
labels["output"].grid(row = 1, column = 1)

labels["Km"] = Label(text = "Km", background="white")
labels["Km"].grid(row = 1, column = 2)

button = Button(text = "Calculate", command = calculate, background="white")
button.grid(row = 2, column = 1)

window.mainloop()