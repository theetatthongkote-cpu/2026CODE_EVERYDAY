# day 31
# big review/big project
import hashlib
import random
import os
import time

FILE = "users.txt"
users = {}


# ---------- FILE HANDLING ----------
def load_users():
    if not os.path.exists(FILE):
        return
    with open(FILE, "r") as file:
        for line in file:
            name, salt, hashed, score, high = line.strip().split(",")
            users[name] = {
                "salt": salt,
                "hash": hashed,
                "score": int(score),
                "high_score": int(high)
            }


def save_users():
    with open(FILE, "w") as file:
        for name, data in users.items():
            file.write(
                f"{name},{data['salt']},{data['hash']},{data['score']},{data['high_score']}\n"
            )


# ---------- AUTH ----------
def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()


def register_user():
    name = input("Enter username: ")
    if name in users:
        print("User already exists")
        return None

    password = input("Enter password: ")
    salt = os.urandom(16).hex()
    hashed = hash_password(password, salt)

    users[name] = {
        "salt": salt,
        "hash": hashed,
        "score": 0,
        "high_score": 0
    }
    save_users()
    return name


def login_user():
    name = input("Username: ")
    password = input("Password: ")

    if name not in users:
        return None

    salt = users[name]["salt"]
    if hash_password(password, salt) == users[name]["hash"]:
        return name
    return None


# ---------- GAME ----------
def choose_difficulty():
    print("\n1. Easy (1–10, 5 tries)")
    print("2. Medium (1–20, 3 tries)")
    print("3. Hard (1–50, 2 tries)")
    choice = input("Choose: ")

    if choice == "1":
        return 10, 5
    elif choice == "2":
        return 20, 3
    else:
        return 50, 2


def play_game(player):
    max_range, max_attempts = choose_difficulty()
    secret = random.randint(1, max_range)
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue

        if guess == secret:
            print("You win 🤠")
            users[player]["score"] += 1
            users[player]["high_score"] = max(
                users[player]["score"],
                users[player]["high_score"]
            )
            save_users()
            return

        print("Too high" if guess > secret else "Too low")
        attempts += 1

    print("Out of attempts ❌")
    print("Number was:", secret)


# ---------- MAIN ----------
load_users()

choice = input("Register or Login? (r/l): ").lower()
player = register_user() if choice == "r" else login_user()

if not player:
    print("Access denied")
    exit()

while True:
    play_game(player)
    print("Score:", users[player]["score"])
    print("High score:", users[player]["high_score"])

    if input("Play again? (y/n): ").lower() != "y":
        break
