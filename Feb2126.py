# day 52
# python depth session 1
# lists vs dicts
# lists are ordered, dicts are not
# lists are indexed by position, dicts are indexed by keys
# lists are mutable, dicts are mutable
# lists are created with [], dicts are created with {}
import json
import os
import random
import time
import hashlib


class User:

    users_dict = {}  # Class variable to store all user instances in a dictionary
    users_count = 0  # Class variable to track the number of users

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def __init__(self, username, password, role='user', is_hashed=False):
        self.username = username
        if is_hashed:
            self.password = password
        else:
            self.password = User.hash_password(password)

            self.role = role

            User.users_dict[self.username] = self
            User.users_count += 1

    @classmethod
    def load_users(cls, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            for user_data in data:
                user = User(user_data['username'], user_data['password'], role=user_data.get(
                    'role', 'user'), is_hashed=True)
                return user

    @classmethod
    def save_users(cls, file_path):
        data = [user.to_dict() for user in cls.users_dict.values()]
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password
        }

    def login(cls, username, password):
        user = cls.users_dict.get(username)
        if user and user.password == cls.hash_password(password):
            print(f"Welcome, {username}!")
            return True
        else:
            print("Invalid username or password.")
            return False


while True:
    print("Welcome to the User Management System!")
    print("1. Create a new user")
    print("2. Save users to file")
    print("3. Load users from file")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = User(username, password)
        print(f"User '{username}' created successfully!")

    elif choice == '2':
        file_path = input("Enter file path to save users: ")
        User.save_users(file_path)
        print(f"Users saved to '{file_path}' successfully!")

    elif choice == '3':
        file_path = input("Enter file path to load users: ")
        User.load_users(file_path)
        print(f"Users loaded from '{file_path}' successfully!")

    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
