from functools import lru_cache

class Solution:
    def maxGold(self, mat):
        # code here
        dirs = [(-1,1),(0,1),(1,1)]
        
        @lru_cache(None)
        def dfs(i,j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return 0
            x = 0
            for dx, dy in dirs:
                x = max(x, dfs(i+dx, j+dy))
            return mat[i][j] + x
        
        res = 0
        n, m = len(mat), len(mat[0])
        
        for i in range(n):
            res = max(res, dfs(i,0))
        return res