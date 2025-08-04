#User function Template for python3

class Solution:
    def getPairs(self, arr):
        # code here
        n = len(arr)
        l, r = 0, n-1
        arr.sort()
        res = []
        
        while l < r:
            x = arr[l]+arr[r]
            if x > 0:
                r -= 1
            elif x < 0:
                l += 1
            else:
                res.append([arr[l], arr[r]])
                x, y = arr[l], arr[r]
                while l < n and arr[l] == x:
                    l += 1
                while r >= 0 and arr[r] == y:
                    r -= 1
        return res