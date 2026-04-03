# day 16
# DEFENSE AGAINST BRUTE FORCE (Rate Limiting + Lockouts)
import hashlib
import time
from datetime import datetime
import os
attempts = 0
Max_attempts = 7
# Stored users (username → hashed password)
users = {
    "admin": hashlib.sha256("ILOVEPIZZA".encode()).hexdigest(),
    "user1": hashlib.sha256("HELLOWORLD".encode()).hexdigest()
}


def log_lockout(username):
    with open("lockouts.log", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} | Account locked: {username}\n")


locked = False
while not locked:
    password = input("Enter password: ")
    hashed = hashlib.sha256(password.encode()).hexdigest()

    if users[password]:
        print("Access granted ✅")
        attempts = 0
        break
    else:
        attempts += 1
        print("Wrong password ❌")

    if attempts >= Max_attempts:
        locked = True
        print("Account locked 🔒")
    elif attempts == 3:
        print("Wait 2 seconds before trying again...")
        time.sleep(2)

    elif attempts >= 5:
        print("Wait 10 seconds before trying again...")
        time.sleep(10)


while locked:
    print("Please wait forever😈😈")
    time.sleep(
        100)
# chat gpt fixed:

attempts = 0
MAX_ATTEMPTS = 7

users = {
    "admin": hashlib.sha256("ILOVEPIZZA".encode()).hexdigest(),
    "user1": hashlib.sha256("HELLOWORLD".encode()).hexdigest()
}


def log_lockout(username):
    with open("lockouts.log", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} | Account locked: {username}\n")


locked = False
username = input("Enter username: ")

while not locked:
    password = input("Enter password: ")
    hashed_guess = hashlib.sha256(password.encode()).hexdigest()

    if username in users and hashed_guess == users[username]:
        print("Access granted ✅")
        attempts = 0
        break
    else:
        attempts += 1
        print("Wrong password ❌")

    if attempts >= MAX_ATTEMPTS:
        locked = True
        log_lockout(username)
        print("Account locked 🔒")

    elif attempts == 3:
        print("Wait 2 seconds before trying again...")
        time.sleep(2)

    elif attempts >= 5:
        print("Wait 10 seconds before trying again...")
        time.sleep(10)


while locked:
    print("Please wait forever 😈😈")
    time.sleep(5)
