# day 160
# today ill be learning about any() and all() functions in python.
def password_strength(password):
    length = len(password) > 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)
    if all([length, has_upper, has_lower, has_digit, has_special]):
        return "Strong"

    else:
        return "Weak"
