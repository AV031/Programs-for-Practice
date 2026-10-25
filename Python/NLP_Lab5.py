import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

paragraph = """
NLP helps computers understand language.
NLP helps computers process language.
Language helps computers communicate.
"""

print("ORIGINAL PARAGRAPH:")
print(paragraph)

# 1. Sentence Tokenization
sentences = sent_tokenize(paragraph)

print("\n1. Sentence Tokenization:")

for i, sentence in enumerate(sentences, 1):
    print(f"Sentence {i}: {sentence}")


# 2. Word Tokenization
print("\n2. Word Tokenization:")

tokenized_sentences = []

for i, sentence in enumerate(sentences, 1):
    words = word_tokenize(sentence)
    tokenized_sentences.append(words)
    print(f"Sentence {i}: {words}")


# 3. Stop Word Removal
stop_words = set(stopwords.words('english'))

filtered_sentences = []

print("\n3. Stop Word Removal:")

for i, words in enumerate(tokenized_sentences, 1):
    filtered_words = []

    for word in words:
        if word.isalpha() and word.lower() not in stop_words:
            filtered_words.append(word)

    filtered_sentences.append(filtered_words)

    print(f"Sentence {i}: {filtered_words}")


# 4. Vocabulary Generation
vocabulary = sorted(
    set(word for sentence in filtered_sentences for word in sentence)
)

print("\n4. Vocabulary:")
print(vocabulary)

print("Vocabulary size:", len(vocabulary))


# 5. Count of Words Matching Vocabulary
print("\n5. Count of Words Matching Vocabulary:")

for i, sentence in enumerate(filtered_sentences, 1):
    count = sum(1 for word in sentence if word in vocabulary)

    print(f"Sentence {i}: {count} words")


# 6. Document Vectors
print("\n6. Document Vectors:")

document_vectors = []

for sentence in filtered_sentences:

    vector = []

    for word in vocabulary:

        if word in sentence:
            vector.append(sentence.count(word))
        else:
            vector.append(0)

    document_vectors.append(vector)


for i, vector in enumerate(document_vectors, 1):

    print(f"Document/Sentence {i}:")

    print(vector)


# 7. Document Matrix
print("\n7. Document Matrix:")

print("\nVocabulary:")
print(vocabulary)

print("\nDocument Matrix:")

for i, vector in enumerate(document_vectors, 1):

    print(f"D{i}: {vector}")


# Document Matrix Table
print("\nDOCUMENT MATRIX TABLE:")

print("    ", end="")

for word in vocabulary:
    print(f"{word:12}", end="")

print()

for i, vector in enumerate(document_vectors, 1):

    print(f"D{i}: ", end="")

    for value in vector:
        print(f"{value:<12}", end="")

    print()