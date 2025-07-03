class Solution:
    def countAtMostK(self, arr, k):
        # Code here
        res = 0
        l = 0
        freq = {}
        for r in range(len(arr)):
            freq[arr[r]] = freq.get(arr[r],0) + 1
            
            while len(freq) > k:
                freq[arr[l]] -= 1
                if freq[arr[l]] == 0:
                    del freq[arr[l]]
                l += 1
            res += (r-l+1)
        return res