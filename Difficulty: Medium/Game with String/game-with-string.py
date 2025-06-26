from collections import Counter 
import heapq

class Solution:
    def minValue(self, s, k):
        #code here
        c = Counter(s)
        c = [-c[i] for i in c]
        heapq.heapify(c)
        
        while c and k > 0:
            x = heapq.heappop(c)
            x += 1
            k -= 1
            heapq.heappush(c, x)
        c = [i**2 for i in c]
        return sum(c)
                    
            