class Solution:
    def diffArray(self, arr, opr):
        # code here
        dif = [0]*(len(arr)+1)
        for l, r, v in opr:
            dif[l] += v
            dif[r+1] -= v
        pref = 0
        for i in range(len(arr)):
            pref += dif[i]
            arr[i] += pref
        return arr