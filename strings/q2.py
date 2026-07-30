a=input("enter the string:")
vowels=0
consonents=0
digits=0
spaces=0
special_characters=0
for char in a:
    if char=="a" or char=="e" or char=="i" or char=="o" or char=="u" or char=="A" or char=="E" or char=="I" or char=="O" or char=="U":
        vowels+=1
    elif char.isdigit():
        digits+=1
    elif char.isspace():
        spaces+=1
    elif  char.isalpha():
        consonents+=1
    else:
        special_characters+=1

print("vowels:",vowels)
print("consonents:",consonents)
print("digits",digits)
print("spaces:",spaces)
print("special_characters:",special_characters)