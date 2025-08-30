class Solution:
    def maxWater(self, arr):
        def calculate(l, r):
            return min(arr[l], arr[r])*(r-l)
        # code here
        n = len(arr)
        l, r, ml = 0, n-1, 0
        
        while l < r:
            ml = max(ml, calculate(l, r))
            if arr[l] < arr[r]:
                l += 1
            else:
                r -= 1
        return ml