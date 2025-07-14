class Solution:
    def maxWater(self, arr):
        n = len(arr)
        lm, rm = [0]*n, [0]*n
        ml, mr = 0, 0

        for i in range(n):
            lm[i] = ml
            ml = max(ml, arr[i])
            rm[n-i-1] = mr
            mr = max(mr, arr[n-i-1])

        res = 0
        for i in range(n):
            res += max(0, min(lm[i], rm[i]) - arr[i])
        return res
