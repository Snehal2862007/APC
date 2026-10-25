def binary(n):
    if n < 2:
        return str(n)
    return binary(n // 2) + str(n % 2)

print(binary(10))