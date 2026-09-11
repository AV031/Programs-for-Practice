# Assignment 2
# Product Rating using Sentiment Analysis
# NLP - Rule Based Approach

import re

# Catalyst words
catalyst_words = {
    "very", "really", "extremely", "highly", "too"
}

# Positive words
positive_words = {
    "good", "great", "excellent", "durable",
    "easy", "effective", "cost-effective",
    "value", "buy", "best", "use"
}

# Negative words
negative_words = {
    "bad", "poor", "worst", "expensive",
    "waste", "problem", "useless"
}

# Inverse words
inverse_words = {
    "not", "never", "don't", "dont", "no"
}

# Stop words
stop_words = {
    "a", "an", "the", "is", "it", "and",
    "to", "for", "of", "but", "one",
    "this", "that", "be", "on", "in"
}

# User comments
comments = [
    "Don't buy! Bad product.",
    "Good product and cost effective.",
    "Durable and easy to use.",
    "Not value for money.",
    "It is a good buy but one time."
]


def analyze_sentiment(comment):
    # Convert to lowercase
    comment = comment.lower()

    # Tokenization
    tokens = re.findall(r'\b[a-z]+\b', comment)

    score = 0
    invert = False

    for word in tokens:

        # Ignore stop words
        if word in stop_words:
            continue

        # Inverse words
        if word in inverse_words:
            invert = True
            continue

        # Catalyst words
        if word in catalyst_words:
            continue

        # Positive words
        if word in positive_words:
            value = 1

            if invert:
                value = -value

            score += value

        # Negative words
        elif word in negative_words:
            value = -1

            if invert:
                value = -value

            score += value

        invert = False

    # Determine sentiment and rating
    if score > 0:
        sentiment = "Positive"
        rating = 5
    elif score < 0:
        sentiment = "Negative"
        rating = 2
    else:
        sentiment = "Neutral"
        rating = 3

    return score, sentiment, rating


# Product rating
total_rating = 0

print("=" * 60)
print("        PRODUCT RATING USING SENTIMENT ANALYSIS")
print("=" * 60)

for number, comment in enumerate(comments, 1):

    score, sentiment, rating = analyze_sentiment(comment)

    total_rating += rating

    print("\nComment", number, ":", comment)
    print("Sentiment :", sentiment)
    print("Sentiment Score :", score)
    print("Rating :", rating, "/ 5")


# Calculate overall rating
overall_rating = total_rating / len(comments)

print("\n" + "=" * 60)
print("Overall Product Rating :", round(overall_rating, 2), "/ 5")

if overall_rating >= 4:
    print("Overall Opinion : Excellent Product")
elif overall_rating >= 3:
    print("Overall Opinion : Average Product")
else:
    print("Overall Opinion : Poor Product")

print("=" * 60)