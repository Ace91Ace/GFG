#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        res = [1]*len(arr)
        pref, suff = [1], [1]
        
        for i, j in zip(arr, arr[::-1]):
            pref.append(i*pref[-1])
            suff.append(j*suff[-1])
        suff, pref = suff[::-1][1::], pref[:-1]
        
        return [pref[i]*suff[i] for i in range(len(pref))]