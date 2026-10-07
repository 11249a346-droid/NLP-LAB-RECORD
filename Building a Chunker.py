import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = input("Enter a sentence: ")
tokens = word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)

grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>+}
    VP: {<VB.*><DT>?<JJ>*<NN.*>+}
"""

chunker = nltk.RegexpParser(grammar)
chunk_tree = chunker.parse(tagged_words)

print("\nPOS tagged sentence:")
print(tagged_words)

print("\nChunk tree:")
print(chunk_tree)

chunk_tree.draw()
