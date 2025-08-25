class Solution:
    def maximizeMedian(self, arr, k):
        n = len(arr)
        inx = (n - 1) // 2
        arr.sort()

        def check(mid):
            diff = 0
            for i in range(inx, n):
                if arr[i] < mid:
                    diff += mid - arr[i]
                if diff > k:
                    return False
            return True

        l, r = arr[inx], arr[inx] + k
        ans = arr[inx]

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        if n % 2:
            return ans
        else:
            return (ans + max(ans, arr[inx + 1])) // 2
