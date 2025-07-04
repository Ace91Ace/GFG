#User function Template for python3
from typing import List
import heapq

class Solution:
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        prnt = [i for i in range(V)]
        def find(u):
            if prnt[u] != u:
                prnt[u] = find(prnt[u])
            return prnt[u]
        
        def union(u,v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            prnt[pu] = pv
            return True
        # code here
        x = [i[::-1] for i in edges]
        heapq.heapify(x)
        cnt = 0
        res = 0
        while x and cnt != V:
            w, u, v = heapq.heappop(x)
            if union(u,v):
                res += w
                cnt += 1
        return res
            
            
            