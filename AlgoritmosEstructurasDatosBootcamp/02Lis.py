import numpy as np

"""  
#Using recursion
def lis(arr, index):
    if index == 0:
        return 1
    mx = 1
    for i in range(0, index):
        if arr[i] < arr[index]:
            mx = max(mx, lis(arr, i) + 1)
        
    return mx

arr = [3, 10, 2, 1, 20, 4, 6, 7, 8, 9] #The correct answer is 6
n = len(arr)
res = 1

for i in range(1, n):
    res = max(res, lis(arr, i))

print(res)
 """
 
""" 

#Using memoization (top down)
def lis(arr, index, memo):
    if index == 0:
        return 1
    if memo[index] != -1:
        return memo[index]
    mx = 1
    for i in range(0, index):
        if arr[i] < arr[index]:
            mx = max(mx, lis(arr, i, memo) + 1)
        
    memo[index] = mx
    return mx

arr = [3, 10, 2, 1, 20, 4, 6, 7, 8, 9] #The correct answer is 6
n = len(arr)
memo = [-1]*n
res = 1

for i in range(1, n):
    res = max(res, lis(arr, i, memo))

print(res)

#Bottom-up approach
arr = [3, 10, 2, 1, 20, 4, 6, 7, 8, 9] #The correct answer is 6
calc = [1]*len(arr)

for i in range(1, len(arr)):
    for j in range(0, i):
        if arr[i] > arr[j] and calc[i] <= calc[j]:
            calc[i] = calc[j] + 1            

print(max(calc))
 """
 