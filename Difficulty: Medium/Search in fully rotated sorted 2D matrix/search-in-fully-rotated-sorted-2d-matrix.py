class Solution:
    def searchMatrix(self, mat, x):
        m, n = len(mat), len(mat[0])
        size = m * n
        
        def get(i):
            x, y = divmod(i, n)
            return mat[x][y]
        
        lo_i, hi_i = 0, size - 1
        while lo_i <= hi_i:
            mid_i = lo_i + (hi_i - lo_i) // 2
            lo, mid, hi = get(lo_i), get(mid_i), get(hi_i)
            if mid == x:
                return True
            if lo <= mid:
                if lo <= x < mid:
                    hi_i = mid_i - 1
                else:
                    lo_i = mid_i + 1
            else:
                if mid < x <= hi:
                    lo_i = mid_i + 1
                else:
                    hi_i = mid_i - 1
        return False