import re

text = input("enter text: ")

pattern = r'\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}'

numbers = re.findall(pattern, text)

print("phone numbers:", numbers)