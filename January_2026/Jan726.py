# day 7
# Dictionaries (dict)
user = {
    "username": "mango",
    "password": "qwerty123",
}
profile_user = {
    "name": "Bob",
    "age": 18,
    "role": "intern"
}

print(user["name"])
print(user["role"])
user["age"] = 18
user["email"] = "alice@email.com"
if "password" in user:
    print("Password exists")
for key, value in user.items():
    print(key, ":", value)
# task 1
cheat_codes = {
    "god_mode": "1234",
    "all_weapons": "6767",
    "infinite_ammo": "2121"
}
attempt_log = []
while True:
    code = (input("Enter cheat code(or 'cancel'): "))
    if code == "1234":
        print("God mode activated")
        attempt_log.append(code)
        break
    elif code == "6767":
        print("All weapons unlocked")
        attempt_log.append(code)
        break
    elif code == "2121":
        print("infinite ammo enabled")
        attempt_log.append(code)
        break
    elif code == "cancel":
        print("Cheat code entry cancelled")
        break
    else:
        print("Invalid cheat code")
        attempt_log.append(code)
# task 2
passwords = {
    "bottle": "water123",
    "flashlight": "bright456",
    "map": "treasure789"
}
attempts = []
while True:
    username = input("Enter username (or 'exit' to quit): ")
    if username == "exit":
        print("Exiting login system.")
        break
    if username not in passwords:
        print("Invalid username.")
        attempts.append((username, "none", "none"))
    if username in passwords:
        attempts.append((username, "none", "none"))
        password = input("Enter password: ")
        if password == passwords[username]:
            print("Login successful!")
            attempts.append((username, password, "Success"))
            print("welcome", username)
            break
        else:
            print("Incorrect password.")
            attempts.append((username, password, "Failed"))
print(username, "here is your password", "*" * len(password))
feed_back = input("do you wish to see your attempt log? (yes/no): ")
if feed_back.lower() == "yes":
    for attempt in attempts:
        print("Username:", attempt[0], "Password:",
              attempt[1], "Status:", attempt[2])

# task 3 Security upgrades

max_attempts = 3
attempts_count = 0
coded_pass_number = 0
coded_pass_max = 3
coded_pass_attempts = []
login_attempts = []
logins = {
    "admin": "rootaccess2024",
    "user1": "passuser123",
    "coconut": "islandlife456"}
while True:
    user_input_name = input("Enter username (or 'quit' to exit): ")
    if user_input_name == "quit":
        print("Exiting the login system.")
        break
    if user_input_name not in logins:
        print("Username not found. Please try again.")
        login_attempts.append((user_input_name, "Username not found"))
        attempts_count += 1
        if attempts_count >= max_attempts:
            print("Maximum login attempts reached."
                  " Account locked.")
            break
        continue
    if user_input_name in logins:
        coded_pass = input("welcome back " + user_input_name +
                           "Please enter password: ")
        if coded_pass == logins[user_input_name]:
            print('Login successful!')
            login_attempts.append((user_input_name, "Success"))
            break
        else:
            print("Incorrect password.Please try again")

            coded_pass_number += 1
            attempts_count += 1
            if coded_pass_number >= coded_pass_max:
                print("Maximum password attempts reached. Account locked.")
                break
            if coded_pass in coded_pass_attempts:
                print("You have already tried this password. "
                      "Please try a different one.")
                continue
            coded_pass_attempts.append(coded_pass)
    if coded_pass == logins[user_input_name]:
        print("Login successful!")
        print("Masked password:", "*" * len(coded_pass))
        break
