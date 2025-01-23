# Ejercicio propuesto:
# Implementar el algoritmo de Dijkstra y detectar en qué parte se aplica 
# un greedy

# Intento frustrado de aplicar Dijkstra por mi cuenta después de entender el concepto
# en próximo archivo estará la implementación oficial y correcta. Uno de los problemas era
# que no se guardaba el camino correcto, sino todos los nodos que se visitaban (eso último es 
# correcto, ya que hay que visitar todos los nodos), por ende tampoco se guardaba bien la 
# distancia recorrida. Había problemas también a la hora de llegar al último nodo.

# Interpreto que la implementación de Greedy sucede cada vez que se selecciona para agregar
# al camino final un nodo, ya que no se puede volver atrás y se espera que a través de ese
# camino parcial que se va armando se llegue al camino final más corto


distances = {
    "start": {"name": "start", "distance": None, "wasVisited": False},
    "A": {"name": "A", "distance": None, "wasVisited": False},
    "B": {"name": "B", "distance": None, "wasVisited": False},
    "final": {"name": "final", "distance": None, "wasVisited": False},
}

edges = {
    "start": [("A", 6), ("B", 2)],
    "B": [("A", 3), ("final", 5)],
    "A": [("final", 1)]
}

road = []

def dijkstra(edges, distances, beginning,  path, final, totalDistance=0):
    
    distances[beginning]["wasVisited"] = True
    
    if beginning in edges:
        for edge, dist in edges[beginning]:
            if(distances[edge]["distance"] == None or (distances[edge]["distance"] != None and 
                                                    totalDistance + dist < distances[edge]["distance"])):
                distances[edge]["distance"] = totalDistance + dist
                totalDistance += dist
        minEdge = checkMinEdge(distances)
        if minEdge!=None:
            path.append(minEdge)
            dijkstra(edges, distances, minEdge, path, totalDistance)
        
    return(distances, totalDistance)
        

def checkMinEdge(distances):
    # Filter elements where wasVisited is False and distance is not None 
    filtered_elements = {k: v for k, v in distances.items() if not v["wasVisited"] and v["distance"] is not None} 
    # Find the element with the minimum distance 
    min_distance_element = min(filtered_elements, key=lambda k: filtered_elements[k]["distance"]) if filtered_elements else None

    return(min_distance_element)


beginning = "start"
final = "final"
path = []
distances[beginning]["distance"] == 0 # Pongo a 0 el elemento elegido como nodo de inicio
response = dijkstra(edges, distances, beginning, path, final)
print("El camino mas corto desde " + beginning + " hasta " + final + " es: " + str(response[1]) + "sumando: " + str(response[0]))
