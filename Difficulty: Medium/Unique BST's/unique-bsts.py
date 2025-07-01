#User function Template for python3

class Solution:
    #Function to return the total number of possible unique BST.
    def numTrees(self,n):
        # code here
        def dfs(i):
            if i in dp:
                return dp[i]
            if i <= 1:
                return 1
                
            res = 0
            for j in range(i):
                res += dfs(j)*dfs(i-j-1)
            dp[i] = res
            return dp[i]
        dp = {}
        return dfs(n)