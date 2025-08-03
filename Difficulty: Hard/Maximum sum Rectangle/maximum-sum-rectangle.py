class Solution:
    def maxRectSum(self, mat):
        n, m = len(mat), len(mat[0])
        mx = -float('inf')
        
        def kadane(arr):
            x = -float('inf')
            curr = 0
            
            for i in arr:
                curr = max(i, curr+i)
                x = max(x, curr)
            return x
        
        for l in range(m):
            temp = [0]*n
            for r in range(l, m):
                for i in range(n):
                    temp[i] += mat[i][r]
                mx = max(mx, kadane(temp))
        
        return mx
