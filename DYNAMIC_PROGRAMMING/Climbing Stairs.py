# MEMOIZATION
# top down approach
# Final Complexity Summary
# ✅ Time Complexity: 
# O(n) (each subproblem is computed once)
# ✅ Space Complexity: 
# O(n) (due to memoization and recursion stack)
# ways(5)
# ├── ways(4)
# │   ├── ways(3)
# │   │   ├── ways(2)
# │   │   │   ├── ways(1)  -> Returns 1
# │   │   │   ├── ways(0)  -> Returns 1
# │   │   │   └── Sum: 1+1=2
# │   │   ├── ways(1)  -> Returns 1
# │   │   └── Sum: 2+1=3
# │   ├── ways(2) -> Retrieved from dp[] (2)
# │   └── Sum: 3+2=5
# ├── ways(3) -> Retrieved from dp[] (3)
# └── Sum: 5+3=8
class Solution:
    def ways(self,n,dp):
        if n == 0:
            return 1
        elif n == 1 :
            return 1
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.ways(n-1,dp)+self.ways(n-2,dp)
        return dp[n]
    def climbStairs(self, n: int) -> int:
        dp = [-1 for i in range(n+1)]
        return self.ways(n,dp)
    

# BOTTOM UP APPROACH
# no recusion stack
class Solution:
    def ways(self,n):
        if n == 1:
            return 1
        prev1,prev2 = 1,1
        cur = 0
        for i in range(2,n+1):
            cur = prev1+prev2
            prev1 = prev2
            prev2 = cur
        return cur
    def climbStairs(self, n: int) -> int:
        return self.ways(n)
    

