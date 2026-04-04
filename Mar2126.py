# day 80
# building a project pt 2
import os
import json
import hashlib
import time
import random


class User:
    count = 0
    users = {}

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.users[username] = password


class Admin:

    @staticmethod
    def register():
        username = input("Enter new username: ")

        if username in User.users:
            print("Username already exists")
            return

        password = input("Enter new password: ")

        User(username, password)
        print("User registered successfully")

    @staticmethod
    def login():
        attempts = 0

        while attempts < 3:
            username = input("Enter username: ")
            password = input("Enter password: ")

            if username in User.users and User.users[username] == password:
                print("Access granted")
                return True
            else:
                print("Wrong username or password")
                attempts += 1

        print("Account locked")
        time.sleep(5)
        return False


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
