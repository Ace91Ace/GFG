class Solution:
    def median(self, mat):
        # code here 
        n, m = len(mat), len(mat[0])
        def lesst(arr, x):
            l, r = 0, m-1
            ans = m
            while l <= r:
                mid = (l+r)//2
                if arr[mid] > x:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return ans
            
        def blackbox(x):
            count = 0
            
            for i in mat:
                count += lesst(i, x)
            return count
            
            
        l = min(row[0] for row in mat)
        r = max(row[-1] for row in mat)
        tgt = n*m//2
        while l <= r:
            mid = (l+r)//2
            cnt = blackbox(mid)
            
            if cnt <= tgt:
                l  = mid + 1
            else:
                r = mid - 1
        return l
            