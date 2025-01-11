For every exercise, I analyze all the possible ways to arrive at a solution to thoroughly understand not only the exercise itself but also the underlying concepts of recursion, memoization, and my personal favorite, the iterative approach.

Sometimes, it was straightforward, while other times, it was a challenging journey that took me up to two weeks to fully grasp a concept (and yes, I still have some doubts xD).

The foundation of every explanation you’ll see here comes from a process I developed after each Código Facilito class. It involved gathering information from a variety of sources: videos, texts, incredible books like Grokking Algorithms, trial and error on a large board, and finally, leveraging the power of AI tools. I enjoy working with AI tools because they help me organize the sometimes chaotic ideas in my brain into words that are easier for everyone to understand.

I hope these explanations help you better understand each process. If you need a more detailed or visual explanation, please don’t hesitate to reach out—it would be a pleasure! You can contact me at pablozaviok@gmail.com.



# LIS (Longest Increasing Subsequence)
According with what I said before, a visual explanation by video could help you, let me know if it's necessary

The Longest Increasing Subsequence problem is solved iteratively, step by step, by using two arrays:

1. Two Arrays:

* The input array: This contains the sequence of numbers for which we want to find the LIS.
* The LIS array: This helps us track the length of the longest increasing subsequence ending at each position in the input array. Initially, every value in this array is set to 1, because the smallest possible subsequence at each position is the number itself (length = 1).

2. The Process:

* For each position in the input array (let's call it the "right position"), we determine the LIS ending at that position by comparing it with all earlier positions ("left positions").
* Key idea: If the number at a left position is smaller than the number at the right position, we check whether the LIS ending at the right position can be extended. This is done by comparing:
    - The current LIS value at the right position.
    - The LIS value at the left position + 1.
* If extending the LIS from the left position results in a larger LIS value for the right position, we update the LIS array for the right position.

3. Step-by-step Explanation:

* Start with the first number in the input array. Its LIS is 1 (since it's the only number in its subsequence so far).
* Move to the second number (the "right position").
    - Compare it with the first number (the "left position").
    - If the first number is smaller than the second number and extending the LIS from the first number gives a larger subsequence, update the LIS value for the second number.
* Move to the third number (next "right position").
    - Compare it with the first and second numbers ("left positions").
    - For each comparison:
        + If the number at the left position is smaller than the number at the right position and extending the LIS from the left position increases the LIS value at the right position, update it.
* Repeat this process for every number in the input array, moving the "right position" one step to the right in each iteration, and comparing it with all "left positions" before it.

4. Final Steps:

- After processing all numbers, the LIS array will contain the length of the longest increasing subsequence ending at each position in the input array.
- The result (length of the LIS for the entire array) is the maximum value in the LIS array.


Example Walkthrough:
Input Array: [10, 22, 9, 33, 21, 50, 41, 60]
LIS Array (initialized to 1): [1, 1, 1, 1, 1, 1, 1, 1]

- Compare 10 (left) with 22 (right). Since 10 < 22, update LIS[1] = LIS[0] + 1 → LIS[1] = 2.
- Compare 10 (left) with 9 (right). No update, as 10 > 9.
- Compare 22 (left) with 33 (right). Since 22 < 33, update LIS[3] = LIS[1] + 1 → LIS[3] = 3.
- Continue comparing each pair, updating the LIS array as described.
Final LIS Array: [1, 2, 1, 3, 2, 4, 4, 5]
Output: Maximum value in the LIS array = 5.

This process ensures that we systematically compute the LIS at every position by incorporating all valid subsequences up to that point.





# 0/1 Knapsack Problem
The key here is to calculate all the possible subsets that fit into the knapsack and then select the subset with the maximum value.

As in previous exercises, we can approach this problem in three ways:
Recursion
Top-down (recursion with memoization)
Bottom-up (iterative)

Using recursion, we check if there are any items left and if the current item fits into the knapsack. If both conditions are met, for each item, we decide whether to include it—reducing the remaining capacity—or exclude it, and then recursively call the function. This process continues until we reach the base case or there is no remaining space in the knapsack.

This recursive function generates all possible subsets, and the subset with the maximum value is then selected.

To be updated...

# MaxValue Exercise (from Divide & Conquer)
Recursion Tree example for MaxValue exercise.
![image](https://github.com/user-attachments/assets/061f1c5b-1b75-4c70-8c1e-3a64313501a2)
