# This exercise is from the 'Algoritmos de aproximación' class
# We have to use a Greedy approach to calculate the way to arrive to an amount
# with as few coins as possible.
# First I did my implementation and after that I saw the implementation we saw
# in the class in order to see the differences and optimizations.

## My implementation-->
def coinChangeGreedy(denominations, amount):
    times = [0] * len(denominations)
        
    for i in range(len(denominations)-1, -1, -1):
        while(amount >= (amount//denominations[i]) and amount//denominations[i]>0):
                amount -= denominations[i]
                times[i] += 1
                
    for i in range(len(times)):
        if times[i] > 0:
            print ("La moneda de $" , denominations[i] , "se usó" ,times[i] , "veces")

denominations = [1, 2, 5, 10, 20, 50]
amount = 73

coinChangeGreedy(denominations, amount)

###############################################################################

## Implementation that we say in the class-->
def coin_change_greedy(denominations, amount):
    """
    Calcula el mínimo número de monedas necesarias para alcanzar el monto dado usando el enfoque greedy.

    denominations: lista de denominaciones de monedas disponibles.
    amount: cantidad total a alcanzar.
    """
    # Ordenar las denominaciones en orden descendente
    denominations.sort(reverse=True)

    result = []
    for coin in denominations:
        if amount == 0:
            break
        # Determinar cuántas monedas de esta denominación se pueden usar
        count = amount // coin
        if count > 0:
            result.append((coin, count))
            amount -= coin * count

    if amount > 0:
        print("No es posible alcanzar el monto con las denominaciones dadas.")
    return result

# Ejemplo de uso
denominations = [1, 2, 5, 10, 20, 50]
amount = 73

result = coin_change_greedy(denominations, amount)
print("Monedas usadas:")
for coin, count in result:
    print(f"Moneda de {coin}: {count} veces")
