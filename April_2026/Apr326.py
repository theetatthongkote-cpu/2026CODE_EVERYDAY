# day 93
# python reset + api basics
import time
import requests
import json

username = "coconut"
password = "vitacoco"
attempts = 0
while True:

    user_input = input("What is your username?\n")
    pass_input = input("What is your password\n")
    if user_input == username and pass_input == password:
        print("Access Granted✅")
        break
    else:
        print("Incorrect username or password❌")
        attempts += 1

    if attempts >= 3:
        print("Account locked🔒")
        time.sleep(10)
        break

response = requests.get("https://api.github.com")
print(response.status_code)
data = response.json
print(data)
res = requests.get("https://official-joke-api.appspot.com/random_joke")
data = res.json()

print(data["setup"])
print(data["punchline"])
print(data["setup"], ["punchline"])
