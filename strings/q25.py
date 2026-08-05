text=input("enter the string:")
freq={}
for ch in text:
    freq[ch]=freq.get(ch,0)+1
sorted_freq=sorted(freq.items(),key=lambda x: x[1],reverse=True)
if len(sorted_freq)>=2:
    print("secomd frequent:",sorted_freq[1][0])
else:
    print("no second frequent")