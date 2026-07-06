# day 109
# chill late night.

class BankAccount:

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        print(f"Account created for {self.name} with balance {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive")
        else:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn.")

    def display(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: ${self.balance:.2f}")

    def transfer(self, other_account, amount):
        if self.withdraw(amount):
            other_account.deposit(amount)
            print(
                f"Successfully transferred ${amount:.2f} from {self.name} to {other_account.name}."
            )
