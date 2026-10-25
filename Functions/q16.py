def second_largest(a):
    b = sorted(set(a))
    return b[-2] if len(b) >= 2 else None

print(second_largest([10, 40, 20, 30]))