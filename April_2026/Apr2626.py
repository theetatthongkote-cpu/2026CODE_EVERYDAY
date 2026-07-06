# day 116
# chiiling and lambda
data = ["apple", "banana", "kiwi", "grape", "watermelon"]
result = list(
    sorted(
        map(lambda x: x.upper(),
            filter(lambda x: len(x) > 5, data)
            ),
        key=lambda x: len(x)
    )
)
print(result)
