# day 100🔥
# 4 questions

# loop characters, build string
def vowel(text):
    result = ""
    vowels = "aeiouAEIOU"

    for char in text:
        if char not in vowels:
            result += char
    return result
# Largest


def largest(lst):
    largest = lst[0]

    for num in lst:
        if num > largest:
            largest = num
    return largest


def second_smallest(lst):
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
# Second smallest


def Second_smallest(lst):
    smallest = min(lst)
    lst.remove(smallest)
    return min(lst)

# Count digits


def count(text):
    count = 0

    for char in text:
        if char.isdigit():
            count += 1

    return count
