# day 105
# holidays pt1
# remove duplicates from list

def remove(lst):
    data = lst.replace("", " ")
    result = []
    for i in data:
        if i not in result and i != " ":
            result.append(i)
    return result


while True:
    user_input = input("Enter a list of items (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    print(remove(user_input))
