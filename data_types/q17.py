import re
text = input("enter text: ")
pattern = r'#\w+'
hashtags = re.findall(pattern, text)
print("hashtags:", hashtags)