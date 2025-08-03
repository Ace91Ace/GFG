class Solution:
    def applyDiff2D(self, mat, opr):
        # code here 
        n, m = len(mat), len(mat[0])
        dif = [[0]*(m+2) for _ in range(n+2)]
        
        for v, x1, y1, x2, y2 in opr:
            dif[x1][y1] += v
            dif[x1][y2+1] -= v
            dif[x2+1][y1] -= v
            dif[x2+1][y2+1] += v

        for i in range(n+1):
            for j in range(1, m+1):
                dif[i][j] += dif[i][j-1]
        
        for j in range(m+1):
            for i in range(1, n+1):
                dif[i][j] += dif[i-1][j]
        
        for i in range(n):
            for j in range(m):
                mat[i][j] += dif[i][j]
        return mat
                
                