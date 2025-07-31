class Solution:
    def countBalanced(self, arr):
        vow = set("aeiou")
        res = []

        for i in arr:
            res.append(sum([1 if j in vow else -1 for j in i]))
        
        count = 0
        pref = 0
        dic = {0: 1}

        for val in res:
            pref += val
            count += dic.get(pref, 0)
            dic[pref] = dic.get(pref, 0) + 1

        return count