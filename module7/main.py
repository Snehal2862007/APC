import recursive as r
n=int(input("nonnegative number: "))
if n<0: raise ValueError("enter a nonnegative number")
print("factorial:",r.factorial(n))
print("fibonacci series:",[r.fibonacci(i) for i in range(n)])
print("sum of digits:",r.digit_sum(n))
print("binary:",r.binary(n))
