class Queue:
    """
    A simple implementation of a Queue data structure using a Python list.

    The queue follows FIFO (First In, First Out) principle where the first element
    added to the queue is the first one to be removed.

    Attributes:
        items (list): Internal list to store queue elements
    """

    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.items = []

    def enqueue(self, item):
        """
        Add an element to the end of the queue.

        Args:
            item: The element to be added to the queue
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the front element from the queue.

        Returns:
            The front element from the queue

        Raises:
            IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        """
        Return the front element from the queue without removing it.

        Returns:
            The front element from the queue

        Raises:
            IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the number of elements in the queue.

        Returns:
            int: The number of elements in the queue
        """
        return len(self.items)

    def __str__(self):
        """
        Return a string representation of the queue.

        Returns:
            str: String representation of the queue
        """
        return f"Queue({self.items})"

    def __repr__(self):
        """
        Return a detailed string representation of the queue.

        Returns:
            str: Detailed string representation of the queue
        """
        return f"Queue(items={self.items})"

# Example usage
if __name__ == "__main__":
    queue = Queue()
    print(f"Is queue empty? {queue.is_empty()}")  # Should print: True
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Queue after enqueue 1, 2, 3: {queue}")
    print(f"Front element (peek): {queue.peek()}")  # Should print: 1
    print(f"Queue size: {queue.size()}")  # Should print: 3
    dequeued_item = queue.dequeue()
    print(f"Dequeued item: {dequeued_item}")  # Should print: 1
    print(f"Queue after dequeue: {queue}")
    print(f"Is queue empty? {queue.is_empty()}")  # Should print: False
