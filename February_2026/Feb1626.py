# day 47
# __repr__, eval/type, __add__ methods by myself


# __repr__ method is used to create a string representation of an object that can be used to recreate the object using eval() function.
# It is often used for debugging and development purposes.

class Basketball_player:
    def __init__(self, name, ppg, rpg, apg):
        self.name = name
        self.ppg = ppg
        self.rpg = rpg
        self.apg = apg

    def __repr__(self):
        return f"Basketball_player(name='{self.name}', ppg={self.ppg}, rpg={self.rpg}, apg={self.apg})"


Sam = Basketball_player("Sam", 25.3, 5.2, 6.1)
print(repr(Sam))

# The __add__ method is used to define the behavior of the addition operator (+) for a class.
# It allows you to specify how two objects of the class should be added together.
# For example, if you have a class representing a vector, you can define the __add__ method
# to add the corresponding components of two vectors together and return a new vector object.


class Bank_account:
    def __init__(self, balance, initial_deposit, account_number, account_holder):
        self.balance = balance
        self.initial_deposit = initial_deposit
        self.account_number = account_number
        self.account_holder = account_holder

    def __str__(self):
        return f"Bank_account(balance={self.balance}, initial_deposit={self.initial_deposit}, \n account_number='{self.account_number}', account_holder='{self.account_holder}')"

    def __repr__(self):
        return f"Bank_account(balance={self.balance}, initial_deposit={self.initial_deposit}, \n account_number='{self.account_number}', account_holder='{self.account_holder}')"

    def print_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")
        print(f"Initial Deposit: ${self.initial_deposit}")

    def __add__(self, other):
        if not isinstance(other, Bank_account):
            return NotImplemented
        total_balance = self.balance + other.balance
        return Bank_account(total_balance, 0, "Combined Account", "John Doe & Jane Smith")


account_1 = Bank_account(1000, 500, "123456789", "John Doe")
account_2 = Bank_account(2000, 1500, "987654321", "Jane Smith")


new_account = account_1 + account_2
print(new_account)
