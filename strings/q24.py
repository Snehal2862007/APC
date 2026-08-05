text=input("enter the string")
freq={}
for ch in text:
    freq[ch]=freq.get(ch,0)+1
max_char=max(freq,key=freq.get)
print("most frequent:",max_char)
print("frequency:",freq[max_char])