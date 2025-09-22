class Node:
    """
    Node for singly linked list.

    Attributes:
        data: The value stored in the node.
        next: Reference to the next node in the list.
    """
    def __init__(self, data):
        """
        Initialize a node with data and next pointer.
        Args:
            data: Value to store in the node.
        """
        self.data = data
        self.next = None

class LinkedList:
    """
    Singly linked list implementation.

    Attributes:
        head: Reference to the first node in the list.
    """
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def insert(self, data):
        """
        Insert a new node with the given data at the end of the list.
        Args:
            data: Value to insert.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        """
        Display all elements in the linked list.
        Prints the data of each node in order.
        """
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    print("Linked List contents:")
    ll.display()  # Output: 10 -> 20 -> 30
