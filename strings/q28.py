text=input("enter a paragraph: ")
words=text.lower().split()
freq={}
for word in words:
    freq[word]=freq.get(word, 0) + 1
print("word Frequencies:")
for word, count in freq.items():
    print(word, ":", count)