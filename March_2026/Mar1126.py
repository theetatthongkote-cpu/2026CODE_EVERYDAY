# day 70
# Number Square

def number_square(n):
    for i in range(1, n+1):
        for j in range(n):
            print(i, end="")
        print()


n = int(input("Enter a number: "))
number_square(n)
