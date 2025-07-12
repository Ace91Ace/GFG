from functools import lru_cache
class Solution:
    def findCatalan(self, n):
        # code here
        @lru_cache
        def dfs(n):
            if n <= 1:
                return 1
            res = 0
            
            for i in range(n):
                res += dfs(i)*dfs(n-i-1)
            return res
        return dfs(n)
        