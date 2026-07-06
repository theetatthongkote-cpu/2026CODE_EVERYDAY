# day 110
# classes again?


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


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance):
        new_account = BankAccount(name, balance)
        self.accounts[name] = new_account

    def get_account(self, name):
        return self.accounts.get(name)

    def transfer(self, from_user, to_user, amount):
        sender = self.get_account(from_user)
        receiver = self.get_account(to_user)

        if sender is None or receiver is None:
            print("Account not found")
            return

        sender.transfer(receiver, amount)
