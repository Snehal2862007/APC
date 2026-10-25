from banking.account import create,balance
from banking.transaction import deposit,withdraw
from banking.loan import interest
a=create("amit",1000)
deposit(a,500)
withdraw(a,200)
print("balance:",balance(a),"loan interest:",interest(10000,8,2))
