class Solution:
    def minRemoval(self, intervals):
        # code here
        intervals.sort()
        stk = [intervals[0]]
        
        for i in intervals:
            j = stk[-1]
            if j[1] > i[0]:
                stk.pop()
                stk.append([min(i[0], i[0]), min(i[1], j[1])])
            else:
                stk.append(i)
        return len(intervals) - len(stk)