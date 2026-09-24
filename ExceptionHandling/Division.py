try:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    result = a / b
except ZeroDivisionError:
    print("not divide by zero")
except ValueError:
    print(" invalid numbers")
else:
    print("executed")
    print("result:", result)
finally:
    print("completed")