# day 15
# weak system brute-forced attacked
import hashlib
import os
password_variable = "ILOVEPIZZA"
hash_password = hashlib.sha256((password_variable).encode()).hexdigest()
salt = os.urandom(16).hex()
hashedandsalted = hashlib.sha256(
    (password_variable + salt).encode()).hexdigest()
common_passwords = ["123456", "123456789", "password", "qwerty", "ILOVEPIZZA"]
for guess in common_passwords:
    print("trying:", guess)
    if guess == password_variable:
        print("Unlocked")
