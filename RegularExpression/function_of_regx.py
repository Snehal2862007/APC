import re
text = "cats are smart. i love 43 cats."
if re.search("smart", text):
    print("found 'smart'!")

if re.match("smart", text):
    print("texxt starts with smart")
else:
    print("does not start with smart")

numbers = re.findall(r"\d+", text)
print(numbers)

words = re.split(r"\s+", text)
print(words)

new_text = re.sub(r"cats", "dogs", text)
print(new_text)
