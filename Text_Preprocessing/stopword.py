import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
para = "I am very happy. I am currently pursuing degree in CSE."
words = word_tokenize(para)
stop_words = stopwords.words('english')
output = [word for word in words if word.lower() not in stop_words]
print(output)