# day 165
# at grandma's house
import calendar

while True:
    y = input("Enter year (or 'exit' to quit): ")
    if y.lower() == 'exit':
        break
    m = input("Enter month (1-12): ")
    if m.lower() == 'exit':
        break
    try:
        year = int(y)
        month = int(m)
        if 1 <= month <= 12:
            print(calendar.month(year, month))
        else:
            print("Invalid month. Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter numeric values for year and month.")
