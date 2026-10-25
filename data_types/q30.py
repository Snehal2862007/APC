class BankAccount:
    count = 1000

    def __init__(self, name):
        BankAccount.count += 1
        self.account_number = BankAccount.count
        self.account_holder = name
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("invalid amount or insufficient balance")

    def display_balance(self):
        print(self.account_holder, self.account_number, self.balance)

    def transfer(self, amount, other):
        if 0 < amount <= self.balance:
            self.balance -= amount
            other.balance += amount
            print("transfer successful")
        else:
            print("insufficient balance or invalid amount")

a = BankAccount("rahul")
b = BankAccount("snehal")

a.deposit(5000)
b.deposit(2000)

a.withdraw(1000)
a.transfer(1500, b)

a.display_balance()
b.display_balance()