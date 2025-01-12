# Se intenta maximizar el valor de los elementos seleccionados 
# para llevar en una mochila con una capacidad limitada.

# Mochila con una capacidad máxima W.
# n objetos, con un valor v y un peso w.
# Se pueden fraccionar los objetos en vez de tomarlos completos.
# Enfoque greedy: selecciona primero los objetos con el mayor valor 
# por unidad de peso hasta que se llena la mochila.

## Como en los otros ejercicios, primero lo trato de resolver y después
## pongo el código visto en clase para comparar 

items = [(60, 10), (100, 20), (120, 30)]  # (valor, peso)
capacity = 55  # Capacidad máxima de la mochila

## My implementation-->
def fractKnapsack(items, capacity):
    # We sort by the average cost/weight
    items = sorted(items, key=lambda x: x[0] / x[1]) 
    knapsack = []
    
    # We loop from the last (the better relation betw cost/weight)
    for item in reversed(items):
        # If we can add the entire item...
        if capacity >= item[1]:
            knapsack.append(item)
            capacity -= item[1]
        # If we still have capacity but not for an entire object,
        # We take a fraction of it
        elif capacity > 0:
            knapsack.append((capacity*item[0]/item[1],item[1]-capacity))
            capacity -= item[1]-capacity
                
    return knapsack

knapsack = fractKnapsack(items, capacity)
total_sum = sum([item[0] for item in knapsack])
print("The choosen items are: 'value/weight'", knapsack)
print("And the value of the knapsack is: ", total_sum)


## Class implementation-->

def fractional_knapsack(items, capacity):
    """
    items: lista de tuplas (valor, peso) de los objetos disponibles.
    capacity: capacidad máxima de la mochila.
    """
    # Ordenar los items por valor/peso de forma descendente
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0  # Valor total acumulado
    for value, weight in items:
        if capacity >= weight:
            # Si cabe el objeto completo, lo tomamos
            total_value += value
            capacity -= weight
        else:
            # Si no cabe el objeto completo, tomamos una fracción
            fraction = capacity / weight
            total_value += value * fraction
            break  # La mochila está llena

    return total_value

# Ejemplo de uso

max_value = fractional_knapsack(items, capacity)
print(f"El valor máximo que se puede llevar en la mochila es: {max_value}")