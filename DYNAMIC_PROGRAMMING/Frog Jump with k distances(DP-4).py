class Solution:
    def minimizeCost(self, k, arr):
        # code here
        n = len(arr)
        if n == 1:
            return 0
        dp = [1e9 for i in range(n)]
        dp[0] = 0
        dp[1] = abs(arr[1]-arr[0])
        for i in range(2,n):
            for j in range(max(0,i-k),i):
                if dp[i] > dp[j] + abs(arr[i]-arr[j]):
                    dp[i] = dp[j] + abs(arr[i]-arr[j])
        return dp[n-1]        