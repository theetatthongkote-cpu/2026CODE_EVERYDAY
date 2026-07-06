# day 73
# cant code pt#2

def number_square(n):
    for i in range(1, n+1):
        for j in range(n):
            print(i, end="digit")
        print("end")


n = int(input("Enter a number: "))
number_square(n)
