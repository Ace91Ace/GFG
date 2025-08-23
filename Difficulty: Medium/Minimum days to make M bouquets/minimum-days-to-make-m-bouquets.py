class Solution:
    def minDaysBloom(self, arr, k, m):
        # Code here
        def check(mid):
            flo = 0
            cnt = 0
            for i in arr:
                flo += 1
                if i <= mid:
                    if flo == k:
                        cnt += 1
                        flo = 0
                else:
                    flo = 0
            return cnt >= m
            
        l, r = min(arr), max(arr)
        ans = -1
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                ans = mid 
                r = mid - 1
            else:
                l = mid + 1
        return ans