import re
html = input("enter html: ")
pattern = r'(?:https?://|www\.)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
urls = re.findall(pattern, html)
print("urls:", urls)