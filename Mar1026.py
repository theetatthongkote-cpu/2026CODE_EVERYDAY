# day 69
# rest day

def brick(n):
    for i in range(n):
        for j in range(n):
            print("#", end="")
        print()   # ← move to next row


n = int(input("Enter a number: "))
brick(n)
