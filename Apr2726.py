# day 117
# Mini Project — “Smart Username Cleaner”
# 🚀 Your Tasks (pipeline style)
# 1️⃣ Clean spaces

# 👉 remove leading/trailing spaces

# 2️⃣ Keep only valid usernames

# 👉 rules:

# length ≥ 5
# only letters + numbers (no _)
# 3️⃣ Format

# 👉 make everything lowercase

# 4️⃣ Sort

# 👉 by length (short → long)

usernames = ["  alice123 ", "BOB", "charlie__", "da", "eve_99", "  franklin  "]

result = list(
    sorted(
        map(lambda x: x.lower(),
            filter(lambda x: len(x) >= 5 and x.isalnum(),
                   map(lambda x: x.strip(), usernames)
                   )
            ),
        key=lambda x: len(x)
    )
)

print(result)
