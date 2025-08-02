class Solution:
    def rowWithMax1s(self, arr):
        # code here
        n, m = len(arr), len(arr[0])
        def bins(ss):
            l, r = 0, m-1
            
            while r >= l:
                mid = (l+r)//2
                if ss[mid] == 0:
                    l = mid + 1
                else:
                    r = mid -1
            return m-l
        mx, mi = -1, -1
        for i, x in enumerate(arr):
            if bins(x) > mx:
                mx = bins(x)
                mi = i
        return mi
            