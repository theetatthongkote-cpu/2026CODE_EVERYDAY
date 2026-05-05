# day 101
# 4 questions

# count letters
def count(text):
    count = 0
    for char in text:
        if char != " ":
            count += 1
    return count

# second smallest


def second(lst):
    smallest = lst[0]

    for num in lst:
        if num < smallest:
            smallest = num

    second = None

    for num in lst:
        if num != smallest:
            if second is None or num < second:
                second = num

    return second

# count digits


def count(text):
    count = 0
    for num in text:
        if num.isdigit():
            count += 1
    return count

# Fix grouping logic properly


def separate(num):
    result = {
        "odd": [],
        "even": []
    }

    for i in num:
        if i % 2 == 0:
            result["even"].append(i)
        else:
            result["odd"].append(i)

    return result
