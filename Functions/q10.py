def vowels(s):
    count = 0
    for i in s.lower():
        if i in "aeiou":
            count += 1
    return count

print(vowels("education"))