# day 95
# questions


# 1 reverse function:
def reverse(str):
    data = str.split()
    return " ".join(data[::-1])

# 2 find missing num:


def find_missing(lst):
    n = len(lst) + 1  # total numbers should be

    for i in range(1, n + 1):
        if i not in lst:
            return i


# 3 check password
def check(password):
    if password.digit and len(password) >= 8:
        return ("strong password!")
    else:
        ("Weak password!")
