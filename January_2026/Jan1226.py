# day 12
# Real Password Security (Salts & Secure Storage)
import hashlib
import os


users = {}
users_file_path = "secure_users.txt"
attempts = 0
max_attempts = 3


def load_users():
    if not os.path.exists(users_file_path):
        return
    with open(users_file_path, "r") as file:
        for line in file:
            username, salt, hashed_password = line.strip().split(',')
            users[username] = {'salt': salt,
                               'hashed_password': hashed_password}


load_users()


def save_users():
    with open(users_file_path, "w") as file:
        for username, data in users.items():
            file.write(
                f"{username},{data['salt']},{data['hashed_password']}\n")


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


while True:
    action = input(
        "Do you want to register or login? (r/l) or 'exit' to quit: ").lower()
    if action == "exit":
        print("Exiting the program.")
        break
    if action == "r":
        username = input("Enter a username to register: ")
        password = input("Enter a password: ")
        if not strong_password(password):
            print("Password is not strong enough. It must be at least 8 characters long and include uppercase, lowercase, digit, and special character.")
            continue
        register_user(username, password)
        break

    elif action == "l":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if verify_user(username, password):
            print("Login successful!")
            attempts = 0
            break
        else:
            print("Login failed! Incorrect username or password.")
            attempts += 1
            print(f"You have", {max_attempts - attempts}, "attempts left!")
            if attempts >= max_attempts:
                print("Maximum login attempts reached. Exiting.")
                break
