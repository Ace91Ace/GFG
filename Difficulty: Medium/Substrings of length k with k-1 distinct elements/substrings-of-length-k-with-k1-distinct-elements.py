class Solution:
    def substrCount(self, s, k):
        # code here
        freq = {}
        l, res = 0, 0
        
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0)+1
            ln = r-l+1 
            
            if ln < k:
                continue
            elif ln > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            if len(freq) == k-1:
                res += 1
        return res
            
        