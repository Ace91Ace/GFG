from functools import lru_cache

class Solution:
    def knapsack(self, W, val, wt):
        # code here
        def dfs(i, x):
            if i == n :
                return 0
            pick = 0
            if wt[i] <= x:
                pick = val[i] + dp[i+1][x - wt[i]]
            no = dp[i+1][x]
            return max(no, pick)
        
        n = len(val)
        dp = [[0] * (W + 1) for _ in range(n + 1)]
        for i in range(n-1, -1, -1):
            for j in range(W+1):
                dp[i][j] = dfs(i,j)
        return dp[0][W]
