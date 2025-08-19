class Solution:
    def farMin(self, arr):
        def bins(i):
            l, r = i+1, n-1
            ans = -1
            while l <= r:
                mid = (l+r)//2
                if suff[mid] < arr[i]:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return ans
        # Code Here
        n = len(arr)
        res = [-1]*n
        suff = [0]*n
        suff[-1] = arr[-1]
        mn = float('inf')
        for i in range(n-2, -1, -1):
            suff[i] = min(arr[i], suff[i+1])
        
        for i in range(n-1):
            res[i] = bins(i)
        return res