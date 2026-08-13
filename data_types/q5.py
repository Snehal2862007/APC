text=input("enter a paragraph: ")
words=text.lower().split()
print("total words:",len(words))
freq={}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print("word frequency:")
for word in freq:
    print(word,":",freq[word])
sorted_words=sorted(freq.items(),key=lambda x:x[1],reverse=True)
print("top 3 most frequent words:")
for word,count in sorted_words[:3]:
    print(word,":",count)
vowels=0
for ch in text.lower():
    if ch in "aeiou":
        vowels+=1
print("total vowels:",vowels)