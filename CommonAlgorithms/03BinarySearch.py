# Binary Search --> Searching algorithm
# Time complexity: O(log n)
# Efficient for searching sorted arrays.
# Binary Search repeatedly divides the sorted array in half:
# 1. Compares the target value to the middle element.
# 2. If the target is less than the middle element, it searches the left half.
# 3. If the target is greater, it searches the right half.
# 4. This process continues until the target value is found or the search space is empty.
# It can be recursive or iterative.

# Recursive Binary Search by me
def binarySearchMe(array, n, beg, end):
    if len(array) == 0:
        return "The array is empty"
    if(n < array[0] or n > array[len(array)-1] or (beg == end and n != array[beg])):
        return "The number " + str(n) + " is not in the array "
    
    pivot = (beg + end) // 2
    if(n == array[pivot]):
        return "The number " + str(n) + " is in the position " + str(pivot)
    elif(n < array[pivot]):
        return binarySearchMe(array, n, beg, end//2)
    elif(n > array[pivot]):
        return binarySearchMe(array, n, end, len(array)-1)



# Improved version
# Recursive calls with appropriate beg and end values
# For the left half: end = pivot - 1
# For the right half: beg = pivot + 1
# The base case is when beg > end
def binarySearchImproved(array, n, beg, end):
    if len(array) == 0:
        return "The array is empty"
    if beg > end:
        return "The number " + str(n) + " is not in the array"

    pivot = (beg + end) // 2
    if n == array[pivot]:
        return "The number " + str(n) + " is in the position " + str(pivot)
    elif n < array[pivot]:
        return binarySearchImproved(array, n, beg, pivot - 1)
    else:
        return binarySearchImproved(array, n, pivot + 1, end)


# Iterative version
def binarySearchIterative(array, n):
    beg = 0
    end = len(array) - 1

    while beg <= end:
        pivot = (beg + end) // 2

        if array[pivot] == n:
            return "The number " + str(n) + " is in the position " + str(pivot)
        elif array[pivot] < n:
            beg = pivot + 1
        else:
            end = pivot - 1

    return "The number " + str(n) + " is not in the array"

array = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
numberToSearch = 6
beg = 0
end = len(array)-1

print(binarySearchMe(array, numberToSearch, beg, end))
print(binarySearchImproved(array, numberToSearch, beg, end))
print(binarySearchIterative(array, numberToSearch))