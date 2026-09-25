#Q) Take a sentence , use Top-Down Parsing Technique , Generate individual tokens ('Tree Structure')

# Top-Down Parsing using Recursive Descent Parser

sentence = "the boy eats the apple"

# Convert sentence into individual tokens
tokens = sentence.split()
position = 0


# Node for the parse tree
class Node:
    def __init__(self, name, children=None):
        self.name = name
        self.children = children if children else []


# Grammar:
# S  -> NP VP
# NP -> Det N
# VP -> V NP
# Det -> the
# N -> boy | apple
# V -> eats


def match(word):
    global position

    if position < len(tokens) and tokens[position] == word:
        position += 1
        return Node(word)

    return None


def parse_det():
    if position < len(tokens) and tokens[position] == "the":
        return Node("Det", [match("the")])

    return None


def parse_noun():
    global position

    if position < len(tokens) and tokens[position] in ["boy", "apple"]:
        word = tokens[position]
        position += 1
        return Node("N", [Node(word)])

    return None


def parse_verb():
    if position < len(tokens) and tokens[position] == "eats":
        return Node("V", [match("eats")])

    return None


def parse_np():
    det = parse_det()
    if det is None:
        return None

    noun = parse_noun()
    if noun is None:
        return None

    return Node("NP", [det, noun])


def parse_vp():
    verb = parse_verb()
    if verb is None:
        return None

    np = parse_np()
    if np is None:
        return None

    return Node("VP", [verb, np])


def parse_sentence():
    np = parse_np()
    if np is None:
        return None

    vp = parse_vp()
    if vp is None:
        return None

    return Node("S", [np, vp])


# Print the tree
def print_tree(node, level=0):
    print("  " * level + "|-- " + node.name)

    for child in node.children:
        print_tree(child, level + 1)


# Start parsing
tree = parse_sentence()

if tree is not None and position == len(tokens):
    print("Tokens:")
    print(tokens)

    print("\nParse Tree:")
    print_tree(tree)

    print("\nSentence successfully parsed using Top-Down Parsing.")

else:
    print("Invalid sentence!")