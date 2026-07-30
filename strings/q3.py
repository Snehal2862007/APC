name=input("enter the string:")
length=0
for char in name:
    length+=1
i=length-1
while i>=0:
    print(name[i],end="")
    i-=1