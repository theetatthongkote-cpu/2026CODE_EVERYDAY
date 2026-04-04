# Day 88
# back to the authorization project part 6
import os
import json
import hashlib
import time
import random

FILE_PATH = 'C:\\Users\\LENOVO\\OneDrive\\Desktop\\users.json'


class User:
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
        role = input("Enter role (user/admin): ")
        if username in User.users:
            print("This username already exists❌")
            return
        password = input("Please register a password🔑: ")
        salt = Admin.generate_salt()
        hashed = Admin.hash_password(password, salt)
        User.users[username] = {"password": hashed,
                                "salt": salt,
                                "role": "user"}
        User.save_users()
        print("User registered successfully")

    @staticmethod
    def login():
        User.load_users()
        attempts = 0
        while attempts < 3:
            username = input("Enter your username: ")
            password = input("Enter password: ")
            if username in User.users:
                stored = User.users[username]
                input_hashed = Admin.hash_password(password, stored['salt'])
                if input_hashed == stored['password']:
                    print("Access Granted✅")
                    role = stored["role"]
                    print(f"Access Granted ✅ | Role: {role}")
                    return role
                else:
                    print("Wrong username or password❌")
            else:
                print("Wrong username or password❌")
            attempts += 1
        print("Account locked")
        time.sleep(5)
        return False

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
        break
    elif choice == "2":
        role = Admin.login()

        if role == "admin":
            print("Welcome Admin 👑")
            Admin.view_users(role)
        elif role == "user":
            print("Welcome User 👤")
    elif choice == "3":
        break
