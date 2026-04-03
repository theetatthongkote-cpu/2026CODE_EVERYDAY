# day 20
# fundamentals
import random
attempts = 0
max_attempts = 3
numbers = random.randint(1, 10)
while True:
    guess = int(input("what is the number?:"))
    if guess == numbers:
        print("True")
        break
    elif guess >= numbers:
        print("Your guess is too high")
        attempts += 1

    elif guess <= numbers:
        print("Your number is too small")
        attempts += 1

    if attempts == max_attempts:
        print("You ran out of guesses please wait 10 seconds")
        break
    else:
        print("Invalid input")
