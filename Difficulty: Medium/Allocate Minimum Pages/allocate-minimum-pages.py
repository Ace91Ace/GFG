class Solution:
    def findPages(self, arr, k):
        def check(m):
            cnt = 1
            sm = 0
            for i in arr:
                sm += i
                if sm > m:
                    sm = i
                    cnt += 1
            return cnt
        
        if k > len(arr):
            return -1

        l, r = max(arr), sum(arr)
        ans = -1
        while l <= r:
            mid = (l+r)//2
            x = check(mid)
            if x <= k:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
