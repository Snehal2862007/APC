def prime(n): return n>1 and all(n%i for i in range(2,int(n**0.5)+1))
def palindrome(n): return str(n)==str(n)[::-1]
def armstrong(n):
    s=str(n)
    return n>=0 and sum(int(x)**len(s) for x in s)==n
def perfect(n): return n>1 and sum(i for i in range(1,n) if n%i==0)==n
