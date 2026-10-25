s = input("enter a string: ")
choice = input("ignore case? (yes/no): ")
if choice == "yes":
    s = s.lower()
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
for ch, count in freq:
    print(ch, ":", count)