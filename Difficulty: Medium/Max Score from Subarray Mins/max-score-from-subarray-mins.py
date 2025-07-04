class Solution:
    def maxSum(self, arr):
        # code here
        res = 0
        arr = [arr[i]+arr[i+1] for i in range(len(arr)-1)]
        return max(arr)
    
