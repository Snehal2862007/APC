n = int(input("enter how many numbers: "))
i = 1
smallest = int(input("enter number: "))
while i < n:
    num = int(input("enter number: "))
    if num < smallest:
        smallest = num
    i += 1
print("Smallest number =", smallest)