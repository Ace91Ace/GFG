#User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        res = []
        vis = set()
        arr2, arr3 = set(arr2), set(arr3)
        for i in arr1:
            if i not in vis and i in arr2 and i in arr3:
                res.append(i)
                vis.add(i)
        return res