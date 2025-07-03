#User function Template for python3
from functools import lru_cache

class Solution:
    def cutRod(self, price):
        n = len(price)  # Length of the rod
        dp = [0] * (n + 1)  # Initialize DP array

    
        for i in range(1, n + 1):  # Rod length
            for j in range(1, i + 1):  # Possible cuts
                dp[i] = max(dp[i], price[j - 1] + dp[i - j])

        return dp[n]  # Maximum obtainable value
