import re

text = input("enter text: ")

stopwords = {"is", "am", "are", "the", "and", "a", "an", "in", "of", "to"}

words = re.findall(r"\w+|[^\w\s]", text)

result = []

for word in words:
    if word.lower() not in stopwords:
        result.append(word)

cleaned = " ".join(result)
cleaned = re.sub(r"\s+([.,!?;:])", r"\1", cleaned)

print("cleaned text:", cleaned)