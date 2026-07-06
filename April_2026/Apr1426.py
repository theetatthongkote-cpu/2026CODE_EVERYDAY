# day 104
# im back

# (Warm-up) Reverse Words in Sentence
def reverse_words(text):
    data = text.split()
    result = " "
    return result.join(data[::-1])

# Find Third Largest (no max())


def third_largest(lst):
    largest = lst[0]
    for i in lst:
        if i > largest:
            largest = i
        for j in lst:
            if j > largest and j != largest:
                second = j
            for k in lst:
                if k > second and k != second and k != largest:
                    third = k
    return third


def third_largest(lst):
    largest = float('-inf')
    second = float('-inf')
    third = float('-inf')

    for num in lst:
        if num > largest:
            third = second
            second = largest
            largest = num
        elif num > second and num != largest:
            third = second
            second = num
        elif num > third and num != second and num != largest:
            third = num

    return third

# Capitalize First Letter Manually


def capitalize_words(text):
    words = text.split()
    result = [word[0].upper() + word[1:].lower() for word in words]
    return " ".join(result)


# Check Palindrome (ignore spaces)


def palindrome(txt):
    data = txt.replace(" ", "")
    return data == data[::-1]
