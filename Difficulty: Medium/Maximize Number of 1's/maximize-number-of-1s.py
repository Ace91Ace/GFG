class Solution:
    def maxOnes(self, arr, k):
        # code here
        l, ml, x = 0, 0, k
        
        for r in range(len(arr)):
            if arr[r] == 0:
                x -= 1
            while x < 0:
                if arr[l] == 0:
                    x += 1
                l += 1
            ml = max(ml, r-l+1)
        return ml
            
        