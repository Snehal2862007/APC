def deposit(account,amount):
    if amount>0: account["balance"]+=amount
def withdraw(account,amount):
    if 0<amount<=account["balance"]: account["balance"]-=amount
    else: print("invalid amount")
