class BankAccount:
    count = 1000

    def __init__(self, name):
        self.account_holder = name
        self.balance = 0
        BankAccount.count += 1
        self.account_number = BankAccount.count

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def transfer(self, amount, other_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Transferred:", amount)
        else:
            print("Insufficient balance or invalid amount")


a1 = BankAccount("Snehal")
a2 = BankAccount("Riya")

a1.deposit(5000)
a2.deposit(3000)

a1.withdraw(1000)
a1.transfer(2000, a2)

a1.display_balance()
a2.display_balance()