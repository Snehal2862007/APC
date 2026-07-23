num = int(input("Enter a number: "))
root = int(num ** 0.5)
factor = 0
for i in range(1, root + 1):
    if root % i == 0:
        factor += 1
if factor == 2:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")