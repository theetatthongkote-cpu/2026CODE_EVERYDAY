# day 97
# questions on weak spots

# Write a function that removes extra spaces between words:
def clean_text(text):
    data = text.split()
    result = []

    for i in data:
        result.append(i)
    return " ".join(result)

# Find Second Largest Number


def second_largest(lst):
    largest = max(lst)
    lst.remove(largest)
    return max(lst)

# Count how many times each character appears:


def char_count(string):
    string = string
    result = {}
    for i in string:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result
