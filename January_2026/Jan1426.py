# day 14
# small project
# one time use calcuulator
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a/b


while True:
    user_input = input(
        "Would you like to add,subtract,multiply, or divide?").lower()
    if user_input == "add":
        a = int(input("What is your first digit:"))
        b = int(input("What is your second digit:"))
        result = add(a, b)
        print(f"Your result is: {result}")
        break
    elif user_input == "substract":
        a = int(input("What is your first digit:"))
        b = int(input("What is your second digit:"))
        result = subtract(a, b)
        print(f"Your result is: {result}")
        break
    elif user_input == "multiply":
        a = int(input("What is your first digit:"))
        b = int(input("What is your second digit:"))
        result = multiply(a, b)
        print(f"Your result is {result}")
        break
    elif user_input == "divide":
        a = int(input("What is your dividend:"))
        b = int(input("What is your divisor:"))
        result = divide(a, b)
        print(f"Your result is {result}")
        break
    else:
        print("Invalid Input try again")
        continue
