import re
def valid_email(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$'
    return re.match(pattern, email) is not None
email = input("enter email: ")
if valid_email(email):
    print("valid email")
else:
    print("invalid email")