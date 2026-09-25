# Assignment 6 
#Q) Take a sentence, use top down parsing technique, generate indvidual tokens (Tree Structure)
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print("  " * level + self.name)
        for child in self.children:
            child.display(level + 1)


# Take sentence from user
sentence = input("Enter a sentence: ")

# Split sentence into words
tokens = sentence.split()

# Create root node
root = Node("S")

# Create NP for first part
np = Node("NP")

# Add words to NP
for word in tokens[:-1]:
    np.add_child(Node(word))

# Create VP for last word
vp = Node("VP")
vp.add_child(Node(tokens[-1]))

# Add NP and VP to root
root.add_child(np)
root.add_child(vp)

# Display tree
print("\nParse Tree:")
root.display()