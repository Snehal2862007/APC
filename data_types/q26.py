import re

text = input("enter text: ").lower()

text = text.replace("don't", "do not")
text = text.replace("can't", "cannot")
text = text.replace("won't", "will not")
text = text.replace("i'm", "i am")
text = text.replace("it's", "it is")

text = re.sub(r"[^a-z\s]", "", text)
text = " ".join(text.split())

print("cleaned text:", text)