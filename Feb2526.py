# day 56
# sleepy calculator: 1234

def calculator():
    while True:
        operation = input(
            "What operation do you want to perform? (add, subtract, multiply, divide) or 'exit' to quit: ")
        if operation == "exit":
            print("Goodbye!")
            break
        elif operation in ["add", "subtract", "multiply", "divide"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if operation == "add":
                result = num1 + num2
                print(f"The result of {num1} + {num2} is: {result}")
            elif operation == "subtract":
                result = num1 - num2
                print(f"The result of {num1} - {num2} is: {result}")
            elif operation == "multiply":
                result = num1 * num2
                print(f"The result of {num1} * {num2} is: {result}")
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is: {result}")
                else:
                    print("Error: Cannot divide by zero.")
        else:
            print("Invalid operation. Please try again.")


calculator()
