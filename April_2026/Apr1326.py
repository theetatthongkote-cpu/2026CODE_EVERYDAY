# day 103
# full restday


def longest(text):
    data = text.split()
    longest = data[0]

    for i in data:
        if len(i) >= len(longest):
            longest = i
    return longest


while True:
    n = input("enter")
    result = longest(n)
    print(result)
