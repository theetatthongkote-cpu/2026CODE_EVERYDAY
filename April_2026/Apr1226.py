# day 102
# rest day

def upper(text):
    result = {
        "upper": [],
        "lower": [],
        "others": []
    }

    for i in text:
        if i.upper():
            result["upper"].append(i)
        if i.lower():
            result["lower"].append(i)
        else:
            result["others"].append(i)
    return result


while True:
    text = input("enter:")
    result = upper(text)
    print(result)
