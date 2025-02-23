# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

 class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m ==1 and n ==1 and obstacleGrid[0][0] ==1 :
            return 0
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if (i==0 and j==0) or obstacleGrid[i][j]==1:
                    continue
                if i == 0:
                    if obstacleGrid[i][j-1]==1:
                        continue
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    if obstacleGrid[i-1][j]==1:
                        continue
                    dp[i][j] = dp[i-1][j]
                elif obstacleGrid[i][j-1] == 1:
                    dp[i][j] = dp[i-1][j]
                elif obstacleGrid[i-1][j] == 1:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]
        
