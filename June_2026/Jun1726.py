# day 164
# holidays
# password cracker
import time
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
password = "a"  # Ensure there are no spaces hidden here

guess = ""
# Added .strip() to both sides to remove any hidden spaces
while guess.strip() != password.strip():
    guess = ""
    for i in range(len(password)):
        guess += random.choice(chars)
    print("\n Trying.....", guess)
    time.sleep(0.1)
print("\nPassword found! It is", guess)
