# Geek is going for a training program for n days. He can perform any of these activities: Running, Fighting, and Learning Practice. Each activity has some point on each day. As Geek wants to improve all his skills, he can't do the same activity on two consecutive days. Given a 2D array arr[][] of size n where arr[i][0], arr[i][1], and arr[i][2] represent the merit points for Running, Fighting, and Learning on the i-th day, determine the maximum total merit points Geek can achieve .

class Solution:
    def maximumPoints(self, arr):
        # Code here
        n = len(arr)
        m = len(arr[0])
        dp = [[0 for j in range(m)] for i in range(n)]
        for i in range(m):
            dp[0][i] = arr[0][i]
        for i in range(1,n):
            for j in range(m):
                maxi_prev = 0
                for k in range(m):
                    if k!=j:
                        if maxi_prev<dp[i-1][k]:
                            maxi_prev = dp[i-1][k]
                dp[i][j] = arr[i][j] + maxi_prev
        maxi = 0
        for i in range(m):
            if maxi < dp[n-1][i]:
                maxi = dp[n-1][i]
        return maxi