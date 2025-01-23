# Interval Scheduling
# Este problema consiste en seleccionar el mayor número posible de actividades 
# que no se superpongan entre sí, dado un conjunto de actividades con tiempos 
# de inicio y fin.
# Enfoque Greedy: Elegir siempre la actividad que termina más temprano, 
# ya que deja el máximo tiempo disponible para otras actividades.
## Como en los otros ejercicios, primero lo trato de resolver y después
## pongo el código visto en clase para comparar 

activities = [
    (1, 4),  # Actividad 1: empieza a las 1 y termina a las 4
    (3, 5),  # Actividad 2: empieza a las 3 y termina a las 5
    (0, 6),  # Actividad 3: empieza a las 0 y termina a las 6
    (5, 7),  # Actividad 4: empieza a las 5 y termina a las 7
    (3, 8),  # Actividad 5: empieza a las 3 y termina a las 8
    (5, 9),  # Actividad 6: empieza a las 5 y termina a las 9
    (6, 10), # Actividad 7: empieza a las 6 y termina a las 10
    (8, 11), # Actividad 8: empieza a las 8 y termina a las 11
]

## My implementation-->

def intervalSch(activities):
    # Se ordena el array considerando el horario de finalización de cada actividad
    activities = sorted(activities, key=lambda x: x[1])
    # e agrega la primer actividad al array de elegidas
    chosenActivities = [activities[0]]
    # A partir de la segunda actividad, se van agregando las que empiezan después de 
    # que haya terminado la anterior elegida.
    for act in activities[1:]:
         #(act[0]) --> horario de inicio de la actividad que se está analizando
         #chosenActivities[-1][1] --> Horario de fin de la última act elegida hasta el momento
        if act[0] >= chosenActivities[-1][1]:
            chosenActivities.append(act)
            
    print ('Las actividades elegidas fueron: ', chosenActivities)

intervalSch(activities)

## Class implementation-->
def interval_scheduling(activities):
    """
    Selecciona el máximo número de actividades que no se solapen.

    activities: lista de tuplas (inicio, fin), donde cada tupla representa una actividad.
    """
    # Ordenar actividades por su tiempo de finalización
    activities.sort(key=lambda x: x[1])
    # Inicializar la selección de actividades
    selected = []
    current_end = 0  # Marca el final de la última actividad seleccionada

    for start, end in activities:
        if start >= current_end:
            # Seleccionar actividad si no se solapa con la anterior
            selected.append((start, end))
            current_end = end

    return selected

max_activities = interval_scheduling(activities)
print(f"Las actividades seleccionadas son: {max_activities}")