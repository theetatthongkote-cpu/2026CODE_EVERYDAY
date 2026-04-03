# day 8
# functions - login system with checks


def username_exists(username, logins):
    return username in logins


def if_duplicate_attempt(password, used_passwords):
    return password in used_passwords


def correct_password(username, password, logins):
    return logins.get(username) == password


def mask_password(password):
    return '*' * len(password)


logins = {
    "admin": "rootaccess2024",
    "user1": "passuser123",
    "coconut": "islandlife456"
}

MAX_ATTEMPTS = 3
attempts = 0
used_passwords = []

while True:
    username = input("Enter username (or 'quit'): ")
    if username == "quit":
        print("Exiting system.")
        break

    if not username_exists(username, logins):
        print("Username not found.")
        attempts += 1
        if attempts >= MAX_ATTEMPTS:
            print("Account locked.")
            break
        continue

    password = input("Enter password: ")

    if if_duplicate_attempt(password, used_passwords):
        print("Password already tried.")
        continue

    used_passwords.append(password)

    if correct_password(username, password, logins):
        print("Login successful!")
        print("Masked password:", mask_password(password))
        break
    else:
        print("Incorrect password.")
        attempts += 1
        if attempts >= MAX_ATTEMPTS:
            print("Account locked.")
            break
