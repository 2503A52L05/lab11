import heapq

class PriorityQueue:
    """
    Priority Queue implementation using Python's heapq module.

    Attributes:
        heap (list): Internal list to store heap elements as (priority, item) tuples.
    """
    def __init__(self):
        """
        Initialize an empty priority queue.
        """
        self.heap = []

    def enqueue(self, item, priority):
        """
        Add an item to the queue with a given priority.
        Args:
            item: The item to add.
            priority: The priority value (lower means higher priority).
        """
        heapq.heappush(self.heap, (priority, item))

    def dequeue(self):
        """
        Remove and return the item with the highest priority (lowest priority value).
        Returns:
            The item with the highest priority.
        Raises:
            IndexError: If the queue is empty.
        """
        if not self.heap:
            raise IndexError("dequeue from empty priority queue")
        return heapq.heappop(self.heap)[1]

    def display(self):
        """
        Display all items in the priority queue in heap order.
        Prints each item with its priority.
        """
        print([f"(priority={p}, item={i})" for p, i in self.heap])

    def is_empty(self):
        """
        Check if the priority queue is empty.
        Returns:
            bool: True if empty, False otherwise.
        """
        return len(self.heap) == 0

# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue("task1", 3)
    pq.enqueue("task2", 1)
    pq.enqueue("task3", 2)
    print("Priority Queue contents:")
    pq.display()
    print("Dequeued:", pq.dequeue())  # Should print: task2
    pq.display()
