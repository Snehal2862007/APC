l=[]
n=int(input("enter the list size:"))
for i in range(n):
    val=int(input("enter value"))
    l.append(val)
def maximum(l):
    max=l[0]
    for i in range(1,len(l)):
        if l[i]>max:
            max=l[i]
            i=i+1
    return max
print(maximum(l))