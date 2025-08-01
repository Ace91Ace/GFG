class Solution:
    def findTriplets(self, arr):
        #code here
        arr.sort()
        n = len(arr)
        for i, m in enumerate(arr):
            l, r = i+1, n-1
            while l < r:
                sm = arr[l] + arr[r]
                if sm + m > 0:
                    r -= 1
                elif sm + m < 0:
                    l += 1
                else:
                    return True
        return False