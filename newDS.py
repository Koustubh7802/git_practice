class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.tree_root = None  # Root of the binary tree
        self.next = None

class Nucleus:
    def __init__(self):
        self.dendrites = []  # List of head nodes for each linked list

    def add_dendrite(self, head_node):
        self.dendrites.append(head_node)

#main
def main():
    # Create a binary tree node
    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(5)
    root.right = BinaryTreeNode(15)

    # Create a linked list node and assign the binary tree root
    linked_list_node = LinkedListNode(1)
    linked_list_node.tree_root = root

    # Create a nucleus and add the linked list node as a dendrite
    nucleus = Nucleus()
    nucleus.add_dendrite(linked_list_node)

    # Output the structure
    print("Nucleus has", len(nucleus.dendrites), "dendrites.")
    print("First dendrite's linked list node value:", nucleus.dendrites[0].value)
    print("Binary tree root value:", nucleus.dendrites[0].tree_root.value)

main()
