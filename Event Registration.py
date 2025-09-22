class EventRegistration:
    """
    Event Registration System using a hash table for fast participant management.

    Methods:
        register(participant_id, name): Add a participant.
        remove(participant_id): Remove a participant.
        search(participant_id): Find a participant by ID.
        display(): Show all registered participants.
    """
    def __init__(self):
        self.table = {}

    def register(self, participant_id, name):
        """Register a new participant."""
        self.table[participant_id] = name

    def remove(self, participant_id):
        """Remove a participant by ID."""
        if participant_id in self.table:
            del self.table[participant_id]
            return True
        return False

    def search(self, participant_id):
        """Search for a participant by ID."""
        return self.table.get(participant_id, None)

    def display(self):
        """Display all registered participants."""
        for pid, name in self.table.items():
            print(f"ID: {pid}, Name: {name}")

# Example usage
if __name__ == "__main__":
    event = EventRegistration()
    event.register(101, "Alice")
    event.register(102, "Bob")
    event.register(103, "Charlie")
    print("All participants:")
    event.display()
    print("Searching for ID 102:", event.search(102))
    print("Removing ID 101:", event.remove(101))
    print("All participants after removal:")
    event.display()