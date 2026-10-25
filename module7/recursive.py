def factorial(n): return 1 if n<=1 else n*factorial(n-1)
def fibonacci(n): return n if n<=1 else fibonacci(n-1)+fibonacci(n-2)
def digit_sum(n): return n if n<10 else n%10+digit_sum(n//10)
def binary(n): return str(n) if n<2 else binary(n//2)+str(n%2)
