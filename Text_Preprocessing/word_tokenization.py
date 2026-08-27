import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
word="hi good morning."
nltk_token=nltk.word_tokenize(word)
print("word",nltk_token)