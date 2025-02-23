# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]
        for i in range(1,n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j]+matrix[i][j],dp[i-1][j+1] + matrix[i][j])
                elif j == n-1:
                    dp[i][j] = min(dp[i-1][j]+matrix[i][j],dp[i-1][j-1] + matrix[i][j])
                else:
                    dp[i][j] = min(min(dp[i-1][j]+matrix[i][j],dp[i-1][j-1] + matrix[i][j]),dp[i-1][j+1] + matrix[i][j])
        mini = 1e9
        for j in range(n):
            if dp[n-1][j] < mini:
                mini = dp[n-1][j]
        return mini