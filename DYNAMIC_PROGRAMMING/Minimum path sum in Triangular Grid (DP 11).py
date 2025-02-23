# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        l = 1
        dp = []
        for i in range(n):
            lev_list = []
            for j in range(l):
                lev_list.append(0)
            dp.append(lev_list)
            l+=1
        dp[0][0] = triangle[0][0]
        for i in range(1,n):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j]+triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j]+triangle[i][j],dp[i-1][j-1] + triangle[i][j])
        mini = 1e9
        for j in range(n):
            if dp[n-1][j] < mini:
                mini = dp[n-1][j]
        return mini
