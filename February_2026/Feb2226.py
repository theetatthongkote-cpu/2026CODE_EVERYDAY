# day 53
# python depth session 2
# Failed Login Tracking + Account Lock
import json
import hashlib
import time
import os
import random


class User:
    user_count = 0
    users_dict = {}

    def __init__(self, username, password):
        self.username = username
        self.password = User.hashed_password(password)
        User.user_count += 1
        User.users_dict[self.username] = self
        self.failed_attempts = 0
        self.is_locked = False

    @staticmethod
    def hashed_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password
        }

    @classmethod
    def load_users(cls, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            for user_data in data:
                user = User(user_data["username"], user_data["password"])
                User.users_dict[user.username, user.password] = user

    @classmethod
    def save_users(cls, file_path):
        data = [user.to_dict() for user in User.users_dict.values()]
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def login(cls, username, password):
        user = cls.users_dict.get(username)

        if not user:
            print("Invalid username or password.")
            return None

        if user.is_locked:
            print("Account is locked.")
            return None
        if user.password == cls.hashed_password(password):
            user.failed_attempts = 0
            print(f"Welcome, {username}!")
            return user
        else:
            user.failed_attempts += 1
            print("Invalid username or password.")

            if user.failed_attempts >= 3:
                user.is_locked = True
                # Simulate delay for account lock
                time.sleep(random.uniform(1, 3))
                print("Too many failed attempts. Account locked.")

            return None
