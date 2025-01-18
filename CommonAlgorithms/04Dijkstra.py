# Dijkstra Algorithm --> Searching for the shortest path algorithm
# Time complexity: O(n^2)
# Especially useful in networking, route planning, cost minimization, and more.
# It involves nodes connected by "bridges" with weights that can represent distances, costs, etc.
# (always positive numbers).

# 1. Choose a node from which distances to the rest of the nodes will be calculated.
# 2. Initialize a table with a distance of 0 from the origin node to itself and ∞ (infinity) to all other nodes.
# 3. Mark all nodes as unvisited.
# 4. From the chosen origin node, calculate the distance to its neighboring nodes.
# 5. Visit the node (among the unvisited ones) with the lowest tentative distance.
# 6. Mark this node as visited and for each unvisited neighbor, calculate the distance from the origin
#    to that node, adding the weight of the bridge to each neighbor.
#   6. a. If this calculated distance is less than the previously assigned distance, update it with
# the new distance.
# 7. Select the next node with the lowest distance from the set of unvisited nodes, and repeat the process
# from step 5 to step 6.a. until the termination condition is met:

# Termination Condition of the Algorithm:
# When all nodes have been visited or until the smallest distance among unvisited nodes is ∞ 
# (this means the nodes are not connected to the origin node).

# Considerations:
# * There will be times when some nodes will never be reachable (those will remain with an infinite distance).
# * It's not only about finding the shortest distance but also finding it in a reasonable amount of time. 
#   It's not useful to save 100 meters if the calculation takes an extra hour.
# Please see this link to see a visualization, it will be very useful to understand the algorithm:
# https://www.cs.usfca.edu/~galles/visualization/Dijkstra.html
# And this link with the most complete explanation: https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php

# Implementation (not using heapq, but using a dictionary):
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


# Example usage
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

start_node = 'A'
distances, shortest_path = dijkstra(graph, start_node)

print("Shortest distances from node", start_node)
for node, distance in distances.items():
    print(f"Distance to {node}: {distance}")

print("\nShortest path tree:")
for node, prev in shortest_path.items():
    print(f"{node} <- {prev}")