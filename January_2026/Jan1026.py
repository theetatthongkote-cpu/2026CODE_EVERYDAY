# day 10
# LOGIN ATTEMPT LOGGING (REAL SECURITY LOGS)
def log_login_attempt(username, status):
    with open("login_attempts.log", "a") as log_file:
        log_file.write(f"User: {username}, Status: {status}\n")


Password_database = {
    "admin": "securepassword",
    "user1": "mypassword",
    "user2": "anotherpassword"
}
attempts = 0
MAX_ATTEMPTS = 3
while True:
    user = input("Enter username (or type 'exit' to quit): ")
    if user.lower() == 'exit':
        break
    if user not in Password_database:
        print("Username not found. Try again.")
        log_login_attempt(user, "FAILURE")
        attempts += 1
        if attempts >= MAX_ATTEMPTS:
            print("Maximum login attempts reached. Exiting.")
            break
        continue
    password = input("Enter password: ")
    if user in Password_database and Password_database[user] == password:
        print("Login successful!")
        log_login_attempt(user, "SUCCESS")
        attempts = 0  # reset attempts after successful login
        break
    else:
        print("Login failed!")
        log_login_attempt(user, "FAILURE")
        attempts += 1
        if attempts >= MAX_ATTEMPTS:
            print("Maximum login attempts reached. Exiting.")
            break
with open("login_attempts.log", "r") as log_file:
    print("Login Attempts Log:")
    print(log_file.read())
