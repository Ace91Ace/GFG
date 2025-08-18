class Solution:
    def hIndex(self, citations):
        n = len(citations)
        citations.sort(reverse=True)
        l, r = 0, n - 1
        res = 0
        
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] >= mid + 1:
                res = mid + 1  
                l = mid + 1
            else:
                r = mid - 1
        return res
