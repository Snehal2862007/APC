s1 = input("enter first string: ")
s2 = input("enter second string: ")
s1 = s1.lower().replace(" ", "")
s2 = s2.lower().replace(" ", "")
if sorted(s1) == sorted(s2):
    print("anagrams")
else:
    print("not anagrams")