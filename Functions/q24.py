balance = 1000
history = []

def deposit(amount):
    global balance
    if amount <= 0:
        return "invalid amount"
    balance += amount
    history.append(("deposit", amount))
    return balance

def withdraw(amount):
    global balance
    if amount <= 0:
        return "invalid amount"
    if amount > balance:
        return "insufficient balance"
    balance -= amount
    history.append(("withdraw", amount))
    return balance

def enquiry():
    return balance

def transactions():
    return history

print(deposit(500))
print(withdraw(300))
print(enquiry())
print(transactions())