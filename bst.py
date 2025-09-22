class BSTNode:
    """
    Node for Binary Search Tree.

    Attributes:
        data: The value stored in the node.
        left: Reference to the left child node.
        right: Reference to the right child node.
    """
    def __init__(self, data):
        """
        Initialize a BST node with data and child pointers.
        Args:
            data: Value to store in the node.
        """
        self.data = data
        self.left = None
        self.right = None

class BST:
    """
    Binary Search Tree implementation.

    Attributes:
        root: Reference to the root node of the BST.
    """
    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert a new value into the BST (recursive).
        Args:
            data: Value to insert.
        """
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """
        Helper method to recursively insert a value.
        """
        if node is None:
            return BSTNode(data)
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        # If data == node.data, do not insert duplicates
        return node

    def in_order_traversal(self):
        """
        Perform in-order traversal and print values in sorted order.
        """
        self._in_order_recursive(self.root)
        print()

    def _in_order_recursive(self, node):
        """
        Helper method for in-order traversal.
        """
        if node:
            self._in_order_recursive(node.left)
            print(node.data, end=" ")
            self._in_order_recursive(node.right)

# Example usage
if __name__ == "__main__":
    bst = BST()
    for value in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(value)
    print("BST in-order traversal:")
    bst.in_order_traversal()  # Output: 20 30 40 50 60 70 80
