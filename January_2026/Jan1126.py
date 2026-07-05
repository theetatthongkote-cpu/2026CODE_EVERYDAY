# day 11
# hash

import hashlib


def hash_password(user_password):
    hashed_password = hashlib.sha256(user_password.encode()).hexdigest()
    return hashed_password


user_input = input("Enter your password: ")
hashed = hash_password(user_input)
print(f"The SHA256 hash of your password is: {hashed}")


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
