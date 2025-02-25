# You are given an n rows and m cols matrix grid representing a field of chocolates where grid[i][j] represents the number of chocolates that you can collect from the (i, j) cell.

# You have two robots that can collect chocolates for you:

# Robot #1 is located at the top-left corner (0, 0), and
# Robot #2 is located at the top-right corner (0, cols - 1).
# Return the maximum number of chocolates collection using both robots by following the rules below:

# From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
# When any robot passes through a cell, It picks up all chocolates, and the cell becomes an empty cell.
# When both robots stay in the same cell, only one takes the chocolates.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in grid.




class Solution:
    def solve(self, n, m, grid):
        # Code here
        # print("jijijij")
        dp = [[[0 for k in range(m)] for j in range(m)] for i in range(n)]
        dp[0][0][m-1] = grid[0][0] + grid[0][m-1]
        for i in range(1,n):
            # print("row",i)
            # print("dp",dp[i])
            for col1 in range(0,i+1):
                for col2 in range(m-1,m-1-i-1,-1):
                    # print("row",i)
                    # print("col1",col1)
                    # print("col2",col2)
                    if col1<m-1 and col1 > 0 and col2 < m-1 and col2 > 0 and col1 != col2:
                        maxi = 0
                        for j in [col2-1,col2,col2+1]:
                            for k in [col1-1,col1,col1+1]:
                                if maxi < dp[i-1][k][j]:
                                    maxi = dp[i-1][k][j]
                        dp[i][col1][col2] = grid[i][col1]+grid[i][col2]+maxi
                    
                    elif col1 == 0 and col2>0 and col2 < m-1 and col1 != col2:
                        maxi = 0
                        for j in [col2-1,col2,col2+1]:
                            for k in [col1,col1+1]:
                                if maxi < dp[i-1][k][j]:
                                    maxi = dp[i-1][k][j]
                        dp[i][col1][col2] = grid[i][col1]+grid[i][col2]+maxi
                    elif col1<m-1 and col1 > 0 and col2 == m-1 and col1 != col2:
                        maxi = 0
                        for j in [col2-1,col2]:
                            for k in [col1-1,col1,col1+1]:
                                if maxi < dp[i-1][k][j]:
                                    maxi = dp[i-1][k][j]
                        dp[i][col1][col2] = grid[i][col1]+grid[i][col2]+maxi
                    elif col1 == 0 and col2 == m-1 and col1 != col2:
                        maxi = 0
                        for j in [col2-1,col2]:
                            for k in [col1,col1+1]:
                                if maxi < dp[i-1][k][j]:
                                    maxi = dp[i-1][k][j]
                        dp[i][col1][col2] = grid[i][col1]+grid[i][col2]+maxi
                        
                    elif col1 == col2 and col1!=0 and col1 != m-1:
                        dp[i][col1][col2] = grid[i][col1]+max(dp[i-1][col1-1][col2],dp[i-1][col1][col2+1])
            # print("dp",dp[i])
                                     
        ans = 0
        for col1 in range(m):
            for col2 in range(m):
                if dp[n-1][col1][col2]>ans:
                    ans = dp[n-1][col1][col2]
        return ans
    
if __name__ == '__main__':
    # t = int(input())
    # t= '4 3'
    #     3 1 1
    #     2 5 1
    #     1 5 5
    #     2 1 1'"
    # for _ in range(t):
    # n,m = map(int, input().split())
    n,m = 4,3
    grid = []
    grid.append([3,1,1])
    grid.append([2,5,1])
    grid.append([1,5,5])
    grid.append([2,1,1])
    ob = Solution()
    print(ob.solve(n,m,grid))
