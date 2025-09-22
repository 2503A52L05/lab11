from collections import deque

class DequeDS:
    """
    Double-ended queue (deque) implementation using collections.deque.

    Supports insertion and removal from both ends.
    """
    def __init__(self):
        """
        Initialize an empty deque.
        """
        self.deque = deque()

    def add_front(self, item):
        """
        Insert an item at the front of the deque.
        Args:
            item: The item to insert.
        """
        self.deque.appendleft(item)

    def add_rear(self, item):
        """
        Insert an item at the rear of the deque.
        Args:
            item: The item to insert.
        """
        self.deque.append(item)

    def remove_front(self):
        """
        Remove and return the item from the front of the deque.
        Returns:
            The item removed from the front.
        Raises:
            IndexError: If the deque is empty.
        """
        if not self.deque:
            raise IndexError("remove_front from empty deque")
        return self.deque.popleft()

    def remove_rear(self):
        """
        Remove and return the item from the rear of the deque.
        Returns:
            The item removed from the rear.
        Raises:
            IndexError: If the deque is empty.
        """
        if not self.deque:
            raise IndexError("remove_rear from empty deque")
        return self.deque.pop()

    def display(self):
        """
        Display the contents of the deque.
        """
        print(list(self.deque))

    def is_empty(self):
        """
        Check if the deque is empty.
        Returns:
            bool: True if empty, False otherwise.
        """
        return len(self.deque) == 0

# Example usage
if __name__ == "__main__":
    dq = DequeDS()
    dq.add_rear(1)
    dq.add_front(2)
    dq.add_rear(3)
    dq.display()  # Output: [2, 1, 3]
    print("Removed from front:", dq.remove_front())  # Output: 2
    print("Removed from rear:", dq.remove_rear())    # Output: 3
    dq.display()  # Output: [1]
