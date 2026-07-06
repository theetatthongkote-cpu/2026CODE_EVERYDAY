# ========================================= #day 61
# TOKENIZATION DIAGRAM
# =========================================

# INPUT STRING
"12+3*4-6/2"

# -----------------------------------------
# INITIALIZE
# -----------------------------------------

current_number = ""
tokens = []

# =========================================
# SCAN LEFT → RIGHT
# =========================================

# Read '1'  → digit
current_number = "1"

# Read '2'  → digit
current_number = "12"

# Read '+'  → operator
# Push current_number
tokens = ["12"]

# Push operator
tokens = ["12", "+"]

# Reset current_number
current_number = ""

# -----------------------------------------

# Read '3'  → digit
current_number = "3"

# Read '*'  → operator
# Push "3"
tokens = ["12", "+", "3"]

# Push "*"
tokens = ["12", "+", "3", "*"]

# Reset current_number
current_number = ""

# -----------------------------------------

# Read '4'  → digit
current_number = "4"

# Read '-'  → operator
# Push "4"
tokens = ["12", "+", "3", "*", "4"]

# Push "-"
tokens = ["12", "+", "3", "*", "4", "-"]

# Reset current_number
current_number = ""

# -----------------------------------------

# Read '6'  → digit
current_number = "6"

# Read '/'  → operator
# Push "6"
tokens = ["12", "+", "3", "*", "4", "-", "6"]

# Push "/"
tokens = ["12", "+", "3", "*", "4", "-", "6", "/"]

# Reset current_number
current_number = ""

# -----------------------------------------

# Read '2'  → digit
current_number = "2"

# END OF STRING
# Push final number
tokens = ["12", "+", "3", "*", "4", "-", "6", "/", "2"]

# =========================================
# FINAL OUTPUT
# =========================================

num = ["12", "+", "3", "*", "4", "-", "6", "/", "2"]
# Join the list into "12 + 3 * 4 - 6 / 2"
f = eval(" ".join(num))
print(f)

expression = "12+3*4-6/2"
result = eval(expression)
print(result)
