# RECURSION

# #Fibonacci using recursion -did by me-
# def fibo (num):
#     if (num <= 1):
#         return num
#     else:
#         return (fibo(num-1) + fibo(num-2))
    
# position = input("Put the number you want the fibonacci sequence to go up to: ")
# print ("The number in the position " + position + " is: " + str(fibo(int(position))))

####################################################################################

# ITERATION

# #Fibonacci using iteration -did by me-
# def fibonacciIter(arr, num):
#     for i in range (num):
#         #Positions 0 and 1 will be 1
#         if (i <= 1):
#             arr.append(1)
#         else:
#             arr.append(arr[i-1] + arr[i-2])
    
#     # Because the array starts at position 0, so, the position 20 in Fib (for people) is position 19 
#     # in the array
#     return arr[num-1]

# #Function to check if the number was calculated before or not
# def checkPos(num):
#     arr = []
#     if(len(arr) >= num):
#         return arr[num-1]
#     else:
#         return fibonacciIter(arr, num)


# position = input("Put the number you want the fibonacci sequence to go up to: ")
# print ("The number in the position " + position + " is: " + str(checkPos(int(position))))

####################################################################################

# TOP DOWN

# #Fibonacci using top down approach
# def fibonacci(n, memo={}):
#     """
#     Top-down recursive function with memoization to find the nth Fibonacci number.
#     :param n: The position in the Fibonacci sequence (0-indexed).
#     :param memo: A dictionary to store previously computed Fibonacci values.
#     :return: The nth Fibonacci number.
#     """
#     # Base cases
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1

#     # Check if the value is already computed
#     if n in memo:
#         return memo[n]

#     # Recursive computation with memoization
#     memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
#     return memo[n]


# position = input("Put the number you want the fibonacci sequence to go up to: ")
# print ("The number in the position " + position + " is: " + str(fibonacci(int(position))))

####################################################################################

# # BOTTOM UP (WITH MEMORY)
# # The same as the code after but storing the numbers in the array, only for the purpose to 
# # compare both methods
# def fibonacciBottomUp(n):
#     if(n <= 1):
#         return n
    
#     array = []
#     array.insert(0,0)
#     array.insert(1,1)
    
#     for i in range(2,n+1):
#         array.insert(i, array[i-1] + array[i-2])
        
#     return array[n]

# position = input("Put the number you want the fibonacci sequence to go up to: ")
# print ("The number in the position " + position + " is: " + str(fibonacciBottomUp(int(position))))

####################################################################################

#BOTTOM UP (NO MEMORY)

#Fibonacci using bottom up approach
#Instead of storing all Fibonacci numbers in an array, only the last two values are kept in memory, 
# reducing space usage to 𝑂(1)
def fibonacci_bottom_up(n):
    """
    Bottom-up approach to find the nth Fibonacci number.
    :param n: The position in the Fibonacci sequence (0-indexed).
    :return: The nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Initialize the first two Fibonacci numbers
    prev, curr = 0, 1

    # Iterate to compute Fibonacci numbers up to n
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


position = input("Put the number you want the fibonacci sequence to go up to: ")
print ("The number in the position " + position + " is: " + str(fibonacci_bottom_up(int(position))))
