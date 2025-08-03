class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        curr = 0
        mx = -float('inf')
        
        for i in arr:
            curr = max(i, curr+i)
            mx = max(mx, curr)
        return mx