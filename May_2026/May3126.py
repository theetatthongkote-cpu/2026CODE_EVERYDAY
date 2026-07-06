# day 148
# cs50 scratch
# paswword cracker
# brute force attack
import time
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password = input("Enter password: ")
print("\nAcccessing database...\n")

guess = ""
while guess != password:
    guess = ""
    for i in range(len(password)):
        guess += random.choice(chars)
    print("\n Trying.....", guess)
    time.sleep(0.1)
print("\nPassword found! It is", guess)
