import random

items = []
for _ in range(1_000):
  items.append((random.randint(1, 100), random.randint(1, 200)))
# Definimos los objetos (valor, peso)

max_weight = 10000  # Peso máximo permitido en la mochila

def greedy_solution(items, max_weight):
    """Genera una solución inicial utilizando una heurística greedy."""
    #!Ojo, se elimina el sort de items para no quitar la aletoriedad
    items_sorted = items#sorted(items, key=lambda x: x[0] / x[1], reverse=True)  # Ordenamos por valor/peso
    solution = []
    total_weight = 0
    total_value = 0
    for value, weight in items_sorted:
        if total_weight + weight <= max_weight:
            solution.append((value, weight))
            total_weight += weight
            total_value += value
    return solution, total_value

def iterated_greedy(items, max_weight, iterations=100):
    """Implementa la búsqueda iterada con la heurística greedy."""
    best_solution = None
    best_value = 0

    for _ in range(iterations):
        # Generamos una solución inicial
        solution, value = greedy_solution(items, max_weight)

        # Aquí se puede aplicar una búsqueda local para mejorar la solución
        # En este ejemplo, solo tomamos la mejor solución encontrada hasta ahora
        if value > best_value:
            best_solution = solution
            best_value = value
            print(f"Valor actual: {best_value}")

        # Introducimos aleatoriedad, como una perturbación de la solución
        random.shuffle(items)  # Aleatorizamos los elementos para explorar nuevas soluciones

    return best_solution, best_value

# Ejecutamos el algoritmo de búsqueda iterada
best_solution, best_value = iterated_greedy(items, max_weight, iterations=1000)

# Mostramos el resultado
print("Mejor solución encontrada:")
for item in best_solution:
    pass
    #print(f"Valor: {item[0]}, Peso: {item[1]}")
print(f"Valor total final: {best_value}")