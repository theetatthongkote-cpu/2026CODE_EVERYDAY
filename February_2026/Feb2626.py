# day 57
# sleepy calculator: 1234 pt 2 in cpis camp

class SleepyCalculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero."


def main():
    calculator = SleepyCalculator()
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
                result = calculator.add(num1, num2)
                print(f"The result of {num1} + {num2} is: {result}")
            elif operation == "subtract":
                result = calculator.subtract(num1, num2)
                print(f"The result of {num1} - {num2} is: {result}")
            elif operation == "multiply":
                result = calculator.multiply(num1, num2)
                print(f"The result of {num1} * {num2} is: {result}")
            elif operation == "divide":
                result = calculator.divide(num1, num2)
                print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Invalid operation. Please try again.")
