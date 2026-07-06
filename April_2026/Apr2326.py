# day 113
# lambda + sorted
# normal function
def multiply(x, y):
    return x * y

# LAMBDA


def q(x, y): return x * y


# practice
data = [("John", 25), ("Alice", 20), ("Bob", 30)]
result = sorted(data, key=lambda x: x[1])
print(result)
