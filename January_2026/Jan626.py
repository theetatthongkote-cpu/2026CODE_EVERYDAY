# day 6
# functions

def function_name():
    print("hello world")


function_name()


def greet(name):
    print("hello " + name)


greet("alice")
greet("bob")


def add(a, b):
    return a + b


result = add(3, 5)
print(result)  # Output: 8


def multiply(x, y):
    return x * y


product = multiply(4, 6)
print(product)  # Output: 24


def is_long_enough(password):
    return len(password) >= 8


pwd = input("Enter your password: ")
if is_long_enough(pwd):
    print("Password is long enough")
else:
    print("Password is too short")
# extra practice


def duolingo_streak(name, days):
    print("Congratulations", name, "Your duolingo streak is", days, "days!")


duolingo_streak("Alice", 45)
duolingo_streak("Bob", 120)
# chat gpt's combining checks


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_upper(password):
    return any(char.isupper() for char in password)


while True:
    pwd = input("Enter your password: ")
    if has_digit(pwd) and has_upper(pwd):
        print("Strong password")
        break
    else:
        print("consider adding a digit and an uppercase letter to your password")
        break
# gpt's password checker(password=code)(#task 1)


def length_check(code):
    return len(code) >= 8


def digit_check(code):
    return any(char.isdigit() for char in code)


def uppercase_check(code):
    return any(char.isupper() for char in code)


while True:
    cde = input("Enter your code: ")
    if length_check(cde) and digit_check(cde) and uppercase_check(cde):
        print("Strong code")
    else:
        print("consider adding a digit, an uppercase letter, and making it at least 8 characters long")
        break
# task 2


def length_check(boarding_pass):
    return len(boarding_pass) == 6


def letter_check(boarding_pass):
    return boarding_pass[0].isalpha() and boarding_pass[1].isalpha()


def digit_check(boarding_pass):
    return boarding_pass[2:].isdigit()


while True:
    bp = input("Enter your boarding pass: ")
    score = 0
    if length_check(bp):
        score += 1
    if letter_check(bp):
        score += 1
    if digit_check(bp):
        score += 1
    if score == 3:
        print("valid boarding pass")
    else:
        print("invalid boarding pass")
    break
# task 3


def mask(email):
    return len(email) * "*"


eml = input("Enter your email: ")
print("Masked email:", mask(eml))
