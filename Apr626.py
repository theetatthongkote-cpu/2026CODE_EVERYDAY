# day 96
# questions


# Write a function that capitalizes the first letter of every word:
def capitalize(text):
    words = text.split()
    result = []

    for word in words:
        result.append(word.capitalize())

    return " ".join(result)
# for fun
# str:"HELLO WORLD THIS IS DAY 96"


def lower(txt):
    info = txt.split()
    lst = []
    for i in info:
        lst.append(i.lower())
    return " ".join(lst)


t = input("enter")
r = lower(t)
print(r)


# Write a function that removes duplicates from a list without changing order:
lst = [1, 2, 2, 3, 1]


def organize(lst):
    organized_list = []
    for i in lst:
        if i not in organized_list:
            organized_list.append(i)
    return organized_list


r = organize(lst)
print(r)

# Write a function that counts how many times each word appears:


def count_words(str):
    words = str.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
