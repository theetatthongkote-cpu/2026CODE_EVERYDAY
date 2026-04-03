# day 5
# Lists & data handling
passwords = [1234, 6767, 2121]
print("Initial password list:", passwords)
# Adding a new password
for pwd in passwords:
    print("Try password:", pwd)
attempts = []
attempts.append(1234)
attempts.append(0000)
print(len(attempts), "attempts made:", attempts)
# Checking if a password is in the list
code = input("Enter any code you like: ")
if "admin" in code.lower():
    print("This code is weak")
else:
    print("This code is strong")
# Password Attempt Logger 🔐📋
attempts_log = []
max_attempts = 100
correct_password = "letmein"
while True:
    user_input = input("Enter your password(or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        print("Exiting password logger.")
        break
    if user_input in attempts_log:
        print("You have already tried this password.")
        continue
    attempts_log.append(user_input)
    if user_input == correct_password:
        print("Access granted!")
        break
    else:
        print("Access denied!")
print("Total attempts made:", len(attempts_log))
print("Your attempts were:", attempts_log)
# Password Strength Analyzer 📊🔐
common_passwords = ["123456", "password", "letmein", "qwerty", "admin"]
while True:
    user_password = input("Enter to create a password: ")
    if user_password in common_passwords:
        print("This password is too common and weak.")
        continue
    elif len(user_password) < 8:
        print("This password is too short.")
        continue
    else:
        print("This password is strong!")
        break
print("Your password:", "*" * len(user_password))
