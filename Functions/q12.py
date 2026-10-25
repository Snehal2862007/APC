def palindrome(s):
    s = str(s)
    return s == s[::-1]

print(palindrome("madam"))