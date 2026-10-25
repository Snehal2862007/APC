import re
from collections import Counter

text = input("enter text: ")

sentences = re.split(r"(?<=[.!?])\s+", text)

words = re.findall(r"\b\w+\b", text.lower())
freq = Counter(words)

scores = []

for sentence in sentences:
    score = sum(freq[w] for w in re.findall(r"\b\w+\b", sentence.lower()))
    scores.append(score)

top = sorted(range(len(sentences)), key=lambda i: scores[i], reverse=True)[:2]

print("summary:")

for i in sorted(top):
    print(sentences[i])