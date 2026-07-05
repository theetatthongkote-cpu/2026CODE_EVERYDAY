# day 27
# lists + loops
import random
import time
number = random.randint(1, 20)
guesses = []
attempts = 0
max_attempts = 3
while True:
    try:
        guess = int(input("What is the secret number?:"))
        guesses.append(guess)
        if guess == number:
            print("correct🤠")
            break
        elif guess >= number:
            print("Your number is too high")
            attempts += 1
        elif guess <= number:
            print("Your number is too low")
    except ValueError:
        print("Invalid input")
        continue
    if attempts >= max_attempts:
        print("You ran out of attempts please wait 20 seconds to try again")
        time.sleep(20)
        continue
