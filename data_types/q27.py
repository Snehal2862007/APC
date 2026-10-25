import re

text = input("enter word or sentence: ")

text = re.sub(r"[^a-z0-9]", "", text.lower())

if text == text[::-1]:
    print("True - palindrome")
else:
    print("False - not palindrome")