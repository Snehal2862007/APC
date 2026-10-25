def total_bill(prices, quantities):
    total = 0
    for p, q in zip(prices, quantities):
        total += p * q
    return total * 0.90

print(total_bill([100, 200], [2, 3]))