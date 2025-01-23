# Bubble Sort --> Sorting algorithm
# Time complexity: O(n^2)
# It is not frequently used because it is slow but it is easy to understand
# Explanation: 
# In each iteration, two adjacent elements are compared, and they are swapped
# if the one on the left is greater than the one on the right. This comparison
# is repeated until the cycle is complete. At the end of each cycle, the largest
# element is positioned at the end of the array, so for the next cycle, the
# iteration count is reduced by one, until i = 1

def bubblesort(array):
    n = len(array)
    iterations = 0
    while n > 1:
        for i in range(n - 1):
            iterations += 1
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                
        n -= 1

    print("Sorted array no flag:", array, "Number of iterations:", iterations)


# It is interesting to see the difference with the following approach with the
# swapped flag. With nearly sorted arrays, this code does less iterations (do it with 
# the array2), but does more iterations with not sorted arrays (see array1)
# With the first code, the number of iterations is constant
def bubble_sort(array):
    iterations = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            iterations += 1
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

    print("Sorted array with flag:", array, "Number of iterations:", iterations)

array1 = [7, 2, 9, 1, 6, 8, 4, 3, 0, 5]
array2 = [1, 2, 3, 4, 5, 6, 8, 7, 9, 10]
bubble_sort(array1)
bubblesort(array1)