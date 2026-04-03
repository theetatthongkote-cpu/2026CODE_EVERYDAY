# day 28
# dictionay review
import time
import random


secret_number = random.randint(1, 20)

player = {
    "guesses": [],
    "attempts": 0,
    "max_attempts": 3,
    "locked": False
}

while True:
    if player["locked"]:
        print("You are locked out ⛔ Waiting 20 seconds...")
        time.sleep(20)
        player["attempts"] = 0
        player["guesses"].clear()
        player["locked"] = False
        print("Try again 🔓")

    try:
        guess = int(input("Guess the number: "))
        player["guesses"].append(guess)
        player["attempts"] += 1

        if guess == secret_number:
            print("Correct 🤠")
            print("Your guesses:", player["guesses"])
            break
        elif guess > secret_number:
            print("Too high ⬆️")
        else:
            print("Too low ⬇️")

    except ValueError:
        print("Invalid input ❌")
        continue

    if player["attempts"] >= player["max_attempts"]:
        player["locked"] = True
