class ageerror(Exception):
    pass
age = int(input("enter your age: "))
try:
    if age < 18:
        raise ageerror("age must be 18 or above")
    print("you are eligible")
except ageerror as e:
    print("exception:", e)