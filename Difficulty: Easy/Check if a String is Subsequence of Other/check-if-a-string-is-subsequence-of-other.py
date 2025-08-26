class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        l = 0
        m = len(s1)
        
        for r in range(len(s2)):
            if s1[l] == s2[r]:
                l += 1
            if l == m:
                return True
        return False