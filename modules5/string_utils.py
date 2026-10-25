def vowels(s): return sum(c.lower() in "aeiou" for c in s)
def reverse(s): return s[::-1]
def palindrome(s): return s==s[::-1]
def words(s): return len(s.split())
def remove_spaces(s): return s.replace(" ","")
