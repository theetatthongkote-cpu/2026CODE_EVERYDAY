# day 55
# sleepy code: 1234


username = {"tigger": 1234, "coconut": 4567, "mango": 8910}

while True:
    login_input = input("What is your user name?:")
    if login_input in username:
        password_input = input("enter your password:")
        if username[login_input] == int(password_input):
            print(f"hello {login_input}")
            break
        else:
            print("incorrect password")
    else:
        print("username not found")
