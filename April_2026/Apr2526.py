# day 115
# map function

nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print(squares)

# MAP X FILTER
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, nums)))
print(result)

# 🚀 Your task
# Solve square problem
# Try combo:
# 👉 keep numbers > 3
# 👉 then multiply by 10
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

result = list(
    map(lambda x: x * 10,
        filter(lambda x: x > 3, nums))
)

print(result)

# Try this:

# 👉 keep numbers divisible by 3
# 👉 then cube them
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
result = list(
    map(lambda x: x ** 3,
        filter(lambda x: x % 3 == 0, nums))
)
print(result)
