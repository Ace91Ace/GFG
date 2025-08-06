class Solution:
    def minDifference(self, arr):
        time, vis = [], set()
        for t in arr:
            h, m, s = map(int, t.split(':'))
            x = h * 3600 + m * 60 + s
            if x in vis:
                return 0
            vis.add(x)
            time.append(x)
        time.sort()
        d = float('inf')
        for i in range(1, len(time)):
            d = min(d, time[i] - time[i - 1])
        res = 86400 - (time[-1] - time[0])
        return min(res, d)
