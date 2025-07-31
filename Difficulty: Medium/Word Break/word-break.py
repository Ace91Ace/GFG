class Solution:
    def wordBreak(self, s, dictionary):
        # code here
        ws = set(dictionary)
        n = len(s)
        dp = [None]*n
        def dfs(i):
            if i == n: return True
            if dp[i] is not None: return dp[i]
            for j in range(i+1, n+1):
                if s[i:j] in ws and dfs(j):
                    dp[i] = True
                    return dp[i]
            dp[i] = False
            return dp[i]
        return dfs(0)