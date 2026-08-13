import re

def check_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_-]).{8,}$'
    return re.match(pattern, password) is not None

password = input("enter password: ")

if check_password(password):
    print("strong password")
else:
    print("weak password")