from collections import deque

def bfs(graph, start_node):
    """
    Performs a Breadth-First Search on a graph starting from a given node.

    Args:
        graph (dict): An adjacency list representation of the graph.
        start_node: The starting node for the traversal.

    Returns:
        list: A list of nodes in the order they were visited by BFS.
    """
    
    # Use a deque as the queue for efficient appends and pops
    queue = deque([start_node])
    
    # Keep track of visited nodes to prevent cycles and redundant processing
    visited = set([start_node])
    
    # List to store the order of visited nodes
    visited_order = []

    while queue:
        # Dequeue a vertex from the queue (popleft() is O(1) for deque)
        current_node = queue.popleft()
        visited_order.append(current_node)
        
        # Get all adjacent vertices of the dequeued vertex
        for neighbor in graph.get(current_node, []):
            # If a neighbor has not been visited yet, mark it as visited
            # and enqueue it
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return visited_order

# Example Usage:

# Define the graph as an adjacency list
# Graph structure:
# A --- B
# |     |
# C --- D
#     / |
#    E  F
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['D'],
    'F': ['D']
}

# Start BFS from node 'A'
start_node = 'A'
traversal_result = bfs(graph, start_node)

print(f"BFS traversal starting from node '{start_node}':")
print(traversal_result)
# Expected output: ['A', 'B', 'C', 'D', 'E', 'F'] (order of B and C might vary)
