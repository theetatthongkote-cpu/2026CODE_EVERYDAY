# day 112
# class + init + static

class Calculator:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")

    @staticmethod
    def multiply(a, b):
        return a*b
