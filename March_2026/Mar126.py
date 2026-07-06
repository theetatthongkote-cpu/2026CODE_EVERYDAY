# day 60
# caluclator app pt 3

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
    anchor="e",
    width=col_count)


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
        if value in top_symbols:
            button.config(fg=color_white, bg=color_light_green)
        elif value in right_symbols:
            button.config(fg=color_white, bg=color_dark_green)
        else:
            button.config(fg=color_white, bg=color_neon_green)
        button.grid(row=row+1, column=column, sticky="nsew")


frame.pack()
for i in range(row_count + 1):
    frame.rowconfigure(i, weight=1)

for j in range(col_count):
    frame.columnconfigure(j, weight=1)


def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None


def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def buttonclicked(value):
    global A, B, operator, waiting_for_second_number

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                try:
                    B = label["text"]
                    if operator == "+":
                        result = float(A) + float(B)
                    elif operator == "-":
                        result = float(A) - float(B)
                    elif operator == "×":
                        result = float(A) * float(B)
                    elif operator == "÷":
                        if float(B) != 0:
                            result = float(A) / float(B)
                        else:
                            label["text"] = "Error"
                            return
                    label["text"] = remove_zero_decimal(result)
                    A = label["text"]
                    B = None
                    operator = None
                    waiting_for_second_number = False
                except:
                    label["text"] = "Error"
        else:
            # Store current value as A and set operator
            A = label["text"]
            operator = value
            waiting_for_second_number = True
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
    elif value == "√":
        result = float(label["text"]) ** 0.5
        label["text"] = remove_zero_decimal(result)
    else:  # digits or .
        if value == ".":
            if "." not in label["text"]:
                if label["text"] == "0" or (waiting_for_second_number and label["text"] == ""):
                    label["text"] = "0."
                else:
                    label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0" or waiting_for_second_number:
                label["text"] = value
                waiting_for_second_number = False
            else:
                label["text"] += value


window.configure(bg=color_black)
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2)-(window_width/2))
window_y = int((screen_height/2)-(screen_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
# Initialize global variables BEFORE mainloop
A = "0"
operator = None
B = None
waiting_for_second_number = False

window.mainloop()
