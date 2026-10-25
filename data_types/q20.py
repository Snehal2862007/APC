import string

with open("sample.txt", "r") as f:
    text = f.read().lower()

text = text.translate(str.maketrans("", "", string.punctuation))
words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("total words:", len(words))
print("top 10 words:")

for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(word, count)