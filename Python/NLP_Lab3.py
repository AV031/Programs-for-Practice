# NLP Assignment
# Spam Detection using Rule Based Approach

import re

# Given mail
mail = "You have won an lottery of 20000$! Hurray! Click the link below to claim now."

# Priority dictionary
priority_dict = {
    "lottery": "high",
    "hurray": "high",
    "congratulation": "low",
    "offer": "medium",
    "claim": "medium",
    "party": "medium",
    "click": "low",
    "link": "low",
    "win": "medium",
    "below": "medium",
    "now": "medium"
}

# Stop words
stop_words = {
    "you", "have", "an", "a", "the", "is", "are",
    "of", "to", "in", "on", "for", "and"
}

print("Original Mail:")
print(mail)

# 1. Lowercase
mail = mail.lower()

print("\n1. Lowercase:")
print(mail)

# 2. Tokenization
tokens = re.findall(r'\b[a-z]+\b', mail)

print("\n2. Tokens:")
print(tokens)

# 3. Stop Word Removal
filtered_tokens = []

for word in tokens:
    if word not in stop_words:
        filtered_tokens.append(word)

print("\n3. After Stop Word Removal:")
print(filtered_tokens)

# 4. Lemmatization
lemma_dictionary = {
    "won": "win"
}

lemmatized_tokens = []

for word in filtered_tokens:
    if word in lemma_dictionary:
        lemmatized_tokens.append(lemma_dictionary[word])
    else:
        lemmatized_tokens.append(word)

print("\n4. After Lemmatization:")
print(lemmatized_tokens)

# 5. Priority Analysis
high_count = 0
medium_count = 0
low_count = 0

print("\n5. Analysis:")

for word in lemmatized_tokens:

    if word in priority_dict:

        priority = priority_dict[word]

        print(word, "->", priority)

        if priority == "high":
            high_count += 1

        elif priority == "medium":
            medium_count += 1

        elif priority == "low":
            low_count += 1

print("\nPriority Counts:")
print("High   =", high_count)
print("Medium =", medium_count)
print("Low    =", low_count)

# Final Spam Classification
if high_count >= 2 and medium_count >= 1:
    print("\nFinal Result: Spam")
else:
    print("\nFinal Result: Not a Spam")