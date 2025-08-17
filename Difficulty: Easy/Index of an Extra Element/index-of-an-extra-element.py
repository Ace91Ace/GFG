class Solution:
    def findExtra(self,a,b):
        #add code here
        for i in range(min(len(a), len(b))):
            if a[i] != b[i]:
                return i
        return min(len(a), len(b))