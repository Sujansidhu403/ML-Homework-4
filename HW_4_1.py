import spacy
from spacy.lang.en.stop_words import STOP_WORDS

nlp = spacy.load("en_core_web_sm")

text = "John enjoys playing football while Mary loves reading books in the library."

doc = nlp(text)

filtered_tokens = []

for token in doc:
    if token.is_stop or token.is_punct:
        continue
    if token.pos_ in ["NOUN", "VERB"]:
        filtered_tokens.append(token.lemma_)

print("Final tokens (nouns & verbs, lemmatized, no stopwords):")
print(filtered_tokens)
