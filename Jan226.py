# day2
# conditions
# if, elif, else
age = int(input("How old are you?:"))
if age >= 18:
    print("You are an adult!", "You can vote!")
elif age == 17:
    print("You are almost an adult!", "You can vote next year!")
else:
    print("You are a minor!", "You cannot vote yet!")
password = input("Enter the password:")
if (len(password) > 8) and ("#" in password):
    print("Strong password")
elif (len(password) < 8) and ("#" in password):
    print("Medium strength password")
else:
    print("okay password")
