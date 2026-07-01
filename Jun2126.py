# day 168
# Objective: refresh python fundamentals
# dictionaries
# nested loops


# Challenge: Dictionary Analyzer

def analyze(string_input):
    total_characters = len(string_input)
    unique_characters = set(string_input)
    dict = {}
    for i in range(len(string_input)):
        char = string_input[i]
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return total_characters, unique_characters, dict


while True:
    input_string = input("Enter a string to analyze (or 'exit' to quit): ")
    if input_string.lower() == 'exit':
        break
    total, unique, char_count = analyze(input_string)
    print(f"Total characters: {total}")
    print(f"Unique characters: {', '.join(unique)}")
    print(f"character count: {char_count}")

# nested loops practice


def draw_double_pyramid(height):
    for i in range(1, height + 1):
        # Calculate spacing and stars for each row
        spaces = " " * (height - i)
        stars = "*" * i

        # Combine left half, center gap, and right half
        print(spaces + stars + "  " + stars)


# Run the function with a height of 5
draw_double_pyramid(5)
