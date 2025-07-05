#User function Template for python3

class Solution:
	def searchWord(self, grid, word):
		# Code here
		n = len(word)
		dir = [[0,1], [1,0], [0,-1], [-1,0], [-1,-1], [1,1], [-1,1], [1,-1]]
		def dfs(x,y,l, dx, dy):
		    if l == n:
		        return True
		    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or word[l] != grid[x][y]:
		        return False
            return dfs(x+dx, y+dy, l+1, dx, dy)
		
		res = []
		for i in range(len(grid)):
		    for j in range(len(grid[0])):
		        if grid[i][j] == word[0]:
		            for dx, dy in dir:
		                if dfs(i,j,0, dx, dy):
		                    res.append((i,j))
		                    break
		return res