class Graph:
    """
    Graph implementation using an adjacency list.

    Attributes:
        adj_list (dict): Dictionary mapping vertices to lists of adjacent vertices.
    """
    def __init__(self):
        """
        Initialize an empty graph.
        """
        self.adj_list = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        Args:
            vertex: The vertex to add.
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        """
        Add an edge between two vertices (undirected).
        Args:
            v1: First vertex.
            v2: Second vertex.
        """
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def display(self):
        """
        Display the graph's adjacency list.
        Prints each vertex and its connections.
        """
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {', '.join(map(str, neighbors))}")

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    print("Graph connections:")
    g.display()
