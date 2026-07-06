# day 108
# holidays pt4
# Move Zeros to End

def move_zeros(lst):
    non_zeroes = [num for num in lst if num != 0]
    zeroes = [num for num in lst if num == 0]
    return non_zeroes + zeroes


while True:
    user_input = input("Enter a list of numbers (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    try:
        numbers = list(map(int, user_input.split()))
        print(move_zeros(numbers))
    except ValueError:
        print("Please enter a valid list of numbers.")
