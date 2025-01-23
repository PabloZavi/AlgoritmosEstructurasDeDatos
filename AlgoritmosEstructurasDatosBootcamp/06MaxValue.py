# This exercise is from the last part of "Dividir Para Conquistar" class.
# The tasks was to find the max value of an array using the "Divide and Conquer" approach
def maxValue(arr):
    if len(arr) == 1:
        return arr[0]
    
    maxElement = max(
        maxValue(arr[ : len(arr)//2]), 
        maxValue(arr[len(arr)//2 : ]))
    return maxElement


array = [15, 7, 22, 9, 3, 18, 66, 5, 12, 1, 11]
print (maxValue(array))