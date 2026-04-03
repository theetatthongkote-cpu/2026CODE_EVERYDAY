# day 3
# loops
# while loop
for i in range(1, 6):
    print("Attempt", i)  # print attempt number
attempt = 1
password = "secret"
while attempt <= 3:
    guess = input("Enter the password: ")
    if guess == password:
        print("Access granted!")
        break
    else:
        print("Access denied!")
    attempt += 1
if attempt == 4:
    print("Too many failed attempts. Access locked.")
