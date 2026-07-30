s=input("enter the string:")
a=s.split()
short=a[0]
for i in a:
    if len(i)<len(short):
        short=i
print("short:",short)