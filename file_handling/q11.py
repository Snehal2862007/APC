filename = input("enter file name: ")
with open(filename, "r") as file:
    content = file.read()
    words = content.split()
longest_word = ""
for word in words:
    clean_word = "".join(char for char in word if char.isalnum())
    if len(clean_word) > len(longest_word):
        longest_word = clean_word
print("longest word:", longest_word)
print("length:", len(longest_word))
