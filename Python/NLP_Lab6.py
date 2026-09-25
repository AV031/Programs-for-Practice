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



sentence = input("Enter a sentence: ")


tokens = sentence.split()


root = Node("S")


np = Node("NP")


for word in tokens[:-1]:
    np.add_child(Node(word))


vp = Node("VP")
vp.add_child(Node(tokens[-1]))


root.add_child(np)
root.add_child(vp)

print("\nParse Tree:")
root.display()