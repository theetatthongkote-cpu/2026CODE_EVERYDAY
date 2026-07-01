# day 160
# restday
# simple function exercise

def has_unique_characters(input):
    data = (input.replace(" ", "")).lower()
    for char in data:
        if data.count(char) > 1:
            return False
    return True


# test cases
while True:
    user_input = input("Enter a string (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    if has_unique_characters(user_input):
        print("The string has all unique characters.")
    else:
        print("The string does not have all unique characters.")
