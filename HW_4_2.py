# Part C - Q2

import spacy

nlp = spacy.load("en_core_web_sm")

text = "Chris met Alex at Apple headquarters in California. He told him about the new iPhone launch."

doc = nlp(text)

# 1. Named Entity Recognition
print("Named Entities:")
for ent in doc.ents:
    print(f"{ent.text} -> {ent.label_}")

# 2. Pronoun ambiguity check
pronouns = {"he", "she", "they", "him", "her", "them"}
found_pronoun = any(token.text.lower() in pronouns for token in doc)

if found_pronoun:
    print("Warning: Possible pronoun ambiguity detected!")
