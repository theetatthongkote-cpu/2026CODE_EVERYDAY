# day 54
# python depth session 3
import json
import hashlib
import time
import os
import random


class User:
    users_dict = {}
    user_count = 0

    def __init__(self, username, password):
        self.username = username
        self.password, self.salt = User.hash_password_and_salt(password)
        self.is_locked = False
        self.attempts = 0
        User.user_count += 1
        User.users_dict[self.username] = self

    def __str__(self):
        return f"User(username='{self.username}', password='{self.password}')"

    def __repr__(self):
        return self.__str__()

    def load_users(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            for user_data in data:
                user = User(user_data["Username"], user_data["Password"])
                User.users_dict[user_data["Username"]] = user

    def save_users(file_path):
        data = [user.to_dict() for user in User.users_dict.values()]
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def to_dict(self):
        return {
            "Username": self.username,
            "Password": self.password
        }

    @staticmethod
    def hash_password_and_salt(password):
        salt = os.urandom(16)
        salted_password = password.encode() + salt
        return hashlib.sha256(salted_password).hexdigest(), salt


class UserManager:
    users_dict = {}
    user_count = 0

    @staticmethod
    def login(username, password):
        user = User.users_dict.get(username)

        if not isinstance(user, User):
            print("Invalid username or password.")
            return None

        if user.is_locked:
            print("Account is locked.")
            return None

        if user.password == User.hash_password_and_salt(password)[0]:
            user.attempts = 0
            print(f"Welcome, {username}!")
            return user
        else:
            user.attempts += 1
            if user.attempts >= 3:
                user.is_locked = True
                print("Account is locked due to too many failed attempts.")
            else:
                print("Invalid username or password.")
            return None

    def register(username, password):
        if username in User.users_dict:
            print("Username already exists.")
            return None
        else:
            user = User(username, password)
            print(f"User '{username}' registered successfully.")
            return user
