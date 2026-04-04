# day 63
# tokenizer😤

def evaluate(tokens):
    result = int(tokens[0])

    for i in range(1, len(tokens), 2):
        if tokens[i] == "+":
            result += int(tokens[i+1])

        elif tokens[i] == "-":
            result -= int(tokens[i + 1])

    return result


print(evaluate(["10", "-", "5", "-", "2"]))
