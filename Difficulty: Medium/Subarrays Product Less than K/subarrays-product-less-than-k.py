#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, arr, n, k):
        
        #Code here
        if k <= 1:
            return 0
        l, count = 0, 0
        pd = 1
        
        for r in range(len(arr)):
            pd *= arr[r]
            
            while pd >= k and l <= r:
                pd //= arr[l]
                l += 1
            count += (r-l+1)
        return count            
    
    
    
    