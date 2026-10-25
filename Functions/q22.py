def details(a):
    return min(a), max(a), sum(a), sum(a) / len(a)

print(details([10, 20, 30, 40]))