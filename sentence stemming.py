import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
sentence = "The quick brown fox jumps over the lazy dog"
words = word_tokenize(sentence)
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)
for w in words:
    print(f"{w} --> {stemmer.stem(w)}")