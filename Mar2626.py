# day 85
# building a project pt 5
# adding salts
import os
import json
import hashlib
import time
import random

DATA_FOLDER = "data"
FILE_PATH = os.path.join(DATA_FOLDER, "users.json")


class User:
    count = 0
    users = {}

    @classmethod
    def load_users(cls):
        if not os.path.exists(FILE_PATH):
            cls.users = {}
            return

        with open(FILE_PATH, "r") as f:
            try:
                cls.users = json.load(f)
            except json.JSONDecodeError:
                cls.users = {}
            except FileNotFoundError:
                cls.users = {}

    @classmethod
    def save_users(cls):
        with open(FILE_PATH, "w") as f:
            json.dump(cls.users, f, indent=4)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.users[username] = password


class Admin:

    @staticmethod
    def register():
        User.load_users()
        username = input("Enter new username: ")

        if username in User.users:
            print("Username already exists")
            return

        password = input("Enter new password: ")
        salt = Admin.generate_salt()
        hashed = Admin.hash_password(password, salt)
        User.users[username]["password"] = {
            "password": hashed,
            "salt": salt}
        User.save_users()
        print("User registered successfully")

    @staticmethod
    def login():
        User.load_users()
        attempts = 0

        while attempts < 3:
            username = input("Enter username: ")
            password = input("Enter password: ")
            hashed = Admin.hash_password(password)
            if username in User.users:
                salt = User.users[username]["salt"]
                hashed = Admin.hash_password(password, salt)
                if User.users[username]["password"] == hashed:
                    print("Access granted")
                    return True
            else:
                print("Wrong username or password")
                attempts += 1

        print("Account locked")
        time.sleep(5)
        return False

    @staticmethod
    def hash_password(password, salt):
        return hashlib.sha256((password + salt).encode()).hexdigest

    @staticmethod
    def generate_salt():
        return os.urandom(16).hex()


while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        Admin.register()
    elif choice == "2":
        Admin.login()
    elif choice == "3":
        break
