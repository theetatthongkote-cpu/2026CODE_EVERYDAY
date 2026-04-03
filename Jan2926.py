# day 29
# Refactoring + Clean Functions
import random
import time


def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy (1–10, 5 attempts)")
    print("2. Medium (1–20, 3 attempts)")
    print("3. Hard (1–50, 2 attempts)")

    choice = input("Select 1, 2, or 3: ")

    if choice == "1":
        return 10, 5
    elif choice == "2":
        return 20, 3
    else:
        return 50, 2


def get_secret_number(max_range):
    return random.randint(1, max_range)


def get_user_guess():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Try again.")


def check_guess(guess, secret):
    if guess > secret:
        return "high"
    elif guess < secret:
        return "low"
    else:
        return "correct"


def play_game(score):
    max_range, max_attempts = choose_difficulty()
    secret = get_secret_number(max_range)

    attempts = 0
    guesses = []

    while attempts < max_attempts:
        guess = get_user_guess()
        guesses.append(guess)

        result = check_guess(guess, secret)

        if result == "correct":
            print("You win 🤠")
            print("Guesses:", guesses)
            score += 1
            print("Score:", score)
            return score

        elif result == "high":
            print("Too high")
        else:
            print("Too low")

        attempts += 1

    print("Out of attempts ❌")
    print("Number was:", secret)
    print("Guesses:", guesses)
    return score
    time.sleep(5)


# MAIN GAME LOOP
score = 0

while True:
    score = play_game(score)

    retry = input("\nPlay again? (yes/no): ").lower()
    if retry != "yes":
        print("Final score:", score)
        break
