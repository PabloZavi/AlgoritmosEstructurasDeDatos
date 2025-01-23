# Como ejercicio del tema "divide y vencerás" se explicó el funcionamiento del algoritmo Merge Sort
# con una animación pero sin código, y se pidió que intentáramos codificar una solución por nuestra
# parte. Este fue el primer intento. Más abajo se harán las correcciones necesarias.

# En esta función se puede dar el caso de que un array tenga un número par o impar de elementos,
# entonces, para tomar en cuenta los dos casos se hacen dos casos base:
# si es par, se va a llegar al caso mínimo de un elemento, y al haber un solo elemento, 
# se va a devolver ese elemento como el mayor, 
# si es impar, en uno de los casos se va a llegar al caso mínimo de dos elementos, por ende 
# se devolverá el máximo de esos dos elementos
def maxValues (arr):
    if len(arr) == 1:
        return arr[0]
    
    if len(arr) == 2:
        return max(arr[0], arr[1])
    
    # Si el array tiene tres elementos o más, se irá dividiendo en dos arrays de forma recursiva 
    # cada vez (pensar como hacia la izquierda un array con los elementos de la primera mitad y 
    # hacia la derecha los elementos de la segunda mitad) hasta llegar a los casos base ya
    # explicados más arriba y a partir de ahí, se irá devolviendo el máximo valor encontrado
    # entre el lado izquierdo y el derecho 
    # ver imagen: https://miro.medium.com/v2/resize:fit:720/format:webp/1*lqCKBNEDvuEoddDlYA42Tw.png
    
    return max(
        maxValues(arr[ : len(arr)//2]), 
        maxValues(arr[len(arr)//2 : ])
    )
        
        
# Esta función recibe un array como parámetro y lo ordena, llamando recursivamente a la función.
# Si el array tiene un solo elemento, devuelve el mismo elemento, ya que de por sí estaría ordenado,
# Si no, llama recursivamente a la función "maxValues" de arriba, y va ordenando (también llamandosé
# recursivamente a sí misma) el array con cada valor devuelto de la función de arriba.
def orderArray(arr):
    if len(arr) == 1:
        return arr
    
    # Invoca a la función de arriba, y el valor devuelto es guardado en un array, borrado
    # del array que se recibe como parámetro y vuelve a llamar recursivamente a la función
    # de arriba hasta que termina de ordenarse.
    
    maxValue = maxValues(arr)
    arr.remove(maxValue)
    orArr = orderArray(arr) + [maxValue]
    return orArr


arr = [23, 5, 12, 8, 35, 18, 67, 45, 2, 31]
print (orderArray(arr))