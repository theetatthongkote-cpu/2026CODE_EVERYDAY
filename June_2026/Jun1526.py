# day 162
# chill day

def letter_count(input):
    count = {}
    for i in input:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


while True:
    user_input = input("Enter a string (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    result = letter_count(user_input)
    print(result)
