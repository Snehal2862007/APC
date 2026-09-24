import re
print("enter your details ")
mobile = input("enter 10-digit mobile number: ").strip()
if re.match("^\d{10}$", mobile):
    print("valid mobile number")
else:
    print("invalid mobile number ")


email=input("enter your email")
if re.match("^[a-z0-9._%+-]+@+gmail+.com$",email):
    print("valid email")
else:
    print("invalid")


password = input("enter password: ").strip()
upper = any(char.isupper() for char in password)
lower = any(char.islower() for char in password)
special = any(not char.isalnum() for char in password)
if len(password) >= 8 and upper and lower and special:
    print("striong password")
else:
    print("weak password.")

