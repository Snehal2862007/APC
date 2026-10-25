import csv
rows = [["deposit", 5000], ["withdrawal", 1200], ["deposit", 800], ["withdrawal", 300]]
with open("transactions.csv", "w", newline="") as f:
    csv.writer(f).writerows(rows)
with open("transactions.csv", newline="") as f:
    transactions = [(kind, float(amount)) for kind, amount in csv.reader(f)]
deposits = sum(amount for kind, amount in transactions if kind == "deposit")
withdrawals = sum(amount for kind, amount in transactions if kind == "withdrawal")
print("deposits:", deposits)
print("withdrawals:", withdrawals)
print("balance:", deposits - withdrawals)
print("largest:", max(transactions, key=lambda x: x[1]))
