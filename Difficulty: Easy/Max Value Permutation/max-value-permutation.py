#User function Template for python3

class Solution:
    def maxValue(self, arr): 
        # Complete the function
        arr.sort()
        return sum([arr[i]*i for i in range(len(arr))])%(10**9 + 7)
