def prime(n): return n>1 and all(n%i for i in range(2,int(n**0.5)+1))
def armstrong(n): return n>=0 and sum(int(x)**len(str(n)) for x in str(n))==n
def palindrome(n): return str(n)==str(n)[::-1]
