import random

# Función objetivo
def objective_function(x):
    return (x - 3)**2

# Búsqueda aleatoria
def random_search(iterations, lower_bound, upper_bound):
    best_solution = None
    best_value = float('inf')

    for _ in range(iterations):
        # Generar una solución aleatoria
        candidate = random.uniform(lower_bound, upper_bound)

        # Evaluar la solución
        candidate_value = objective_function(candidate)
        print(candidate, candidate_value)
        # Si es la mejor solución encontrada, actualizar
        if candidate_value < best_value:
            best_solution = candidate
            best_value = candidate_value
            print("actualizado", candidate, candidate_value)


    return best_solution, best_value

# Parámetros
iterations = 10
lower_bound = -100
upper_bound = 100

# Ejecutar la búsqueda aleatoria
best_solution, best_value = random_search(iterations, lower_bound, upper_bound)

print(f"Best solution: {best_solution}")
print(f"Best value: {best_value}")
