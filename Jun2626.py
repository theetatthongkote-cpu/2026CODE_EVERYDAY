# day 172
# chill day.
import random
key = random.randint(1, 10)
try:
    while True:
        print("--NUMBER GUESSING GAME--")
        guess = int(input("Guess a number between 1-10: \n"))
        if guess == key:
            print(f"Congrats! You've guessed {guess}, which is correct!✅ ")
            break
        elif guess > key:
            print(f"Too High, Try Again!")
        elif guess < key:
            print(f"Too Low, Try Again!")
except ValueError:
    print("try again")
