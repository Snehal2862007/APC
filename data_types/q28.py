import re
from collections import Counter

text = input("enter text: ").lower()

stopwords = {"is", "the", "a", "an", "and", "of", "to", "in", "for", "are"}

words = re.findall(r"\b[a-z]+\b", text)

words = [w for w in words if w not in stopwords]

freq = Counter(words)

print("top 5 keywords:")

for word, count in freq.most_common(5):
    print(word, count)