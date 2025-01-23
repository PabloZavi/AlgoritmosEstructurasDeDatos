from typing import List, Dict
from pydantic import BaseModel
import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt

class Graph(BaseModel):
    nodes: List[List[int]]  # Adjacency list representation

class Ant:
    def __init__(self, graph: Graph, pheromone: List[float], alpha: float = 1, beta: float = 2):
        self.graph = graph
        self.pheromone = pheromone
        self.alpha = alpha
        self.beta = beta
        self.solution: List[int] = []

    def choose_node(self, available_nodes: List[int]) -> int:
        # Calcula las probabilidades de elegir cada nodo basado en la feromona (atracción global)
        # y la heurística local (grado del nodo inverso)
        probabilities = []
        for node in available_nodes:
            tau = self.pheromone[node] ** self.alpha  # Influencia de la feromona
            eta = (1 / len(self.graph.nodes[node])) ** self.beta
            probabilities.append(tau * eta)

        probabilities = np.array(probabilities)
        probabilities /= probabilities.sum()  # Normaliza las probabilidades
        return np.random.choice(available_nodes, p=probabilities)

    def construct_solution(self) -> List[int]:
        # Construye una solución independiente para el conjunto
        self.solution = []
        available_nodes = list(range(len(self.graph.nodes)))

        while available_nodes:
            node = self.choose_node(available_nodes)
            self.solution.append(node)

            # Elimina el nodo elegido y sus vecinos de los nodos disponibles
            to_remove = [node] + self.graph.nodes[node]
            available_nodes = [n for n in available_nodes if n not in to_remove]

        return self.solution


def initialize_pheromone(graph: Graph, initial_pheromone: float) -> List[float]:
    # Inicializa la cantidad de feromona en cada nodo con un valor constante
    return [initial_pheromone] * len(graph.nodes)



def update_pheromone(pheromone: List[float], ants: List[Ant], evaporation_rate: float = 0.5, Q: float = 100):
    # Evapora un porcentaje de la feromona en cada iteración para evitar convergencia prematura
    pheromone[:] = [p * (1 - evaporation_rate) for p in pheromone]

    # Recompensa a los nodos presentes en las soluciones de las hormigas
    for ant in ants:
        for node in ant.solution:
            pheromone[node] += Q / len(ant.solution)


def aco_maximum_independent_set(graph: Graph, n_ants: int = 10, n_iterations: int = 50, initial_pheromone: float = 1, alpha: float = 1, beta: float = 2, evaporation_rate: float = 0.5, Q: float = 100) -> List[int]:
    pheromone = initialize_pheromone(graph, initial_pheromone)
    best_solution: List[int] = []

    for iteration in range(n_iterations):
        # Crea hormigas y les permite construir soluciones
        ants = [Ant(graph, pheromone, alpha, beta) for _ in range(n_ants)]
        solutions = [ant.construct_solution() for ant in ants]

        # Encuentra la mejor solución en esta iteración
        best_solution_in_iteration = max(solutions, key=len)
        if len(best_solution_in_iteration) > len(best_solution):
            best_solution = best_solution_in_iteration

        # Actualiza las feromonas basado en las soluciones generadas
        update_pheromone(pheromone, ants, evaporation_rate, Q)

        print(f"Iteration {iteration + 1}, Best solution size: {len(best_solution)}")

    return best_solution


def visualize_graph(graph: Graph, solution: List[int]):
    # Crea un grafo usando NetworkX
    G = nx.Graph()

    # Añade nodos y aristas al grafo
    for node, neighbors in enumerate(graph.nodes):
        G.add_node(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Asigna colores a los nodos según si están en la solución
    node_colors = ["red" if node in solution else "blue" for node in G.nodes()]

    # Dibuja el grafo
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color=node_colors, node_size=800, font_size=10, font_color="white", edge_color="gray")
    plt.title("Grafo con la Solución del Conjunto Independiente Máximo")
    plt.show()

# Example usage
def main():
    # Ejemplo sencillo de grafo (lista de adyacencia)
    # 0 -- 1
    # |    |
    # 2 -- 3
    graph_data = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2]
    }

    graph_list = [graph_data[node] for node in sorted(graph_data)]
    graph = Graph(nodes=graph_list)

    print("Running simple example:")
    best_solution = aco_maximum_independent_set(graph)
    print("Best solution:", best_solution)
    visualize_graph(graph, best_solution)

    # Ejemplo más complejo de grafo
    # Representa una estructura de red más amplia
    complex_graph_data = {
        0: [1, 2, 3],
        1: [0, 4, 5],
        2: [0, 6, 7],
        3: [0, 8],
        4: [1, 9, 10],
        5: [1, 11, 12],
        6: [2, 13],
        7: [2, 14],
        8: [3, 15],
        9: [4],
        10: [4],
        11: [5],
        12: [5],
        13: [6],
        14: [7],
        15: [8]
    }

    complex_graph_list = [complex_graph_data[node] for node in sorted(complex_graph_data)]
    complex_graph = Graph(nodes=complex_graph_list)

    print("\nRunning complex example:")
    best_solution_complex = aco_maximum_independent_set(complex_graph, n_ants=20, n_iterations=100)
    print("Best solution:", best_solution_complex)
    visualize_graph(complex_graph, best_solution_complex)

if __name__ == "__main__":
    main()
