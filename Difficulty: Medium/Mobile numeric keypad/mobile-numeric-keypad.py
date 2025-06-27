class Solution:
	def getCount(self, n):
		# code here
		nei = [
		    [0,8],
		    [1,2,4],
		    [2,1,3,5],
		    [3,2,6],
		    [4,1,5,7],
		    [5,2,4,6,8],
		    [6,3,5,9],
		    [7,4,8],
		    [8,0,5,7,9],
		    [9,6,8]
		]
		
		dp = [[0]*10 for _ in range(n)]
		for i in range(10):
		    dp[0][i] = 1
		for i in range(1,n):
		    for j in range(10):
		        for k in nei[j]:
		            dp[i][j] += dp[i-1][k]
		return sum(dp[-1])