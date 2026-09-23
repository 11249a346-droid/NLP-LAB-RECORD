import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = input("Enter the sentence: ")

words = word_tokenize(sentence)
pos_tagged = nltk.pos_tag(words)

print("\nPOS Tagged Output:")
print(pos_tagged)

print("\n{:<15}{}".format("Word", "POS Tag"))
print("-" * 25)

for word, tag in pos_tagged:
    print("{:<15}{}".format(word, tag))