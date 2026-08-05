import re
email=input("enter email: ")
pattern=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
if re.match(pattern, email):
    print("valid email")
else:
    print("invalid email")