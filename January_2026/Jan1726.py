# day 17
# User Management System (Fundamentals Edition)
import os
import hashlib
import time
users = {}
users_file_path = "secure_log.txt"
attempts = 0
max_attempts = 7


def load_users():
    if not os.path.exists(users_file_path):
        return
    with open(users_file_path, "r") as file:
        for line in file:
            username, salt, hashed_password = line.strip().split(',')
            users[username] = {
                "salt": salt,
                "hashed_password": hashed_password
            }


load_users()


def save_users():
    with open(users_file_path, "w") as file:
        for username, data in users.items():
            file.write(
                f"{username},{data["salt"], data["hashed_password"]} \n"
            )


def verify_user(username, password):
    if username not in users:
        print("Your usename has not been verified or your password is wrong!")
        print("Please wait 5 seconds")
        time.sleep(5)
        return False
    salt = users[username]["salt"]
    hashed = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed == users[username]["hashed_password"]


def strong_password(password):
    if (len(password) < 8 or
        not any(c.islower() for c in password) or
        not any(c.isupper() for c in password) or
        not any(c.isdigit() for c in password) or
            not any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password)):
        return False
    return True


def register_user(username, password):
    if username in users:
        print("Username already exists. Please choose a different username.")
        return
    salt = os.urandom(16).hex()  # generate a random salt
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    users[username] = {'salt': salt, 'hashed_password': hashed_password}
    print(f"User {username} registered successfully.")
    save_users()
    print("User data saved to secure_users.txt")


while True:
    user_input = input("would you like to reigister or login(r,l)"
                       "'exit' to cancel:").lower()
    if user_input == "exit":
        print("exiting program.....")
        break
    if user_input == "r":
        username = input("What is your username(or 'exit' to stop):").lower()
        if username == "exit":
            print("exiting program.....")
            break
        password = input("Please register a password:")
        if not strong_password(password):
            print("Password is not strong enough. It must be at least 8 characters long and include uppercase, lowercase, digit, and special character.")
            continue
        register_user(username, password)
        break
    if user_input == "l":
        username = input()
        username = input("What is your username(or 'exit' to stop):").lower()
        if username == "exit":
            print("exiting program.....")
            break

    password = input("what is your password")
    if password not in verify_user:
        print("incorrect password")
        attempts += 1

        continue

    if user_input == "r":
        register_user = input("enter a username:")

    password = input("what is your password:")

# gpt mini rewire
users = {}
users["admin"] = {
    "salt": "abc",
    "hashed_password": "123"
}
