# day 25
# Smart Guessing Game(refreshing fundamentals)
import random
import time
secret_number = random.randint(1, 10)
print(secret_number)
attempts = 0
max_attempts = 3
while True:
    guess = int(input("what is the number?:"))
    if guess == secret_number:
        print("True")
        break
    elif guess > secret_number:
        print("Your guess is too high")
        attempts += 1

    elif guess < secret_number:
        print("Your number is too small")
        attempts += 1

    if attempts == max_attempts:
        print("You ran out of guesses please wait 10 seconds")
        time.sleep(10)
        break

    else:
        print("Invalid input")
        attempts += 1
