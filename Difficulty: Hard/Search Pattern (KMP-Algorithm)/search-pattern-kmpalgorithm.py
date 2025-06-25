#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        l = []
        n = len(pat)
        
        for i in range(len(txt)):
            if txt[i:i+n] == pat:
                l += [i]
        return l