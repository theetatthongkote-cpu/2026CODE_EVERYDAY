# day 132
# chill ass day
try:
    print("Pick a number from 1 to 10")
    user_input = int(input("Enter a number: "))
    if user_input == 7:
        print("Lucky Number🍀")

    else:
        print("Not lucky today🐈‍⬛")

except ValueError:
    print("Please enter a valid integer.")
