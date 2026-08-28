# Sentiment Analysis using Basic NLP

import re

# Input paragraph
text = """I really enjoyed using this application. The interface is simple,
attractive, and easy to understand. The features work smoothly, and the
response time is excellent. I am very happy with the overall experience and
would definitely recommend this application to my friends. However, a few
features could be improved to make it even better."""

# Convert text to lowercase
text = text.lower()

# Tokenization
words = re.findall(r'\b[a-z]+\b', text)

# Positive and negative words
positive_words = [
    "enjoyed", "simple", "attractive", "easy", "smoothly",
    "excellent", "happy", "good", "better", "recommend"
]

negative_words = [
    "bad", "poor", "worst", "hate", "difficult",
    "slow", "disappointing", "problem", "negative"
]

# Count positive and negative words
positive_count = 0
negative_count = 0

for word in words:
    if word in positive_words:
        positive_count += 1
    elif word in negative_words:
        negative_count += 1

# Display results
print("Positive Words:", positive_count)
print("Negative Words:", negative_count)

# Determine sentiment
if positive_count > negative_count:
    print("Overall Sentiment: Positive")
elif negative_count > positive_count:
    print("Overall Sentiment: Negative")
else:
    print("Overall Sentiment: Neutral")
