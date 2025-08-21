import math

class Solution:
    def findSmallestMaxDist(self, stations, k):
        def check(d):
            c = 0
            for i in range(1, n):
                c += math.ceil((stations[i] - stations[i-1]) / d) - 1
            return c <= k

        n = len(stations)
        l, r = 0, stations[-1] - stations[0]

        while r - l > 1e-6:
            mid = (l + r) / 2.0
            if check(mid):
                r = mid
            else:
                l = mid
        return r
