class Solution:
    def subarraySum(self, arr, target):
        dic = {0: 0}
        pref = 0

        for i, x in enumerate(arr):
            pref += x
            if pref - target in dic:
                return [dic[pref - target] + 1, i + 1]
            if pref not in dic:
                dic[pref] = i + 1
        return [-1]
