#User function Template for python3
from functools import lru_cache
class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, s1, s2):
        #code here
        @lru_cache(None)
        def LCS(i, j):
            if i >= len(s1) or j >= len(s2) :
                return 0
            if s1[i] == s2[j]:
                return 1 + LCS(i+1, j+1)
            return max(LCS(i+1, j), LCS(i, j+1))
            
        x = LCS(0, 0)
        return len(s1) + len(s2) - x