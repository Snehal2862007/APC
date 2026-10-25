words = ["apple", "banana", "python", "cat", "elephant"]

def lengths(words):
    return list(map(lambda x: len(x), words))

def long_words(words):
    return list(filter(lambda x: len(x) > 5, words))

def sort_words(words):
    return sorted(words, key=lambda x: len(x))

print("lengths:", lengths(words))
print("long words:", long_words(words))
print("sorted words:", sort_words(words))