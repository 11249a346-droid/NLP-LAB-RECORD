import spacy
nlp = spacy.load("en_core_web_sm")
text = input("Enter a sentence: ")
doc = nlp(text)
print("\nNamed Entities")
print("_" * 40)
for ent in doc.ents:
    print(f"Entity: {ent.text}")
    print(f"Label: {ent.label_}")
    print("_" * 40)ad