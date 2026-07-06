# day 71
# Even and Odd Counter
def Even_Counter(n):
    count = 0

    for i in range(1, n+1):
        if i % 2 == 0:
            count += 1
    return count


def Odd_counter(n):
    count = 0

    for j in range(1, n+1):
        if j % 2 != 0:
            count += 1
    return count


n = int(input("Enter a number to check evens:"))
even_result = Even_Counter(n)
n = int(input("Enter a number to check odds:"))
odd_result = Odd_counter(n)

print("Even numbers:", even_result)
print("odd numbers:", odd_result)
