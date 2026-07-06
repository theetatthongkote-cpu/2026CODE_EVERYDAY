# day 107
# holidays pt3
# Find First Non-Repeating Character

def non(txt):
    counts = {}
    for char in txt:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
        return counts[char] == 1
    return None


while True:
    user_input = input("Enter a string (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    result = non(user_input)
    if result is not None:
        print(f"The first non-repeating character is: {result}")
    else:
        print("No non-repeating character found.")
