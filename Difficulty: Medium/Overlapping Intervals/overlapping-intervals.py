class Solution:
    def mergeOverlap(self, arr):
        #Code here
        arr.sort()
        stk = [arr[0]]
        
        for i in arr[1:]:
            s, e = stk[-1]
            if i[0] <= e:
                stk.pop()
                stk.append([s, max(e,i[1])])
            else:
                stk.append(i)
        return stk
