class HashTable:
    """
    Hash table implementation using chaining for collision handling.

    Attributes:
        size (int): Number of buckets in the hash table.
        table (list): List of buckets, each a list for chaining.
    """
    def __init__(self, size=10):
        """
        Initialize the hash table with a given number of buckets.
        Args:
            size: Number of buckets (default 10).
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Compute the hash value for a given key.
        Args:
            key: The key to hash.
        Returns:
            int: The bucket index for the key.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If the key already exists, update its value.
        Args:
            key: The key to insert.
            value: The value to associate with the key.
        """
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def search(self, key):
        """
        Search for a key in the hash table and return its value if found.
        Args:
            key: The key to search for.
        Returns:
            The value associated with the key, or None if not found.
        """
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        """
        Delete a key-value pair from the hash table if it exists.
        Args:
            key: The key to delete.
        Returns:
            bool: True if the key was found and deleted, False otherwise.
        """
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def __str__(self):
        """
        Return a string representation of the hash table.
        """
        return str(self.table)

# Example usage
if __name__ == "__main__":
    ht = HashTable(size=5)
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("orange", 30)
    print("HashTable:", ht)
    print("Search 'banana':", ht.search("banana"))  # Output: 20
    print("Delete 'apple':", ht.delete("apple"))   # Output: True
    print("HashTable after delete:", ht)
    print("Search 'apple':", ht.search("apple"))   # Output: None
