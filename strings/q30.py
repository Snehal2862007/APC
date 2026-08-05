s1=input("enter first string: ")
s2=input("enter second string: ")
if len(s1)==len(s2) and s2 in (s1 + s1):
    print("yes")
else:
    print("no")