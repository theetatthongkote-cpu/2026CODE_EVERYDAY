# day 64
# tokenizer upgrade in like 10 mins

def tokenize(expression):

    tokens = []
    number = ""

    for char in expression:

        if char.isdigit():
            number += char

        else:
            tokens.append(number)
            tokens.append(char)
            number = ""

    tokens.append(number)

    return tokens


print(tokenize("10-5-2"))
