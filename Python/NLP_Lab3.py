# Assignment Question 3
# Spam Detection using NLP - Rule Based Approach

import re

# Priority dictionary
priority_dict = {
    "lottery": "high",
    "hurray": "high",
    "congratulation": "low",
    "offer": "medium",
    "claim": "high",
    "party": "medium",
    "click": "low",
    "link": "high",
    "win": "medium",
    "won": "medium",
    "below": "medium",
    "now": "medium"
}

# Stop words
stop_words = {
    "you", "have", "an", "a", "the", "is", "are",
    "of", "to", "in", "on", "for", "and"
}

# Accept 5 sentences from the user
sentences = []

print("Enter 5 sentences:")

for i in range(5):
    sentence = input(f"Sentence {i + 1}: ")
    sentences.append(sentence)


# Function to check spam
def check_spam(sentence):

    # Convert to lowercase
    sentence = sentence.lower()

    # Word tokenization
    tokens = re.findall(r'\b[a-z]+\b', sentence)

    # Stop word removal
    filtered_tokens = []

    for word in tokens:
        if word not in stop_words:
            filtered_tokens.append(word)

    # Lemmatization
    lemma_dictionary = {
        "won": "win"
    }

    lemmatized_tokens = []

    for word in filtered_tokens:
        if word in lemma_dictionary:
            lemmatized_tokens.append(lemma_dictionary[word])
        else:
            lemmatized_tokens.append(word)

    # Priority analysis
    high_count = 0
    medium_count = 0
    low_count = 0

    for word in lemmatized_tokens:

        if word in priority_dict:

            priority = priority_dict[word]

            if priority == "high":
                high_count += 1

            elif priority == "medium":
                medium_count += 1

            elif priority == "low":
                low_count += 1

    # Spam classification
    if high_count >= 2 and medium_count >= 1:
        return "Spam"
    else:
        return "Not Spam"


# Display results
print("\n" + "=" * 50)
print("          SPAM DETECTION RESULTS")
print("=" * 50)

for i, sentence in enumerate(sentences, 1):

    result = check_spam(sentence)

    print("\nSentence", i, ":", sentence)
    print("Result :", result)

print("\n" + "=" * 50)