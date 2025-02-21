# Given an integer array height[] where height[i] represents the height of the i-th stair, a frog starts from the first stair and wants to reach the top. From any stair i, the frog has two options: it can either jump to the (i+1)th stair or the (i+2)th stair. The cost of a jump is the absolute difference in height between the two stairs. Determine the minimum total cost required for the frog to reach the top.

# Example:

# Input: heights[] = [20, 30, 40, 20] 
# Output: 20
# Explanation:  Minimum cost is incurred when the frog jumps from stair 0 to 1 then 1 to 3:
# jump from stair 0 to 1: cost = |30 - 20| = 10
# jump from stair 1 to 3: cost = |20-30|  = 10
# Total Cost = 10 + 10 = 20



class Solution:
    def minCost(self, height):
        # code here
        if len(height) == 1:
            return 0
        if len(height) == 2:
            return abs(height[1]-height[0])
        dp = [0 for i in range(len(height))]
        dp[0] = 0
        dp[1] = abs(height[1]-height[0])
        # if len(height)==1:
        #     return dp[1]
        for i in range(2,len(height)):
            dp[i] = min(dp[i-1]+abs(height[i]-height[i-1]),dp[i-2]+abs(height[i]-height[i-2]))
        return dp[len(height)-1]
    

    

