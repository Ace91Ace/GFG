#User function Template for python3
from functools import lru_cache
class Solution:
    def maximumPath(self, mat):
        # code here
        m, n = len(mat), len(mat[0])
        
        @lru_cache(None)
        def dfs(x,y):
            if y < 0 or x < 0 or x >= m or y >= n:
                return -1
            if x == m-1:
                return mat[x][y]
            return mat[x][y] + max(dfs(x+1, y-1), dfs(x+1, y), dfs(x+1,y+1))
        
        mx = 0
        for i in range(n):
            mx = max(mx,dfs(0,i))
        return mx
        
            