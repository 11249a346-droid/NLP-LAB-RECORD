import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ['running', 'runs', 'ran', 'easily', 'fairly', 'studying']
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)