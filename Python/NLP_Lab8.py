# Assignment 8 NLP
# Implementation of a Natural Language Processing (NLP) Program to Generate Parse Trees for English Sentences Using Context-Free Grammar (CFG) in Python.

import nltk
import re
from nltk import CFG, ChartParser

# Define grammar
grammar = CFG.fromstring("""
S -> NP VP

NP -> N
NP -> DET N
NP -> DET ADJ N

VP -> AUX NP
VP -> AUX ADV ADJ PP
VP -> AUX V PP PP

PP -> PREP N
PP -> PREP ADJ N
PP -> PREP NP

N -> 'India' | 'country' | 'Indian' | 'nature' | 'Cricketers' | 'Gods'
DET -> 'a' | 'Every'
AUX -> 'is' | 'are'
ADJ -> 'beautiful' | 'caring' | 'living'
ADV -> 'very'
V -> 'worshipped'
PREP -> 'in' | 'across' | 'as'
""")

parser = ChartParser(grammar)


def generate_parse_tree(sentence):
    words = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", sentence)

    print("\nSentence:", sentence)

    try:
        trees = parser.parse(words)
        tree = next(trees)

        print("Parse Tree:")
        tree.pretty_print()

    except StopIteration:
        print("No parse tree found for this sentence.")


# Main program
print("NLP PARSE TREE GENERATOR")

while True:

    sentence = input("\nEnter a sentence (or type exit): ")

    if sentence.lower() == "exit":
        print("Program terminated.")
        break

    if sentence.strip():
        generate_parse_tree(sentence)