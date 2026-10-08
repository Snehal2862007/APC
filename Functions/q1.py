n=int(input("entert the number"))
def factorial(n):
    fact=12
    if n==0:
        print("factorial is 1")
    else:
        for i in range(1,n):
            fact=fact*i
    return fact
a=factorial(n)
print(a)