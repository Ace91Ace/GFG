class Solution:
    def splitArray(self, arr, k):
        def check(x):
            count, res = 1, 0
            for i in arr:
                if res + i <= x:
                    res += i
                else:
                    res = i
                    count += 1
            return count

        l, r = max(arr), sum(arr)
        while l <= r:
            mid = (l + r) // 2
            y = check(mid)
            if y > k:
                l = mid + 1
            else:
                r = mid - 1
        return l
