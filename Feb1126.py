# day 42
# static method +


from symtable import Class


class MathTool:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def is_odd(number):
        return number % 2 != 0

    @staticmethod
    def subtract(a, b):
        return a - b


print(MathTool.is_even(8))  # True
print(MathTool.is_even(5))  # False

print(MathTool.is_odd(8))   # False
print(MathTool.is_odd(5))   # T
