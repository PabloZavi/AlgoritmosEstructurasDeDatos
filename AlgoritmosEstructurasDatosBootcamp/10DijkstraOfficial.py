# Ejercicio propuesto:
# Implementar el algoritmo de Dijkstra y detectar en qué parte se aplica 
# un greedy

# Esta sería la implementación oficial ya que mi intento por diseñar el algoritmo
# por mi cuenta fue un naufragio en toda regla.

# Usaré un diccionario de nodos que encontré que me resultó interesante por su extensión
# (ver video en el enlace al final del Readme)

import heapq

def dijkstra(graph, start):
    # We initialize priority queue to store (distance, node) -from the start node-
    # Ex: (0, 'A'), (3, 'B')... (the distance from start to A is 0, from start to B is 3...)
    pq = [(0, start)]
    # We initialize a dictionary to store the shortest distance to each node (from start to each node)
    # Ex: {'A': 0, 'B': 3, 'C': 5...}
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0 # The start node has a distance of 0
    # Dictionary to store the previous node for each node in the shortest path tree.
    shortest_path = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If the distance is greater than the recorded shortest distance, skip
        if current_distance > distances[current_node]:
            continue

        # Loop through all the neighbors of the current node and calculate the distance to each neighbor
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If the calculated distance is less than the recorded distance for a neighbor,
            # update the distance and path. Push the neighbor into the priority queue with
            # the updated distance.
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # distances: The shortest distance from the start node to each node.
    # shortest_path: The shortest path tree showing how each node is reached.
    return distances, shortest_path

# Graph representation (is a dictionary of dictionaries with all the edges)
graph = {
    'A': {'B': 8, 'E': 4, 'D': 5},
    'B': {'A': 8, 'C': 3, 'E': 12, 'F': 4},
    'C': {'B': 3, 'F': 9, 'G': 11},
    'D': {'E': 9, 'A': 5, 'H': 6},
    'E': {'A': 4, 'D': 9, 'I': 8, 'J': 5, 'B': 12, 'F': 3},
    'F': {'B': 4, 'C': 9, 'E': 3, 'G': 1, 'K': 8},
    'G': {'C': 11, 'F': 1, 'K': 8, 'L': 7},
    'H': {'I': 2, 'M': 7, 'D': 6},
    'I': {'E': 8, 'H': 2, 'J': 10, 'M': 6},
    'J': {'I': 10, 'K': 6, 'N': 9, 'E': 5},
    'K': {'F': 8, 'G': 8, 'J': 6, 'L': 5, 'P': 7},
    'L': {'G': 7, 'K': 5, 'P': 6},
    'M': {'H': 7, 'I': 6, 'N': 2},
    'N': {'J': 9, 'M': 2, 'P': 12},
    'P': {'K': 7, 'L': 6, 'N': 12}
}

# Example usage
start_node = 'A'
distances, shortest_path = dijkstra(graph, start_node)

print("Shortest distances from node", start_node)
for node, distance in distances.items():
    print(f"Distance to {node}: {distance}")

print("\nShortest path tree:")
for node, prev in shortest_path.items():
    print(f"Node {node} is reached from {prev}")


# Without using heapq library:
"""
def dijkstra(graph, start):
    # Initialize distances and shortest path dictionaries
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    shortest_path = {node: None for node in graph}
    
    # List to store nodes to be processed
    nodes = list(graph.keys())

    while nodes:
        # Find the node with the smallest distance
        current_node = min(nodes, key=lambda node: distances[node])
        
        # Remove the current node from the list
        nodes.remove(current_node)

        if distances[current_node] == float('infinity'):
            break
        
        # Update the distances for the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_node

    return distances, shortest_path


"""