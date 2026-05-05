# day 99

# Keep Only Consonants
def keep_con(text):
    result = ""
    vowels = "aeiouAEIOU"

    for char in text:
        if char not in vowels:
            result += char

    return result

# Find the Largest Number (no max())


def max(lst):
    largest = lst[0]

    for num in lst:
        if num > largest:
            largest = num

    return largest

# Separate Positive and Negative Numbers


def separate(num):
    result = {
        "negative": [],
        "positive": []
    }

    for i in num:
        if i < 0:
            result["negative"].append(i)
        elif i > 0:
            result["positive"].append(i)

    return result
