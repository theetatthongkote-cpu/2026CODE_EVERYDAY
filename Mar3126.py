# day 90
# part 8

import os
import json
import hashlib
import time
import random

FILE_PATH = "C:\\Users\\LENOVO\\OneDrive\\Desktop\\users.json"


class User:
    users = {}
    count = 0

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
            except IOError:
                cls.users = {}

    @classmethod
    def save_users(cls):
        with open(FILE_PATH, "w") as f:
            json.dump(cls.users, f, indent=4)


class Admin:
    @staticmethod
    def register():
        User.load_users()
        username = input("Enter new username to register: ")
        if username in User.users:
            print("This username already exists❌")
            return

        while True:
            role = input("Enter role (user/admin): ").lower()
            if role in ["user", "admin"]:
                print(f"Hello {role}")
                break
            else:
                print("Invalid role. Please enter 'user' or 'admin'.")

        password = input("Please register a password🔑: ")
        salt = Admin.generate_salt()
        hashed = Admin.hash_password(password, salt)
        User.users[username] = {"password": hashed,
                                "salt": salt,
                                "role": role,
                                "attempts": 0,
                                "locked_until": 0}
        User.save_users()
        print("User registered successfully")

    @staticmethod
    def login():
        User.load_users()

        while True:
            username = input("Enter your username: ")
            password = input("Enter password: ")
            if username in User.users:
                stored = User.users[username]
                current_time = time.time()
                if current_time < stored["locked_until"]:
                    print("Account is temporarily locked ⏳")
                    return False
                input_hashed = Admin.hash_password(password, stored['salt'])
                if input_hashed == stored['password']:
                    role = stored["role"]
                    print(f"Access Granted ✅ | Role: {role}")
                    stored["attempts"] = 0
                    return role
                else:
                    print("Wrong username or password❌")
                    stored["attempts"] += 1

                if stored["attempts"] >= 3:
                    stored["locked_until"] = time.time() + 30  # 30 seconds
                    stored["attempts"] = 0
                    print("Too many attempts. Account locked 🔒")
            else:
                print("Wrong username or password❌")
                continue
            User.save_users()

    @staticmethod
    def hash_password(password, salt):
        return hashlib.sha256((password + salt).encode()).hexdigest()

    @staticmethod
    def generate_salt():
        return os.urandom(16).hex()

    @staticmethod
    def view_users(role):
        if role == "admin":
            for user in User.users:
                print(user)
        else:
            print("Only admins can view users")


while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        Admin.register()
    elif choice == "2":
        role = Admin.login()

        if role == "admin":
            print("Welcome Admin 👑")
            Admin.view_users(role)
        elif role == "user":
            print("Welcome User 👤")
    elif choice == "3":
        break
