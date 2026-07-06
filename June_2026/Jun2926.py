# day 175
# random
# https://www.youtube.com/watch?v=HDVl8-cy928


def a_square(nums: str) -> str | None:
    data = nums.split()
    if len(data) != 4:
        return "no"
    if len(set(data)) == 1:
        return "yes"
    else:
        return "no"


print(a_square("4 4 4 4"))  # Output: yes
print(a_square("4 5 4 4"))  # Output: no
print(a_square("5 5 5"))    # Output: no
