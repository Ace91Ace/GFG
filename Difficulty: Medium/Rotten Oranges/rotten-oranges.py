from collections import deque

class Solution:
    def orangesRotting(self, mat):
        dire = [(0,1), (1,0), (0,-1), (-1,0)]
        q = deque()
        n, m = len(mat), len(mat[0])
        fre = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    q.append((i, j))
                elif mat[i][j] == 1:
                    fre += 1

        t = 0
        while q and fre > 0:
            for _ in range(len(q)):  
                x, y = q.popleft()
                
                for dx, dy in dire:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1:  
                        mat[nx][ny] = 2
                        fre -= 1
                        q.append((nx, ny))
            t += 1 

        return t if fre == 0 else -1

        

