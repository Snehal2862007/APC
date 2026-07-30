a= input("Enter a sentence: ")
b= a.split()
longest = ""
for i in b:
    if len(i) > len(longest):
        longest = i
print("longest:", longest)