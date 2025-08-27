class Solution:
    def countTriangles(self, arr):
        arr.sort()
        cnt, n = 0, len(arr)
        
        for i in range(n-1, 1, -1):
            l, r = 0, i-1
            while l < r:
                if arr[l]+arr[r] > arr[i]:
                    cnt += (r-l)
                    r -= 1
                else:
                    l += 1
        return cnt
                