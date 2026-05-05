# day 98
# questions

# Write a function that removes all vowels from a string:
def vowel_del(str):
    data = str.split()
    vowels = "aeiouAEIOU"
    for char in str:
        if char not in vowels:
            result += char

    return result
# Without using min(), find the smallest number:


def smallest(lst):
    smallest = lst[0]

    for num in lst:
        if num < smallest:
            smallest = num

    return smallest

# Group Even and Odd


def evenodd(lst):
    result = {
        "even": [],
        "odd": []
    }

    for i in lst:
        if i % 2 == 0:
            result["even"].append(i)
        else:
            result["odd"].append(i)

    return result
