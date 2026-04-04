# day 59
# caluclator app pt 2

import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
col_count = len(button_values[0])

color_light_green = "#162a1a"
color_black = "#0d1110"
color_dark_green = "#00c853"
color_neon_green = "#69f0ae"
color_white = "#e8ffe8"

window = tkinter.Tk()
window.title("Calculator")
window.resizable(True, True)

frame = tkinter.Frame(window, bg=color_black)

label = tkinter.Label(
    frame,
    text="0",
    font=("Times New Roman", 45),
    bg=color_black,
    fg=color_neon_green,
    anchor="e")


label.grid(row=0, column=0,
           columnspan=col_count, sticky="we")

for row in range(row_count):
    for column in range(col_count):
        value = button_values[row][column]
        button = tkinter.Button(
            frame, text=value,
            font=("times new roman", 30),
            height=1,
            command=lambda value=value: buttonclicked(value))

        button.grid(row=row+1, column=column, sticky="nsew")


frame.pack()
for i in range(row_count + 1):
    frame.rowconfigure(i, weight=1)

for j in range(col_count):
    frame.columnconfigure(j, weight=1)


def buttonclicked(value):
    print(value)


window.configure(bg=color_black)
window.mainloop()
