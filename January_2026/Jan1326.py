# day 13
# reviewing days 9, 10, 11, 12
import os
import hashlib
users = {}
user_file_path = "secure_users.txt"
attempts = 0
Max_attempts = 3


def load_users():
    if not os.path.exists(user_file_path):
        return
    with open(user_file_path, "r") as file:
        for line in file:
            username, salt, hashed_password = line.strip().split(',')


def save_users():
    with open(user_file_path, "w") as file:
        for username, data in users.item():
            file.write(
                f"{username},{data["salt"], data["hashed password"]} \n"
            )


def verify_user(username, password):
    if username not in users:
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
