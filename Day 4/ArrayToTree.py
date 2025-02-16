class node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None




def array_to_tree(arr, i, n):
    root = None
    
    # Base case for recursion - if index exceeds array length
    if i < n:
        # Create new node with current element
        root = node(arr[i])
        
        # Insert left child - 2*i + 1 is left child index in array
        root.left = array_to_tree(arr, 2*i + 1, n)
        
        # Insert right child - 2*i + 2 is right child index in array
        root.right = array_to_tree(arr, 2*i + 2, n)
        
    return root



arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
root = array_to_tree(arr, 0, n)

print("Node at index 2:", root.left.right.key)
print("Node at index 3:", root.right.left.key)
print("Left child of node at index 2: ", root.left.left.key)
print("Node at index 0:", root.key)
# For a node at index i, its right child is at index 2*i + 2
i = 3
right_child_index = 2*i + 2
print(f"Right child of node at index {i} is at index {right_child_index}")