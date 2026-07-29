n = int(input("enter how many numbers: "))
i = 1
largest = int(input("enter number: "))
while i < n:
    num = int(input("enter number: "))
    if num > largest:
        largest = num
    i += 1
print("Largest number =", largest)