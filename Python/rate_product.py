# NLP Based Product Rating System
# Assignment - 2

import re

# ---------------------------------------------------
# Step 1: User Comments
# ---------------------------------------------------

comments = [
    "Don't buy! Bad product",
    "Good product and cost effective",
    "Durable and easy to use",
    "Not value for money",
    "It's a good buy but one time"
]

# ---------------------------------------------------
# Step 2: Sentiment Words
# ---------------------------------------------------

positive_words = {
    "good": 1,
    "great": 2,
    "excellent": 3,
    "best": 3,
    "durable": 2,
    "easy": 1,
    "effective": 1,
    "cost": 0,
    "buy": 1,
    "value": 1,
    "use": 1
}

negative_words = {
    "bad": 3,
    "worst": 4,
    "poor": 3,
    "don't": 3,
    "not": 2,
    "expensive": 2,
    "waste": 3,
    "useless": 4
}


# ---------------------------------------------------
# Step 3: Text Preprocessing
# ---------------------------------------------------

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s']", "", text)
    words = text.split()
    return words


# ---------------------------------------------------
# Step 4: Calculate Sentiment
# ---------------------------------------------------

def calculate_rating(comment):

    words = preprocess(comment)

    positive_score = 0
    negative_score = 0

    for word in words:

        if word in positive_words:
            positive_score += positive_words[word]

        if word in negative_words:
            negative_score += negative_words[word]

    # Handle "not" before a positive word
    if "not" in words:

        not_index = words.index("not")

        if not_index + 1 < len(words):
            next_word = words[not_index + 1]

            if next_word in positive_words:
                negative_score += positive_words[next_word]
                positive_score -= positive_words[next_word]

    # Handle "don't"
    if "don't" in words:
        negative_score += 2

    # Determine rating
    sentiment_score = positive_score - negative_score

    if sentiment_score >= 4:
        rating = 5
        sentiment = "Very Positive"

    elif sentiment_score >= 2:
        rating = 4
        sentiment = "Positive"

    elif sentiment_score >= 0:
        rating = 3
        sentiment = "Neutral"

    elif sentiment_score >= -2:
        rating = 2
        sentiment = "Negative"

    else:
        rating = 1
        sentiment = "Very Negative"

    return rating, sentiment


# ---------------------------------------------------
# Step 5: Analyze All Comments
# ---------------------------------------------------

total_rating = 0

print("=" * 60)
print("          NLP BASED PRODUCT RATING SYSTEM")
print("=" * 60)

for i, comment in enumerate(comments, start=1):

    rating, sentiment = calculate_rating(comment)

    total_rating += rating

    print("\nComment", i, ":", comment)
    print("Sentiment :", sentiment)
    print("Rating    :", rating, "/ 5")


# ---------------------------------------------------
# Step 6: Calculate Overall Product Rating
# ---------------------------------------------------

overall_rating = total_rating / len(comments)

print("\n" + "=" * 60)
print("Overall Product Rating :", round(overall_rating, 2), "/ 5")
print("=" * 60)

# Product recommendation
if overall_rating >= 4:
    print("Recommendation : BUY - Highly Recommended")

elif overall_rating >= 3:
    print("Recommendation : BUY - Good Product")

elif overall_rating >= 2:
    print("Recommendation : THINK BEFORE BUYING")

else:
    print("Recommendation : DON'T BUY - Poor Product")