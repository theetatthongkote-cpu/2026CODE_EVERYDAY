# day 94
# 3 questions

# Write a function that takes a string and returns the number of vowels.
def num_vowels(text):
    return len(text)


# Write a function that takes a list and returns the most frequent element.
def find_common(lst):
    counts = {}
    for num in lst:
        if num in lst:
            counts[num] += 1
        else:
            counts[num] = 1
    max_count = 0
    result = None
    for max in counts:
        if counts[max] > max_count:
            max_count = counts[max]
            result = max
    return result


# create a Simple Login System
users = {
    "admin": "1234",
    "user1": "pass",
    "guest": "guest"
}

attemmpts = 0


def login(username, password):

    if attempts >= 3:
        return ("locked")

    if username not in users:
        attempts += 1
        return "User not found"

    if users[username] == password:
        return "Access granted"
    else:
        attempts += 1
        return "Wrong password"
