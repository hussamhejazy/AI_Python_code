#pip install spacy

#python -m spacy download en_core_web_sm


import spacy

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in April 1976. " \
       "It is headquartered in Cupertino, California."

# Process the text with spaCy
doc = nlp(text)

# Extract named entities and their labels
print("Named Entities:")
for entity in doc.ents:
    print(f"{entity.text} ({entity.label_})")
