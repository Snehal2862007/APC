n = int(input("enter a number: "))
temp = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10
if temp == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")