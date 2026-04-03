# day 18
# relearning essential lessons
import os
import hashlib
import time
from datetime import datetime

# ===================== CONFIG =====================
USERS_FILE = "secure_users.txt"
MAX_ATTEMPTS = 5

# ===================== DATA =====================
users = {}              # username -> {salt, hashed_password}
attempts = {}           # username -> attempt count

# ===================== FILE HANDLING =====================


def load_users():
    if not os.path.exists(USERS_FILE):
        return

    with open(USERS_FILE, "r") as file:
        for line in file:
            username, salt, hashed_password = line.strip().split(",")
            users[username] = {
                "salt": salt,
                "hashed_password": hashed_password
            }


def save_users():
    with open(USERS_FILE, "w") as file:
        for username, data in users.items():
            file.write(
                f"{username},{data['salt']},{data['hashed_password']}\n"
            )


load_users()

# ===================== SECURITY FUNCTIONS =====================


def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()


def strong_password(password):
    return (
        len(password) >= 8 and
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password)
    )


# ===================== USER FUNCTIONS =====================
def register_user():
    username = input("Choose a username: ").lower()

    if username in users:
        print("❌ Username already exists.")
        return

    password = input("Choose a strong password: ")

    if not strong_password(password):
        print("❌ Weak password.")
        print("Must contain uppercase, lowercase, number & symbol.")
        return

    salt = os.urandom(16).hex()
    hashed_password = hash_password(password, salt)

    users[username] = {
        "salt": salt,
        "hashed_password": hashed_password
    }

    save_users()
    print("✅ Registration successful!")


def login_user():
    username = input("Username: ").lower()

    if username not in users:
        print("❌ Username not found.")
        return

    if username not in attempts:
        attempts[username] = 0

    while attempts[username] < MAX_ATTEMPTS:
        password = input("Password: ")

        salt = users[username]["salt"]
        hashed = hash_password(password, salt)

        if hashed == users[username]["hashed_password"]:
            print("✅ Login successful!")
            attempts[username] = 0
            return
        else:
            attempts[username] += 1
            remaining = MAX_ATTEMPTS - attempts[username]
            print(f"❌ Incorrect password ({remaining} attempts left)")

            # rate limiting
            if attempts[username] == 3:
                print("⏳ Too many attempts. Waiting 5 seconds...")
                time.sleep(5)

            if attempts[username] >= MAX_ATTEMPTS:
                print("🔒 Account locked.")
                return


# ===================== MAIN LOOP =====================
while True:
    print("\n--- Secure Login System ---")
    choice = input("(r)egister | (l)ogin | exit: ").lower()

    if choice == "exit":
        print("Exiting program.")
        break
    elif choice == "r":
        register_user()
    elif choice == "l":
        login_user()
    else:
        print("Invalid option.")
