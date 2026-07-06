# day 122
height = 4

for i in range(height):
    print("*"*(i+1))
height = 4

for i in range(height):
    print(" " * (height - i - 1) + "#" * (i + 1))
