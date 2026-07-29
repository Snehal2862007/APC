n = int(input("enter the number of terms: "))
i= 0
j= 1
count = 0
while count < n:
    print(i,end=" ")
    k=i+j
    i=j
    j =k
    count += 1