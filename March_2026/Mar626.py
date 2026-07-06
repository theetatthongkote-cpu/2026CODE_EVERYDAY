# day 65
# Day 65 - March Code

# Topics Learned
# - Expression evaluation logic
# - Running result pattern
# - Operator and number scanning
# - Why languages like C require type declarations
# - Memory layout of arrays in C

# Key Concepts

# Expression Evaluation:
# Instead of solving the whole equation at once, computers process
# expressions step-by-step by scanning operators and applying them
# to a running result.

# Example:
10 - 5 - 2

# Start:
result = 10

# Step 1:
# result = 10 - 5 → 5

# Step 2:
# result = 5 - 2 → 3

# Running Result:
# A variable that continuously stores the current answer as
# operations are applied.

# C vs Python Variables:
# C requires specifying types (int, char, etc.) because memory
# must be allocated in advance.

# Example:
# 3int x = 5;

# Python variables instead reference objects and can change type.

# Example:
x = 5
x = "hello"

# Arrays in C:
# Arrays store elements next to each other in memory.

# Example:
# int numbers[3] = {1,2,3}

# Memory layout:
# [1][2][3]

# This makes arrays very fast to access.
