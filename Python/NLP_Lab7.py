import nltk
import pandas as pd

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Take input from user
text = input("Enter a sentence or passage: ")

# Tokenize and perform POS tagging
words = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(words)

# Create lists
nouns = []
verbs = []
adjectives = []
adverbs = []

# Identify parts of speech
for word, tag in pos_tags:
    if tag.startswith("NN"):
        nouns.append(word)
    elif tag.startswith("VB"):
        verbs.append(word)
    elif tag.startswith("JJ"):
        adjectives.append(word)
    elif tag.startswith("RB"):
        adverbs.append(word)

# Display all categories in a table
table = {
    "Nouns": pd.Series(nouns),
    "Verbs": pd.Series(verbs),
    "Adjectives": pd.Series(adjectives),
    "Adverbs": pd.Series(adverbs)
}

df = pd.DataFrame(table)
print("\nParts of Speech Table:")
print(df.fillna("").to_string(index=False))