class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        arr = [1 if i > k else -1 for i in arr]
        pref = [0]
        for i in arr:
            pref.append(i+pref[-1])
        stk = []
        for i in range(len(pref)):
            if not stk or pref[i] < pref[stk[-1]]:
                stk.append(i)
        res = 0
        for i in range(len(pref)-1, -1, -1):
            while stk and pref[i] > pref[stk[-1]]:
                res = max(res, i - stk.pop())
        return res
            
        