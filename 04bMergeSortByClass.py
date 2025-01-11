# Este es el código que se mostró en clase, adaptado de C++ a Python,
# pero optimizado acorde a Python con la ayuda de Copilot.    
# La diferencia con el código que hice es que la función merge que ordena el array
# es iterativa (no recursiva como la que hice) y la función mergeSort es recursiva.

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

# Función que recibe un array y divide el array en dos partes cada vez hasta llegar al mínimo elemento
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergeSort(arr[:mid]) #Divide desde la mitad del array a la izquierda hasta que queda un elemento
    right = mergeSort(arr[mid:]) #Divide desde la mitad del array a la derecha hasta que queda un elemento
    # Y a partir de que queda un elemento en cada lado, se empieza a ordenar el array completo
    # llamando a la función de arriba, pasandolé el array a la izquierda y el array a la derecha
    return merge(left, right)

arr = [23, 5, 12, 8, 35, 18, 67, 45, 2, 31]
print(mergeSort(arr))
