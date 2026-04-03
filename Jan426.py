# day 4
# strings
# string methods
# functions
print("Welcome to the password validator!")
password = input("Please enter your password: ")
print("Length of your password is:", len(password))
print("Is your password all uppercase?", password.isupper())
print("Is your password all lowercase?", password.islower())
print("Does your password contain any digits?",
      any(char.isdigit() for char in password))
print("Does your password contain any letters?",
      any(char.isalpha() for char in password))
special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
print("does your password contain any special characters?",
      any(not char in special_characters for char in password))
# or you can use this "any(not char.isalnum() for char in password)" to check for special characters

verification_code = input("Please enter the verification code: ")
has_digit = any(char.isdigit() for char in verification_code)
has_upper = any(char.isupper() for char in verification_code)
has_lower = any(char.islower() for char in verification_code)
has_special = any(not char.isalnum() for char in verification_code)
print("Your code has", has_digit, "digit(s),", has_upper, "uppercase letter(s),",
      has_lower, "lowercase letter(s),", "and", has_special, "special character(s).")

Key = input("Please enter the key: ")
if len(Key) <= 8:
    print("key is too short")
elif len(Key) >= 16:
    print("key is too long")
if not any(char.isdigit() for char in Key):
    print("key must contain at least one digit")
if not any(char.isupper() for char in Key):
    print("please include an uppercase letter in your key")
if not any(not char.isalnum() for char in Key):
    print("please include a special character in your key")
score = 0
if 8 < len(Key) < 16:
    score += 1
if any(char.isdigit() for char in Key):
    score += 1
if any(char.isupper() for char in Key):
    score += 1
if any(not char.isalnum() for char in Key):
    score += 1
print("Your key rating is:", score, "out of 4😀")
if score == 4:
    print("Excellent key!")
elif score == 3:
    print("Good key!")
elif score == 2:
    print("Fair key!")
else:
    print("Weak key, please improve it.")
