
import nltk
import re
from nltk import CFG, ChartParser, BottomUpChartParser

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

# Create parsers
top_down_parser = ChartParser(grammar)
bottom_up_parser = BottomUpChartParser(grammar)


def generate_parse_tree(sentence):
    words = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", sentence)

    print("\nSentence:", sentence)

    # TOP-DOWN PARSING
    print("\n--- TOP-DOWN PARSING ---")

    try:
        trees = top_down_parser.parse(words)
        tree = next(trees)

        print("Top-Down Parse Tree:")
        tree.pretty_print()

    except StopIteration:
        print("No Top-Down parse tree found.")

    # BOTTOM-UP PARSING
    print("\n--- BOTTOM-UP PARSING ---")

    try:
        trees = bottom_up_parser.parse(words)
        tree = next(trees)

        print("Bottom-Up Parse Tree:")
        tree.pretty_print()

    except StopIteration:
        print("No Bottom-Up parse tree found.")


# Main program
print("NLP PARSE TREE GENERATOR")
print("Top-Down and Bottom-Up Parsing")

while True:

    sentence = input("\nEnter a sentence (or type exit): ")

    if sentence.lower() == "exit":
        print("Program terminated.")
        break

    if sentence.strip():
        generate_parse_tree(sentence)
    else:
        print("Please enter a valid sentence.")
