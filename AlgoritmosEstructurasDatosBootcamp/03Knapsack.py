#Using recursion
""" def knapsack(capacity, weights, profits, n):
    if n == 0 or capacity == 0:
        return 0
    if weights[n-1] > capacity:
        return knapsack(capacity, weights, profits, n-1)
    else:
        return max(profits[n-1] + knapsack(capacity-weights[n-1], weights, profits, n-1), 
                   knapsack(capacity, weights, profits, n-1))

capacity = 5
weights = [1, 2, 3]
profits = [1, 7, 11]
n = len(weights) #Number of items
print(knapsack(capacity, weights, profits, n)) # 18
 """

#Using memoization (top down)
""" 
def knapsack(capacity, weights, profits, n, memo):
    if n == 0 or capacity == 0:
        return 0
    if weights[n-1] > capacity:
        return knapsack(capacity, weights, profits, n-1, memo)
    elif memo[n][capacity] != -1:
        return memo[n][capacity]
    else:
        memo[n][capacity] = max(profits[n-1] + knapsack(capacity-weights[n-1], weights, profits, n-1, memo), 
                   knapsack(capacity, weights, profits, n-1, memo))
        return memo[n][capacity]

capacity = 5
weights = [1, 2, 3]
profits = [1, 7, 11]
n = len(weights) #Number of items
memo = [[-1 for _ in range(capacity+1)] for _ in range(n+1)]
print(knapsack(capacity, weights, profits, n, memo)) # 18
 """
 
#Using bottom up
def knapsack(capacity, weights, profits, n):
    memo = [[0 for _ in range(capacity+1)] for _ in range(n+1)] 
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if weights[i-1] > j:
                memo[i][j] = memo[i-1][j]
            else:
                memo[i][j] = max(profits[i-1] + memo[i-1][j-weights[i-1]], memo[i-1][j])
    return memo[n][capacity]

capacity = 5
weights = [1, 2, 3]
profits = [1, 7, 11]
n = len(weights) #Number of items
print(knapsack(capacity, weights, profits, n)) # 18