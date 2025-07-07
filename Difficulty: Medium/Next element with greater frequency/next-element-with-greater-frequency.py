from collections import Counter

class Solution:
    def findGreater(self, arr):
        # code here
        c = Counter(arr)
        stk = []
        freq = [c[i] for i in arr]
        res = [-1]*len(arr)

        for i, x in enumerate(arr):
            while stk and freq[stk[-1]] < freq[i]:
                p = stk.pop()
                res[p] = x
            stk.append(i)
        return res
            