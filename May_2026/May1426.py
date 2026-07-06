# day 133
# basics of python to prevent burnout
try:
    temperature = int(input("What is the temperature? "))
    if temperature > 30:
        print("It's hot outside🔥")
    elif 20 <= temperature <= 30:
        print("It's nice outside 🌞")
    else:
        print("It's cold outside ❄️")
except ValueError:
    print("Please enter a valid integer😒")
