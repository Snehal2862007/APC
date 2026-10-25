import re

text = input("enter text: ")
word = input("enter search word: ")

matches = re.findall(re.escape(word), text, re.IGNORECASE)

result = re.sub(
    re.escape(word),
    lambda m: "**" + m.group() + "**",
    text,
    flags=re.IGNORECASE
) if word else text

print("count:", len(matches) if word else 0)
print("highlighted text:", result)