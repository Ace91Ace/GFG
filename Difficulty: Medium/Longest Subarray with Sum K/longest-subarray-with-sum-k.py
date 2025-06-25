# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        sm, ml = 0, 0
        pref = {0:-1}
        
        for i,x in enumerate(arr):
            sm += x
            if sm-k in pref:
                ml = max(ml, i-pref[sm-k])
            if sm not in pref:
                pref[sm] = i
        return ml
    
