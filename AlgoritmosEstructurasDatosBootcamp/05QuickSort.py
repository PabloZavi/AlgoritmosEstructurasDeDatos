def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    # We choose as a pivot the first element of the array
    pivot = arr[0]
    bigger = 1
    smaller = len(arr) - 1

    while bigger <= smaller:
        # Move bigger pointer to the right until a value greater than the pivot is found
        while bigger <= smaller and arr[bigger] <= pivot:
            bigger += 1
        # Move smaller pointer to the left until a value less than the pivot is found
        while bigger <= smaller and arr[smaller] >= pivot:
            smaller -= 1
        # We arrive until here when the bigger pointer found a value greater than the pivot
        # and the smaller pointer found a value less than the pivot
        # Swap elements at bigger and smaller pointers if they haven't crossed
        if bigger < smaller:
            arr[bigger], arr[smaller] = arr[smaller], arr[bigger]
    
    # We arrive here when all the bigger elements than the pointer are on the right
    # and all the smaller elements than the pointer are on the left, so, we have to put
    # the pivot in the correct position (between the two subarrays)
    # Swap pivot with the element at the smaller pointer to place it in the correct position
    arr[0], arr[smaller] = arr[smaller], arr[0]

    # Recursively sort the bigger and smaller subarrays
    return quickSort(arr[:smaller]) + [arr[smaller]] + quickSort(arr[smaller + 1:])

array = [12, 7, 23, 1, 9, 34, 5, 18, 3, 21]
retArray = quickSort(array)
print(retArray)
