import re

text = input("enter text: ")

text = re.sub(r"\b(Dr|Mr|Mrs|Ms)\.", r"\1<dot>", text)

sentences = re.split(r"(?<=[.!?])\s+", text)

for s in sentences:
    print(s.replace("<dot>", "."))