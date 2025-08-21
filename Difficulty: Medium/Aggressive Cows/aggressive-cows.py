class Solution:
    def aggressiveCows(self, stalls, k):
        def can(d):
            c = 1
            last = stalls[0]
            for i in range(1, len(stalls)):
                if stalls[i] - last >= d:
                    c += 1
                    last = stalls[i]
                if c >= k:
                    return True
            return False
        
        stalls.sort()
        l, r = 1, stalls[-1] - stalls[0]  
        
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if can(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res
