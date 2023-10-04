import spacy

nlp = spacy.load("en_core_web_sm")

sentence = "The quick brown fox jumps over the lazy dog."

doc = nlp(sentence)

print("Token\t\tPOS\tDependency")

for token in doc:
    print(f"{token.text}\t\t{token.pos_}\t{token.dep_}")