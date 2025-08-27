#User function Template for python3

class Solution:
    def wordBoggle(self,board,dictionary):
        # return list of words(str) found in the board
        dire = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

        def dfs(x, y, i, word, vis):
            n = len(word)
            if x < 0 or x >= r or y < 0 or y >= c or (x,y) in vis or board[x][y] != word[i]:
                return 
            if i == n-1:
                return True
            vis.add((x,y))
            for dx, dy in dire:
                if dfs(x+dx, y+dy, i+1, word, vis):
                    return True
            vis.remove((x,y))
            return False
            
        def exist(word):
            n = len(word)
            for i in range(r):
                for j in range(c):
                    if word[0] == board[i][j]:
                        if dfs(i, j, 0, word, set()):
                            return True
            return False
            
        r, c = len(board), len(board[0])
        res = []
        for word in dictionary:
            if exist(word):
                res.append(word)
        return res