class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

# Initialize root node
root = Node(10)

# Create child nodes
root.left = Node(5)
root.right = Node(15)

# Create grandchildren nodes
root.left.left = Node(2)
root.left.right = Node(7)

print("Node at left child of root: ", root.left.key)
print("Left child of left child of root: ", root.left.left.key)
