class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        dic = {0:1}
        pref = 0
        count = 0
        
        for i in arr:
            pref += i
            if pref - k in dic:
                count += dic[pref-k]
            dic[pref] = dic.get(pref, 0) + 1
        return count
