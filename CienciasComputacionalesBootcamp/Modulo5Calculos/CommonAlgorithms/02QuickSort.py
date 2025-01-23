# Quick Sort --> Sorting algorithm
# Time complexity: O(n log n)
# It is frequently used because it is fast
# Explanation:
# The quick sort algorithm partitions the array into
# two subarrays: 
# 1. One with elements smaller than the pivot.
# 2. One with elements greater than the pivot.
# It then recursively sorts these subarrays.

def quickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array)//2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quickSort(left) + middle + quickSort(right)

array = [7, 2, 9, 1, 6, 8, 4, 3, 0, 5]
sortedArray = quickSort(array)

print(sortedArray)


# The following code is more efficient because sorts the array in-place
# (doesn't create subarrays in each partition)

def quicksort2(array, start, end):
    if start < end:
        pivot_index = partition(array, start, end)
        quicksort2(array, start, pivot_index - 1)  # Sort the left subarray
        quicksort2(array, pivot_index + 1, end)    # Sort the right subarray

def partition(array, start, end):
    pivot = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1

# Example usage
array2 = [10, 7, 8, 9, 1, 5]
quicksort2(array2, 0, len(array2) - 1)
print("Sorted array:", array2)
