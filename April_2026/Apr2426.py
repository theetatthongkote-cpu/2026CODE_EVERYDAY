# day 114
# lambda + filter

# normal function
def is_even(n):
    return n % 2 == 0


# LAMBDA
nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)

# Try:
# 👉 keep numbers greater than 3
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
result = list(filter(lambda x: x > 3, nums))
print(result)
