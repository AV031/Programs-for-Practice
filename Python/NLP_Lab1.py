# NLP Assignment 4
#Paragraph Tokenization, Word Tokenization, Stop Word Removal and Sentiment Analysis

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Given paragraph
paragraph = """Nepal was hit by a devastating flood.
Over 1000 persons are assumed dead.
Different countries are providing medical support."""

# 1. Sentence Tokenization
sentences = sent_tokenize(paragraph)

print("1. Sentence Tokenization:")
for sentence in sentences:
    print(sentence)

# 2. Word Tokenization
words = word_tokenize(paragraph)

print("\n2. Word Tokenization:")
print(words)

# 3. Stop Word Removal
stop_words = set(stopwords.words('english'))

filtered_words = []

for word in words:
    if word.lower() not in stop_words and word.isalnum():
        filtered_words.append(word)

print("\n3. After Stop Word Removal:")
print(filtered_words)

# 4. Sentiment Analysis
sia = SentimentIntensityAnalyzer()

sentiment_score = sia.polarity_scores(paragraph)

print("\n4. Sentiment Score:")
print(sentiment_score)

# Determine sentiment
compound_score = sentiment_score['compound']

if compound_score >= 0.05:
    print("Overall Sentiment: Positive")
elif compound_score <= -0.05:
    print("Overall Sentiment: Negative")
else:
    print("Overall Sentiment: Neutral")