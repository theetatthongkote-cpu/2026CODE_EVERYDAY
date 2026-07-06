# day 106
# holidays pt2
# Count Words Frequency

def counter(str):
    words = str.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


while True:
    user_input = input("Enter a sentence (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    print(counter(user_input))
