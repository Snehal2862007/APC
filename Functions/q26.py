def units_charge(u):
    if u <= 100:
        return u * 5
    elif u <= 200:
        return 500 + (u - 100) * 7
    return 1200 + (u - 200) * 10

def bill(u):
    amount = units_charge(u) + 50
    tax = amount * 0.05
    discount = amount * 0.10 if u <= 100 else 0
    return amount + tax - discount

print(bill(150))