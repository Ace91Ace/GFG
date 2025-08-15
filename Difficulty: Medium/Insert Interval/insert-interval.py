class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        intervals.append(newInterval)
        intervals.sort()
        
        stk = [intervals[0]]
        for a, b in intervals[1:]:
            x, y = stk[-1]
            if y >= a:
                stk.pop()
                stk.append([x, max(b, y)])
            else:
                stk.append([a,b])
        return stk
            
        