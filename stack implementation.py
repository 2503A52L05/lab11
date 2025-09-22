class Stack:
    """
    A simple implementation of a Stack data structure using a Python list.

    The stack follows LIFO (Last In, First Out) principle where the last element
    added to the stack is the first one to be removed.

    Attributes:
        items (list): Internal list to store stack elements
    """

    def __init__(self):
        """
        Initialize an empty stack.

        Creates a new stack instance with no elements.
        """
        self.items = []

    def push(self, item):
        """
        Add an element to the top of the stack.

        Args:
            item: The element to be added to the stack

        Returns:
            None
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top element from the stack.

        Returns:
            The top element from the stack

        Raises:
            IndexError: If the stack is empty
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """
        Return the top element from the stack without removing it.

        Returns:
            The top element from the stack

        Raises:
            IndexError: If the stack is empty
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the number of elements in the stack.

        Returns:
            int: The number of elements in the stack
        """
        return len(self.items)

    def __str__(self):
        """
        Return a string representation of the stack.

        Returns:
            str: String representation of the stack
        """
        return f"Stack({self.items})"

    def __repr__(self):
        """
        Return a detailed string representation of the stack.

        Returns:
            str: Detailed string representation of the stack
        """
        return f"Stack(items={self.items})"


# Example usage
if __name__ == "__main__":
    # Create a new stack
    stack = Stack()

    # Test is_empty
    print(f"Is stack empty? {stack.is_empty()}")  # Should print: True

    # Test push
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack after pushing 1, 2, 3: {stack}")

    # Test peek
    print(f"Top element (peek): {stack.peek()}")  # Should print: 3

    # Test size
    print(f"Stack size: {stack.size()}")  # Should print: 3

    # Test pop
    popped_item = stack.pop()
    print(f"Popped item: {popped_item}")  # Should print: 3
    print(f"Stack after pop: {stack}")

    # Test is_empty again
    print(f"Is stack empty? {stack.is_empty()}")  # Should print: False